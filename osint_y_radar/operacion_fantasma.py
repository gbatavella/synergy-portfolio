from playwright.sync_api import sync_playwright
import json
import os
import sys
from datetime import datetime

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

KEYWORDS = ["conversion", "pricing", "stripe", "purchasing power", "churn", "sales dropped"]

def operacion_fantasma_hitl():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} SYNERGY GHOST NAVIGATOR (HITL OSINT SCRAPER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    with sync_playwright() as p:
        # HEADLESS=FALSE: Despliegue visual para intervención humana
        print(f"{GRAY}[*] Iniciando motor Chromium (Modo Headful para soporte HITL)...{RESET}")
        browser = p.chromium.launch(headless=False)
        
        # Spoofing de Identidad
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

        url_objetivo = "https://www.indiehackers.com/group/growth"
        print(f"{CYAN}🔗 Aterrizando en ecosistema objetivo: {BOLD}{url_objetivo}{RESET}")
        
        try:
            page.goto(url_objetivo)
            
            # --- HUMAN IN THE LOOP (HITL) ---
            print(f"\n{RED}{BOLD}{'-'*50}{RESET}")
            print(f"{RED}{BOLD} [!] PROTOCOLO HITL ACTIVADO: CONTROL CEDIDO AL OPERADOR {RESET}")
            print(f"{YELLOW} Tienes 15 segundos de ventana táctica.{RESET}")
            print(f"{YELLOW} Si Cloudflare exige verificación ('Verify you are human'), resuélvelo AHORA.{RESET}")
            print(f"{RED}{BOLD}{'-'*50}{RESET}\n")
            
            page.wait_for_timeout(15000) 
            
            print(f"{GREEN}[+] Ventana HITL cerrada. Retomando control autónomo (Scraping)...{RESET}")
            # -------------------------

            print(f"{GRAY}[*] Escaneando la matriz renderizada y aplicando filtros de dolor (Keywords)...{RESET}")
            enlaces = page.locator("a").all()
            botin = []

            for enlace in enlaces:
                texto = enlace.inner_text().lower()
                if len(texto) < 15: continue 

                hits = [kw for kw in KEYWORDS if kw in texto]
                
                if hits:
                    href = enlace.get_attribute("href")
                    if href and ("/post/" in href or "/interview/" in href):
                        full_url = f"https://www.indiehackers.com{href}" if href.startswith("/") else href
                        botin.append({
                            "plataforma": "IndieHackers",
                            "dolor": hits,
                            "titulo": texto.replace('\n', ' ')[:80],
                            "url": full_url
                        })
                        print(f"{GREEN}  🎯 ¡ORO FANTASMA! Hit: {BOLD}{hits}{RESET}{GREEN} | {WHITE}{texto[:40]}...{RESET}")

            if botin:
                # Deduplicación criptográfica (Hash por URL)
                botin_unico = {item['url']: item for item in botin}.values()
                archivo = f"Botin_IH_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.json"
                
                with open(archivo, 'w', encoding='utf-8') as f:
                    json.dump(list(botin_unico), f, indent=4, ensure_ascii=False)
                
                print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
                print(f"{GREEN}✓ Extracción completada. {len(botin_unico)} presas aseguradas en: {archivo}{RESET}")
                print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")
            else:
                print(f"\n{YELLOW}! Radar limpio. No se detectaron dolores específicos en esta batida.{RESET}\n")
                
        except Exception as e:
            print(f"\n{RED}X Fricción estructural en la operación: {e}{RESET}\n")
            
        finally:
            print(f"{GRAY}💨 Apagando motores de navegación y borrando rastro local...{RESET}\n")
            browser.close()

if __name__ == "__main__":
    operacion_fantasma_hitl()
