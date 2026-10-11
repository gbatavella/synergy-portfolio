import time
import requests
import os
import sys
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def iniciar_custodio():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🛡️ SYNERGY CUSTODIAN AGENT (FINOPS & TELEGRAM ALERTER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # EXTRACCIÓN SEGURA DE CREDENCIALES (OPSEC)
    # ==========================================
    load_dotenv()
    
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    GUMROAD_TOKEN = os.getenv("GUMROAD_TOKEN")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    if not all([OPENROUTER_API_KEY, GUMROAD_TOKEN, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID]):
        print(f"{RED}❌ [ERROR CRÍTICO] Faltan credenciales financieras o de Telegram en el archivo .env.{RESET}")
        print(f"{GRAY}>> Abortando inicio del Custodio para prevenir falsos positivos.{RESET}\n")
        sys.exit(1)

    # Memoria para no repetir alertas de la misma venta
    ventas_procesadas = set()

    def enviar_alerta(mensaje):
        """Despacha notificaciones Push vía Telegram."""
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje}
        try:
            requests.post(url, json=payload, timeout=10)
            print(f"{GRAY} ↳ 📲 Alerta enviada al canal seguro de Telegram.{RESET}")
        except Exception as e:
            print(f"{RED} ❌ Error de red al comunicar con Telegram: {e}{RESET}")

    def revisar_finanzas():
        """Audita el flujo de caja: Costos (OpenRouter) e Ingresos (Gumroad)."""
        print(f"\n{GRAY}[*] Iniciando barrido de auditoría financiera...{RESET}")

        # 1. Vigilancia de Gasto Operativo (OpenRouter)
        headers_or = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}
        try:
            res_or = requests.get("https://openrouter.ai/api/v1/credits", headers=headers_or, timeout=10)
            if res_or.status_code == 200:
                data = res_or.json()
                creditos_restantes = data.get("total_credits", 0)
                print(f" {CYAN}💰 Liquidez IA (OpenRouter): {BOLD}${creditos_restantes:.2f}{RESET}")
                
                # Disyuntor financiero (Umbral de seguridad)
                if creditos_restantes < 5.0:
                    alerta_or = f"⚠️ [SYNERGY ALERTA] Liquidez de OpenRouter crítica: ${creditos_restantes:.2f}. Recarga requerida para evitar caída del enjambre."
                    print(f" {RED}! Nivel crítico alcanzado.{RESET}")
                    enviar_alerta(alerta_or)
            else:
                print(f" {YELLOW}⚠️ Fricción al leer OpenRouter (HTTP {res_or.status_code}).{RESET}")
        except Exception as e:
            print(f" {RED}❌ Timeout en conexión con OpenRouter: {e}{RESET}")

        # 2. Radar de Ingresos (Gumroad)
        headers_gum = {"Authorization": f"Bearer {GUMROAD_TOKEN}"}
        try:
            res_gum = requests.get("https://api.gumroad.com/v2/sales", headers=headers_gum, timeout=10)
            if res_gum.status_code == 200:
                ventas = res_gum.json().get("sales", [])
                
                nuevas_ventas = 0
                for venta in ventas:
                    id_venta = venta.get('id')
                    if id_venta not in ventas_procesadas:
                        precio = venta.get('price', 0) / 100
                        producto = venta.get('product_name', 'Synergy Product')
                        
                        alerta_gum = f"💵 [NUEVO INGRESO] Venta detectada: {producto} por ${precio:.2f}"
                        enviar_alerta(alerta_gum)
                        
                        ventas_procesadas.add(id_venta)
                        nuevas_ventas += 1
                
                if nuevas_ventas > 0:
                    print(f" {GREEN}✅ Se registraron {nuevas_ventas} nuevas transacciones de entrada.{RESET}")
                else:
                    print(f" {GRAY}✅ Perímetro de ventas limpio. Sin nuevas transacciones.{RESET}")
            else:
                print(f" {YELLOW}⚠️ Fricción al leer Gumroad (HTTP {res_gum.status_code}).{RESET}")
        except Exception as e:
            print(f" {RED}❌ Timeout en conexión con Gumroad: {e}{RESET}")

    # ==========================================
    # BUCLE DE EJECUCIÓN (DAEMON)
    # ==========================================
    print(f"{GREEN}[+] Custodio en línea. Entrando en modo vigilancia perimetral...{RESET}\n")
    try:
        while True:
            revisar_finanzas()
            print(f"\n{GRAY}⏳ El Custodio entra en hibernación. Próximo escaneo en 60 minutos...{RESET}")
            time.sleep(3600)  # Ciclo de 1 hora
    except KeyboardInterrupt:
        print(f"\n{YELLOW}🛑 Operación cancelada por el Comandante. Apagando sensores.{RESET}\n")

if __name__ == "__main__":
    iniciar_custodio()
