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

def iniciar_forjador():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 📜 SYNERGY BLUEPRINT FORGER V1.1 (LEAD MAGNET ENGINE) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CONEXIÓN AL CEREBRO AI (OPSEC)
    # ==========================================
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")
    
    if not API_KEY:
        print(f"{RED}X [ERROR CRÍTICO] Falta GEMINI_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    ARCHIVO_SALIDA = "No_BS_SaaS_Blueprint_Borrador.md"

    print(f"{GRAY}[*] Conectando a la Matriz (gemini-2.5-flash) para síntesis de documento...{RESET}")
    
    try:
        client = genai.Client(api_key=API_KEY)
        
        prompt_maestro = """
        Eres Gabriel Tavella, CEO de 'Synergy Human & AI Agents'. Eres un experto en automatización que está harto de ver cómo estafan a los emprendedores en foros como BlackHatWorld y Warrior Forum con software inútil y soporte inexistente.
        
        Tu objetivo es escribir el borrador completo de un Lead Magnet (un documento PDF gratuito) llamado:
        "The No-BS SaaS Success Blueprint: A Vendor-Agnostic Guide to Choosing and Implementing Digital Tools Without the Headaches".
        
        El tono debe ser directo, honesto, empático (de colega a colega) y CERO promocional. NO intentes vender nada. El objetivo es pura construcción de confianza ("Trusted Advisor").
        
        Escribe el contenido completo en INGLÉS, estructurado en estas 4 partes:
        
        1. INTRODUCCIÓN (La Verdad Cruda): Empatiza con el dolor de comprar software que resulta ser una estafa, con "upsells" infinitos y sin soporte. Explica por qué escribiste esta guía.
        
        2. EL CHECKLIST PRE-COMPRA (Cómo evitar estafas): Crea una lista de 5 preguntas difíciles que el usuario debe investigar ANTES de darle su tarjeta de crédito a cualquier "gurú". (Ej: ¿Hay costos ocultos? ¿El soporte técnico es humano o un bot inútil? ¿La promesa es realista o puro hype?).
        
        3. LA GUÍA DE IMPLEMENTACIÓN (Sobreviviendo al Setup): Da 3 pasos claros sobre cómo enfrentar la instalación de un software complejo sin frustrarse (Ej: documentar el proceso, no intentar integrar todo el primer día).
        
        4. CONCLUSIÓN Y LÍNEA DIRECTA: Cierra ofreciendo tu ayuda desinteresada. Menciona que si están estancados con alguna herramienta, pueden escribirte. Usa esta frase exacta para el cierre:
        "If you just want to vent about another broken tool you've encountered, feel free to hit me up directly. NO CREDIT CARD REQUIRED. ONLY YOUR ATTENTION PLEASE.
        My direct email: ceo.synergy@proton.me
        Gabriel Tavella, CEO."
        
        Escribe el documento en formato Markdown para que sea fácil de leer y convertir a PDF.
        """

        print(f"{YELLOW}⏳ Forjando activos de autoridad (Inbound Marketing)...{RESET}")
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_maestro
        )
        
        borrador = response.text
        
        with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
            f.write(borrador)
            
        print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
        print(f"{GREEN}✓ Borrador del Blueprint forjado y estructurado con éxito.{RESET}")
        print(f"{GREEN}✓ El documento te espera en: {BOLD}{ARCHIVO_SALIDA}{RESET}")
        print(f"{GRAY}>> Ábrelo, revísalo y compílalo en PDF para la campaña de distribución.{RESET}")
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")
        
    except Exception as e:
        print(f"\n{RED}X Fricción en la conexión neuronal con Google GenAI: {e}{RESET}")
        print(f"{GRAY}>> Verifica tu cuota de API y la disponibilidad del modelo.{RESET}\n")

if __name__ == "__main__":
    iniciar_forjador()
