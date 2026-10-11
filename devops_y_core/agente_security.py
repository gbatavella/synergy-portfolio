import imaplib
import os
import time
import subprocess
import sys
from datetime import datetime, timedelta
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

def iniciar_watchdog():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🛡️ SYNERGY WATCHDOG (IMAP SECURITY & KILL SWITCH) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÓVEDA SEGURA (OPSEC)
    # ==========================================
    load_dotenv()
    EMAIL = os.getenv("IMAP_USER")
    PASSWORD = os.getenv("IMAP_APP_PASSWORD")
    IMAP_SERVER = os.getenv("IMAP_HOST", "imap.gmail.com")

    if not all([EMAIL, PASSWORD]):
        print(f"{RED}❌ [ERROR CRÍTICO] Faltan credenciales IMAP (IMAP_USER/IMAP_APP_PASSWORD) en la bóveda .env.{RESET}")
        sys.exit(1)

    # UMBRALES DE EMERGENCIA
    LIMITE_REBOTES = 3  
    VENTANA_TIEMPO = 15 # Minutos de retrospectiva
    PROCESO_OBJETIVO = "hermes_sniper.py" # Cambiar por el nombre de tu agente de envío activo (ej. agente_trafficker_v5.py)

    def buscar_rebotes_recientes():
        """Se conecta al servidor IMAP y cuenta la densidad de rebotes del Mailer-Daemon."""
        try:
            mail = imaplib.IMAP4_SSL(IMAP_SERVER)
            mail.login(EMAIL, PASSWORD)
            mail.select("inbox")

            # Cálculo de ventana retrospectiva en formato IMAP
            desde_cuando = (datetime.now() - timedelta(minutes=VENTANA_TIEMPO)).strftime("%d-%b-%Y")
            
            # Filtro restrictivo directo en el servidor
            status, mensajes = mail.search(None, f'(FROM "mailer-daemon@googlemail.com" SINCE {desde_cuando})')
            
            if mensajes[0]:
                ids = mensajes[0].split()
                total_rebotes = len(ids)
            else:
                total_rebotes = 0
                
            mail.logout()
            return total_rebotes
            
        except Exception as e:
            print(f" {RED}❌ Fricción en el enlace IMAP: {e}{RESET}")
            return 0

    def abortar_mision():
        """Protocolo de interrupción de procesos (Dead Man's Switch)."""
        print(f"\n{RED}{BOLD}{'='*65}{RESET}")
        print(f"{RED}{BOLD} 🚨 [ALERTA CRÍTICA] UMBRAL DE TOXICIDAD SUPERADO 🚨{RESET}")
        print(f"{RED}{BOLD}{'='*65}{RESET}\n")
        print(f"{YELLOW}[*] Ejecutando protocolo de emergencia: Aniquilando enjambres emisores...{RESET}")
        
        # Intervención a nivel Kernel (pkill)
        try:
            resultado = subprocess.run(["pkill", "-f", PROCESO_OBJETIVO], capture_output=True, text=True)
            if resultado.returncode == 0:
                print(f" {GREEN}✅ OPERACIÓN ABORTADA. El proceso [{PROCESO_OBJETIVO}] ha sido neutralizado con éxito.{RESET}")
            else:
                print(f" {GRAY}⚠️ El proceso [{PROCESO_OBJETIVO}] no estaba en ejecución o ya colapsó.{RESET}")
        except Exception as e:
            print(f" {RED}❌ Fallo estructural al intentar invocar pkill: {e}{RESET}")

        print(f" {CYAN}📢 Notificando a Goalkeeper para reporte de telemetría a Telegram...{RESET}\n")

    # ==========================================
    # BUCLE DE EJECUCIÓN (DAEMON)
    # ==========================================
    print(f"{GREEN}[+] Sonda IMAP armada y enlazada.{RESET}")
    print(f"{GRAY}[*] Iniciando patrullaje. (Límite crítico: {BOLD}{LIMITE_REBOTES}{RESET}{GRAY} rebotes cada {VENTANA_TIEMPO} min){RESET}\n")
    
    try:
        while True:
            ahora = datetime.now().strftime("%H:%M:%S")
            conteo = buscar_rebotes_recientes()
            
            if conteo >= LIMITE_REBOTES:
                print(f"\r{RED}[{ahora}] 🚩 PELIGRO: Se detectaron {conteo} rebotes en la matriz.{RESET}")
                abortar_mision()
                break # El guardia finaliza su turno tras activar el botón rojo
            else:
                sys.stdout.write(f"\r{GREEN}[{ahora}] ✅ Ecosistema estable. Rebotes detectados: {conteo}    {RESET}")
                sys.stdout.flush()
                
            # Latencia táctica (5 minutos)
            time.sleep(300)
            
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}🛑 Operación cancelada por el Comandante. Guardián retirado.{RESET}\n")

if __name__ == "__main__":
    iniciar_watchdog()
