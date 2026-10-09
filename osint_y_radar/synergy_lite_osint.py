import json
import time
import requests
import os
import sys
from bs4 import BeautifulSoup
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

def iniciar_radar_lite():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🦆 SYNERGY LITE OSINT (DDG NO-JS EXPLOITER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    load_dotenv()
    
    # Abstracción OPSEC de las rutas
    archivo_entrada = os.getenv("JSON_TARGET_COMPANIES", "DIRECTORIO_B2B_TARGET.json")
    archivo_salida = os.getenv("JSON_LEADS_OUTPUT", "DECISORES_OSINT_TARGET.json")
    rol_objetivo = os.getenv("OSINT_TARGET_ROLE", '"Logística" OR "Depósito" OR "Supply Chain"')

    print(f"{GRAY}[*] Iniciando radar profundo vía vector asíncrono (DDG Lite)...{RESET}")

    try:
        with open(archivo_entrada, "r", encoding="utf-8") as f:
            datos = json.load(f)
            clave_base = next(iter(datos.keys())) if isinstance(datos, dict) else None
            empresas = datos.get(clave_base, []) if clave_base else datos
    except FileNotFoundError:
        print(f"{RED}❌ [ERROR CRÍTICO] Bóveda de empresas no encontrada: {archivo_entrada}{RESET}")
        sys.exit(1)

    decisores_encontrados = []

    # Cabeceras ultraligeras simulando un navegador básico/antiguo
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    print(f"{GREEN}[+] {len(empresas)} nodos detectados. Desplegando inyección de formularios.{RESET}\n")

    for i, empresa_data in enumerate(empresas):
        # Desempaquetado dinámico
        if "content" in empresa_data and isinstance(empresa_data["content"], dict):
            nombre = empresa_data["content"].get("nombre_empresa", "NA")
        else:
            nombre = empresa_data.get("nombre_empresa", "NA")
            
        if nombre == "NA" or not nombre:
            continue
            
        print(f"{CYAN}[{i+1}/{len(empresas)}] 🎯 Rastreando cúpula gerencial de: {BOLD}{nombre}{RESET}")
        
        # El Dork letal apuntando a LinkedIn
        query = f'site:linkedin.com/in {rol_objetivo} "{nombre}" Argentina'
        
        try:
            # Atacamos el endpoint Lite (Bypass de JS y Firewalls pesados)
            url_ddg_lite = "https://lite.duckduckgo.com/lite/"
            payload = {'q': query}
            
            respuesta = requests.post(url_ddg_lite, data=payload, headers=headers, timeout=15)
            
            if respuesta.status_code == 200:
                soup = BeautifulSoup(respuesta.text, 'html.parser')
                
                # DDG Lite guarda los resultados en tablas (result-snippet) y anclas (result-url)
                titulos = soup.find_all('a', class_='result-url', limit=2)
                descripciones = soup.find_all('td', class_='result-snippet', limit=2)
                
                candidatos = []
                if titulos:
                    for idx, titulo_tag in enumerate(titulos):
                        titulo_texto = titulo_tag.text.strip()
                        enlace = titulo_tag.get('href', '')
                        
                        # Emparejamiento con el fragmento de texto (snippet)
                        snippet_texto = descripciones[idx].text.strip() if idx < len(descripciones) else "NA"
                        
                        print(f"   {GREEN}👤 Decisor Detectado: {titulo_texto[:45]}...{RESET}")
                        candidatos.append({
                            "nombre_y_cargo": titulo_texto,
                            "linkedin_url": enlace,
                            "detalle": snippet_texto
                        })
                else:
                    print(f"   {YELLOW}⚠️ Espectro limpio. No se detectaron perfiles en la red.{RESET}")
                    
                decisores_encontrados.append({
                    "empresa_objetivo": nombre,
                    "candidatos": candidatos
                })
                
                # Checkpointing dinámico
                with open(archivo_salida, "w", encoding="utf-8") as f_out:
                    json.dump({"decisores_osint": decisores_encontrados}, f_out, indent=4, ensure_ascii=False)
                    
            else:
                print(f"   {RED}❌ Fricción HTTP: El servidor devolvió código {respuesta.status_code}{RESET}")
                
            # Pausa táctica corta (DDG Lite es altamente permisivo)
            time.sleep(4)
            
        except requests.exceptions.Timeout:
            print(f"   {RED}⏳ TIMEOUT: El servidor tardó demasiado en responder.{RESET}")
        except Exception as e:
            print(f"   {RED}❌ Error en el túnel de red con {nombre}: {e}{RESET}")

    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{GREEN}{BOLD} 🚀 ¡EXTRACCIÓN DE DECISORES FINALIZADA!{RESET}")
    print(f"{BLUE} 📂 Bóveda de inteligencia: {archivo_salida}{RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

if __name__ == "__main__":
    iniciar_radar_lite()
