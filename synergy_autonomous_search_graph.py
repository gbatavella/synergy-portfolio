import os
import json
import time
import sys
import nest_asyncio
from dotenv import load_dotenv
from scrapegraphai.graphs import SearchGraph

# --- SEGURIDAD Y CONFIGURACIÓN ---
load_dotenv()
nest_asyncio.apply()

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def efecto_tipeo(texto, retraso=0.015):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(retraso)
    print()

def rapid_output(text, delay=0.03):
    print(text)
    time.sleep(delay)

def iniciar_motor_semantico():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🕸️ SYNERGY AUTONOMOUS SEARCHGRAPH (SEMANTIC SCRAPER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    if not OPENROUTER_API_KEY:
        print(f"{RED}❌ [ALERTA CRÍTICA] No se encontró OPENROUTER_API_KEY en el entorno (.env){RESET}")
        sys.exit(1)

    rapid_output(f"{GRAY}[*] Conectando a nodos LLM de OpenRouter...{RESET}")
    
    # 2. Configuración (Modo Fantasma Autónomo)
    graph_config = {
        "llm": {
            "api_key": OPENROUTER_API_KEY,
            "model": "openai/openrouter/auto",
            "base_url": "https://openrouter.ai/api/v1",
        },
        "verbose": True,
        "headless": True, 
    }

    print(f"\n{YELLOW}>> Configuración de Target B2B{RESET}")
    nicho = input(f"{GREEN}🎯 Ingresa el nicho (ej. Agencias de Marketing, Corralones): {RESET}").strip()
    ubicacion = input(f"{GREEN}📍 Ingresa la ubicación (ej. Madrid, Miami, Junín): {RESET}").strip()
    cantidad = input(f"{GREEN}🔢 Cantidad de prospectos a extraer (ej. 3, 5, 10): {RESET}").strip()

    if not nicho or not ubicacion:
        nicho, ubicacion, cantidad = "SaaS Startups", "Austin, Texas", "3"
        print(f"{YELLOW}[!] Datos incompletos. Ejecutando objetivo de demostración: {nicho} en {ubicacion}{RESET}")

    # 3. El Prompt Semántico (La Orden de Cacería)
    prompt_busqueda = f"""
    Busca en internet {cantidad} empresas reales ({nicho}) ubicadas en {ubicacion}.
    Entra a sus páginas o directorios y extrae estrictamente:
    1. Nombre de la Empresa.
    2. Dirección exacta.
    3. Teléfono de contacto para negocios B2B.
    Devuelve los resultados en un formato JSON limpio y estructurado.
    """

    # 4. Ignición del Motor Autónomo
    print(f"\n{BLUE}🚀 Iniciando Flujo Multi-Agente (SearchGraph Autónomo)...{RESET}")
    efecto_tipeo(f"{GRAY}>> Delegando navegación y parseo semántico al enjambre LLM...{RESET}")
    
    try:
        search_graph = SearchGraph(
            prompt=prompt_busqueda,
            config=graph_config
        )

        # 5. El motor busca, navega y extrae
        resultado = search_graph.run()

        # 6. Guardar el resultado en un archivo .json físico
        nombre_archivo = f"LEADS_{nicho.replace(' ', '_').upper()}_{ubicacion.replace(' ', '_').upper()}.json"

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(resultado, archivo, indent=4, ensure_ascii=False)

        print(f"\n{GREEN}{BOLD}{'='*65}{RESET}")
        print(f"{GREEN}{BOLD} ✅ ¡ÉXITO ABSOLUTO! Extracción semántica completada.{RESET}")
        print(f"{GREEN}{BOLD}{'='*65}{RESET}")
        print(f"{BLUE}>> Los prospectos corporativos se han guardado en: {nombre_archivo}{RESET}")
        print(f"{GRAY}>> ¡El ecosistema Synergy está listo para iniciar el contacto!{RESET}\n")

    except Exception as e:
        print(f"\n{RED}❌ Fricción detectada durante la extracción autónoma: {e}{RESET}")

if __name__ == "__main__":
    iniciar_motor_semantico()
