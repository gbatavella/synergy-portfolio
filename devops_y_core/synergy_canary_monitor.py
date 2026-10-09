import asyncio
import os
import sys
from playwright.async_api import async_playwright

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

async def check_search_health(engine_name, url):
    async with async_playwright() as p:
        # Modo headless activado para integración continua (CI/CD)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            print(f"{GRAY}[*] Desplegando sonda asíncrona hacia el nodo: {BOLD}{engine_name}{RESET}...")
            await page.goto(url, timeout=30000)
            
            # Verificamos si la estructura clásica de resultados (H3) sigue intacta
            h3_count = await page.locator("h3").count()
            
            if h3_count > 0:
                print(f"   {GREEN}✅ {engine_name}: NODO OPERATIVO. ({h3_count} firmas estructurales detectadas){RESET}")
            else:
                print(f"   {YELLOW}⚠️ {engine_name}: MUTACIÓN ESTRUCTURAL. El DOM ha cambiado o hay bloqueo.{RESET}")
                
                # TOMA DE EVIDENCIA FORENSE VISUAL
                evidence_file = f"evidencia_canario_{engine_name.lower()}.png"
                await page.screenshot(path=evidence_file)
                print(f"   {RED}📸 [ALERTA] Evidencia visual del bloqueo capturada: '{evidence_file}'{RESET}")
                
                # Diagnóstico secundario
                print(f"   {GRAY}🔍 Analizando nueva topología DOM...{RESET}")
                links = await page.query_selector_all('a')
                print(f"      - Se detectaron {len(links)} enlaces genéricos, pero la estructura <h3> está ausente.")
                print(f"      - Sugerencia: Revisar la imagen forense para descartar WAF o CAPTCHA de Cloudflare.")

        except Exception as e:
            print(f"   {RED}❌ {engine_name}: BLOQUEO SEVERO O TIMEOUT DETECTADO. Detalle: {e}{RESET}")
        finally:
            await browser.close()
            print(f"{BLUE}{'-'*65}{RESET}")

async def main():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🐦 SYNERGY CANARY MONITOR (DOM HEALTH & WAF EVASION) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    print(f"{CYAN}📡 Iniciando protocolo de monitoreo estructural sobre gigantes de búsqueda...{RESET}\n")

    # 1. Los Gigantes Clásicos
    await check_search_health("Google", "https://www.google.com/search?q=test+contact+email")
    await check_search_health("Bing", "https://www.bing.com/search?q=test+contact+email")
    
    # 2. Rutas Alternativas de Reconocimiento
    await check_search_health("Yahoo", "https://search.yahoo.com/search?p=test+contact+email")
    await check_search_health("DuckDuckGo (HTML)", "https://html.duckduckgo.com/html/?q=test+contact+email")
    
    print(f"\n{GREEN}{BOLD}🏁 Patrullaje de salud de red finalizado.{RESET}\n")

if __name__ == "__main__":
    # Verificación de plataforma para evitar errores de Loop en Windows/Linux
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{RED}Monitoreo abortado por el operador.{RESET}")
