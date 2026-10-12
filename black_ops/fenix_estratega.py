import requests
import json
import os
import time
import sys
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

def iniciar_fenix():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🏛️  SYNERGY PHOENIX STRATEGIST (FORENSIC LEGAL AGENT) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 🏛️ CONFIGURACIÓN DE ÉLITE - SYNERGY (OPSEC)
    # ==========================================
    load_dotenv()
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    if not OPENROUTER_API_KEY:
        print(f"{RED}X [ERROR CRÍTICO] Falta OPENROUTER_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    MODELO_PRINCIPAL = os.getenv("PHOENIX_MODEL", "anthropic/claude-3.5-sonnet")

    def consultar_fenix_estratega(orden_director):
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        
        adn_prompt = """Eres 'Fénix Estratega', la unidad de inteligencia superior de Synergy.
        Tu misión es la recuperación legal/fiscal de TAVSOL S.A. y MUSTAFÁ SH.
        Roles: Experto Legal (Derecho Administrativo/Comercial), Actuario Financiero e Investigador Forense.
        Jurisdicción: Villa Dolores, Córdoba (República Argentina).
        Objetivo: Prescripción de deudas de +8 años, recuperación de loteos/parque industrial y blindaje patrimonial de los directores."""

        data = {
            "model": MODELO_PRINCIPAL,
            "messages": [
                {"role": "system", "content": adn_prompt},
                {"role": "user", "content": orden_director}
            ],
            "timeout": 60
        }

        # 🔄 MOTOR DE REINTENTOS (ANTI-ERROR 'CHOICES')
        for intento in range(1, 4):
            try:
                response = requests.post(url, headers=headers, data=json.dumps(data), timeout=60)
                
                if response.status_code == 200:
                    resultado = response.json()
                    if 'choices' in resultado:
                        return resultado['choices'][0]['message']['content']
                    else:
                        print(f"\r{YELLOW}   [⚠️] Micro-falla estructural en el clúster. Reintentando ({intento}/3)...{RESET}", end="")
                        time.sleep(2)
                else:
                    print(f"\r{YELLOW}   [⚠️] Rechazo HTTP {response.status_code}. Reintentando ({intento}/3)...{RESET}", end="")
                    time.sleep(2)
                    
            except requests.exceptions.RequestException as e:
                print(f"\r{YELLOW}   [⚠️] Latencia o corte de red: {e}. Reintentando ({intento}/3)...{RESET}", end="")
                time.sleep(2)

        return f"\n{RED}🛑 ERROR CRÍTICO: El volumen de datos superó el tiempo de espera o el clúster falló 3 veces consecutivas.{RESET}"

    # --- BUCLE DE INTERACCIÓN (REPL) ---
    print(f"{GREEN}[+] Bóveda de credenciales validada.{RESET}")
    print(f"{GRAY}[*] Enlazando con el nodo lógico forense ({MODELO_PRINCIPAL})...{RESET}")
    print(f"{WHITE}>> Ingresa 'salir' o 'exit' para cerrar la sesión clasificada.{RESET}\n")
    
    while True:
        try:
            orden = input(f"{YELLOW}⚖️ [Director] > {RESET}").strip()
            if orden.lower() in ['salir', 'exit', 'quit']: 
                print(f"\n{GRAY}💨 Cerrando túnel de inteligencia forense. Sesión finalizada.{RESET}\n")
                break
                
            if not orden:
                continue
                
            print(f"{GRAY}🔍 Fénix procesando directivas legales y datos forenses...{RESET}", end="")
            
            respuesta_fenix = consultar_fenix_estratega(orden)
            
            print(f"\r{GREEN}✓ Análisis completado.{RESET}\n")
            print(f"{CYAN}{BOLD}🛡️ [Fénix Estratega]:{RESET}\n")
            print(f"{WHITE}{respuesta_fenix}{RESET}\n")
            print(f"{BLUE}{'-'*65}{RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{RED} Operación cancelada por el usuario.{RESET}\n")
            break

if __name__ == "__main__":
    iniciar_fenix()
