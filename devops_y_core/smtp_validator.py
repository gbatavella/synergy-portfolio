import os
import sys
import smtplib
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def validar_smtp():
    print(f"\n{BLUE}{BOLD}{'='*55}{RESET}")
    print(f"{BLUE}{BOLD} 🔐 SYNERGY SMTP VALIDATOR (GMAIL INFRASTRUCTURE) {RESET}")
    print(f"{BLUE}{BOLD}{'='*55}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÚNKER (OPSEC)
    # ==========================================
    print(f"{GRAY}[*] Accediendo a la bóveda .env...{RESET}")
    load_dotenv()
    
    REMITENTE = os.getenv("SMTP_EMAIL")
    PASSWORD = os.getenv("SMTP_PASSWORD")

    if not REMITENTE or not PASSWORD:
        print(f"{RED}❌ [ERROR CRÍTICO] Faltan credenciales SMTP (SMTP_EMAIL o SMTP_PASSWORD) en la bóveda .env.{RESET}")
        sys.exit(1)

    # ==========================================
    # 2. PRUEBA DE CONEXIÓN Y AUTENTICACIÓN
    # ==========================================
    print(f"{GRAY}[*] Iniciando handshake con smtp.gmail.com en puerto 587...{RESET}")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(REMITENTE, PASSWORD)
        print(f"\n{GREEN}✅ ¡CONEXIÓN EXITOSA!{RESET}")
        print(f"{GREEN}La llave es válida y el motor tiene permiso para disparar desde: {BOLD}{REMITENTE}{RESET}\n")
        server.quit()
    except Exception as e:
        print(f"\n{RED}❌ ACCESO DENEGADO. Error de conexión:{RESET} {e}")
        print(f"{YELLOW}👉 Diagnóstico: Asegúrate de que la 'Contraseña de Aplicación' esté activa y sin espacios en tu .env.{RESET}\n")

if __name__ == "__main__":
    validar_smtp()
