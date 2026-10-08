import os
import sys
import time
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

def obtener_config_proxy():
    """
    Extrae las credenciales de red del entorno (ej. IPRoyal) 
    y formatea la cadena de conexión autenticada para el navegador.
    """
    user = os.getenv("RESIDENTIAL_PROXY_USER")
    password = os.getenv("RESIDENTIAL_PROXY_PASS")
    proxy_url = os.getenv("RESIDENTIAL_PROXY_HOST_PORT") # Ejemplo: geo.iproyal.com:12321

    if not all([user, password, proxy_url]):
        print(f"{RED}⚠️ [OPSEC WARNING] Credenciales de red incompletas en el archivo .env.{RESET}")
        print(f"{GRAY}>> El motor operará con la IP pública expuesta del host.{RESET}")
        return None

    # Formato estándar para Selenium/Undetected Chromedriver
    proxy_config = f"http://{user}:{password}@{proxy_url}"
    return proxy_config

def inyectar_proxy_en_ares(options):
    """
    Middleware: Recibe las opciones nativas de Chrome/Firefox 
    y muta el objeto inyectando el camuflaje de red.
    """
    proxy = obtener_config_proxy()
    if proxy:
        print(f"{BLUE}🛡️ [MIDDLEWARE ARES] Escudo de Invisibilidad Acoplado.{RESET}")
        print(f"{GRAY}>> Enrutando tráfico a través del nodo residencial seguro...{RESET}")
        options.add_argument(f'--proxy-server={proxy}')
    return options

if __name__ == "__main__":
    # --- PRUEBA UNITARIA DEL MIDDLEWARE EN TERMINAL ---
    print(f"\n{BLUE}{BOLD}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD} 🔌 SYNERGY PROXY INJECTOR (ARES MIDDLEWARE) - UNIT TEST {RESET}")
    print(f"{BLUE}{BOLD}{'='*60}{RESET}\n")
    
    print(f"{YELLOW}[*] Simulando instanciación de ChromeOptions...{RESET}")
    time.sleep(1)
    
    # Creamos un objeto dummy para simular el comportamiento de uc.ChromeOptions()
    class DummyOptions:
        def __init__(self):
            self.arguments = []
        def add_argument(self, arg):
            self.arguments.append(arg)
            
    opciones_simuladas = DummyOptions()
    
    print(f"{GRAY}[*] Invocando inyector de red...{RESET}\n")
    opciones_mutadas = inyectar_proxy_en_ares(opciones_simuladas)
    
    print(f"\n{GREEN}{BOLD}✅ DIAGNÓSTICO DEL OBJETO MUTADO:{RESET}")
    if opciones_mutadas.arguments:
        print(f"{WHITE}Argumentos inyectados en el binario:{RESET}")
        for arg in opciones_mutadas.arguments:
            # Enmascaramos la contraseña en la salida de consola por seguridad
            if "://" in arg and "@" in arg:
                safe_arg = arg.split("://")[0] + "://[HIDDEN_CREDENTIALS]@" + arg.split("@")[1]
                print(f"{GREEN} -> {safe_arg}{RESET}")
            else:
                print(f"{GREEN} -> {arg}{RESET}")
    else:
        print(f"{RED} -> Ningún argumento inyectado (Verifique el .env).{RESET}")
    print("\n")
