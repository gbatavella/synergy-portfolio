import os
import sys
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def iniciar_enjambre_global():
    # ==========================================
    # 1. PREPARACIÓN Y CREDENCIALES
    # ==========================================
    load_dotenv()
    modelo_directo = os.getenv("GLOBAL_PROSPECTOR_LLM", "openrouter/anthropic/claude-3-haiku")
    
    if not os.getenv("SERPER_API_KEY"):
        print(f"{RED}❌ [ERROR CRÍTICO] Falta SERPER_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)
        
    herramienta_busqueda = SerperDevTool()

    # Protección de infraestructura I/O
    if not os.path.exists('data'):
        os.makedirs('data')

    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🎯 SYNERGY GLOBAL PROSPECTOR (SAAS & HIGH-TICKET SWARM) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    print(f"{GRAY}[*] Enlazando sensores OSINT y forzando matriz CSV...{RESET}\n")

    # ==========================================
    # 2. OPERADORES OSINT (DISCIPLINA ESTRICTA)
    # ==========================================
    francotirador = Agent(
        role='Francotirador de Élite OSINT',
        goal='Extraer URLs de Súper Afiliados y dueños de SaaS High-Ticket.',
        backstory="""Operador de inteligencia Tier 1. Eres una máquina analítica. 
        NO conversas. NO te disculpas. Entregas listas de objetivos precisas.""",
        verbose=True,
        allow_delegation=False,
        llm=modelo_directo,
        tools=[herramienta_busqueda]
    )

    cazador = Agent(
        role='Extractor de Doxing Comercial y DM Hunter',
        goal='Extraer Emails, LinkedIn y redes sociales y formatear estrictamente como CSV.',
        backstory="""Eres un autómata generador de CSV. Tienes PROHIBIDO usar lenguaje natural. 
        PROHIBIDO decir "Entiendo su petición". Si falta un dato, dejas el espacio en blanco. 
        Tu única salida permitida es el formato separado por comas.""",
        verbose=True,
        allow_delegation=False,
        llm=modelo_directo,
        tools=[herramienta_busqueda]
    )

    # ==========================================
    # 3. ÓRDENES DE OPERACIONES (SAAS & HIGH TICKET)
    # ==========================================
    tarea_prospeccion = Task(
        description='''Ejecuta búsquedas profundas usando la herramienta para nichos de altísima rentabilidad:
        1. site:kiwify.com.br "produtor" OR "top afiliado" 
        2. site:maxbounty.com "super affiliate"
        3. site:skool.com "marketing" OR "business"
        4. site:gohighlevel.com "agency owner"
        5. site:systeme.io "top affiliate"
        
        Extrae EXACTAMENTE 15 objetivos de altísimo valor. 
        Devuelve la lista limpia de 15 empresas y URLs al Cazador.''',
        expected_output='Lista estricta de 15 Súper Afiliados/SaaS con sus URLs.',
        agent=francotirador
    )

    tarea_extraccion = Task(
        description='''Toma la lista de 15 URLs. Busca para cada una:
        1. Email corporativo.
        2. LinkedIn.
        3. DM_Directo (WhatsApp, Telegram, o Twitter/X).
        
        REGLA DE MUERTE: Tu respuesta final debe ser ÚNICAMENTE el texto en formato CSV. 
        Si incluyes una sola palabra conversacional antes o después del CSV, la misión fracasa.
        Columnas exactas: Mercado,Empresa,URL,Email,LinkedIn,DM_Directo''',
        expected_output='CSV puro con columnas: Mercado,Empresa,URL,Email,LinkedIn,DM_Directo',
        agent=cazador,
        output_file='data/botin_elite_espectro_total.csv'
    )

    # ==========================================
    # 4. GATILLO DE EJECUCIÓN
    # ==========================================
    enjambre_global = Crew(
        agents=[francotirador, cazador],
        tasks=[tarea_prospeccion, tarea_extraccion],
        verbose=True,
        process=Process.sequential
    )

    print(f"{CYAN}🚀 Iniciando infiltración en redes de afiliación y plataformas SaaS...{RESET}")
    
    try:
        enjambre_global.kickoff()
        print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
        print(f"{GREEN}{BOLD} 🏁 ¡EXTRACCIÓN COMPLETADA! Botín asegurado en 'data/botin_elite_espectro_total.csv'.{RESET}")
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")
    except Exception as e:
        print(f"\n{RED}❌ Fricción crítica durante el despliegue del enjambre: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_enjambre_global()
