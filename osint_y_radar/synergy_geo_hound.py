import pandas as pd
import time
import sys
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# --- SEGURIDAD Y CONFIGURACIÓN ---
load_dotenv()

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

# --- INYECCIÓN TÁCTICA: PROTOCOLO DE AISLAMIENTO ---
# from aislamiento_norberto import desplegar_norberto
def desplegar_perfil_aislado(modo_fantasma=False):
    """Simulación del despliegue del perfil Firefox aislado para el repo público."""
    options = Options()
    if modo_fantasma:
        options.add_argument("--headless")
    # Configuración anti-detección básica
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("useAutomationExtension", False)
    return webdriver.Firefox(options=options)

def hunt_leads(niche, location):
    print(f"\n{RED}{BOLD}{'='*60}{RESET}")
    print(f"{RED}{BOLD} 🐺 SYNERGY GEO-HOUND (BROWSER ISOLATION PROTOCOL) {RESET}")
    print(f"{RED}{BOLD}{'='*60}{RESET}\n")
    
    rapid_output(f"{YELLOW}🔥 [SISTEMA] Iniciando Sabueso GEO - Misión: Extracción Total...{RESET}")
    
    # ---------------------------------------------------------
    # DESPLIEGUE DEL MOTOR AISLADO 
    # ---------------------------------------------------------
    rapid_output(f"{GRAY}  ⏳ Levantando navegador Firefox en sector aislado...{RESET}")
    driver = desplegar_perfil_aislado(modo_fantasma=False)

    if not driver:
        print(f"{RED}❌ Error fatal: No se pudo levantar el motor Firefox.{RESET}")
        return

    search_query = f"{niche} in {location} contact email"
    print(f"{BLUE}🔎 [OBJETIVO] {search_query}{RESET}")

    try:
        driver.get(f"https://www.google.com/search?q={search_query}")

        # BLOQUEO HITL (Human In The Loop)
        if "google.com/sorry" in driver.current_url or len(driver.find_elements(By.ID, "captcha-form")) > 0:
            print(f"\n{RED}{BOLD}⚠️ [ALERTA] Captcha/WAF en pantalla. ¡Resuélvelo, Comandante!{RESET}")
            input(f"{GREEN}⌨️  UNA VEZ VEAS LOS RESULTADOS EN EL NAVEGADOR, presiona ENTER aquí...{RESET}")

        print(f"{YELLOW}📡 [SISTEMA] Succionando datos del DOM...{RESET}")
        time.sleep(3) # Pausa táctica para asegurar carga del DOM

        # ESTRATEGIA DE FUERZA BRUTA: Capturamos todos los encabezados y links
        leads = []
        
        resultados = driver.find_elements(By.CSS_SELECTOR, "div.g")
        for res in resultados:
            try:
                titulo = res.find_element(By.TAG_NAME, "h3").text
                link = res.find_element(By.TAG_NAME, "a").get_attribute("href")
                
                if titulo and link:
                    leads.append({
                        "Target_Name": titulo,
                        "Source_URL": link
                    })
                    print(f"{GRAY}  [+] Nodo capturado: {titulo[:35]}...{RESET}")
            except Exception:
                continue

        print(f"\n{GREEN}{BOLD}✅ [ÉXITO] Extracción completada: {len(leads)} prospectos asegurados en memoria.{RESET}")
        
        # Consolidación y Exportación vía Pandas
        if leads:
            df = pd.DataFrame(leads)
            archivo_salida = f"botin_geo_{niche.replace(' ', '_')}_{location.replace(' ', '_')}.csv"
            df.to_csv(archivo_salida, index=False, encoding='utf-8')
            print(f"{BLUE}💾 Carga exportada a la bóveda: {archivo_salida}{RESET}")
        else:
            print(f"{RED}⚠️ La extracción no produjo resultados válidos.{RESET}")

    except Exception as e:
        print(f"\n{RED}❌ Error durante la cacería táctica: {e}{RESET}")
    finally:
        driver.quit()
        print(f"\n{GRAY}🔌 Motor Firefox aislado apagado. Rastro digital borrado.{RESET}\n")

if __name__ == "__main__":
    target_niche = os.getenv("HOUND_NICHE", "B2B Wholesalers")
    target_location = os.getenv("HOUND_LOCATION", "Miami FL")
    
    hunt_leads(target_niche, target_location)
