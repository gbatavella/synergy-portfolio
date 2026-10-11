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

def iniciar_planificador():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 📅 SYNERGY OPERATIONS PLANNER (COO AGENT) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # CARGA DE BÓVEDA SEGURA (OPSEC)
    # ==========================================
    load_dotenv()
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    
    if not OPENROUTER_API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta OPENROUTER_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    MODELO_PRINCIPAL = os.getenv("PLANNER_AGENT_MODEL", "anthropic/claude-3.5-sonnet")

    def consultar_planificador(reporte_director):
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        
        adn_prompt = """Eres el 'Agente Planificador', el Jefe de Operaciones (COO) implacable de Synergy.
        Tu trabajo es auditar el desempeño del Director (Gabriel) y organizar su agenda.
        
        REGLAS DEL MASTER PLAN:
        - Lunes y Martes: Ventas, Agente Prospectador, LinkedIn, Agencias de Autos.
        - Miércoles y Jueves: Ecosistema, Blog Hostinger, Zaga 'Ingeniero Autónomo'.
        - Viernes: Proyecto Fénix (Limpieza fiscal TAVSOL/MUSTAFÁ).

        MISIÓN:
        Cuando el Director te hable, evalúa qué día de la semana es (si lo menciona o puedes inferirlo), pregúntale por sus avances en los objetivos correspondientes, audita si se está desviando del foco y entrégale las 3 tareas prioritarias del día. Sé directo, corporativo y enfocado en la facturación y la eficiencia."""

        data = {
            "model": MODELO_PRINCIPAL,
            "messages": [
                {"role": "system", "content": adn_prompt},
                {"role": "user", "content": f"Reporte del Director:\n{reporte_director}"}
            ],
            "timeout": 60
        }

        for intento in range(1, 4):
            try:
                response = requests.post(url, headers=headers, data=json.dumps(data))
                if response.status_code == 200:
                    resultado = response.json()
                    if 'choices' in resultado:
                        return resultado['choices'][0]['message']['content']
                else:
                    print(f"\r {YELLOW}⚠️ Fricción en API (HTTP {response.status_code}). Reintentando...{RESET}", end="")
            except Exception as e:
                print(f"\r {YELLOW}⚠️ Latencia de red. Reintento {intento}/3...{RESET}", end="")
                time.sleep(2)
                
        return f"\n{RED}🛑 ERROR CRÍTICO DE RED. El clúster no responde.{RESET}"

    # ==========================================
    # BUCLE DE INTERACCIÓN (REPL)
    # ==========================================
    print(f"{GREEN}[+] Bóveda de credenciales validada.{RESET}")
    print(f"{GRAY}[*] Enlazando con el núcleo directivo ({MODELO_PRINCIPAL})...{RESET}")
    print(f"{WHITE}>> Ingresa 'salir' o 'exit' para apagar la mesa de control.{RESET}\n")
    
    while True:
        try:
            orden = input(f"{YELLOW}📊 [Reporte del Director] > {RESET}").strip()
            
            if orden.lower() in ['salir', 'exit', 'quit']:
                print(f"\n{GRAY}🛑 Apagando el panel de control ejecutivo. Sesión finalizada.{RESET}\n")
                break
                
            if not orden:
                continue
                
            print(f" {GRAY}⏳ Auditando cronograma, métricas y desviaciones del Master Plan...{RESET}", end="")
            
            # Llamada al LLM
            output_planificador = consultar_planificador(orden)
            
            print(f"\r {GREEN}✅ Auditoría completada. Directivas ejecutivas generadas.{RESET}\n")
            print(f"{CYAN}{BOLD}📋 [COO Synergy]:{RESET}\n")
            print(f"{WHITE}{output_planificador}{RESET}\n")
            print(f"{BLUE}{'-'*65}{RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{RED}🛑 Operación cancelada por el usuario.{RESET}\n")
            break

if __name__ == "__main__":
    iniciar_planificador()
