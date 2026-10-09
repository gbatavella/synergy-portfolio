import json
import time
import requests
import re
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

def ejecutar_asalto_rapido():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} ⚡ SYNERGY RAPID HARVESTER (REGEX EMAIL SCRAPER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    load_dotenv()
    
    # Abstracción de archivos para protección de OPSEC
    archivo_entrada = os.getenv("JSON_DOMAINS_INPUT", "TARGET_DOMAINS.json")
    archivo_salida = os.getenv("JSON_EMAILS_OUTPUT", "EXTRACTED_CONTACTS.json")

    print(f"{GRAY}[*] Iniciando secuencia de barrido de alta velocidad...{RESET}")

    try:
        with open(archivo_entrada, "r", encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        print(f"{RED}❌ [ERROR CRÍTICO] No se encontró el directorio de objetivos: {archivo_entrada}.{RESET}")
        sys.exit(1)

    # Adaptación a la estructura del JSON entrante
    clave_base = next(iter(datos.keys())) if isinstance(datos, dict) else None
    empresas = datos.get(clave_base, []) if clave_base else datos
    resultados_directos = []

    # Cabeceras de camuflaje (Mimetismo de Navegador)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    print(f"{GREEN}[+] {len(empresas)} dominios cargados en la recámara. Fuego a discreción.{RESET}\n")

    for i, empresa_data in enumerate(empresas):
        # Desempaquetado estructural
        if "content" in empresa_data and isinstance(empresa_data["content"], dict):
            empresa = empresa_data["content"]
            url = empresa_data.get("url_origen", empresa.get("url_origen", "NA"))
        else:
            empresa = empresa_data
            url = empresa.get("url_origen", "NA")
            
        nombre = empresa.get("nombre_empresa", "NA")
        
        if not url or url == "NA" or not url.startswith("http"):
            print(f"{GRAY}[{i+1}/{len(empresas)}] ⏭️ Saltando {nombre}: URL inválida o ausente.{RESET}")
            continue
            
        print(f"{CYAN}[{i+1}/{len(empresas)}] 🎯 Infiltrando nodo: {BOLD}{nombre}{RESET}")
        
        try:
            # Petición HTTP cruda con restricción de tiempo severa
            respuesta = requests.get(url, headers=headers, timeout=10)
            
            if respuesta.status_code == 200:
                # Extracción por patrón Regex en el código fuente
                patron_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
                emails_encontrados = set(re.findall(patron_email, respuesta.text))
                
                # Filtros heurísticos para limpiar la basura de desarrolladores
                basura_tecnica = ["sentry", "w3.org", "example", "domain", "test"]
                emails_limpios = [
                    email for email in emails_encontrados 
                    if not any(basura in email.lower() for basura in basura_tecnica)
                ]
                
                if emails_limpios:
                    print(f"   {GREEN}✅ ¡BINGO! Huellas detectadas: {emails_limpios}{RESET}")
                else:
                    print(f"   {YELLOW}⚠️ Superficie limpia. No se detectaron correos en el código fuente.{RESET}")
                    
                resultados_directos.append({
                    "empresa_objetivo": nombre,
                    "url": url,
                    "emails_capturados": emails_limpios
                })
                
            else:
                print(f"   {RED}❌ Fricción WAF: El servidor rechazó el acceso (HTTP {respuesta.status_code}).{RESET}")
                
        except requests.exceptions.Timeout:
            print(f"   {YELLOW}⏳ TIMEOUT: Umbral de latencia superado. Abortando nodo...{RESET}")
        except requests.exceptions.ConnectionError:
            print(f"   {RED}❌ ERROR: Conexión rechazada o dominio inexistente.{RESET}")
        except Exception as e:
            print(f"   {RED}❌ Anomalía de red con {nombre}: {e}{RESET}")

        # Guardado Dinámico (Checkpointing por iteración)
        with open(archivo_salida, "w", encoding="utf-8") as f:
            json.dump({"contactos_web": resultados_directos}, f, indent=4, ensure_ascii=False)

    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{GREEN}{BOLD} 🚀 ¡BARRIDO FINALIZADO! Matriz de contactos asegurada en:{RESET}")
    print(f"{BLUE} 📂 {archivo_salida}{RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

if __name__ == "__main__":
    ejecutar_asalto_rapido()
