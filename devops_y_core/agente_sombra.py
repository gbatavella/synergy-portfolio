import psutil
import subprocess
import time
import os
import sys

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def iniciar_agente_sombra():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🥷 SYNERGY SHADOW AGENT (AIR-GAP DEAD MAN'S SWITCH) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # Verifica que el Arquitecto sea Root para manipular interfaces de red
    if os.geteuid() != 0:
        print(f"{RED}❌ [DENEGADO] El Sombra requiere permisos de Root para invocar el Air-Gap.{RESET}")
        print(f"{GRAY}>> Ejecútalo con: sudo python3 agente_sombra.py{RESET}\n")
        sys.exit(1)

    NOMBRE_PROCESO_CENTINELA = "agente_centinela.py"

    def verificar_centinela():
        """Escanea el árbol de procesos del Kernel buscando la firma del Centinela."""
        for proceso in psutil.process_iter(['cmdline']):
            try:
                # Comprobamos si la línea de comandos del proceso contiene nuestra firma
                if proceso.info['cmdline'] and any(NOMBRE_PROCESO_CENTINELA in cmd for cmd in proceso.info['cmdline']):
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Ignoramos procesos efímeros o protegidos del sistema
                pass
        return False

    def protocolo_aislamiento():
        """Corta todas las conexiones de red del Host (Air-Gapping)."""
        print(f"\n{RED}{BOLD}{'='*65}{RESET}")
        print(f"{RED}{BOLD} 🚨 [CRÍTICO] SE PERDIÓ LA SEÑAL DEL CENTINELA 🚨{RESET}")
        print(f"{RED}{BOLD}{'='*65}{RESET}\n")
        print(f"{YELLOW}[*] Posible compromiso del servidor detectado.{RESET}")
        print(f"{YELLOW}[*] Ejecutando protocolo de Hombre Muerto: Desconectando interfaces (AIR-GAP)...{RESET}")
        
        try:
            # Apaga todas las conexiones de red mediante NetworkManager
            subprocess.run(["nmcli", "networking", "off"], check=True)
            print(f"\n {GREEN}🛡️ MÁQUINA DESCONECTADA DE INTERNET. BÓVEDA LOCAL ASEGURADA.{RESET}")
            print(f" {GRAY}>> Para reactivar el enlace tras purgar la amenaza, ejecute manualmente:{RESET}")
            print(f" {WHITE}{BOLD}sudo nmcli networking on{RESET}\n")
        except Exception as e:
            print(f" {RED}❌ Fallo estructural al intentar aislar la red: {e}{RESET}")

    # ==========================================
    # BUCLE DE VIGILANCIA EN SIGILO
    # ==========================================
    print(f"{GRAY}[*] Operando en sigilo. Dando 5 segundos de ventaja al Centinela para arranque...{RESET}")
    time.sleep(5)
    
    # Comprobación inicial
    if not verificar_centinela():
        print(f"{RED}❌ [ERROR] El Centinela no está corriendo. Inícielo antes de desplegar al Sombra.{RESET}\n")
        sys.exit(1)

    print(f"{GREEN}[+] Enlace de supervisor establecido. Vigilando latido del Centinela.{RESET}\n")
    
    try:
        while True:
            if not verificar_centinela():
                protocolo_aislamiento()
                break # Sale del bucle y muere tras cortar la conexión (Misión Cumplida)
                
            # Sobrescribe la misma línea para telemetría limpia
            sys.stdout.write(f"\r{GRAY} 🥷 Patrullaje sombra: Centinela Activo. Sistema Seguro.{RESET} ")
            sys.stdout.flush()
            
            # Latencia de supervisión (3 segundos)
            time.sleep(3)
            
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}🛑 Operación Sombra cancelada por el Comandante.{RESET}\n")

if __name__ == "__main__":
    iniciar_agente_sombra()
