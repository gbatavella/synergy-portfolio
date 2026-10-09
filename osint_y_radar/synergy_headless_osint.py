import json
import time
import os
import sys
from playwright.sync_api import sync_playwright
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

def iniciar_radar_fantasma():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 👻 SYNERGY HEADLESS OSINT (PLAYWRIGHT DORKING) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    load_dotenv()
    
    # Abstracción OPSEC de las rutas
    archivo_empresas = os.getenv("JSON_TARGET_COMPANIES", "DIRECTORIO_B2B_TARGET.json")
    archivo_salida = os.getenv("JSON_LEADS_OUTPUT", "GERENTES_OSINT_TARGET.json")
    rol_objetivo = os.getenv("OSINT_TARGET_ROLE", '"Logística" OR "Depósito"')

    print(f"{GRAY}[*] Iniciando motor Playwright en Modo Invisible (Headless)...{RESET}")
    
    try:
        with open(archivo_empresas, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print(f"{RED}❌ [ERROR CRÍTICO] Bóveda de empresas objetivo no encontrada: {archivo_empresas}{RESET}")
        sys.exit(1)

    # Adaptación dinámica a la estructura del JSON
    clave_base = next(iter(datos.keys())) if isinstance(datos, dict) else None
    empresas = datos.get(clave_base, []) if clave_base else datos
    
    decisores_osint = []

    print(f"{GREEN}[+] {len(empresas)} organizaciones en cola para escrutinio profundo.{RESET}\n")

    # Búsqueda Táctica Simulando Humano
    with sync_playwright() as p:
        # Lanzamiento del clúster Chromium en modo invisible
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        for i, empresa_data in enumerate(empresas):
            if "content" in empresa_data and isinstance(empresa_data["content"], dict):
                empresa = empresa_data["content"]
            else:
                empresa = empresa_data
                
            nombre_empresa = empresa.get("nombre_empresa", "NA")
            
            if nombre_empresa == "NA" or not nombre_empresa:
                continue

            print(f"{CYAN}[{i+1}/{len(empresas)}] 👻 Buscando huellas digitales de: {BOLD}{nombre_empresa}{RESET}")
            
            # Dork directo a LinkedIn sin pasar por la búsqueda interna de la plataforma
            query = f'site:linkedin.com/in {rol_objetivo} "{nombre_empresa}" Argentina'
            gerentes_encontrados = []
            
            try:
                # Infiltración en el motor de búsqueda
                page.goto("https://www.google.com/", wait_until="domcontentloaded")
                
                # Inyección del Dork
                page.fill('textarea[name="q"]', query)
                page.keyboard.press("Enter")
                
                # Espera estructural
                page.wait_for_selector('div#search', timeout=15000)
                
                # Extracción de la capa de inteligencia (Títulos y URLs)
                resultados = page.locator('div.g').all()
                for res in resultados[:2]: # Limitamos a los 2 prospectos más relevantes
                    titulo = res.locator('h3').text_content()
                    enlace = res.locator('a').first.get_attribute('href')
                    
                    if titulo:
                        print(f"   {GREEN}✅ Objetivo Encontrado: {titulo[:50]}...{RESET}")
                        gerentes_encontrados.append({
                            "titulo": titulo,
                            "perfil_linkedin": enlace
                        })
                        
            except Exception as e:
                print(f"   {YELLOW}⚠️ Fricción WAF/DOM en {nombre_empresa}. Saltando al siguiente nodo...{RESET}")
                
            decisores_osint.append({
                "empresa": nombre_empresa,
                "candidatos": gerentes_encontrados
            })
            
            # Checkpointing: Guardado Dinámico por iteración
            with open(archivo_salida, "w", encoding="utf-8") as file:
                json.dump({"radar_osint": decisores_osint}, file, indent=4, ensure_ascii=False)
                
            # Control de Cadencia (Rate Limit Evasion)
            time.sleep(10)

        browser.close()

    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{GREEN}{BOLD} 🚀 ¡RADAR OSINT COMPLETADO!{RESET}")
    print(f"{BLUE} 📂 El manifiesto de decisores está asegurado en: {archivo_salida}{RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

if __name__ == "__main__":
    iniciar_radar_fantasma()
