import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time
import json
import sys
import os

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def iniciar_ares_delta():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} SYNERGY ARES DELTA V1 (STEALTH OSINT INFILTRATOR) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    print(f"{GRAY}[*] Iniciando máscara biométrica y evasión anti-bot (undetected-chromedriver)...{RESET}")

    # Inicializamos el navegador fantasma
    opciones = uc.ChromeOptions()
    opciones.binary_location = '/usr/bin/chromium' 
    
    try:
        driver = uc.Chrome(options=opciones)
    except Exception as e:
        print(f"{RED}X Fallo al instanciar Chromium enmascarado. Verifica la ruta binaria: {e}{RESET}")
        sys.exit(1)

    # Coordenadas hostiles: Sección de Reseñas
    url_objetivo = "https://www.warriorforum.com/internet-marketing-product-reviews-ratings/"
    archivo_salida = "inteligencia_warrior.json"
    
    try:
        print(f"{CYAN}🔗 Aterrizando en territorio hostil: {BOLD}{url_objetivo}{RESET}")
        driver.get(url_objetivo)
        
        # Simulación humana para evadir heurísticas
        print(f"{YELLOW}⏳ Pausa táctica (8 segundos). Simulando lectura humana para evadir WAF...{RESET}")
        time.sleep(8)
        
        print(f"{GRAY}[*] Extrayendo código matriz (DOM) de la página...{RESET}")
        html_crudo = driver.page_source
        
        # Bisturí semántico
        sopa = BeautifulSoup(html_crudo, 'html.parser')
        
        print(f"\n{GREEN}{BOLD}--- INTELIGENCIA EXTRAÍDA (RADARES ENEMIGOS) ---{RESET}\n")
        
        enlaces = sopa.find_all('a', href=True)
        hilos_detectados = []
        
        for enlace in enlaces:
            texto = enlace.get_text(strip=True)
            # Filtro Heurístico
            if len(texto) > 25 and "http" not in texto:
                if texto not in [h['titulo'] for h in hilos_detectados]: 
                    hilos_detectados.append({"titulo": texto, "enlace": enlace['href']})
        
        # Telemetría de los primeros 10 impactos
        for i, hilo in enumerate(hilos_detectados[:10]):
            print(f"{WHITE} 🎯 Hilo {i+1}: {hilo['titulo']}{RESET}")

        # Serialización de datos
        with open(archivo_salida, "w", encoding="utf-8") as f:
            json.dump(hilos_detectados, f, indent=4)
            
        print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
        print(f"{GREEN}✓ Operación exitosa. {len(hilos_detectados)} coordenadas aseguradas en '{archivo_salida}'.{RESET}")
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")

    except Exception as e:
        print(f"\n{RED}X Los sensores enemigos nos detectaron o hubo fricción estructural: {e}{RESET}\n")
    finally:
        print(f"{GRAY}💨 Ares Delta lanzando bomba de humo y cerrando túnel de conexión...{RESET}\n")
        driver.quit()

if __name__ == "__main__":
    iniciar_ares_delta()
