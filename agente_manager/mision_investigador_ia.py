import os
import sys
from crewai import Agent, Task, Crew, Process

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def iniciar_investigacion():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧠 SYNERGY ADVANCED RESEARCHER (CREWAI CONTENT STRATEGIST) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # Prevención de Error: Crea la carpeta 'data' si no existe
    if not os.path.exists('data'):
        os.makedirs('data')
        print(f"{GRAY}[*] Directorio 'data/' creado para almacenamiento de reportes.{RESET}")

    print(f"{GRAY}[*] Instanciando red de agentes autónomos (CrewAI)...{RESET}")

    # ==========================================
    # DEFINICIÓN DE LOS AGENTES
    # ==========================================
    agente_scout_ia = Agent(
        role='Investigador Tecnológico de Vanguardia',
        goal='Escudriñar la web para encontrar los últimos avances, modelos y herramientas de Inteligencia Artificial y LLMs.',
        backstory='Eres un analista de datos obsesionado con la innovación. Tu especialidad es leer papers, documentación de Google Cloud, OpenAI y repositorios de GitHub para identificar qué tecnologías están a punto de cambiar el mercado.',
        verbose=True,
        allow_delegation=False,
        # tools=[herramienta_de_busqueda_web] <-- Aquí conectaremos la API de búsqueda luego
        # llm=modelo_inteligencia <-- Tu llave de OpenRouter o Gemini
    )

    agente_estratega_contenido = Agent(
        role='Estratega de Producto y Contenido Tech',
        goal='Tomar la investigación técnica y transformarla en ideas de infoproductos y posts virales para LinkedIn/X.',
        backstory='Eres un visionario de negocios digitales. Sabes exactamente cómo traducir jerga técnica compleja en oportunidades de nicho rentables y contenido que atrapa a la audiencia.',
        verbose=True,
        allow_delegation=False,
        # llm=modelo_inteligencia
    )

    # ==========================================
    # ASIGNACIÓN DE TAREAS
    # ==========================================
    tarea_investigacion = Task(
        description='''Busca en la web las 3 noticias o lanzamientos más importantes sobre Modelos de Lenguaje (LLMs) y agentes autónomos de esta semana. 
        Extrae el nombre de la tecnología, quién la lanzó y para qué sirve.''',
        expected_output='Un reporte estructurado con los 3 avances más importantes, incluyendo enlaces o referencias.',
        agent=agente_scout_ia
    )

    tarea_sintesis = Task(
        description='''Toma el reporte de investigación. Selecciona la tecnología más prometedora y redacta:
        1. Una idea de infoproducto (ej. un curso, una guía, un script automatizado) basada en esa tecnología.
        2. Un borrador corto y atractivo para publicar en LinkedIn sobre ese avance.''',
        expected_output='Un documento con la idea del infoproducto y el borrador del post listo para revisión.',
        agent=agente_estratega_contenido,
        output_file='data/borrador_tendencias_ia.txt'
    )

    # ==========================================
    # ORQUESTACIÓN DEL ENJAMBRE
    # ==========================================
    equipo_investigacion = Crew(
        agents=[agente_scout_ia, agente_estratega_contenido],
        tasks=[tarea_investigacion, tarea_sintesis],
        verbose=True,
        process=Process.sequential
    )

    print(f"\n{YELLOW}⚠️ [MODO PLANTILLA] El motor está configurado en modo andamiaje.{RESET}")
    print(f"{GRAY}>> Descomenta 'tools' y 'llm' e inyecta los motores cuando las APIs estén enlazadas.{RESET}\n")

    # --- EJECUCIÓN (Comentada hasta inyectar el LLM) ---
    # print(f"{CYAN}🚀 Iniciando Protocolo Synergy: Escaneo de Tecnologías IA...{RESET}")
    # resultado = equipo_investigacion.kickoff()
    # print(f"{GREEN}✅ Búsqueda finalizada. Revisa la carpeta 'data/borrador_tendencias_ia.txt'{RESET}")

if __name__ == "__main__":
    iniciar_investigacion()
