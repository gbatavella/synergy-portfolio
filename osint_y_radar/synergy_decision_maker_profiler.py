import os
import json
import nest_asyncio
import time
import sys
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

def iniciar_perfilador():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🎯 SYNERGY DECISION-MAKER PROFILER (LINKEDIN DORKING) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    if not OPENROUTER_API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta OPENROUTER_API_KEY en el entorno (.env).{RESET}")
        sys.exit(1)

    # 2. Configuración del Agente Explorador
    graph_config = {
        "llm": {
            "api_key": OPENROUTER_API_KEY,
            "model": "openai/openrouter/auto", 
            "base_url": "https://openrouter.ai/api/v1",
        },
        "verbose": False, # Desactivado para mantener la consola limpia
        "headless": True,
    }

    # 3. Ingesta de Datos (Soporte para Mock Data en repositorios públicos)
    archivo_empresas = os.getenv("TARGET_COMPANIES_FILE", "DIRECTORIO_B2B_TARGET.json")
    print(f"{GRAY}🔥 Intentando ingestar matriz de empresas desde: {archivo_empresas}...{RESET}")

    empresas = []
    try:
        with open(archivo_empresas, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            empresas = datos.get("empresas", [])
            print(f"{GREEN}✅ Base de datos cargada. {len(empresas)} entidades detectadas.{RESET}")
    except FileNotFoundError:
        print(f"{YELLOW}⚠️ Archivo no detectado. Generando matriz de simulación en memoria (Mock Mode)...{RESET}")
        empresas = [
            {"content": {"nombre_empresa": "Globant"}},
            {"content": {"nombre_empresa": "Mercado Libre"}},
            {"content": {"nombre_empresa": "Uala"}}
        ]

    decisores_extraidos = []
    
    cargo_objetivo = input(f"\n{GREEN}🎯 Ingresa el Cargo a perfilar (ej. CEO, Director de Marketing): {RESET}").strip()
    if not cargo_objetivo:
        cargo_objetivo = "Director de Recursos Humanos"
        
    archivo_salida = f"DECISORES_{cargo_objetivo.replace(' ', '_').upper()}.json"

    # 4. Ignición del Perfilador Blindado (Checkpointing)
    print(f"\n{BLUE}🚀 INICIANDO PROTOCOLO DE RESOLUCIÓN DE IDENTIDAD...{RESET}\n")
    
    for i, empresa_data in enumerate(empresas):
        if "content" in empresa_data and isinstance(empresa_data["content"], dict):
            empresa = empresa_data["content"]
        else:
            empresa = empresa_data
            
        nombre_empresa = empresa.get("nombre_empresa", "NA")
        
        if nombre_empresa == "NA" or not nombre_empresa:
            continue

        print(f"{GRAY}[{i+1}/{len(empresas)}] [PERFILANDO] -> Buscando {cargo_objetivo} en: {BOLD}{nombre_empresa}{RESET}")
        
        # PROMPT SEMÁNTICO Y DORK BOOLEANO
        prompt_perfilador = f"""
        Realiza una búsqueda DORK estricta en Google usando:
        site:linkedin.com/in "{cargo_objetivo}" "{nombre_empresa}" Argentina
        
        Extrae la información de la primera persona relevante que aparezca en los resultados.
        
        Extrae ESTRICTAMENTE:
        1. "nombre_decisor": Nombre y Apellido.
        2. "cargo": El puesto exacto que ocupa.
        3. "linkedin_url": El enlace a su perfil.
        4. "email_estimado": Si figura algún email, anótalo. Si no, pon "NA".
        
        Devuelve un JSON limpio. Si no encuentras, indica "No encontrado".
        """
        
        try:
            search_graph = SearchGraph(prompt=prompt_perfilador, config=graph_config)
            resultado = search_graph.run()
            
            # Blindaje contra variaciones de respuesta del LLM
            if isinstance(resultado, list):
                for item in resultado:
                    if isinstance(item, dict):
                        item['empresa_objetivo'] = nombre_empresa
                decisores_extraidos.extend(resultado)
            elif isinstance(resultado, dict):
                resultado['empresa_objetivo'] = nombre_empresa
                decisores_extraidos.append(resultado)
            else:
                decisores_extraidos.append({
                    "empresa_objetivo": nombre_empresa,
                    "datos_crudos": str(resultado)
                })
                
            print(f"{GREEN}  ✅ Decisor asegurado para {nombre_empresa}.{RESET}")
            
            # GUARDADO DINÁMICO (CHECKPOINT)
            with open(archivo_salida, "w", encoding="utf-8") as file:
                json.dump({"decisores": decisores_extraidos}, file, indent=4, ensure_ascii=False)
                
            # PAUSA TÁCTICA PARA CUIDAR EL ENDPOINT
            print(f"{GRAY}  ⏳ Enfriando motor (15s)...{RESET}")
            time.sleep(15)
            
        except Exception as e:
            print(f"{RED}  ❌ Fricción al perfilar {nombre_empresa}: {e}{RESET}")
            print(f"{YELLOW}  ⚠️ Aplicando pausa de castigo de seguridad (30s)...{RESET}")
            time.sleep(30)

    print(f"\n{GREEN}{BOLD}🚀 ¡PERFILADO COMPLETO Y BLINDADO!{RESET}")
    print(f"{BLUE}>> Los objetivos están asegurados en la bóveda: {archivo_salida}{RESET}\n")

if __name__ == "__main__":
    iniciar_perfilador()
