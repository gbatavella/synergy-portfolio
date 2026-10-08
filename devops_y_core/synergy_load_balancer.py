import os
import time
import sys
import requests
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

# --- INICIALIZACIÓN DE SEGURIDAD ---
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def verificar_llave(api_key):
    print(f"{GRAY}🔑 [SEGURIDAD] Verificando estado de la API Key en OpenRouter...{RESET}")
    if not api_key:
        print(f"{RED}❌ [CRÍTICO] No hay llave configurada en la bóveda .env.{RESET}")
        return False
    
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get("https://openrouter.ai/api/v1/auth/key", headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"{GREEN}✅ [LLAVE OPERATIVA] Autenticación exitosa. Acceso autorizado.{RESET}")
            return True
        else:
            print(f"{RED}❌ [LLAVE INVÁLIDA] El servidor rechazó la llave (HTTP {response.status_code}).{RESET}")
            return False
    except Exception as e:
        print(f"{RED}💥 [ERROR DE RED] No se pudo conectar al endpoint de autenticación: {e}{RESET}")
        return False

def load_balancer(modelos_candidatos):
    print(f"\n{YELLOW}⚖️ [LOAD BALANCER] Iniciando escaneo de holgura y disponibilidad...{RESET}")
    
    # Headers institucionales extraídos del entorno para proteger OPSEC
    app_url = os.getenv("SYNERGY_APP_URL", "https://synergy-raas.com")
    app_title = os.getenv("SYNERGY_APP_TITLE", "Synergy Autonomous AI")
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": app_url, 
        "X-Title": app_title
    }

    for modelo in modelos_candidatos:
        print(f"{GRAY}🔍 Evaluando nodo de procesamiento: {BOLD}{modelo}{RESET}...")
        payload = {
            "model": modelo,
            "messages": [{"role": "user", "content": "Responde solo con la palabra 'Activo'."}],
            "max_tokens": 5 # Consumo mínimo para testear latencia y estado
        }
        
        try:
            # Ping asíncrono simulado a la API
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=8 
            )
            
            if response.status_code == 200:
                print(f"{GREEN}  ✅ [SELECCIONADO] {modelo} está EN LÍNEA y con holgura de uso.{RESET}")
                return modelo 
            else:
                print(f"{YELLOW}  ⚠️ [SATURADO/ERROR] {modelo} devolvió error {response.status_code}. Evaluando respaldo...{RESET}")
                time.sleep(1)
                
        except Exception as e:
            print(f"{RED}  ❌ [CAÍDO] Falla de conexión estructural con {modelo}: {e}{RESET}")

    print(f"\n{RED}{BOLD}🚨 [CRÍTICO] Ningún motor de la lista candidata está disponible.{RESET}")
    return None

def iniciar_balanceador():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🔀 SYNERGY LOAD BALANCER (API HEALTH & FALLBACK ALGORITHM) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    if verificar_llave(OPENROUTER_API_KEY):
        titanes_disponibles = [
            "anthropic/claude-3.5-sonnet",
            "anthropic/claude-3-haiku",
            "google/gemini-1.5-flash"
        ]
        
        mejor_modelo = load_balancer(titanes_disponibles)
        
        if mejor_modelo:
            print(f"\n{GREEN}{BOLD}🚀 [RUTEO COMPLETADO] El Load Balancer inyectará '{mejor_modelo}' en el Core.{RESET}\n")
        else:
            print(f"\n{RED}🛑 [FALLA CASCADA] Imposible iniciar el enjambre. Todos los nodos están caídos.{RESET}\n")
    else:
        print(f"\n{RED}🛑 Operación abortada: Repare su API Key criptográfica antes de continuar.{RESET}\n")

if __name__ == "__main__":
    iniciar_balanceador()
