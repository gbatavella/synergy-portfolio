import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def ejecutar_prueba_balistica():
    print(f"\n{RED}{BOLD}{'='*65}{RESET}")
    print(f"{RED}{BOLD} 🎯 SYNERGY SMTP BALLISTIC TEST (ZERO-FRICTION PAYLOAD) {RESET}")
    print(f"{RED}{BOLD}{'='*65}{RESET}\n")
    
    # 1. CARGA DE BÓVEDA (OPSEC Strict)
    load_dotenv()
    
    remitente = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASS")
    servidor_smtp = os.getenv("SMTP_HOST", "mail.privateemail.com")
    puerto_smtp = int(os.getenv("SMTP_PORT", "587"))
    destinatario = os.getenv("SMTP_TEST_TARGET", "test@synergy-labs.com")
    
    if not remitente or not password:
        print(f"{RED}❌ [ERROR CRÍTICO] Faltan credenciales SMTP_USER o SMTP_PASS en el .env.{RESET}")
        print(f"{GRAY}>> Abortando disparo para proteger la infraestructura.{RESET}\n")
        sys.exit(1)

    print(f"{GRAY}[*] Enlazando con el silo de lanzamiento: {servidor_smtp}:{puerto_smtp}...{RESET}")
    
    # 2. CARGANDO LA MUNICIÓN Y LA FIRMA
    asunto = "fintech growth"
    cuerpo = """Hi Taylor,

We deployed a Swarm Protocol (autonomous AI agents) that handles 24/7 outbound prospecting for companies like American Fintech Council.
Mind if I send a 2-min video showing how we fill your pipeline?

Gabriel Tavella
Founder & CEO | Synergy (Human & AI Agents)"""

    print(f"{CYAN}>> Ensamblando misil MIME (Payload: {asunto})...{RESET}")

    # 3. ENSAMBLANDO EL MISIL
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

    # 4. LANZAMIENTO
    try:
        print(f"{YELLOW}⏳ Iniciando secuencia de ignición STARTTLS...{RESET}")
        servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
        servidor.starttls() 
        servidor.login(remitente, password)
        servidor.send_message(msg)
        servidor.quit()
        print(f"{GREEN}{BOLD}✅ IMPACTO CONFIRMADO: El payload atravesó las defensas. Revisa la bandeja de entrada de {destinatario}.{RESET}\n")
    except smtplib.SMTPAuthenticationError:
        print(f"\n{RED}❌ FALLO DE AUTENTICACIÓN: El servidor rechazó las credenciales.{RESET}")
        print(f"{GRAY}>> Verifica tu SMTP_USER y SMTP_PASS en el archivo .env.{RESET}\n")
    except Exception as e:
        print(f"\n{RED}❌ FALLO DE IGNICIÓN. Detalle técnico: {e}{RESET}\n")

if __name__ == "__main__":
    ejecutar_prueba_balistica()
