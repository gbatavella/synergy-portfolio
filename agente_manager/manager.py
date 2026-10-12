from googlesearch import search
from openai import OpenAI
import os
import sys
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

def iniciar_manager_investigador():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧠 SYNERGY NICHE MANAGER (TRINITY WEB INVESTIGATOR) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÚNKER SEGURO (OPSEC)
    # ==========================================
    load_dotenv()
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    if not OPENROUTER_API_KEY:
        print(f"{RED}X [ERROR CRÍTICO] Falta OPENROUTER_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )

    # ==========================================
    # 2. EL SABUESO BUSCA "DOLORES" EN LA RED
    # ==========================================
    nicho_objetivo = input(f"{YELLOW}🎯 Ingresa el nicho o dolor a investigar (ej. mayores problemas emprendedores 2026): {RESET}").strip()
    
    if not nicho_objetivo:
        nicho_objetivo = "mayores problemas de emprendedores digitales 2026"
        print(f"{GRAY}>> Utilizando nicho por defecto: '{nicho_objetivo}'{RESET}")

    print(f"\n{GRAY}[*] Desplegando rastreadores SERP en Google...{RESET}")
    textos_recolectados = ""

    try:
        # Extracción de los 5 mejores artículos
        resultados = search(nicho_objetivo, num_results=5, lang="es", advanced=True)
        
        for res in resultados:
            textos_recolectados += f"- {res.title}: {res.description}\n"
            
        print(f"{GREEN}[+] Datos orgánicos extraídos con éxito.{RESET}")
        print(f"{GRAY}[*] Transfiriendo inteligencia cruda al clúster cognitivo (Trinity) para análisis...{RESET}\n")
        
        # ==========================================
        # 3. ANÁLISIS Y SÍNTESIS ESTRATÉGICA
        # ==========================================
        prompt_manager = f"""
        Eres el Agente Manager del ecosistema 'Synergy Human & AI Agents', liderado por el Ingeniero Autónomo. 
        Tu trabajo es analizar información de la web y encontrar nichos rentables.
        
        Aquí tienes un resumen de lo que la gente está buscando en Google sobre el nicho objetivo:
        {textos_recolectados}
        
        Basado estrictamente en estos dolores reales, debes entregar un reporte de 2 puntos:
        1. ¿Cuál es el problema número 1 que más se repite en estas búsquedas?
        2. Propón 1 título "gancho" y altamente vendedor para un infoproducto (PDF o Curso corto) que solucione este problema. 
        
        REGLA DE ORO: La solución y el título del infoproducto DEBEN incluir el uso de "Agentes IA", "Inteligencia Artificial" o "Automatización Inteligente" como el vehículo para resolver el problema.
        """

        response = client.chat.completions.create(
            model="arcee-ai/trinity-large-preview:free",
            messages=[{"role": "user", "content": prompt_manager}],
            extra_headers={"HTTP-Referer": "https://t.me", "X-Title": "Synergy Manager"}
        )

        analisis_final = response.choices[0].message.content
        
        print(f"{BLUE}{BOLD}{'='*65}{RESET}")
        print(f"{GREEN}{BOLD} 💎 REPORTE ESTRATÉGICO PARA EL INGENIERO AUTÓNOMO 💎 {RESET}")
        print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
        print(f"{WHITE}{analisis_final}{RESET}\n")
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")

    except Exception as e:
        print(f"\n{RED}X Anomalía en la matriz de investigación: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_manager_investigador()
