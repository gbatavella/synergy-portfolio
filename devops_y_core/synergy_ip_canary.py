import requests
import os
import sys
from datetime import datetime

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def check_canary():
    """
    Synergy IP Canary: Guardián de Huella Digital Operativa.
    Audita la IP pública y previene la contaminación cruzada de identidades.
    """
    HISTORY_FILE = 'ip_history_log.txt'
    
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🛡️ SYNERGY IP CANARY (IDENTITY FOOTPRINT GUARD) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    print(f"{GRAY}[*] Iniciando protocolo de telemetría de red. Escaneando túnel de salida...{RESET}")
    
    try:
        # Resolución de IP pública cruda
        current_ip = requests.get('https://api.ipify.org', timeout=10).text.strip()
        print(f"{CYAN}📡 Firma de Red Detectada (External IP): {BOLD}{current_ip}{RESET}\n")
    except requests.exceptions.RequestException as e:
        print(f"{RED}❌ [ERROR CRÍTICO] Falla de conexión. No se puede validar la huella de red: {e}{RESET}")
        print(f"{YELLOW}>> Revise su conexión a internet o la configuración de su VPN/Proxy.{RESET}\n")
        sys.exit(1)

    # Evaluación de Contaminación Cruzada
    print(f"{GRAY}[*] Cruzando datos con la bóveda histórica de identidades...{RESET}")
    
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                history = f.read()
                
            if current_ip in history:
                print(f"{RED}{BOLD}⚠️ [PELIGRO OPSEC] COLISIÓN DETECTADA: Esta IP ya fue 'quemada' previamente.{RESET}")
                print(f"{YELLOW}>> ACCIÓN REQUERIDA: Cambie su nodo Proxy, VPN o reinicie el router para forzar una nueva IP antes de operar.{RESET}\n")
            else:
                print(f"{GREEN}✅ [VÍA LIBRE] IP Virgen confirmada. Cero riesgo de contaminación cruzada.{RESET}")
                registrar_huella(HISTORY_FILE, current_ip)
                
        except Exception as e:
            print(f"{RED}❌ Error al leer la bóveda histórica: {e}{RESET}")
    else:
        print(f"{YELLOW}ℹ️ Bóveda histórica no detectada. Inicializando el primer registro operativo...{RESET}")
        registrar_huella(HISTORY_FILE, current_ip)

def registrar_huella(archivo, ip):
    """Sella la IP en la bitácora inmutable."""
    try:
        with open(archivo, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] Canary OPSEC Check | IP_LOCKED: {ip}\n")
        print(f"{GRAY}>> Firma {ip} registrada en la bitácora '{archivo}'.{RESET}\n")
    except Exception as e:
        print(f"{RED}❌ Falla al escribir en la bitácora: {e}{RESET}\n")

if __name__ == "__main__":
    check_canary()
