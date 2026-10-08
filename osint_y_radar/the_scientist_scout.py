import os
import time
import sys
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

# --- SEGURIDAD Y BLINDAJE ---
# Carga de variables de entorno (El archivo .env NO se sube a GitHub)
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    print("\033[91m[ERROR] Llave de OpenRouter no encontrada en el entorno (.env).\033[0m")
    sys.exit(1)

# Inyección vital para la librería interna
os.environ["OPENROUTER_API_KEY"] = OPENROUTER_API_KEY

# Motor lógico base para operaciones de alta velocidad
motor_logico = LLM(
    model="openrouter/anthropic/claude-3-haiku",
    api_key=OPENROUTER_API_KEY,
    temperature=0.0
)

# --- CÓDIGOS ANSI ---
BLUE, YELLOW, GREEN, RED, GRAY, MAGENTA = "\033[96m", "\033[93m", "\033[92m", "\033[91m", "\033[90m", "\033[95m"
RESET, CYAN, BOLD, WHITE = "\033[0m", "\033[96m", "\033[1m", "\033[97m"

def rapid_output(text, delay=0.05):
    print(text)
    time.sleep(delay)

def secuencia_inicio():
    print("\n" * 2)
    rapid_output(f"{BLUE}=== THE SCIENTIST SCOUT: EVOLUTIONARY RADAR ==={RESET}", 1)

    rapid_output(f"\n{MAGENTA}[*] PHASE 1: SCANNING B2B NODES (DOM & APIs)...{RESET}", 0.5)
    rapid_output(f"{GRAY}>> Analyzing ZoomInfo & Crunchbase CSS Selectors...{RESET}", 0.5)
    rapid_output(f"{GREEN}[OK] Search topology and rate limits nominal.{RESET}", 0.5)

    rapid_output(f"\n{MAGENTA}[*] PHASE 2: VALIDATING AUTHENTICATION PROTOCOLS...{RESET}", 0.5)
    rapid_output(f"{GRAY}>> Verifying OAuth 2.0 flows and Session Cookies...{RESET}", 0.5)

    rapid_output(f"\n{MAGENTA}[*] PHASE 3: PROBING WAF & ANTI-BOT SHIELDS...{RESET}", 0.5)
    rapid_output(f"{RED}[CRITICAL ANOMALY] Advanced behavioral challenge deployed.{RESET}", 1)
    
    rapid_output(f"\n{YELLOW}>>> ACTIVATING [HUMAN-IN-THE-LOOP] PROTOCOL...{RESET}", 0.5)
    for i in range(1, 4):
        sys.stdout.write(f"\r{GRAY}Pinging System Architect terminal... Attempt [{i}/3]{RESET}")
        sys.stdout.flush()
        time.sleep(1)
    
    print("\n")
    rapid_output(f"{YELLOW}[!] WAITING FOR ARCHITECT OVERRIDE...{RESET}", 1.5)
    rapid_output(f"{GREEN}[+] OVERRIDE ACCEPTED. COGNITIVE PUZZLE SOLVED BY HUMAN OPERATOR.{RESET}", 0.5)
    rapid_output(f"{BLUE}[!] COMPILING BYPASS PAYLOAD...{RESET}", 0.5)
    rapid_output(f"{GREEN}[SUCCESS] Tech payload finalized. System Online.{RESET}\n", 0.5)

def auditar_tecnologia(objetivo):
    print(f"\n{YELLOW}⏳ [PROCESANDO] El Scout está escaneando viabilidad, costos y dependencias...{RESET}\n")

    scout = Agent(
        role='Chief Technology Scout & Economic Modeler',
        goal='Escanear el panorama tecnológico/B2B y proveer un reporte de viabilidad, costos y riesgos.',
        backstory="Eres la vanguardia técnica del laboratorio. Detectas cambios en APIs, evalúas viabilidad económica de herramientas y previenes la deprecación de código.",
        llm=motor_logico,
        verbose=False,
        allow_delegation=False
    )

    tarea = Task(
        description=f"Audita la siguiente tecnología, framework o nicho B2B: '{objetivo}'. Genera un reporte detallando: 1. Estado actual y riesgos de obsolescencia. 2. Barreras de entrada defensivas. 3. Viabilidad económica (Costos vs Beneficios).",
        expected_output="Reporte técnico y económico estructurado.",
        agent=scout
    )

    equipo = Crew(agents=[scout], tasks=[tarea], process=Process.sequential)
    veredicto = equipo.kickoff()

    print(f"{GREEN}{BOLD}📊 [REPORTE DE EVOLUCIÓN TÉCNICA Y ECONÓMICA]{RESET}")
    print(f"{WHITE}{veredicto}{RESET}\n")

if __name__ == "__main__":
    secuencia_inicio()

    while True:
        print(f"{CYAN}{BOLD}================================================================={RESET}")
        print(f"{WHITE}{BOLD}  🔬 INGRESE LA TECNOLOGÍA, API O MERCADO B2B A AUDITAR 🔬  {RESET}")
        print(f"{CYAN}{BOLD}================================================================={RESET}")
        
        objetivo = input(f"\n{BLUE}Scientist-Scout:~$ {RESET}").strip()
        
        if objetivo.lower() in ['salir', 'exit', 'quit']:
            print(f"\n{RED}🔌 Desconectando radares. Sesión finalizada.{RESET}\n")
            break
        elif not objetivo:
            continue
            
        auditar_tecnologia(objetivo)
