import os
import time
import sys
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

# --- INICIALIZACIÓN DE SEGURIDAD ---
load_dotenv()

# --- CÓDIGOS ANSI: TERMINAL ARCHITECT FERRARI ---
RED = '\033[91m'
WHITE = '\033[97m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def iniciar_auditor():
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    if not OPENROUTER_API_KEY:
        print(f"{RED}❌ [ALERTA CRÍTICA] No se encontró la llave en el archivo .env.{RESET}")
        sys.exit(1)

    # 🔥 MOTOR LÓGICO NATIVO: CLAUDE 3.5 SONNET (EL JUEZ SUPREMO)
    # Temperatura baja (0.1) para forzar lógica estricta y anular creatividad divagante
    motor_logico = LLM(
        model="openrouter/anthropic/claude-3-5-sonnet-20240620",
        api_key=OPENROUTER_API_KEY,
        temperature=0.1
    )

    def auditar_hipotesis(hipotesis_del_scientist):
        """El Auditor evalúa la información bajo la Filosofía Synergy"""
        print(f"\n{RED}{BOLD}{'='*65}{RESET}")
        print(f"{WHITE}{BOLD}   🇺🇸 SYNERGY LABS: AGENTE AUDITOR (CEREBRO SONNET) 🇺🇸        {RESET}")
        print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
        
        print(f"{CYAN}⚖️ [AUDITOR] Inicializando corteza prefrontal lógica...{RESET}")
        print(f"{WHITE}📥 [INPUT RECIBIDO DE LA RED]: '{hipotesis_del_scientist}'{RESET}\n")
        
        auditor_jefe = Agent(
            role='Auditor Supremo del Sistema Synergy y Estratega DeFi',
            goal='Destruir la narrativa financiera tradicional basada en deuda y validar modelos de costo marginal cero y liquidez total.',
            backstory="""Eres la máxima autoridad analítica del ecosistema Synergy. Desprecias el sistema 
            financiero fiduciario y la reserva fraccionaria. 
            Operas bajo la 'Premisa Synergy': El activo más infinito es la Información. Un sistema descentralizado basado 
            en información tiene costo marginal cero, lo que permite un crecimiento taquiónico 
            y liquidez instantánea sin secuestrar el capital. Tu misión es aplastar las falacias centralizadas.""",
            llm=motor_logico, 
            verbose=False, # Silenciado para el output final limpio
            allow_delegation=False
        )

        tarea_auditoria = Task(
            description=f"""Analiza la siguiente afirmación del sistema tradicional: '{hipotesis_del_scientist}'.
            Refuta esta falacia. Explica por qué al migrar a un ecosistema donde el producto principal es la Información 
            (costo marginal cero), el flujo de capital es instantáneo y las ganancias no se limitan por retención artificial de liquidez. 
            Redacta un veredicto de 3 a 4 párrafos implacables y profesionales.""",
            expected_output="Veredicto estructurado destruyendo la lógica tradicional.",
            agent=auditor_jefe
        )

        equipo_auditor = Crew(
            agents=[auditor_jefe],
            tasks=[tarea_auditoria],
            process=Process.sequential
        )

        print(f"{YELLOW}⏳ [PROCESANDO] El Auditor está deliberando. Aplicando Doctrina Synergy...{RESET}\n")
        
        try:
            veredicto_final = equipo_auditor.kickoff()
            
            print(f"{GREEN}{BOLD}📜 [VEREDICTO DEFINITIVO EMITIDO]{RESET}")
            print(f"{WHITE}{veredicto_final}{RESET}\n")
        except Exception as e:
            print(f"{RED}❌ Fricción en el procesamiento lógico: {e}{RESET}")

    # Bucle interactivo para la terminal
    print(f"\n{CYAN}{BOLD}📡 --- TERMINAL DE AUDITORÍA SUPREMA --- 📡{RESET}")
    while True:
        hipotesis_usuario = input(f"{WHITE}⚖️ Ingresa la hipótesis tradicional a refutar (o 'salir'): {RESET}").strip()
        if hipotesis_usuario.lower() in ['salir', 'exit', 'quit']:
            print(f"{GRAY}[*] Apagando núcleo lógico. Sesión finalizada.{RESET}")
            break
        if hipotesis_usuario:
            auditar_hipotesis(hipotesis_usuario)

if __name__ == "__main__":
    iniciar_auditor()
