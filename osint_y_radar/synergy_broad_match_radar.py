import os
import json
import sys
import time
import nest_asyncio
from dotenv import load_dotenv
from scrapegraphai.graphs import SearchGraph

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def iniciar_red_arrastre():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 📡 SYNERGY BROAD MATCH RADAR (LOGISTICS OSINT) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # 1. Carga de Credenciales y Parche Asíncrono
    load_dotenv()
    nest_asyncio.apply()

    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    if not OPENROUTER_API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta OPENROUTER_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    print(f"{GRAY}[*] Enlazando clúster de investigación autónoma...{RESET}")

    # 2. Configuración del Grafo Autónomo
    graph_config = {
        "llm": {
            "api_key": OPENROUTER_API_KEY,
            "model": "openai/openrouter/auto",
            "base_url": "https://openrouter.ai/api/v1",
        },
        "verbose": False, # Silenciado para una consola táctica impecable
        "headless": True, 
    }

    # Parámetros logísticos dinámicos (Protege tus nichos en el repo público)
    zona_origen = os.getenv("RADAR_ZONA_ORIGEN", "Junín (BA), La Carlota (Córdoba), SW Córdoba")
    zona_destino = os.getenv("RADAR_ZONA_DESTINO", "Provincia de Buenos Aires (Zona Sur)")
    nicho_busqueda = os.getenv("RADAR_NICHO", "FÁBRICAS, PRODUCTORES AGRÍCOLAS o DISTRIBUIDORAS")

    # 3. Prompt Semántico: La Red de Arrastre
    prompt_embudo = f"""
    Realiza una investigación profunda en internet para encontrar un listado amplio de {nicho_busqueda} ubicadas específicamente en las siguientes regiones:
    - {zona_origen}

    El requisito fundamental es que estas entidades realicen envíos de CARGAS GENERALES, materiales o mercadería hacia {zona_destino}.

    Extrae al menos 5 empresas diferentes que cumplan el criterio. Para cada una, proporciona:
    1. "nombre_empresa": Nombre oficial de la empresa.
    2. "rubro": Tipo de mercadería que producen o mueven.
    3. "ubicacion": Ubicación exacta (Ciudad y Provincia).
    4. "logistica": Un breve resumen de su logística (¿mencionan envíos a la zona de destino?).
    5. "contacto": Teléfono o email de contacto B2B.

    Devuelve los resultados ESTRICTAMENTE en un formato JSON ordenado.
    """

    nombre_archivo = os.getenv("JSON_BROAD_MATCH_OUTPUT", "DEMANDA_AMPLIA_RUTAS.json")

    print(f"{YELLOW}>> Parámetros del Sonar Configurados:{RESET}")
    print(f"{WHITE}   - Origen: {zona_origen}{RESET}")
    print(f"{WHITE}   - Destino: {zona_destino}{RESET}")
    print(f"{WHITE}   - Nicho: {nicho_busqueda}{RESET}\n")

    # 4. Ignición
    print(f"{CYAN}⏳ Desplegando agentes de búsqueda en internet. Mapeando corredores logísticos...{RESET}")
    
    try:
        search_graph = SearchGraph(
            prompt=prompt_embudo,
            config=graph_config
        )

        resultado = search_graph.run()
        print(f"   {GREEN}✅ Nodos detectados y analizados con éxito.{RESET}")

        # 5. Volcado de Datos
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(resultado, archivo, indent=4, ensure_ascii=False)

        print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
        print(f"{GREEN}{BOLD} 🚀 ¡EXTRACCIÓN COMPLETADA! {RESET}")
        print(f"{BLUE} 📂 El embudo inicial se ha consolidado en: {nombre_archivo}{RESET}")
        print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    except Exception as e:
        print(f"\n{RED}❌ Fricción cognitiva durante la investigación autónoma: {e}{RESET}")

if __name__ == "__main__":
    iniciar_red_arrastre()
