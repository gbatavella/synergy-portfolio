import imaplib
import email
import re
import pandas as pd
import os
import sys
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def iniciar_depurador():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧹 SYNERGY BOUNCE SCRUBBER (IMAP DATA CLEANSER V2) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # EXTRACCIÓN SEGURA DE CREDENCIALES (OPSEC)
    # ==========================================
    load_dotenv()
    
    EMAIL = os.getenv("IMAP_USER", "gbatavella@gmail.com")
    PASSWORD = os.getenv("IMAP_APP_PASSWORD") 
    IMAP_SERVER = os.getenv("IMAP_HOST", "imap.gmail.com")

    if not PASSWORD:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta IMAP_APP_PASSWORD en la bóveda .env.{RESET}")
        sys.exit(1)

    archivo_objetivo = input(f"{YELLOW}📁 Ingresa el nombre del CSV a depurar (ej. prospectos.csv): {RESET}").strip()
    
    if not os.path.exists(archivo_objetivo):
        print(f"\n{RED}❌ ERROR: No se encuentra el archivo '{archivo_objetivo}' en este directorio.{RESET}\n")
        sys.exit(1)

    def conectar_correo():
        print(f"{GRAY}[*] Estableciendo túnel SSL con la base de datos IMAP ({IMAP_SERVER})...{RESET}")
        try:
            mail = imaplib.IMAP4_SSL(IMAP_SERVER)
            mail.login(EMAIL, PASSWORD)
            print(f"{GREEN}[+] Enlace IMAP establecido con éxito.{RESET}")
            return mail
        except Exception as e:
            print(f"{RED}❌ Fallo de autenticación IMAP: {e}{RESET}")
            sys.exit(1)

    def extraer_correos_rebotados(mail):
        mail.select("inbox")
        print(f"{GRAY}[*] Escaneando historial de rebotes (Mailer-Daemon)...{RESET}")
        status, mensajes = mail.search(None, '(FROM "mailer-daemon@googlemail.com")')
        
        correos_fallidos = set()
        
        if mensajes[0]:
            lista_ids = mensajes[0].split()
            print(f"{CYAN} ↳ Analizando {len(lista_ids)} reportes de error estructural...{RESET}")
            
            for num in lista_ids:
                status, data = mail.fetch(num, '(RFC822)')
                mensaje_bruto = data[0][1]
                msg = email.message_from_bytes(mensaje_bruto)
                
                # Parseo recursivo multipart
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            cuerpo = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                            match = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', cuerpo)
                            if match:
                                correos_fallidos.add(match.group(0))
                else:
                    cuerpo = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                    match = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', cuerpo)
                    if match:
                        correos_fallidos.add(match.group(0))
                        
        return list(correos_fallidos)

    def limpiar_lista(correos_fallidos, archivo_csv):
        print(f"\n{YELLOW}⚠️ Se extrajeron {BOLD}{len(correos_fallidos)}{RESET}{YELLOW} correos tóxicos de la red.{RESET}")
        
        if not correos_fallidos:
            print(f"{GREEN}✅ La lista base está limpia. No hay acciones de purga necesarias.{RESET}\n")
            return

        print(f"{GRAY}[*] Inyectando toxinas en motor Pandas para vectorización...{RESET}")
        try:
            df = pd.read_csv(archivo_csv)
            
            # Detectar el nombre exacto de la columna de email (Tolerancia a mayúsculas)
            columna_email = None
            for col in df.columns:
                if col.strip().lower() == 'email':
                    columna_email = col
                    break
                    
            if not columna_email:
                print(f"{RED}❌ ERROR: El esquema CSV carece de la columna primaria 'Email'.{RESET}")
                return

            # Filtrado Vectorizado
            df_limpio = df[~df[columna_email].isin(correos_fallidos)]
            registros_eliminados = len(df) - len(df_limpio)
            
            # Serialización de salidas
            archivo_salida = archivo_csv.replace('.csv', '_depurado.csv')
            df_limpio.to_csv(archivo_salida, index=False)
            print(f"{GREEN}✅ Botín depurado exportado exitosamente: {archivo_salida}{RESET}")
            print(f"{GRAY} ↳ {registros_eliminados} registros purgados de la matriz principal.{RESET}")
            
            # Reporte de Auditoría
            archivo_auditoria = archivo_csv.replace('.csv', '_LISTA_NEGRA.txt')
            with open(archivo_auditoria, 'w') as f:
                for correo in correos_fallidos:
                    f.write(f"{correo}\n")
            print(f"{RED}🕵️‍♂️ Inteligencia forense (Lista Negra) compilada en: {archivo_auditoria}{RESET}\n")
            
        except Exception as e:
            print(f"{RED}❌ Fricción durante la mutación del CSV: {e}{RESET}\n")

    # Ejecución Core
    buzon = conectar_correo()
    malos = extraer_correos_rebotados(buzon)
    limpiar_lista(malos, archivo_objetivo)

if __name__ == "__main__":
    iniciar_depurador()
