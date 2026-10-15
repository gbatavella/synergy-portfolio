import requests
import sys

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def run_geo_pricing_agent():
    print(f"\n{BLUE}{BOLD}{'='*55}{RESET}")
    print(f"{BLUE}{BOLD} SYNERGY GEO-PRICING AGENT (LIVE FOREX ROUTER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*55}{RESET}\n")

    # API pública de Open Exchange Rates (Base USD)
    url = "https://open.er-api.com/v6/latest/USD"

    while True:
        try:
            print(f"{GRAY}[*] Esperando parámetros de cotización... (Escribe 'salir' para abortar){RESET}")
            entrada = input(f"{YELLOW} Precio Base del Producto (USD): {RESET}")
            
            if entrada.lower() in ['salir', 'exit', 'quit']:
                print(f"\n{GREEN} Apagando motor de Geo-Pricing.{RESET}\n")
                break
                
            base_price_usd = float(entrada)
            target_currency = input(f"{YELLOW} Moneda del Cliente (ej. EUR, GBP, ARS, MXN): {RESET}").upper()
            
            print(f"{GRAY}[*] Interrogando oráculo financiero en tiempo real...{RESET}")
            response = requests.get(url, timeout=5)
            data = response.json()
            
            if response.status_code == 200:
                rates = data.get("rates", {})
                
                if target_currency in rates:
                    exchange_rate = rates[target_currency]
                    final_price = round(base_price_usd * exchange_rate, 2)
                    
                    print(f"\n{GREEN}✓ Tasa de Cambio Activa: 1 USD = {exchange_rate} {target_currency}{RESET}")
                    print(f"{BLUE}{BOLD}>>> PRECIO FINAL LOCALIZADO: {final_price} {target_currency}{RESET}\n")
                else:
                    print(f"{RED}X Error: Divisa '{target_currency}' no soportada por el oráculo.{RESET}\n")
            else:
                print(f"{RED}X Error de red: No se pudo conectar a la base de datos financiera.{RESET}\n")
                
        except ValueError:
            print(f"{RED}X Error de sintaxis: Ingresa un valor numérico válido (ej. 197.50).{RESET}\n")
        except requests.exceptions.RequestException as e:
            print(f"{RED}X Fricción de red detectada: {e}{RESET}\n")

if __name__ == "__main__":
    run_geo_pricing_agent()
