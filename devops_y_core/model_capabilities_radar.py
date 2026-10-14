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
CYAN = "\033[96m"

def iniciar_escaneo_capacidades():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🔍 SYNERGY CAPABILITIES RADAR (GENAI SCANNER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÚNKER (OPSEC)
    # ==========================================
    load_dotenv()
    
    # KILL SWITCH: Anula llaves globales del sistema operativo
    if "GOOGLE_API_KEY" in os.environ:
        del os.environ["GOOGLE_API_KEY"]
        
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta GEMINI_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    genai.configure(api_key=api_key)

    # ==========================================
    # 2. ESCANEO Y FILTRADO DE CAPACIDADES
    # ==========================================
    print(f"{GRAY}[*] Escaneando el depósito de motores de Google AI Studio...{RESET}")
    print(f"{YELLOW}[*] Filtrando estrictamente por método admitido: 'generateContent'{RESET}\n")
    
    print(f"{GREEN}=== MOTORES DISPONIBLES PARA TU SISTEMA ==={RESET}")
    
    try:
        contador = 0
        for modelo in genai.list_models():
            if 'generateContent' in modelo.supported_generation_methods:
                print(f"{CYAN} ⚡ {modelo.name}{RESET}")
                contador += 1
                
        print(f"\n{GRAY}[*] Total de modelos aptos para inferencia generativa: {BOLD}{contador}{RESET}\n")
    except Exception as e:
        print(f"{RED}❌ Error crítico al consultar la API de Google: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_escaneo_capacidades()
