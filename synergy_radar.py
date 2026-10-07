import time
import os
from dotenv import load_dotenv
from duckduckgo_search import DDGS

# Carga de entorno para ocultar los Dorks de prospección reales
load_dotenv()

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def radar_synergy(dorks, max_resultados=10):
    print(f"\n{BLUE}{BOLD}======================================={RESET}")
    print(f"{BLUE}{BOLD} 🛰️  SYNERGY RADAR OSINT (DDG CORE) - EN LÍNEA{RESET}")
    print(f"{BLUE}{BOLD}======================================={RESET}\n")
    
    resultados_totales = set()
    
    # Abrimos conexión directa y anónima con DuckDuckGo
    with DDGS() as ddgs:
        for dork in dorks:
            print(f"{YELLOW}[*] Ejecutando escaneo táctico con: {dork}{RESET}")
            try:
                # Pausa táctica de estabilización de red
                time.sleep(2)
                
                # Extracción de la matriz
                resultados = list(ddgs.text(dork, max_results=max_resultados))
                
                if not resultados:
                    print(f"{GRAY}  [-] La red devolvió 0 resultados. Intentando próximo dork.{RESET}")
                    continue
                    
                for res in resultados:
                    url = res.get('href')
                    # Filtramos para asegurar que solo guardamos las URLs
                    if url and url not in resultados_totales:
                        print(f"{GREEN}  [+] Objetivo detectado: {url}{RESET}")
                        resultados_totales.add(url)
                        
            except Exception as e:
                print(f"{RED}  [!] Error en el escaneo del nodo: {e}{RESET}")

    print(f"\n{BLUE}======================================={RESET}")
    print(f"{GREEN}{BOLD}✅ BARRIDO COMPLETADO. {len(resultados_totales)} URLs aseguradas.{RESET}")
    print(f"{BLUE}======================================={RESET}")
    
    # Guardar en archivo para el pipeline del siguiente agente
    output_file = os.getenv("DDG_RADAR_OUTPUT", "objetivos_extraidos.txt")
    with open(output_file, "w") as f:
        for url in resultados_totales:
            f.write(f"{url}\n")

if __name__ == "__main__":
    # Inyección de Dorks desde entorno (.env) separados por coma
    # Fallback a Dorks de demostración si el script se corre en entorno vacío (GitHub clone)
    dorks_env = os.getenv("RADAR_DDG_DORKS")
    
    if dorks_env:
        mis_dorks = [d.strip() for d in dorks_env.split(",")]
    else:
        mis_dorks = [
            'site:github.com "AI agents" "founder"',
            'site:linkedin.com/in/ "CEO" "machine learning"'
        ]
    
    # Limite ajustable por variable de entorno
    limite = int(os.getenv("RADAR_MAX_RESULTS", "15"))
    
    radar_synergy(mis_dorks, max_resultados=limite)
