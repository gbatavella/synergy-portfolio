import json
import os
import sys
import time
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

def iniciar_infiltracion_persistente():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧠 SYNERGY PERSISTENT OSINT (HITL & SESSION MEMORY) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    load_dotenv()
    
    # Abstracción de OPSEC
    archivo_empresas = os.getenv("JSON_TARGET_COMPANIES", "DIRECTORIO_B2B_TARGET.json")
    archivo_salida = os.getenv("JSON_OSINT_OUTPUT", "GERENTES_V2.json")
    directorio_sesion = os.getenv("PLAYWRIGHT_SESSION_DIR", "./sesion_google_persistente")

    print(f"{GRAY}[*] Ingestando base de coordenadas desde: {archivo_empresas}...{RESET}")

    try:
        with open(archivo_empresas, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            # Adaptación para leer tu estructura específica o un JSON genérico
            clave_base = next(iter(datos.keys())) if isinstance(datos, dict) else None
            empresas = datos.get(clave_base, []) if clave_base else datos
            
    except FileNotFoundError:
        print(f"{RED}❌ [ERROR CRÍTICO] Archivo origen no detectado.{RESET}")
        sys.exit(1)

    if not empresas:
        print(f"{YELLOW}⚠️ Base de datos vacía o ilegible.{RESET}")
        sys.exit(1)

    print(f"{GREEN}[+] {len(empresas)} nodos detectados. Levantando perfil persistente...{RESET}\n")

    with sync_playwright() as p:
        # Motor con retención de cookies y sesión física
        browser = p.chromium.launch_persistent_context(
            user_data_dir=directorio_sesion, 
            headless=False, # Mantenemos visibilidad para la intervención humana
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = browser.pages[0]
        decisores_osint = []

        for i, empresa in enumerate(empresas):
            # Soporte para desempaquetado de diccionario
            if "content" in empresa and isinstance(empresa["content"], dict):
                nombre = empresa["content"].get("nombre_empresa", "NA")
            else:
                nombre = empresa.get("nombre_empresa", "NA")
                
            if nombre == "NA": 
                continue
            
            print(f"{CYAN}[{i+1}/{len(empresas)}] 🔎 Reconocimiento profundo: {BOLD}{nombre}{RESET}")
            query = f"{nombre} Spegazzini Ezeiza contacto telefono"
            
            try:
                page.goto("https://www.google.com/", timeout=45000)
                page.fill('textarea[name="q"]', query)
                page.keyboard.press("Enter")
                
                # --- PUNTO DE INTERCEPCIÓN HITL (Human-in-the-Loop) ---
                print(f"{RED}{BOLD}🛑 PAUSA TÁCTICA DE SEGURIDAD (HITL){RESET}")
                print(f"{WHITE}>> Si el WAF arroja CAPTCHA, resuélvelo en el navegador AHORA.{RESET}")
                input(f"{YELLOW}>> Presiona ENTER en esta terminal cuando veas los resultados para continuar... {RESET}")
                
                # Sincronización post-validación humana
                page.wait_for_selector('div#search', timeout=60000)
                
                # Escrutinio Estructural
                res = page.locator('div.g').first
                titulo = res.locator('h3').text_content()
                enlace = res.locator('a').first.get_attribute('href')
                
                print(f"   {GREEN}✅ Pista Asegurada: {titulo[:50]}...{RESET}")
                decisores_osint.append({"empresa": nombre, "titulo": titulo, "url": enlace})
                
                # Serialización dinámica (Checkpointing)
                with open(archivo_salida, "w", encoding="utf-8") as f:
                    json.dump(decisores_osint, f, indent=4, ensure_ascii=False)
                
            except Exception as e:
                print(f"   {YELLOW}⚠️ Fricción en el nodo {nombre}: {e}{RESET}")
            
            print(f"{GRAY}{'-'*65}{RESET}")
            
        print(f"\n{BLUE}[*] Extracción masiva finalizada. Liberando candado de sesión.{RESET}")
        browser.close()

if __name__ == "__main__":
    iniciar_infiltracion_persistente()
