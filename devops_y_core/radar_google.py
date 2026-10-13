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
CYAN = "\033[96m"

def iniciar_radar_google():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 📡 SYNERGY MODEL RADAR (GOOGLE GENAI SCANNER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÚNKER SEGURO (OPSEC)
    # ==========================================
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")

    if not API_KEY:
        print(f"{RED}X [ERROR CRÍTICO] Falta GEMINI_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    print(f"{GRAY}[*] Estableciendo enlace con la fábrica de Google AI Studio...{RESET}")

    try:
        client = genai.Client(api_key=API_KEY)
        modelos = client.models.list()
        
        contador = 0
        print(f"\n{GREEN}[+] Modelos detectados en el clúster:{RESET}\n")
        
        for m in modelos:
            print(f"  {CYAN}✓{RESET} {WHITE}{m.name}{RESET}")
            contador += 1
            
        print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
        print(f"{GREEN}🎯 Total de nodos detectados: {BOLD}{contador}{RESET}")
        print(f"{GRAY}>> Copia el nombre del modelo 'flash' o 'pro' más reciente para tu configuración.{RESET}")
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")

    except Exception as e:
        print(f"\n{RED}X Fricción al consultar la Matriz de Google: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_radar_google()
