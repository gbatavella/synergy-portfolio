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

def validar_llave_google():
    print(f"\n{BLUE}{BOLD}{'='*55}{RESET}")
    print(f"{BLUE}{BOLD} 🛡️ SYNERGY GOOGLE API VALIDATOR {RESET}")
    print(f"{BLUE}{BOLD}{'='*55}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÚNKER (OPSEC)
    # ==========================================
    print(f"{GRAY}[*] Accediendo a la bóveda .env...{RESET}")
    load_dotenv()
    
    # KILL SWITCH: Purga llaves globales del SO para evitar conflictos (como vimos ayer)
    if "GOOGLE_API_KEY" in os.environ:
        del os.environ["GOOGLE_API_KEY"]
        
    api_key = os.getenv("GEMINI_API_KEY") # Usamos el estándar de la agencia

    if not api_key:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta GEMINI_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    print(f"{GRAY}[*] Verificando llave: {api_key[:8]}...{RESET}")

    # ==========================================
    # 2. PRUEBA DE INFERENCIA
    # ==========================================
    genai.configure(api_key=api_key)
    
    try:
        print(f"{GRAY}[*] Conectando al clúster (gemini-1.5-flash)...{RESET}")
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Responde solo con la palabra: FUNCIONA")
        print(f"\n{GREEN}✅ ¡LLAVE VÁLIDA! El motor tiene permiso de inferencia.{RESET}")
        print(f"{GREEN}Respuesta del modelo: {BOLD}{response.text.strip()}{RESET}\n")
    except Exception as e:
        print(f"\n{RED}❌ ERROR CRÍTICO DE AUTENTICACIÓN:{RESET} {e}")
        print(f"{YELLOW}👉 Diagnóstico: Verifica que la llave en .env sea correcta y tenga saldo operativo.{RESET}\n")

if __name__ == "__main__":
    validar_llave_google()
