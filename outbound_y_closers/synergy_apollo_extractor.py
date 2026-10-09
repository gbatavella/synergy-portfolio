import json
import csv
import os
import sys
import time
from urllib.parse import urlparse
from dotenv import load_dotenv

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

def iniciar_extraccion_apollo():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🎯 SYNERGY APOLLO EXTRACTOR (CRM DOMAIN PARSER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # Archivos dinámicos extraídos del entorno o argumentos
    archivo_entrada = os.getenv("JSON_TARGET_FILE", "DIRECTORIO_B2B_TARGET.json")
    archivo_salida = os.getenv("CSV_APOLLO_OUTPUT", "DOMINIOS_APOLLO.csv")

    print(f"{GRAY}[*] Iniciando motor ETL. Buscando matriz de datos en: {archivo_entrada}...{RESET}")
    time.sleep(1)

    try:
        with open(archivo_entrada, "r", encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        print(f"{RED}❌ [ERROR CRÍTICO] No se encontró el archivo de origen {archivo_entrada}.{RESET}")
        print(f"{YELLOW}>> Verifique la ruta o genere el directorio B2B primero.{RESET}\n")
        sys.exit(1)

    # Detección dinámica de la clave principal del JSON
    clave_directorio = next(iter(datos.keys())) if isinstance(datos, dict) else None
    empresas = datos.get(clave_directorio, []) if clave_directorio else datos
    
    if not empresas:
        print(f"{YELLOW}⚠️ El directorio está vacío o tiene una estructura no reconocida.{RESET}")
        sys.exit(1)

    registros_csv = []
    print(f"{CYAN}>> Analizando y sanitizando URLs corporativas...{RESET}\n")

    for i, empresa_data in enumerate(empresas):
        # Desempaquetado estructural
        if "content" in empresa_data and isinstance(empresa_data["content"], dict):
            empresa = empresa_data["content"]
        else:
            empresa = empresa_data
            
        nombre = empresa.get("nombre_empresa", "NA")
        url = empresa.get("url_origen", "NA")
        
        # Filtrar solo URLs válidas y activas
        if url != "NA" and url.startswith("http"):
            # Extracción del dominio limpio usando urllib
            dominio = urlparse(url).netloc
            if dominio.startswith("www."):
                dominio = dominio[4:] # Strip del 'www.'
                
            registros_csv.append([nombre, dominio])
            print(f"{GREEN} [+] Limpio: {RESET}{nombre[:30]:<30} -> {BOLD}{dominio}{RESET}")

    # Serialización en CSV con formato nativo para Apollo.io
    with open(archivo_salida, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Cabeceras exactas que el algoritmo de Apollo lee para auto-mapeo
        writer.writerow(["Company Name", "Company Domain"]) 
        writer.writerows(registros_csv)

    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{GREEN}{BOLD} 🚀 ¡EXTRACCIÓN EXITOSA! {len(registros_csv)} dominios estructurados.{RESET}")
    print(f"{BLUE} 📂 Bóveda de salida: {archivo_salida}{RESET}")
    print(f"{GRAY} >> Archivo listo para importación e inyección en secuencias B2B.{RESET}\n")

if __name__ == "__main__":
    iniciar_extraccion_apollo()
