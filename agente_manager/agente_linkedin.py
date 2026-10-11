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

def iniciar_fabrica_contenido():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 📢 SYNERGY LINKEDIN GENERATOR (B2B CONTENT FACTORY) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # CARGA DE BÓVEDA SEGURA (OPSEC)
    # ==========================================
    load_dotenv()
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    
    if not OPENROUTER_API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta OPENROUTER_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    MODELO_PRINCIPAL = os.getenv("LINKEDIN_AGENT_MODEL", "anthropic/claude-3.5-sonnet")

    def consultar_linkedin(idea_cruda):
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        
        adn_prompt = """Eres el 'Agente Generador B2B' de Synergy. Eres un experto en Copywriting para LinkedIn.
        El Director te dará una idea cruda, un pensamiento o un audio transcrito.
        
        TU MISIÓN:
        Debes devolverle 3 opciones de posteo para LinkedIn basadas en esa idea:
        - Opción 1: Estilo 'Historia de Negocios' (Storytelling).
        - Opción 2: Estilo 'Directo y al hueso' (Problema -> Solución con IA).
        - Opción 3: Estilo 'Polémico/Contraintuitivo' (Para generar debate).
        
        REGLAS:
        - Usa frases cortas y espaciadas.
        - Incluye un 'Gancho' (Hook) fuerte en la primera línea.
        - Cierra siempre con una pregunta para fomentar comentarios.
        - Usa un tono corporativo moderno, de autoridad, sin vender humo."""

        data = {
            "model": MODELO_PRINCIPAL,
            "messages": [
                {"role": "system", "content": adn_prompt},
                {"role": "user", "content": f"Transforma esta idea cruda en posteos B2B:\n\n{idea_cruda}"}
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
    print(f"{GRAY}[*] Enlazando con el núcleo semántico ({MODELO_PRINCIPAL})...{RESET}")
    print(f"{WHITE}>> Ingresa 'salir' o 'exit' para apagar la terminal de contenido.{RESET}\n")
    
    while True:
        try:
            orden = input(f"{YELLOW}💡 [Idea Cruda del Director] > {RESET}").strip()
            
            if orden.lower() in ['salir', 'exit', 'quit']:
                print(f"\n{GRAY}🛑 Apagando motores de redacción. Sesión finalizada.{RESET}\n")
                break
                
            if not orden:
                continue
                
            print(f" {GRAY}⏳ Procesando idea y aplicando gatillos mentales...{RESET}", end="")
            
            # Llamada al LLM
            output_linkedin = consultar_linkedin(orden)
            
            print(f"\r {GREEN}✅ Matriz de Copywriting generada con éxito.{RESET}\n")
            print(f"{CYAN}{BOLD}🚀 [Agente LinkedIn]:{RESET}\n")
            print(f"{WHITE}{output_linkedin}{RESET}\n")
            print(f"{BLUE}{'-'*65}{RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{RED}🛑 Operación cancelada por el usuario.{RESET}\n")
            break

if __name__ == "__main__":
    iniciar_fabrica_contenido()
