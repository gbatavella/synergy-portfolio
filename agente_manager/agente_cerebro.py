import os
import sys
from google import genai
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

def iniciar_cerebro_macro():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧠 SYNERGY MARKET BRAIN (GEMINI 2.5 MACRO-PROFILER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÓVEDA SEGURA (OPSEC)
    # ==========================================
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")
    
    if not API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta GEMINI_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    ARCHIVO_DOLORES = "inteligencia_bruta_dolores.txt"
    ARCHIVO_INFORME = "perfil_psicologico_mercado.md"

    if not os.path.exists(ARCHIVO_DOLORES):
        print(f"{RED}❌ [FALLA ESTRUCTURAL] Falta el archivo de alimentación: {ARCHIVO_DOLORES}{RESET}")
        print(f"{GRAY}>> Extraiga transcripciones del campo de batalla antes de invocar a la matriz.{RESET}\n")
        sys.exit(1)

    print(f"{GRAY}[*] Ingestando transcripciones del campo de batalla...{RESET}")
    try:
        with open(ARCHIVO_DOLORES, "r", encoding="utf-8") as f:
            textos_brutos = f.read()
    except Exception as e:
        print(f"{RED}❌ Error de I/O al leer el botín: {e}{RESET}")
        sys.exit(1)

    # Truncado de seguridad para ventana de contexto
    texto_a_analizar = textos_brutos[:30000] 
    print(f"{CYAN} ↳ Bloque de datos cargado: {len(texto_a_analizar)} caracteres.{RESET}")

    print(f"\n{YELLOW}⏳ Conectando a la Matriz (gemini-2.5-flash) para psicoanálisis profundo...{RESET}")
    
    # Inicializamos el cliente con la nueva arquitectura SDK
    client = genai.Client(api_key=API_KEY)
    
    prompt_maestro = f"""
    Eres un experto en psicología del consumidor, especializado en el mercado anglosajón B2B y marketing digital.
    A continuación, te proporcionaré transcripciones reales de foros donde los usuarios se quejan de herramientas y creadores de software.
    
    Tu objetivo es leer estos textos y crear un "Buyer Persona" hiper-realista. No uses lenguaje de marketing tradicional. Esta gente está traumatizada por estafas y "upsells". Necesitan transparencia radical, honestidad y conexión humana (Trusted Advisor).
    
    Debes entregarme un informe con la siguiente estructura:
    1. DIAGNÓSTICO DEL DOLOR: ¿De qué están hartos exactamente? (Menciona sus miedos a los setups complejos, soporte fantasma, etc.).
    2. EL ANTÍDOTO DE TRANSPARENCIA: ¿Qué podemos regalarles (Lead Magnet) que realmente les sirva y les demuestre que somos éticos y transparentes?
    3. EL COPY PERFECTO: Redacta una plantilla de correo (en inglés) que no suene a vendedor, sino a un "colega honesto" que les ofrece ayuda genuina sin pedirles la tarjeta, incluyendo mi correo de contacto directo (ceo.synergy@proton.me).
    
    Aquí están las transcripciones de las trincheras:
    {texto_a_analizar}
    """

    try:
        # Disparo del prompt con el nuevo método SDK
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_maestro
        )
        
        informe = response.text
        
        with open(ARCHIVO_INFORME, "w", encoding="utf-8") as f:
            f.write(informe)
            
        print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
        print(f"{GREEN}{BOLD} ✅ PSICOANÁLISIS DE MERCADO COMPLETADO CON ÉXITO.{RESET}")
        print(f"{WHITE} 💎 El perfil del mercado y el copy de transparencia radical te esperan en:{RESET}")
        print(f"{BLUE} 📂 {ARCHIVO_INFORME}{RESET}")
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")
        
    except Exception as e:
        print(f"\n{RED}❌ Fricción en la conexión neuronal con Google GenAI: {e}{RESET}")
        print(f"{GRAY}>> Verifica el estado de tu API Key y la disponibilidad del modelo 2.5.{RESET}\n")

if __name__ == "__main__":
    iniciar_cerebro_macro()
