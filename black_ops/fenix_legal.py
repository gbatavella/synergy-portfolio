import requests
import json
import os
import sys
import time
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

def iniciar_fenix_legal():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🏛️  SYNERGY PHOENIX LEGAL (HIGH-AVAILABILITY COUNSEL) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CONFIGURACIÓN DEL BÚNKER LEGAL VIP (OPSEC)
    # ==========================================
    load_dotenv()
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    if not OPENROUTER_API_KEY:
        print(f"{RED}X [ERROR CRÍTICO] Falta OPENROUTER_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    # 🛡️ SISTEMA DE CASCADA PREMIUM (ALTA DISPONIBILIDAD VIP)
    MODELOS_CASCADA = [
        "anthropic/claude-3.5-sonnet",       # Bala 1: El mejor analista legal/fiscal
        "openai/gpt-4o",                     # Bala 2: Respaldo de inteligencia extrema
        "meta-llama/llama-3.3-70b-instruct"  # Bala 3: Contingencia táctica (Open Source)
    ]

    def consultar_agente_legal(consulta_ceo):
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        
        # ADN PREMIUM DEL AGENTE FÉNIX
        sistema_prompt = """Eres 'Fénix', el Agente Legal y Fiscal Senior de Synergy Human & AI Agents.
        Tu misión es la recuperación legal y financiera de las empresas MUSTAFÁ SH y TAVSOL S.A. en Argentina.
        Hablas con terminología técnica jurídica y contable. Eres implacable en la protección patrimonial y experto en normativas de AFIP e IGJ.
        Te diriges al usuario como 'Comandante' o 'Director'. Tus respuestas deben ser precisas, estratégicas y orientadas a resultados corporativos."""

        # 🔄 MOTOR DE AUTO-RECUPERACIÓN VIP (CASCADE ROUTING)
        for modelo in MODELOS_CASCADA:
            data = {
                "model": modelo,
                "messages": [
                    {"role": "system", "content": sistema_prompt},
                    {"role": "user", "content": consulta_ceo}
                ],
                "timeout": 60
            }

            try:
                response = requests.post(url, headers=headers, data=json.dumps(data), timeout=60)
                resultado = response.json()
                
                # Evaluación de fallas a nivel API
                if 'error' in resultado or 'choices' not in resultado:
                    print(f"\r{YELLOW}   [⚠️] Satélite {modelo.split('/')[1]} reporta anomalía. Ruteando al siguiente...{RESET}", end="")
                    time.sleep(1)
                    continue 
                    
                print(f"\r{GREEN}   [✅] Enlace VIP establecido vía: {BOLD}{modelo.split('/')[1]}{RESET}       ")
                return resultado['choices'][0]['message']['content']
                
            except requests.exceptions.RequestException as e:
                print(f"\r{YELLOW}   [⚠️] Falla de red en satélite {modelo.split('/')[1]}. Ruteando...{RESET}", end="")
                time.sleep(1)
                continue

        return f"\n{RED}🛑 ALERTA CRÍTICA: Todos los satélites VIP están fuera de línea. Falla sistémica.{RESET}"

    # ==========================================
    # 4. INTERFAZ DE MANDO CORPORATIVO
    # ==========================================
    print(f"{GREEN}[+] Sistemas Synergy Online. Módulo de Alta Disponibilidad Activo.{RESET}")
    print(f"{GRAY}[*] Esperando instrucciones operativas...{RESET}\n")
    
    while True:
        try:
            orden = input(f"{YELLOW}⚖️ [Director] > {RESET}").strip()
            if orden.lower() in ['salir', 'exit', 'quit']:
                print(f"\n{GRAY}💨 Cerrando despacho legal. Hasta pronto, Comandante.{RESET}\n")
                break
                
            if not orden:
                continue
                
            print(f"{GRAY}🔍 Fénix auditando la situación a través del clúster...{RESET}", end="")
            
            respuesta = consultar_agente_legal(orden)
            
            print(f"\n{CYAN}{BOLD}🛡️ [Fénix Legal]:{RESET}\n")
            print(f"{WHITE}{respuesta}{RESET}\n")
            print(f"{BLUE}{'-'*65}{RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{RED} Operación cancelada por el usuario.{RESET}\n")
            break

if __name__ == "__main__":
    iniciar_fenix_legal()
