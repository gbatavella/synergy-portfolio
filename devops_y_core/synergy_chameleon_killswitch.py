import time
import requests
import os
import sys
import subprocess
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

# =====================================================================
# CONFIGURACIÓN OPSEC: AISLAMIENTO DE IP REAL
# =====================================================================
load_dotenv()
IP_REAL_PELIGRO = os.getenv("HOST_REAL_IP")

def obtener_ip_actual():
    """Interroga la red para obtener la IP pública de salida."""
    try:
        respuesta = requests.get('https://api.ipify.org', timeout=5)
        return respuesta.text.strip()
    except requests.RequestException:
        return None

def activar_kill_switch():
    """Protocolo de Autodestrucción Selectiva."""
    print(f"\n{RED}{BOLD}{'='*65}{RESET}")
    print(f"{RED}{BOLD} 🚨 [ALERTA ROJA CRÍTICA] ¡FUGA DE RED DETECTADA! 🚨{RESET}")
    print(f"{RED}{BOLD} 🚨 LA IP MATRIZ ESTÁ EXPUESTA. TÚNEL COMPROMETIDO. 🚨{RESET}")
    print(f"{RED}{BOLD}{'='*65}{RESET}\n")
    
    print(f"{YELLOW}[*] Ejecutando Francotirador Camaleón. Aniquilando contenedores...{RESET}")
    
    # Asesina SOLO los perfiles de los agentes (Aislamiento de Procesos POSIX)
    # Se utiliza subprocess para evitar inyecciones en shell
    avatares_activos = ["Norberto", "Diego_Samsung", "Luis", "Marita"]
    
    for avatar in avatares_activos:
        try:
            # Comando: pkill -f 'firefox.*-P NombrePerfil'
            subprocess.run(['pkill', '-f', f'firefox.*-P {avatar}'], check=False)
            print(f"{GRAY}   ↳ Perfil [{avatar}] neutralizado.{RESET}")
        except Exception as e:
            print(f"{RED}   ↳ Error al neutralizar [{avatar}]: {e}{RESET}")
            
    print(f"\n{GREEN}{BOLD}🛡️ [ESTADO] Contenedores operativos destruidos. Identidades protegidas.{RESET}")
    print(f"{CYAN}{BOLD}💻 [ESTADO] Tu sesión personal (Host Browser) sigue viva e intacta.{RESET}")
    print(f"{GRAY}>> Abortando hilo de ejecución.{RESET}\n")
    sys.exit(1)

def iniciar_auditoria_continua():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🦎 SYNERGY CHAMELEON (SELECTIVE KILL SWITCH) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    if not IP_REAL_PELIGRO:
        print(f"{RED}❌ [ERROR OPSEC] La variable HOST_REAL_IP no está configurada en la bóveda .env.{RESET}")
        print(f"{GRAY}>> Es imperativo definir la IP a evitar antes de patrullar.{RESET}\n")
        sys.exit(1)

    print(f"{CYAN}📡 Iniciando Agente Camaleón (Modo Francotirador)...{RESET}")
    # Ocultamos parte de la IP en la consola para no exponerla en capturas de pantalla
    ip_oculta = ".".join(IP_REAL_PELIGRO.split(".")[:2]) + ".***.***"
    print(f"{GRAY}👁️ Vigilando estrictamente que la IP NO retroceda a la matriz: {BOLD}{ip_oculta}{RESET}\n")
    
    try:
        while True:
            ip_actual = obtener_ip_actual()
            
            if ip_actual:
                if ip_actual == IP_REAL_PELIGRO:
                    activar_kill_switch()
                else:
                    # Sobrescribe la misma línea en la terminal para no saturar el log
                    sys.stdout.write(f"\r{GREEN}   ✅ [TÚNEL SEGURO] Operando bajo IP enmascarada: {BOLD}{ip_actual}{RESET}   ")
                    sys.stdout.flush()
            else:
                sys.stdout.write(f"\r{YELLOW}   ⚠️ [ESPERA] Fricción de red. Verificando...{RESET}                 ")
                sys.stdout.flush()
                
            time.sleep(5)
            
    except KeyboardInterrupt:
        print(f"\n\n{GRAY}🛑 Protocolo Camaleón desactivado manualmente por el operador.{RESET}\n")

if __name__ == "__main__":
    iniciar_auditoria_continua()
