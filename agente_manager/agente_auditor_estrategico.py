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

def auditoria_estrategica_synergy():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 📊 SYNERGY STRATEGIC AUDITOR (SEO & MARKET RESEARCH) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÚNKER (OPSEC)
    # ==========================================
    print(f"{GRAY}[*] Autenticando bóveda y enlazando Gemini 2.5 Flash...{RESET}")
    load_dotenv()
    
    # KILL SWITCH: Evitamos colisiones de llaves globales
    if "GOOGLE_API_KEY" in os.environ:
        del os.environ["GOOGLE_API_KEY"]
        
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta GEMINI_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # ==========================================
    # 2. INGENIERÍA DE PROMPTS (ESTRATEGIA MACRO)
    # ==========================================
    prompt = """
    Analiza el mercado actual (Octubre 2026) bajo nuestra planificación maestra B2B:
    
    1. SEO EN GOOGLE: Identifica las 10 palabras clave 'Long Tail' con baja competencia para posicionar infoproductos técnicos.
    2. AMAZON KDP: Detecta 2 micro-nichos de E-books que tengan demanda hoy y poca oferta.
    3. ESTRATEGIA SOCIAL: Define un ángulo de venta para TikTok, LinkedIn y Marketplace (Meta).
    
    Para cada punto, dame el 'Título Gancho', la 'Propuesta de Valor' y por qué representa una oportunidad de facturación de 1M USD.
    Formatea tu respuesta en Markdown puro, con viñetas y títulos. Cero introducciones o saludos.
    """
    
    print(f"{YELLOW}[*] Ejecutando escaneo macroeconómico de activos digitales...{RESET}")
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"{RED}❌ Error en la matriz neuronal: {e}{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    reporte = auditoria_estrategica_synergy()
    
    print(f"\n{GREEN}{BOLD}--- REPORTE MAESTRO DE ACTIVOS DIGITALES (SEO & AMAZON) ---{RESET}\n")
    print(reporte)
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}\n")
