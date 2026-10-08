import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def iniciar_canario():
    print(f"\n{BLUE}{BOLD}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD} 🐦 SYNERGY CANARY NODE (GEMINI MODEL SCANNER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*60}{RESET}\n")

    print(f"{GRAY}[*] Accediendo a la bóveda de credenciales (.env)...{RESET}")
    load_dotenv()
    llave = os.getenv("GEMINI_API_KEY")

    if not llave:
        print(f"\n{RED}❌ [ERROR DE SEGURIDAD] No se encontró GEMINI_API_KEY en la bóveda.{RESET}")
        print(f"{YELLOW}>> Verifique su archivo .env antes de iniciar el despliegue del enjambre.{RESET}\n")
    else:
        print(f"{GREEN}[+] Credenciales detectadas. Iniciando protocolo de enlace con Google...{RESET}")
        
        try:
            # Autenticamos al canario
            genai.configure(api_key=llave)
            time.sleep(1) # Simulación de latencia de red
            print(f"{BLUE}✅ Autenticación exitosa. Escaneando arquitectura de modelos...{RESET}\n")
            
            print(f"{YELLOW}{BOLD}>> MODELOS LLM DISPONIBLES (Soporte generateContent):{RESET}")
            
            # Listamos y filtramos modelos
            modelos_encontrados = 0
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    print(f"{GREEN}  -> Nombre exacto:{RESET} {WHITE}{m.name}{RESET}")
                    modelos_encontrados += 1
                    time.sleep(0.05)
            
            print(f"\n{GRAY}[*] Escaneo finalizado. {modelos_encontrados} motores listos para integración.{RESET}\n")

        except Exception as e:
            print(f"\n{RED}❌ Falla en el enlace con los servidores de Google: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_canario()
