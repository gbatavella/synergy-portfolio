import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def forjar_contenido():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} ✍️ SYNERGY CONTENT FORGE (KDP E-BOOK GENERATOR) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÚNKER (OPSEC)
    # ==========================================
    print(f"{GRAY}[*] Autenticando bóveda y cargando Gemini 2.5 Flash...{RESET}")
    load_dotenv()
    
    if "GOOGLE_API_KEY" in os.environ:
        del os.environ["GOOGLE_API_KEY"]
        
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta GEMINI_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # ==========================================
    # 2. INGENIERÍA DE PROMPTS (EDITORIAL)
    # ==========================================
    prompt = """
    Eres el 'Agente Content Forge', un escritor técnico experto en Inteligencia Artificial y un autor Bestseller en Amazon KDP.
    
    Tu tarea hoy es redactar la CONCLUSIÓN y DESPEDIDA del E-book titulado:
    "El Ingeniero Autónomo: Construye y Despliega Agentes de IA con LangChain y AutoGPT".
    
    Título de la Conclusión: "El Futuro es Autónomo, y Tú Tienes el Control"
    
    Temas exactos a desarrollar:
    1. Un resumen poderoso del viaje del lector (desde configurar la terminal hasta el despliegue de su ejército de IA).
    2. Un llamado a la acción (Call to Action) inspirador: El momento de construir y dominar el mercado es AHORA.
    3. Una despedida memorable que eleve el estatus del lector confirmando su nuevo título de "Ingeniero Autónomo".
    
    Reglas de redacción:
    1. Tono: Épico, motivador, directo y definitivo.
    2. Formato: Usa Markdown estricto (`##`, `###`).
    3. Cero relleno: Ve directo al contenido del libro, sin saludos ni introducciones tuyas.
    """
    
    print(f"{YELLOW}[*] Forjando capítulo: 'El Futuro es Autónomo, y Tú Tienes el Control'...{RESET}")
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"{RED}❌ Error en la generación neuronal: {e}{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    capitulo = forjar_contenido()
    
    nombre_archivo = "06_Conclusion.md"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(capitulo)
        
    print(f"\n{GREEN}✅ ¡ÉXITO DIRECTOR! La Conclusión se ha guardado físicamente en: {BOLD}{nombre_archivo}{RESET}\n")
