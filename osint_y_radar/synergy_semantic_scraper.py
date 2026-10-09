import os
import json
import time
import sys
import nest_asyncio
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def iniciar_filtro_semantico():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🕸️ SYNERGY SEMANTIC SCRAPER (SMARTGRAPH WEB PARSER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # 1. Carga de Bóveda Criptográfica y Async Patch
    load_dotenv()
    nest_asyncio.apply()

    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    if not OPENROUTER_API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Fuga de credenciales. OPENROUTER_API_KEY no detectada.{RESET}")
        sys.exit(1)

    print(f"{GRAY}[*] Enlazando con clústeres cognitivos vía OpenRouter...{RESET}")

    # 2. Configuración del Grafo Lector
    graph_config = {
        "llm": {
            "api_key": OPENROUTER_API_KEY,
            "model": "openai/openrouter/auto",
            "base_url": "https://openrouter.ai/api/v1",
        },
        "verbose": False, # Desactivado para mantener telemetría táctica limpia
        "headless": True, 
    }

    # 3. Prompt Semántico (El Extractor de Inteligencia B2B)
    prompt_extraccion = """
    Eres un Agente B2B analizando la página web oficial de una empresa.
    Extrae la siguiente información de contacto y negocio:
    1. "nombre_empresa": El nombre oficial o marca de la empresa.
    2. "rubro": A qué se dedican (ej. plásticos, logística, software, alimentos).
    3. "telefono": El número de teléfono principal o de ventas B2B.
    4. "direccion": La ubicación física o sede central si figura.
    5. "email": Correo electrónico de contacto si está disponible.

    Devuelve ESTRICTAMENTE esta información en formato JSON limpio. Si algún dato no se encuentra en el texto de la web, indica "NA".
    """

    # 4. Ingesta Estructural de URLs (Abstracción de OPSEC)
    archivo_urls = os.getenv("TXT_TARGET_URLS", "URLS_OBJETIVO_B2B.txt")
    nombre_archivo_salida = os.getenv("JSON_SEMANTIC_OUTPUT", "DIRECTORIO_B2B_SEMANTICO.json")
    directorio_final = []

    print(f"{GRAY}[*] Cargando matriz de coordenadas web desde: {archivo_urls}{RESET}")

    try:
        with open(archivo_urls, "r", encoding="utf-8") as file:
            # Saneamiento de lista (Elimina saltos y blancos)
            lista_urls = [line.strip() for line in file if line.strip()]
            
        print(f"{GREEN}[+] Se detectaron {len(lista_urls)} nodos web operativos. Iniciando escaneo profundo...{RESET}\n")

        # 5. Iteración y Extracción Semántica
        for i, url in enumerate(lista_urls):
            print(f"{CYAN}🎯 [{i+1}/{len(lista_urls)}] Infiltrando y analizando: {BOLD}{url}{RESET}")
            
            try:
                smart_scraper_graph = SmartScraperGraph(
                    prompt=prompt_extraccion,
                    source=url,
                    config=graph_config
                )
                
                # Ejecución del grafo
                resultado = smart_scraper_graph.run()
                
                # Enriquecimiento del payload con la URL de origen
                if isinstance(resultado, dict):
                    resultado['url_origen'] = url 
                    directorio_final.append(resultado)
                else:
                    directorio_final.append({"url_origen": url, "datos_crudos": str(resultado)})
                    
                print(f"   {GREEN}✅ Parseo semántico exitoso. Entidades extraídas.{RESET}")
                
            except Exception as e:
                print(f"   {RED}❌ Falla estructural al escanear el nodo: {e}{RESET}")
            
            # Latencia estocástica para proteger el endpoint del LLM de bloqueos por Rate Limit
            time.sleep(2)

    except FileNotFoundError:
        print(f"\n{RED}❌ [ERROR DE RADAR] No se encontró el archivo de rutas '{archivo_urls}'.{RESET}")
        sys.exit(1)

    # 6. Serialización y Consolidación del Directorio
    try:
        with open(nombre_archivo_salida, "w", encoding="utf-8") as archivo:
            json.dump({"empresas_extraidas": directorio_final}, archivo, indent=4, ensure_ascii=False)
        
        print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
        print(f"{GREEN}{BOLD} 🚀 ¡FILTRO SEMÁNTICO COMPLETADO! {len(directorio_final)} empresas perfiladas.{RESET}")
        print(f"{BLUE} 📂 Bóveda de salida: {nombre_archivo_salida}{RESET}")
        print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    except Exception as e:
        print(f"\n{RED}❌ Error al intentar guardar la bóveda de datos: {e}{RESET}")

if __name__ == "__main__":
    iniciar_filtro_semantico()
