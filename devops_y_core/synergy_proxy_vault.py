import requests
import os
import time
import sys
from datetime import datetime
from dotenv import load_dotenv

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

class ProxyVault:
    def __init__(self, proxy_config_path='proxies.json'):
        self.config_path = proxy_config_path
        self.history_file = 'ip_history_log.txt'
        
    def get_current_ip(self, proxies=None):
        """Verifica la firma digital (IP Externa) actual del motor."""
        try:
            response = requests.get('https://api.ipify.org?format=json', proxies=proxies, timeout=10)
            return response.json()['ip']
        except requests.exceptions.RequestException as e:
            return f"Error_Network_Timeout"
        except Exception as e:
            return f"Error_Unknown: {e}"

    def log_ip_usage(self, identity_name, ip_address):
        """Audita la IP asignada a una identidad para prevenir contaminación cruzada."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.history_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] IDENTITY_NODE: {identity_name} | EXTERNAL_IP: {ip_address}\n")
        print(f"{GREEN}✅ [OPSEC LOG] Firma {ip_address} blindada y asignada al avatar '{identity_name}'{RESET}")

    def test_connection(self, username, password, host, port):
        """Establece y testea el túnel HTTP/S a través de la red residencial."""
        proxy_url = f"http://{username}:{password}@{host}:{port}"
        proxies = {
            "http": proxy_url,
            "https": proxy_url,
        }
        
        print(f"{YELLOW}🔄 [ENRUTAMIENTO] Construyendo túnel a través del nodo: {host}:{port}...{RESET}")
        time.sleep(1)
        
        ip = self.get_current_ip(proxies)
        
        if "Error" not in ip:
            print(f"{BLUE}📡 [PRESENCIA VIRTUAL ESTABLECIDA] IP Camuflada: {ip}{RESET}")
            return proxies, ip
        else:
            print(f"{RED}❌ [FALLO DE ENRUTAMIENTO] El nodo residencial no responde. {ip}{RESET}")
            return None, None

if __name__ == "__main__":
    print(f"\n{BLUE}{BOLD}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD} 🛡️ SYNERGY PROXY VAULT (IDENTITY FARMING & OPSEC CORE) {RESET}")
    print(f"{BLUE}{BOLD}{'='*60}{RESET}\n")
    
    vault = ProxyVault()
    print(f"{GRAY}[*] Inicializando Bóveda de Red. Lista para asignación de Identidades.{RESET}\n")
    
    # Simulación de extracción de credenciales seguras (Protegiendo IPRoyal en GitHub)
    PROXY_USER = os.getenv("RESIDENTIAL_PROXY_USER")
    PROXY_PASS = os.getenv("RESIDENTIAL_PROXY_PASS")
    PROXY_HOST = os.getenv("RESIDENTIAL_PROXY_HOST", "geo.iproyal.com")
    PROXY_PORT = os.getenv("RESIDENTIAL_PROXY_PORT", "12321")
    
    # Interfaz de pruebas interactiva
    if PROXY_USER and PROXY_PASS:
        avatar_target = input(f"{YELLOW}🎯 Ingresa el Avatar a desplegar (ej. Norberto_Sintra_01): {RESET}").strip()
        
        if avatar_target:
            proxies_dict, ip_asignada = vault.test_connection(PROXY_USER, PROXY_PASS, PROXY_HOST, PROXY_PORT)
            
            if ip_asignada:
                vault.log_ip_usage(avatar_target, ip_asignada)
                print(f"\n{GREEN}{BOLD}🚀 El Avatar '{avatar_target}' está listo para operar de forma anónima.{RESET}\n")
    else:
        print(f"{RED}⚠️ Credenciales residenciales no detectadas en .env.{RESET}")
        print(f"{GRAY}>> Ejecución en modo simulado. Configure RESIDENTIAL_PROXY_USER para conectar.{RESET}\n")
