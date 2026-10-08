import os
import sys
import time
import socket
from dotenv import load_dotenv

# Manejo de error para asegurar que el entorno tenga scapy instalado
try:
    from scapy.all import ARP, Ether, srp
except ImportError:
    print("\033[91m❌ [ERROR] La librería 'scapy' no está instalada.\033[0m")
    print("\033[93m>> Ejecute: pip install scapy\033[0m")
    sys.exit(1)

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

# --- INICIALIZACIÓN DE SEGURIDAD ---
load_dotenv()

# Abstracción de la Lista Blanca (MAC Addresses) al .env
# Formato esperado en .env: LAN_WHITELIST="00:1A:2B:3C:4D:5E,11:22:33:44:55:66"
macs_autorizadas = os.getenv("LAN_WHITELIST", "")
lista_blanca = [mac.strip().upper() for mac in macs_autorizadas.split(",")] if macs_autorizadas else []

def obtener_ip_base():
    """Detecta el propio rango de red automáticamente a través de un socket dummy."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        partes = ip.split('.')
        return f"{partes[0]}.{partes[1]}.{partes[2]}.0/24"
    except Exception as e:
        print(f"{RED}❌ Error al derivar la IP de red local: {e}{RESET}")
        sys.exit(1)

def scan_network():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🛡️  SYNERGY LAN SENTINEL (ZERO-TRUST NETWORK RECON) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # Verificación de privilegios Root (scapy requiere acceso de bajo nivel a red)
    if os.geteuid() != 0:
        print(f"{YELLOW}⚠️ [ADVERTENCIA] Este motor intercepta tráfico de Capa 2 (ARP).{RESET}")
        print(f"{GRAY}>> Es probable que requiera privilegios elevados. Si falla, ejecute con 'sudo'.{RESET}\n")

    ip_range = obtener_ip_base()
    print(f"{GRAY}📡 [SISTEMA] Barriendo el perímetro y emitiendo paquetes ARP en: {BOLD}{ip_range}{RESET}...")
    
    # Construcción de la trama de red
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    print(f"{YELLOW}⏳ Disparando radar y esperando respuestas de hardware...{RESET}\n")
    try:
        # Disparamos el radar de red (timeout ajustable)
        result = srp(packet, timeout=3, verbose=0)[0]
    except PermissionError:
        print(f"{RED}❌ [DENEGADO] Permisos insuficientes para abrir sockets raw.{RESET}")
        print(f"{WHITE}>> Vuelva a ejecutar el motor como root: sudo python3 synergy_lan_sentinel.py{RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"{RED}❌ [ERROR DE RED] Falla en la inyección de paquetes: {e}{RESET}")
        sys.exit(1)

    print(f"{BLUE}{BOLD}🎯 REPORTE DE RADAR (Firmas Físicas Encontradas):{RESET}")
    print(f"{WHITE}{'-' * 70}{RESET}")
    print(f"{BOLD}{'DIRECCIÓN IP':<18} | {'HUELLA MAC (ÚNICA)':<20} | {'ESTADO DE CONFIANZA'}{RESET}")
    print(f"{WHITE}{'-' * 70}{RESET}")
    
    anomalias = 0
    for sent, received in result:
        ip_detectada = received.psrc
        mac_detectada = received.hwsrc.upper()
        
        if mac_detectada in lista_blanca:
            estado = f"{GREEN}✅ AUTORIZADO (Lista Blanca){RESET}"
        else:
            estado = f"{RED}⚠️ DESCONOCIDO (Posible Intrusión){RESET}"
            anomalias += 1
            
        print(f"{ip_detectada:<18} | {mac_detectada:<20} | {estado}")
    
    print(f"\n{GRAY}[*] Escaneo finalizado.{RESET}")
    if anomalias > 0:
        print(f"{RED}{BOLD}🚨 ALERTA: Se detectaron {anomalias} dispositivos no registrados en la red.{RESET}\n")
    else:
        print(f"{GREEN}{BOLD}🛡️ Perímetro seguro. Todos los nodos están autorizados.{RESET}\n")

if __name__ == "__main__":
    scan_network()
