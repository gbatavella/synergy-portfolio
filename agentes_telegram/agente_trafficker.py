import os
import sys
from openai import OpenAI
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

def iniciar_trafficker():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} SYNERGY COMPETITOR X-RAY (TRAFFICKER AGENT V1.0) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # --- CARGA DE BÓVEDA SEGURA (OPSEC) ---
    load_dotenv()
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    if not OPENROUTER_API_KEY:
        print(f"{RED}X [ERROR CRÍTICO] Falta OPENROUTER_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    MODELO_IA = os.getenv("TRAFFICKER_MODEL", "google/gemini-2.0-flash-001")

    # Inicialización del cliente OpenAI enrutado a OpenRouter
    client = OpenAI(
        base_url="[https://openrouter.ai/api/v1](https://openrouter.ai/api/v1)",
        api_key=OPENROUTER_API_KEY,
    )

    PROMPT_SISTEMA = """
    Eres un Senior Growth Hacker y Analista de Competencia experto en Infoproductos.
    Tu objetivo es transformar las reseñas negativas de competidores en 'Oportunidades de Oro' para el producto 'El Clon Vendedor'.

    Para cada reseña negativa que recibas, debes generar un JSON con:
    1. "dolor_detectado": El problema real del cliente (ej: mala configuración).
    2. "oportunidad_de_oro": Cómo 'El Clon Vendedor' va a resolver esto mejor.
    3. "gancho_comercial": Una frase para el copy de Gumroad que ataque esa debilidad.
    4. "nivel_prioridad": (Alta/Media/Baja) basado en qué tanto se repite el problema.

    Sé cínico con la competencia y brillante con la solución.
    """

    # --- SIMULADOR DE RECOLECCIÓN (Input manual o Scraping) ---
    resenas_ejemplo = """
    'The setup is too complicated for non-tech people.'
    'I bought the prompts but they don't work for Spanish markets.'
    'The seller never answers the support emails.'
    'It is just a PDF, I expected a step-by-step video.'
    """

    print(f"{GRAY}[*] Enlazando con el clúster cognitivo {BOLD}{MODELO_IA}{RESET}{GRAY} vía API...{RESET}")
    print(f"{YELLOW}[*] Ingiriendo quejas de consumidores del mercado competidor...{RESET}\n")

    try:
        response = client.chat.completions.create(
            model=MODELO_IA,
            messages=[
                {"role": "system", "content": PROMPT_SISTEMA},
                {"role": "user", "content": f"Analiza estas reseñas de productos de la competencia en Gumroad y extrae las Oportunidades de Oro: \n\n{resenas_ejemplo}"}
            ],
            response_format={ "type": "json_object" } # Coerción de salida limpia
        )
        
        # Limpieza de backticks de Markdown residuales
        respuesta_cruda = response.choices[0].message.content
        respuesta_limpia = respuesta_cruda.replace("```json", "").replace("```", "").strip()
        
        print(f"{GREEN}[+] Análisis de vulnerabilidades del mercado completado con éxito.{RESET}\n")
        print(f"{CYAN}{BOLD} [REPORTE DE OPORTUNIDADES ESTRATÉGICAS]: {RESET}\n")
        print(f"{WHITE}{respuesta_limpia}{RESET}\n")
        
        # Exportación de Inteligencia
        archivo_salida = "reporte_oportunidades.json"
        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.write(respuesta_limpia)
            
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}")
        print(f"{GREEN}✓ Inteligencia comercial asegurada en: {archivo_salida}{RESET}")
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")
        
    except Exception as e:
        print(f"\n{RED}X Fricción crítica en la matriz de análisis: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_trafficker()
