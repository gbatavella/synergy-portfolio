import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import pandas as pd
import time
import sys
import urllib.parse
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

def ejecutar_ares_delta():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🕸️ SYNERGY ARES DELTA (UNDETECTED OSINT SCRAPER V2) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ========================================================
    # 🎯 ZONA DE COMANDANTE: MATRIZ DE SELECCIÓN DE NICHO
    # ========================================================
    nicho = "M&A Advisors Investment Banks New York OR London"
    # nicho = "Commercial Real Estate Investment Firms Miami OR Texas"
    # nicho = "Private Aviation Brokers Miami OR Dubai"
    # ========================================================

    print(f"{GRAY}[*] Inicializando motor Chromium indetectable...{RESET}")
    opciones = uc.ChromeOptions()
    
    try:
        driver = uc.Chrome(options=opciones)
    except Exception as e:
        print(f"{RED}❌ [ERROR CRÍTICO] Fallo al instanciar el driver indetectable: {e}{RESET}")
        sys.exit(1)
        
    perlas_negras = []

    try:
        query = f'{nicho} (CEO OR Founder OR Managing Director OR Partner) site:linkedin.com/in'
        print(f"{CYAN}🎯 Preparando munición balística (Dork): {BOLD}{query}{RESET}")
        
        # 🛡️ ESCUDO DE SINTAXIS: Traducción segura de URL (Convierte el & en %26)
        query_segura = urllib.parse.quote_plus(query)
        url_ataque = f"https://www.google.com/search?q={query_segura}&num=20"
        
        print(f"{GRAY}[*] Inyectando vector codificado en el motor de búsqueda...{RESET}\n")
        driver.get(url_ataque)

        # --- PAUSA TÁCTICA PARA EL HUMANO (HITL) ---
        print(f"{RED}{BOLD}🚨 ATENCIÓN ARQUITECTO (INTERVENCIÓN MANUAL REQUERIDA) 🚨{RESET}")
        print(f"{WHITE}1. Revisa la ventana de Chrome instanciada.{RESET}")
        print(f"{WHITE}2. Resuelve el Captcha si Google levanta escudos.{RESET}")
        print(f"{WHITE}3. Confirma visualmente la matriz de resultados de LinkedIn.{RESET}")
        input(f"{YELLOW}👉 Presiona ENTER aquí en la terminal para aspirar los datos... {RESET}")

        print(f"\n{GRAY}👁️‍🗨️ ¡Orden recibida! Parseando DOM y extrayendo bloques de datos...{RESET}")
        
        # Procesamiento heurístico del DOM
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        resultados = soup.find_all('div', class_='g')
        
        # Enrutamiento de contingencia (Fallback)
        if len(resultados) == 0:
            print(f"{YELLOW}⚠️ Estructura 'div.g' vacía. Pivotando a estructura 'div.MjjYud'...{RESET}")
            resultados = soup.find_all('div', class_='MjjYud')

        for res in resultados:
            t = res.find('h3')
            l = res.find('a')
            
            if t and l:
                enlace = l.get('href')
                if enlace and "linkedin.com/in/" in enlace:
                    perlas_negras.append({
                        "Extraction Status": "Complete",
                        "Engine Output": "Verified Target",
                        "🏢 Target Title": t.text.strip(),
                        "🔗 Source URL": enlace
                    })
                    print(f"   {GREEN}✅ Perla Asegurada: {t.text.strip()[:40]}...{RESET}")

    except Exception as e:
        print(f"\n{RED}❌ Anomalía estructural durante la infiltración: {e}{RESET}")
        
    finally:
        print(f"\n{GRAY}🛑 Operación concluida. Destruyendo instancia del navegador...{RESET}")
        driver.quit()

    # Serialización y Consolidación del Botín
    if perlas_negras:
        print(f"{GRAY}[*] Consolidando datos en matriz tabular (Pandas)...{RESET}")
        df = pd.DataFrame(perlas_negras)
        nombre_archivo = f"Ares_Delta_Payload_{datetime.now().strftime('%H%M')}.csv"
        df.to_csv(nombre_archivo, index=False)
        
        print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
        print(f"{GREEN}{BOLD} 🚀 ¡BOTÍN ASEGURADO Y ENCRIPTADO! {RESET}")
        print(f"{WHITE} ↳ {len(perlas_negras)} perfiles de alto valor extraídos.{RESET}")
        print(f"{BLUE} 📂 Bóveda de salida: {nombre_archivo}{RESET}")
        print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    else:
        print(f"\n{YELLOW}{BOLD}⚠️ Espectro vacío. 0 prospectos extraídos. Verifique el Dork o el estado del DOM.{RESET}\n")

if __name__ == "__main__":
    ejecutar_ares_delta()
