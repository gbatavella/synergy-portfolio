import os
import time
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# Carga de variables de entorno para proteger los Dorks privados
load_dotenv()

# --- CÓDIGOS ANSI ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def radar_pesado(dorks):
    print(f"\n{BLUE}{BOLD}======================================={RESET}")
    print(f"{BLUE}{BOLD} 🛰️  SYNERGY RADAR - TÁCTICA HUMAN IN THE LOOP{RESET}")
    print(f"{BLUE}{BOLD}======================================={RESET}\n")
    
    resultados_totales = set()

    with sync_playwright() as p:
        print(f"{YELLOW}[*] Iniciando motor Chromium (CONEXIÓN DIRECTA)...{RESET}")
        
        # Visión táctica activada para que el humano pueda intervenir
        navegador = p.chromium.launch(headless=False)
        contexto = navegador.new_context()
        pagina = contexto.new_page()

        for dork in dorks:
            print(f"\n{YELLOW}[*] Ejecutando escaneo táctico: {dork}{RESET}")
            try:
                # Construir la URL de búsqueda de forma nativa
                url_busqueda = f"https://www.google.com/search?q={dork}"
                
                # Navegar y esperar carga de red
                pagina.goto(url_busqueda, timeout=60000, wait_until="domcontentloaded")
                time.sleep(4) # Pausa inicial de estabilización
                
                enlaces = pagina.locator('a[jsname="UWckNb"]').all()
                
                # --- TÁCTICA HUMAN IN THE LOOP (HITL) ---
                if not enlaces:
                    print(f"\n{RED}  [!] ALERTA: No se encontraron resultados. Posible bloqueo de CAPTCHA/WAF.{RESET}")
                    print(f"{YELLOW}  [👁️] MIRA EL NAVEGADOR: Si hay un desafío, resuélvelo manualmente ahora.{RESET}")
                    input(f"{GREEN}{BOLD}  [👉] PRESIONA 'ENTER' AQUÍ EN LA TERMINAL CUANDO LO HAYAS RESUELTO...{RESET}")
                    
                    # El operador resolvió el obstáculo. Recargamos selectores.
                    time.sleep(2)
                    enlaces = pagina.locator('a[jsname="UWckNb"]').all()
                    
                    if not enlaces:
                        print(f"{RED}  [-] Sigue sin haber resultados post-HITL. Saltando al siguiente objetivo.{RESET}")
                        continue
                
                # Extracción y limpieza
                for enlace in enlaces:
                    url = enlace.get_attribute('href')
                    if url and "google.com" not in url and url not in resultados_totales:
                        print(f"{GREEN}  [+] Objetivo asegurado: {url}{RESET}")
                        resultados_totales.add(url)
                        
            except Exception as e:
                print(f"{RED}  [!] Error en el escaneo de este nodo: {e}{RESET}")

        navegador.close()

    print(f"\n{BLUE}======================================={RESET}")
    print(f"{GREEN}{BOLD}✅ BARRIDO COMPLETADO. {len(resultados_totales)} URLs aseguradas.{RESET}")
    print(f"{BLUE}======================================={RESET}")
    
    # Salida a archivo de texto plano
    output_file = os.getenv("RADAR_OUTPUT_FILE", "objetivos_pesados.txt")
    with open(output_file, "w") as f:
        for url in resultados_totales:
            f.write(f"{url}\n")

if __name__ == "__main__":
    # Permite inyectar dorks desde el .env separados por comas.
    # Si no existe, usa Dorks genéricos B2B para demostración en GitHub.
    dorks_env = os.getenv("RADAR_DORKS")
    if dorks_env:
        mis_dorks = [d.strip() for d in dorks_env.split(",")]
    else:
        mis_dorks = [
            'site:linkedin.com/in/ "founder" "AI automation"',
            'site:twitter.com "building in public" "SaaS"'
        ]
    
    radar_pesado(mis_dorks)
