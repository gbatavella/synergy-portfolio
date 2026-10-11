import os
import time
import subprocess
import re
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

def iniciar_centinela():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🛡️ SYNERGY SENTINEL AGENT (UFW ACTIVE FIREWALL & IDS) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # Verifica que el Arquitecto sea Root
    if os.geteuid() != 0:
        print(f"{RED}❌ [DENEGADO] El Centinela requiere privilegios militares (Root).{RESET}")
        print(f"{GRAY}>> Ejecútalo con: sudo python3 agente_centinela.py{RESET}\n")
        sys.exit(1)

    ARCHIVO_LOG = "/var/log/auth.log"
    UMBRAL_FALLOS = 3
    intentos_fallidos = {}
    ips_bloqueadas = set()

    if not os.path.exists(ARCHIVO_LOG):
        print(f"{RED}❌ [ERROR] Archivo de auditoría no encontrado: {ARCHIVO_LOG}{RESET}")
        print(f"{GRAY}>> Este módulo está diseñado para entornos basados en Debian/Ubuntu.{RESET}\n")
        sys.exit(1)

    print(f"{GRAY}[*] Inicializando monitor de red. Vigilando puertos de la base de operaciones...{RESET}")

    def bloquear_ip(ip):
        """Despliega reglas de bloqueo en el firewall del kernel."""
        if ip not in ips_bloqueadas:
            print(f"\n{RED}{BOLD}🚨 [AMENAZA DETECTADA] IP {ip} superó el límite de fallos ({UMBRAL_FALLOS}).{RESET}")
            print(f"{YELLOW}[*] Levantando Muro Defensivo (UFW) contra {ip}...{RESET}")
            
            try:
                # Ejecuta el comando nativo de Linux para bloquear la IP
                subprocess.run(["ufw", "deny", "from", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                ips_bloqueadas.add(ip)
                print(f" {GREEN}✅ Enemigo bloqueado permanentemente a nivel OS.{RESET}")
            except Exception as e:
                print(f" {RED}❌ Fallo al levantar el escudo: {e}{RESET}")

    def vigilar_log():
        """Bucle infinito de lectura de logs (Tailing) con análisis Regex."""
        try:
            with open(ARCHIVO_LOG, "r") as log:
                # Mover el puntero al final del archivo
                log.seek(0, os.SEEK_END)
                print(f"{GREEN}[+] Sonda conectada al archivo de auditoría. Escuchando en tiempo real...{RESET}\n")
                
                while True:
                    linea = log.readline()
                    if not linea:
                        time.sleep(0.5)
                        continue
                    
                    # Firmas heurísticas de ataque SSH
                    if "Failed password" in linea or "Connection closed by authenticating user" in linea or "Invalid user" in linea:
                        # Extracción de IP atacante
                        match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', linea)
                        if match:
                            ip_atacante = match.group(0)
                            intentos_fallidos[ip_atacante] = intentos_fallidos.get(ip_atacante, 0) + 1
                            
                            # Log táctico en consola
                            print(f"{GRAY} ↳ Fricción detectada: {ip_atacante} (Intento {intentos_fallidos[ip_atacante]}/{UMBRAL_FALLOS}){RESET}")
                            
                            if intentos_fallidos[ip_atacante] >= UMBRAL_FALLOS:
                                bloquear_ip(ip_atacante)
                                
        except KeyboardInterrupt:
            print(f"\n{YELLOW}🛑 Operación cancelada por el Comandante. Apagando escudos...{RESET}\n")

    # Ejecutar la sonda
    vigilar_log()

if __name__ == "__main__":
    iniciar_centinela()
