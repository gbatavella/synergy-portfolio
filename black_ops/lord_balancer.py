import os
import time
import sys
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def rapid_output(text, delay=0.03):
    print(text)
    time.sleep(delay)

def iniciar_lord_balancer():
    print(f"\n{RED}{BOLD}{'='*65}{RESET}")
    print(f"{RED}{BOLD} ⚖️  SYNERGY LORD BALANCER (COGNITIVE ROUTING CORE) {RESET}")
    print(f"{RED}{BOLD}{'='*65}{RESET}\n")

    # 1. CARGA AUTOMÁTICA DE CREDENCIALES
    load_dotenv() 
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    if not OPENROUTER_API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta OPENROUTER_API_KEY en el entorno (.env).{RESET}")
        sys.exit(1)

    rapid_output(f"{GRAY}[*] Iniciando enrutador cognitivo. Puenteando a OpenRouter...{RESET}")

    # 2. EL CEREBRO NATIVO DE CREWAI
    # Usamos la clase LLM oficial de CrewAI para evitar el error de Pydantic
    claude_nativo = LLM(
        model="openrouter/anthropic/claude-3-5-sonnet-20240620",
        api_key=OPENROUTER_API_KEY
    )

    rapid_output(f"{GREEN}[+] Cerebro Claude 3.5 Sonnet enlazado con éxito.{RESET}\n")

    target_niche = input(f"{YELLOW}🎯 Ingresa el nicho y ubicación (ej. Clínicas Dentales en Austin, TX): {RESET}").strip()
    if not target_niche:
        target_niche = "Dental Clinics in Austin, Texas"

    # 3. DEFINICIÓN DEL AGENTE
    manager = Agent(
        role='Synergy Sales Manager Elite',
        goal='Convert raw leads into RaaS subscribers using advanced psychological profiling.',
        backstory="""You are a High-Ticket sales strategist. You understand that business owners 
        are tired of tools that break when Google or LinkedIn update. Your unique value is 
        the 'Swarm Evolution Protocol'—a system of agents that never stops working.""",
        verbose=False, # Silenciado para mantener la consola táctica limpia
        allow_delegation=False,
        llm=claude_nativo 
    )

    # 4. DEFINICIÓN DE LA MISIÓN
    task1 = Task(
        description=f"""Draft a hyper-personalized, 3-sentence cold email outreach template 
        targeting {target_niche}. 
        Sentence 1: Authority hook. 
        Sentence 2: Expose the fragility of traditional tools against web updates. 
        Sentence 3: Introduce our RaaS Swarm Evolution Protocol as the ultimate solution. 
        Keep it punchy, professional, and High-Ticket.""",
        agent=manager,
        expected_output="A single, highly persuasive cold email template."
    )

    # 5. ORQUESTACIÓN DEL ENJAMBRE
    synergy_crew = Crew(
        agents=[manager],
        tasks=[task1],
        process=Process.sequential,
        verbose=False
    )

    print(f"\n{BLUE}🚀 [MANAGER] Protocolo Synergy Iniciado.{RESET}")
    print(f"{BLUE}🧠 [MANAGER] Despertando a Claude 3.5 Sonnet (Cerebro Nativo)...{RESET}\n")

    try:
        result = synergy_crew.kickoff()

        print(f"{GREEN}{BOLD}{'='*65}{RESET}")
        print(f"{GREEN}{BOLD} 🎯 REPORTE ESTRATÉGICO FINAL (COPYWRITING B2B): {RESET}")
        print(f"{GREEN}{BOLD}{'='*65}{RESET}")
        print(f"{WHITE}{result}{RESET}")
        print(f"{GREEN}{BOLD}{'='*65}{RESET}\n")
    except Exception as e:
        print(f"{RED}❌ Fricción cognitiva detectada: {e}{RESET}")

if __name__ == "__main__":
    iniciar_lord_balancer()
