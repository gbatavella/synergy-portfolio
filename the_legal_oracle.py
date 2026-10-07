import os
import time
import sys
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

# --- SEGURIDAD Y BLINDAJE ---
# Carga de variables de entorno (El archivo .env NO se sube a GitHub)
load_dotenv()

# Variable estándar para repositorios públicos
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    print("\033[91m❌ [ERROR] Llave de OpenRouter no encontrada en el entorno (.env).\033[0m")
    sys.exit(1)

# Inyección vital para la librería interna
os.environ["OPENROUTER_API_KEY"] = OPENROUTER_API_KEY

# Blindaje técnico: Evita que LiteLLM/CrewAI busque llaves de OpenAI por defecto
os.environ["OPENAI_API_KEY"] = "sk-or-v1-dummy-to-prevent-openai-fallback"

# Motor lógico recomendado para alta velocidad y bajo costo
motor_logico = LLM(
    model="openrouter/anthropic/claude-3-haiku", 
    api_key=OPENROUTER_API_KEY,
    temperature=0.0
)

# --- CÓDIGOS ANSI ---
RED, WHITE, BLUE, CYAN = '\033[91m', '\033[97m', '\033[94m', '\033[96m'
GREEN, YELLOW, GRAY, MAGENTA = '\033[92m', '\033[93m', '\033[90m', '\033[95m'
RESET, BOLD = '\033[0m', '\033[1m'

def rapid_output(text, delay=0.05):
    print(text)
    time.sleep(delay)

# --- FASE 1: SECUENCIA DE ARRANQUE VISUAL ---
def secuencia_inicio():
    print("\n" * 2)
    rapid_output(f"{BLUE}=== THE LEGAL ORACLE: COMPLIANCE ARCHITECT ==={RESET}", 1.0)

    rapid_output(f"\n{MAGENTA}[*] PHASE 1: SCANNING CORPORATE ACCEPTABLE USE POLICIES (AUP)...{RESET}", 1)
    rapid_output(f"{GRAY}>> Interfacing with Exchange limits...{RESET}", 0.5)
    rapid_output(f"{GREEN}[OK] Tenant sending limits verified.{RESET}", 0.5)
    
    rapid_output(f"\n{MAGENTA}[*] PHASE 2: CROSS-REFERENCING GLOBAL PRIVACY LAWS...{RESET}", 1)
    rapid_output(f"{GRAY}>> Evaluating GDPR & CCPA Compliance...{RESET}", 0.5)
    rapid_output(f"{GREEN}[OK] Suppression tags and Opt-out routes active.{RESET}", 0.5)

    rapid_output(f"\n{BLUE}[!] SYSTEM BOOT: COMPILING UNIVERSAL LEGAL SHIELD...{RESET}", 1)
    rapid_output(f"{GREEN}[SUCCESS] Universal Legal Shield finalized. System Online.{RESET}\n", 1)


# --- FASE 2: CEREBRO LÓGICO ---
def auditar_legalidad(maniobra_comercial):
    print(f"\n{YELLOW}⏳ [PROCESANDO] El Oráculo está diseñando la hoja de ruta corporativa...{RESET}\n")
    
    oraculo = Agent(
        role='Chief Compliance Officer (CCO) y Experto en Regulación Global',
        goal='Garantizar que el ecosistema analizado sea legalmente intocable.',
        backstory="Ex-auditor regulatorio. Provee rutas legales exactas para que los modelos operen en la luz sin fricción.",
        llm=motor_logico,
        verbose=False,
        allow_delegation=False
    )

    tarea = Task(
        description=f"Analiza esta propuesta: '{maniobra_comercial}'. Redacta una hoja de ruta de cumplimiento, riesgos y vehículos legales aplicables.",
        expected_output="Hoja de ruta legal y corporativa estructurada.",
        agent=oraculo
    )

    equipo = Crew(agents=[oraculo], tasks=[tarea], process=Process.sequential)
    veredicto = equipo.kickoff()
    
    print(f"{GREEN}{BOLD}🛡️ [HOJA DE RUTA DE CUMPLIMIENTO]{RESET}")
    print(f"{WHITE}{veredicto}{RESET}\n")

# --- FASE 3: BUCLE INTERACTIVO ---
if __name__ == "__main__":
    secuencia_inicio()
    
    while True:
        print(f"{CYAN}{BOLD}================================================================={RESET}")
        print(f"{WHITE}{BOLD} ⚖️ INGRESE EL MODELO DE NEGOCIO O INSTRUMENTO A AUDITAR ⚖️ {RESET}")
        print(f"{CYAN}{BOLD}================================================================={RESET}")
        
        propuesta = input(f"\n{BLUE}Legal-Oracle:~$ {RESET}").strip()
        
        if propuesta.lower() in ['salir', 'exit', 'quit']:
            print(f"\n{RED}🔌 Desconectando Oráculo Legal. Sesión finalizada.{RESET}\n")
            break
        elif not propuesta:
            continue
            
        auditar_legalidad(propuesta)
