import os
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

def verificar_llave(api_key):
    print(f"\n{GRAY}[*] Verificando estado de la API Key en OpenRouter...{RESET}")
    if not api_key:
        print(f"{RED}❌ [CRÍTICO] No hay llave configurada en el .env.{RESET}")
        return False
    
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get("https://openrouter.ai/api/v1/auth/key", headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"{GREEN}✅ [LLAVE OPERATIVA] Autenticación exitosa. Tienes acceso autorizado.{RESET}")
            return True
        else:
            print(f"{RED}❌ [LLAVE INVÁLIDA] El servidor rechazó la llave (Código {response.status_code}).{RESET}")
            return False
    except Exception as e:
        print(f"{RED}💥 [ERROR DE RED] No se pudo conectar al servidor de autenticación: {e}{RESET}")
        return False

def load_balancer(api_key, modelos_candidatos):
    print(f"\n{YELLOW}⚖️ [LOAD BALANCER] Iniciando escaneo de holgura y disponibilidad...{RESET}")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://synergy-raas.com", 
        "X-Title": "Synergy Autonomous AI"
    }

    for modelo in modelos_candidatos:
        print(f"{GRAY}🔍 Evaluando motor: {modelo}...{RESET}")
        payload = {
            "model": modelo,
            "messages": [{"role": "user", "content": "Responde solo con la palabra 'Activo'."}],
            "max_tokens": 5 
        }
        
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=8 
            )
            
            if response.status_code == 200:
                print(f"{GREEN}✅ [SELECCIONADO] {modelo} está EN LÍNEA y con holgura de uso.{RESET}")
                return modelo 
            else:
                print(f"{YELLOW}⚠️ [SATURADO/ERROR] {modelo} devolvió error {response.status_code}. Saltando al siguiente...{RESET}")
                
        except Exception as e:
            print(f"{RED}❌ [CAÍDO] Falla de conexión con {modelo}: {e}{RESET}")

    print(f"{RED}🚨 [CRÍTICO] Ningún motor de la lista está disponible en este momento.{RESET}")
    return None

def iniciar_balanceador():
    print(f"\n{BLUE}{BOLD}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD} ⚖️ SYNERGY OPENROUTER LOAD BALANCER (GLOBAL ROUTER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*60}{RESET}\n")

    load_dotenv()
    key = os.getenv("API_KEY_Manager_Claude_35")

    if verificar_llave(key):
        titanes_disponibles = [
            "anthropic/claude-3.5-sonnet",
            "anthropic/claude-3-haiku",
            "google/gemini-1.5-flash"
        ]
        mejor_modelo = load_balancer(key, titanes_disponibles)
        
        if mejor_modelo:
            print(f"\n{GREEN}{BOLD}🚀 RESULTADO: El Load Balancer recomienda inyectar '{mejor_modelo}' en el Oráculo.{RESET}\n")
        else:
            print(f"\n{RED}🛑 Operación abortada: Ningún modelo superó el test de latencia.{RESET}\n")
    else:
        print(f"\n{RED}🛑 Operación abortada: Repara tu API Key en el archivo .env antes de continuar.{RESET}\n")

if __name__ == "__main__":
    iniciar_balanceador()
