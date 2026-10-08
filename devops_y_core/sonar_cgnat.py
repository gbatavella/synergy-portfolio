import subprocess
import requests
import time
import sys
import os
from dotenv import load_dotenv

# --- SEGURIDAD Y CONFIGURACIÓN ---
load_dotenv()

ISP_NAME = os.getenv("ISP_NAME", "Local ISP Node")
SYSTEM_NAME = os.getenv("SYSTEM_NAME", "Central Core")

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def rapid_output(text, delay=0.03):
    print(text)
    time.sleep(delay)

def detectar_cgnat():
    print(f"\n{BLUE}{BOLD}=============================================================={RESET}")
    print(f"{BLUE}{BOLD}  📡 SONAR ANTI-CGNAT: NETWORK RECON & ANTI-BAN PROTOCOL  {RESET}")
    print(f"{BLUE}{BOLD}=============================================================={RESET}\n")
    
    try:
        # 1. Obtener IP Pública
        rapid_output(f"{GRAY}[*] Interrogando APIs de resolución externa...{RESET}")
        ip_publica = requests.get('https://api.ipify.org').text
        rapid_output(f"{GREEN}🌐 IP Pública actual (Visible para {SYSTEM_NAME}): {ip_publica}{RESET}\n")

        # 2. Rastrear la ruta (Salto de red)
        rapid_output(f"{YELLOW}⏳ Disparando pulso de rastreo ICMP hacia {ISP_NAME}...{RESET}")
        
        # Ejecutamos traceroute a los servidores de Google para ver el camino
        # Nota: Requiere entorno Linux/WSL con 'traceroute' instalado
        resultado = subprocess.run(['traceroute', '-n', '-m', '3', '8.8.8.8'], capture_output=True, text=True)
        lineas = resultado.stdout.split('\n')

        if len(lineas) > 2:
            # Analizamos el segundo salto (la antena/nodo del ISP)
            salto_2 = lineas[2]
            rapid_output(f"{BLUE}📍 Coordenadas del Salto 2 (ISP Gate): {salto_2.strip()}{RESET}")

            # Identificación de rangos CGNAT o Privados (RFC 1918 / RFC 6598)
            if " 100." in salto_2 or " 10." in salto_2 or " 172." in salto_2 or " 192.168." in salto_2:
                print(f"\n{RED}{BOLD}🛑 DICTAMEN: INFRAESTRUCTURA BAJO CGNAT (CARRIER-GRADE NAT).{RESET}")
                print(f"{RED}>> Peligro de IP Compartida: Tus vecinos utilizan tu misma firma pública.{RESET}")
                print(f"{GRAY}>> Táctica: Reiniciar el router NO cambiará la IP pública. Para blanquearla con Microsoft/Google, deberás esperar TTL (24h) o rotar Proxies.{RESET}")
            else:
                print(f"\n{GREEN}{BOLD}✅ DICTAMEN: IP PÚBLICA DIRECTA (NO CGNAT). CONEXIÓN LIMPIA.{RESET}")
                print(f"{GREEN}>> Táctica: Si los envíos son bloqueados, apagar el router de {ISP_NAME} por 5 minutos forzará un cambio de IP, evadiendo el baneo.{RESET}")
        else:
            print(f"\n{RED}⚠️ El pulso de rastreo fue bloqueado por un Firewall (ICMP Drop). No se pudo determinar topología.{RESET}")

    except FileNotFoundError:
        print(f"\n{RED}❌ Error Crítico: Módulo 'traceroute' no detectado en el sistema.{RESET}")
        print(f"{GRAY}>> Solución: Ejecuta 'sudo apt install traceroute' en tu terminal Linux/WSL.{RESET}")
    except Exception as e:
        print(f"\n{RED}❌ Error en los sensores del Sonar: {e}{RESET}")

if __name__ == "__main__":
    detectar_cgnat()
