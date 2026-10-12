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

def iniciar_hermes_vip():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🛡️ SYNERGY HERMES VIP (HIGH-TICKET HITL DISPATCHER) 🛡️ {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CONFIGURACIÓN DEL BÚNKER (OPSEC)
    # ==========================================
    load_dotenv()
    remitente = os.getenv("SMTP_USER", "gbatavella@gmail.com")
    password = os.getenv("SMTP_APP_PASSWORD") 
    CORREO_CEO = os.getenv("ADMIN_EMAIL", "ceo.synergy@proton.me")

    if not password:
        print(f"{RED}X [ERROR CRÍTICO] Falta SMTP_APP_PASSWORD en la bóveda .env.{RESET}")
        print(f"{GRAY}>> Abortando ignición para prevenir fallos de autenticación SSL/TLS.{RESET}\n")
        sys.exit(1)

    # Parametrización dinámica del botín VIP
    archivo_csv = input(f"{YELLOW}📁 Ingresa el archivo VIP a atacar (ej. Botin_VIP_Sinergy.csv): {RESET}").strip()
    
    if not os.path.exists(archivo_csv):
        print(f"\n{RED}⚠️ ERROR: No se encuentra el botín de datos '{archivo_csv}' en el perímetro.{RESET}\n")
        sys.exit(1)

    # ==========================================
    # 2. MUNICIÓN B2B (SYNERGY HUMAN & AI)
    # ==========================================
    asunto = "¿Su empresa está aprovechando la nueva ola de Inteligencia Artificial? / Propuesta Privada"
    cuerpo_base = """Hola, espero que se encuentren excelente.

Les escribo directamente porque desde Synergy Human & AI Agents hemos analizado el posicionamiento de su empresa y sabemos que tienen el perfil exacto para implementar lo que nosotros llamamos 'La Pecera'.

Actualmente, las empresas líderes no están buscando clientes uno por uno; están utilizando Agentes de Inteligencia Artificial para prospectar, filtrar y cerrar reuniones automáticamente, 24/7. Nosotros diseñamos e integramos estos Agentes a medida para que ustedes solo se sienten a hablar con clientes calificados y listos para comprar.

Me gustaría mostrarles, en una llamada de 10 minutos, cómo un Agente de IA puede integrarse en su modelo de negocio esta misma semana para multiplicar su capacidad operativa.

¿Tienen disponibilidad para una breve charla este miércoles o jueves?

Saludos cordiales,
Gabriel Tavella
Director de Synergy Human & AI Agents"""

    # ==========================================
    # 3. MOTOR DE DISPARO CON CENTINELA
    # ==========================================
    def motor_envio(destinatario, debug=False):
        try:
            msg = MIMEMultipart()
            msg['From'] = remitente
            msg['To'] = destinatario
            msg['Subject'] = asunto
            msg.attach(MIMEText(cuerpo_base, 'plain', 'utf-8'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            if debug: 
                server.set_debuglevel(1) 
                
            server.starttls()
            server.login(remitente, password)
            server.sendmail(remitente, destinatario, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(f"\n{RED}[!!!] FALLO ESTRUCTURAL EN TÚNEL SMTP: {e}{RESET}")
            return False

    # ==========================================
    # 4. PROTOCOLO DE SEGURIDAD
    # ==========================================
    print(f"\n{GRAY}[*] PASO 1: Verificación de salida hacia el CEO: {CORREO_CEO}{RESET}")
    confirmar_test = input(f"{YELLOW}¿Lanzar prueba de calidad ahora? (s/n): {RESET}").lower()
    
    if confirmar_test == 's':
        print(f"{GRAY}Estableciendo conexión TLS/SSL de Alta Seguridad...{RESET}")
        if motor_envio(CORREO_CEO, debug=True):
            print(f"\n{GREEN}{BOLD}✅ PRUEBA ENVIADA EXITOSAMENTE.{RESET}")
            
            luz_verde = input(f"\n{RED}{BOLD}¿Recibió el correo en Proton? Escriba 'SYNERGY' para liberar la lista VIP: {RESET}").upper()
            
            if luz_verde == 'SYNERGY':
                os.system('clear')
                print(f"{BLUE}{BOLD}{'='*65}{RESET}")
                print(f"{BLUE}{BOLD} 🚀 SEGURIDAD APROBADA. INICIANDO BARRIDO VIP. 🚀 {RESET}")
                print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
                
                try:
                    with open(archivo_csv, mode='r', encoding='utf-8') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            email_dest = row.get('Correo Electrónico', row.get('Email', '')).strip()
                            if not email_dest or email_dest == CORREO_CEO:
                                continue

                            print(f"{CYAN}\n🎯 OBJETIVO VIP FIJADO: {BOLD}{email_dest}{RESET}")
                            opcion = input(f"{YELLOW}👉 ¿Autoriza disparo? (s/n/salir): {RESET}").lower()
                            
                            if opcion == 's':
                                if motor_envio(email_dest):
                                    print(f"{GREEN}  ✓ IMPACTO CONFIRMADO EN {email_dest}. {GRAY}Enfriando cañones (10 segundos)...{RESET}")
                                    time.sleep(10)
                            elif opcion == 'salir':
                                print(f"\n{GRAY}💨 Abortando misión VIP a petición del Comandante.{RESET}\n")
                                break
                            else:
                                print(f"{GRAY}  >> Objetivo omitido.{RESET}")
                                
                    print(f"\n{GREEN}{BOLD}Misión de Outbound VIP finalizada.{RESET}\n")
                except Exception as e:
                    print(f"{RED}X Error de lectura en el botín CSV: {e}{RESET}")
            else:
                print(f"\n{YELLOW}❌ EL TEST SIGUE FALLANDO O LA CLAVE ES INCORRECTA. Revise la llave en su .env y la bandeja de entrada.{RESET}")
        else:
            print(f"{RED}X Fallo en el test de conexión.{RESET}")
    else:
        print(f"{GRAY}Operación cancelada.{RESET}")

if __name__ == "__main__":
    iniciar_hermes_vip()
