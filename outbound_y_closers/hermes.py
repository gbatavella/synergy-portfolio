import csv
import smtplib
import time
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def iniciar_hermes():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🛡️ SYNERGY HERMES SENTINEL (HITL SMTP DISPATCHER) 🛡️ {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CONFIGURACIÓN DEL BÚNKER (OPSEC)
    # ==========================================
    load_dotenv()
    remitente = os.getenv("SMTP_USER", "gbatavella@gmail.com")
    password = os.getenv("SMTP_APP_PASSWORD") 
    
    if not password:
        print(f"{RED}X [ERROR CRÍTICO] Falta SMTP_APP_PASSWORD en la bóveda .env.{RESET}")
        print(f"{GRAY}>> Abortando ignición para prevenir fallos de autenticación SSL/TLS.{RESET}\n")
        sys.exit(1)

    archivo_csv = "Botin_Sinergy_General.csv"
    CORREO_CEO = "ceo.synergy@proton.me"

    # ==========================================
    # 2. MUNICIÓN ESTRATÉGICA (PAYLOAD)
    # ==========================================
    asunto = "Propuesta estratégica para tu proyecto en Redes Sociales"
    cuerpo_base = """Hola, un gusto saludarte.

Te contacto porque estuve analizando tu perfil y veo un gran potencial para implementar soluciones de Inteligencia Artificial que optimicen tu tiempo y resultados.

Desde Synergy Human & AI Agents, ayudamos a profesionales y empresas a automatizar sus procesos de venta y atención.

¿Te interesaría una breve charla para ver cómo podemos potenciar lo que estás haciendo?

Saludos,
Gabriel Tavella
Director de Synergy Human & AI Agents"""

    # ==========================================
    # 3. MOTOR SENTINEL (SMTP)
    # ==========================================
    def motor_envio(destinatario, debug=False):
        try:
            msg = MIMEMultipart()
            msg['From'] = remitente
            msg['To'] = destinatario
            msg['Subject'] = asunto
            msg.attach(MIMEText(cuerpo_base, 'plain'))
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            if debug: 
                server.set_debuglevel(1)
                
            server.starttls()
            server.login(remitente, password)
            server.sendmail(remitente, destinatario, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(f"\n{RED}[!!!] Falla estructural en el túnel SMTP: {e}{RESET}")
            return False

    # ==========================================
    # 4. PROTOCOLO DE DESPLIEGUE
    # ==========================================
    if not os.path.exists(archivo_csv):
        print(f"{YELLOW}⚠️ Alerta: El botín de datos '{archivo_csv}' no se encuentra en el directorio actual.{RESET}")
    
    print(f"{GRAY}[*] PASO 1: Prueba de túnel y entregabilidad hacia el Comando Central ({CORREO_CEO}){RESET}")
    
    if input(f"{YELLOW}¿Autoriza lanzamiento de prueba? (s/n): {RESET}").lower() == 's':
        print(f"{GRAY}Estableciendo conexión TLS/SSL...{RESET}")
        
        if motor_envio(CORREO_CEO, debug=True):
            print(f"\n{GREEN}{BOLD}✅ TEST EXITOSO. TÚNEL SMTP OPERATIVO.{RESET}")
            
            confirmacion = input(f"\n{RED}{BOLD}Escriba 'SYNERGY' para desbloquear el armamento y activar el envío masivo: {RESET}").upper()
            if confirmacion == 'SYNERGY':
                os.system('clear')
                print(f"{BLUE}{BOLD}{'='*65}{RESET}")
                print(f"{BLUE}{BOLD} 🚀 PROTOCOLO DE FUEGO A DISCRECIÓN ACTIVADO 🚀 {RESET}")
                print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
                
                try:
                    with open(archivo_csv, mode='r', encoding='utf-8') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            # Tolerancia a variaciones en nombre de columna
                            email_dest = row.get('Correo Electrónico', row.get('Email', '')).strip()
                            
                            if not email_dest or email_dest == CORREO_CEO: 
                                continue
                                
                            print(f"{CYAN}🎯 OBJETIVO FIJADO: {BOLD}{email_dest}{RESET}")
                            accion = input(f"{YELLOW}¿Disparar payload? (s/n/salir): {RESET}").lower()
                            
                            if accion == 's':
                                if motor_envio(email_dest):
                                    print(f"{GREEN}  ✓ IMPACTO CONFIRMADO. {GRAY}Enfriando cañones (5 seg)...{RESET}\n")
                                    time.sleep(5)
                            elif accion == 'salir':
                                print(f"\n{GRAY}💨 Abortando misión a petición del Comandante.{RESET}\n")
                                break
                            else:
                                print(f"{GRAY}  >> Objetivo omitido.{RESET}\n")
                                
                    print(f"{GREEN}{BOLD}Misión de Outbound finalizada.{RESET}\n")
                except Exception as e: 
                    print(f"{RED}X Fricción en la lectura del botín: {e}{RESET}")
            else:
                print(f"{YELLOW}Clave incorrecta. Abortando misión masiva.{RESET}")
        else:
            print(f"{RED}X Fallo en el test de conexión.{RESET}")
    else:
        print(f"{GRAY}Operación cancelada.{RESET}")

if __name__ == "__main__":
    iniciar_hermes()
