import os
import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
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

load_dotenv()

def desplegar_norberto(modo_fantasma=False):
    """
    Protocolo Norberto: Despliega Firefox con perfil aislado,
    blindaje anti-fugas WebRTC y silenciador de errores gráficos.
    """
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🛡️ PROTOCOLO NORBERTO (FIREFOX WEBRTC HARDENING) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # Ruta dinámica del perfil basada en variables de entorno o fallback seguro
    perfil_defecto = "~/.mozilla/firefox/hptk86m8.Norberto Zinta Devito"
    ruta_perfil_norberto = os.path.expanduser(os.getenv(
        "FIREFOX_PROFILE_PATH", 
        perfil_defecto
    ))
    
    opciones = Options()
    
    if os.path.exists(ruta_perfil_norberto):
        opciones.add_argument("-profile")
        opciones.add_argument(ruta_perfil_norberto)
        print(f"{GRAY}[*] Perfil persistente enlazado:{RESET} {BOLD}{ruta_perfil_norberto}{RESET}")
    else:
        print(f"{YELLOW}⚠️ [ADVERTENCIA] Ruta de perfil no localizada. Desplegando perfil efímero limpio.{RESET}")
    
    # ---------------------------------------------------------
    # 🛡️ BLINDAJE DE RED Y CHAMÁN (WebRTC & DNS Defense)
    # ---------------------------------------------------------
    # 1. Aniquilación de WebRTC para evitar fugas de IP real
    opciones.set_preference("media.peerconnection.enabled", False)
    opciones.set_preference("media.navigator.enabled", False)
    
    # 2. Sellar fugas de DNS forzando el tráfico a través del Proxy SOCKS
    opciones.set_preference("network.proxy.socks_remote_dns", True)
    opciones.set_preference("network.dns.disablePrefetch", True)

    # 3. Supresión de logs basura de Linux (Headless / GPU flags)
    os.environ['MOZ_HEADLESS_DISABLE_XSS'] = '1'
    opciones.add_argument("--disable-gpu") 

    if modo_fantasma:
        opciones.add_argument("--headless")
        print(f"{YELLOW}👻 [MODO FANTASMA] Instancia de Norberto ejecutándose en segundo plano (Headless).{RESET}")
        
    try:
        print(f"{GREEN}[+] Inicializando Enjambre: Motor de aislamiento preparado...{RESET}")
        
        # Redirigir la telemetría de errores del driver a devnull
        servicio = Service(log_output=os.devnull)
        
        driver = webdriver.Firefox(options=opciones, service=servicio)
        print(f"{GREEN}{BOLD}✅ TÚNEL ESTABLECIDO: Norberto operativo y blindado.{RESET}\n")
        return driver
        
    except Exception as e:
        print(f"\n{RED}❌ [ERROR CRÍTICO] Fallo en el despliegue del Protocolo Norberto: {e}{RESET}")
        print(f"{GRAY}>> Verifique que Geckodriver y Firefox estén correctamente instalados en el entorno.{RESET}\n")
        return None

if __name__ == "__main__":
    # Prueba unitaria de despliegue si se ejecuta directamente
    d = desplegar_norberto(modo_fantasma=True)
    if d:
        print(f"{GRAY}[*] Ejecutando prueba de humo en Google...{RESET}")
        d.get("https://www.google.com")
        print(f"{GREEN}[OK] Título obtenido: {d.title}{RESET}")
        d.quit()
        print(f"{GRAY}[*] Instancia cerrada con éxito.{RESET}\n")
