import smtplib
import time
import random
import os
import sys
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- SEGURIDAD Y CONFIGURACIÓN ---
load_dotenv()

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def iniciar_goalkeeper():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧤 SYNERGY GOALKEEPER SENDER (PROTON E2EE EDITION) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # Configuración de Mando (Extraída del .env para OPSEC)
    PROTON_USER = os.getenv("PROTON_USER")
    # La clave que te da el Bridge local, NO tu clave de login de cuenta
    PROTON_PASS = os.getenv("PROTON_BRIDGE_PASS") 
    SMTP_SERVER = os.getenv("PROTON_BRIDGE_HOST", "127.0.0.1") 
    SMTP_PORT = int(os.getenv("PROTON_BRIDGE_PORT", "1025")) 

    if not PROTON_USER or not PROTON_PASS:
        print(f"{RED}❌ [ERROR CRÍTICO] Credenciales de Proton Bridge no encontradas en .env.{RESET}")
        sys.exit(1)

    print(f"{GRAY}[*] Enlazando con Proton Mail Bridge en {SMTP_SERVER}:{SMTP_PORT}...{RESET}")

    def send_targeted_email(target_email, target_name, target_firm):
        msg = MIMEMultipart()
        msg['From'] = f"Gabriel Alejandro Tavella <{PROTON_USER}>"
        msg['To'] = target_email
        msg['Subject'] = f"{target_name} — Mandate Origination vs. Analyst Burnout"

        body = f"""Dear {target_name},

I’ve been tracking your recent activity at {target_firm}. In the current climate, I know the primary bottleneck isn't capital—it's Sell-side Mandate Origination.

We’ve developed an AI-led ecosystem specifically for M&A that automates high-conviction prospecting and slashes Due Diligence cycles by 60%.

Do you have 7 minutes this Thursday to discuss how we’re injecting automated Deal Flow into your pipeline?

Best regards,

Gabriel Alejandro Tavella
President, Tavsol S.A. | Synergy AI Labs
"""
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Enrutamiento hacia el túnel local cifrado
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(PROTON_USER, PROTON_PASS)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"{RED}  ❌ Fricción en el servidor local al enviar a {target_name}: {e}{RESET}")
            return False

    # --- ASALTO PERSONALIZADO (DATOS DE DEMOSTRACIÓN B2B) ---
    objetivos = [
        {"nombre": "Andres R.", "email": "andres.r@ejemplo-b2b.com", "cargo": "Financial Advisor at Apex Partners"},
        {"nombre": "John K.", "email": "john.k@ejemplo-b2b.com", "cargo": "Managing Director at Apex Partners"}
    ]
    
    print(f"\n{YELLOW}🚀 [SISTEMA] Iniciando secuencia de asalto aéreo...{RESET}\n")
    
    for obj in objetivos:
        if obj["email"] == "PROXIMO_PASO" or "ejemplo" in obj["email"]:
            print(f"{GRAY}🔍 Modo Demo: Saltando envío real para {obj['nombre']} ({obj['email']})...{RESET}")
            continue
            
        print(f"{CYAN}>> Preparando payload para {BOLD}{obj['nombre']}{RESET}...")
        
        if send_targeted_email(obj["email"], obj["nombre"], obj["cargo"]):
            print(f"{GREEN}  ✅ ¡Impacto confirmado en la bandeja de {obj['nombre']}!{RESET}")
            
            pausa = random.randint(60, 120)
            print(f"{GRAY}  ⏳ Inyectando pausa táctica anti-spam ({pausa}s)...{RESET}")
            time.sleep(pausa) 
            
    print(f"\n{BLUE}[*] Operación de despliegue finalizada. Cerrando túnel SMTP.{RESET}\n")

if __name__ == "__main__":
    iniciar_goalkeeper()
