import os
import sys
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def iniciar_operacion_sw4():
    # ==========================================
    # 1. ZONA DE AUTORIZACIÓN (Bóveda Segura)
    # ==========================================
    load_dotenv()
    
    # Definimos el motor de inteligencia
    modelo_inteligencia = os.getenv("SW4_LIQUIDATOR_LLM", "openrouter/anthropic/claude-3-haiku")
    
    # Protección de infraestructura I/O
    if not os.path.exists('data'):
        os.makedirs('data')

    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🚙 SYNERGY ASSET LIQUIDATOR (SW4 AUTO-BROKER SWARM) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    print(f"{GRAY}[*] Enlazando clúster cognitivo para infiltración B2C...{RESET}\n")

    # ==========================================
    # 2. CREACIÓN DE AGENTES
    # ==========================================
    agente_enjambre = Agent(
        role='Especialista en Extracción de Prospectos Automotrices',
        goal='Identificar compradores con liquidez para vehículos 4x4 de alta gama.',
        backstory='Eres un rastreador digital implacable. Infiltras foros, grupos de Facebook de agro y redes de negocios en Argentina buscando personas que necesiten o deseen vehículos de alta gama.',
        verbose=True,
        allow_delegation=False,
        llm=modelo_inteligencia
    )

    agente_profiler = Agent(
        role='Ingeniero de Conversión y Copywriting',
        goal='Analizar leads y redactar correos en frío altamente persuasivos y personalizados.',
        backstory='Eres un experto en psicología de ventas. Sabes cómo contactar a inversores y empresarios sin sonar como un vendedor de concesionaria, utilizando un tono directo, corporativo y de oportunidad.',
        verbose=True,
        allow_delegation=False,
        llm=modelo_inteligencia
    )

    # ==========================================
    # 3. ASIGNACIÓN DE TAREAS (La Directiva del CEO)
    # ==========================================
    tarea_extraccion = Task(
        description='''Rastrear la web abierta, foros automotores y redes profesionales (LinkedIn, Facebook Groups de alta gama) 
        buscando prospectos con interés explícito o capacidad de compra para una Toyota Hilux SW4 de segunda mano. 
        El epicentro de la geolocalización debe ser Cañuelas, Buenos Aires, expandiéndose a un radio provincial. 
        Extraer exactamente 10 leads con contacto directo (Email, Teléfono, o URL de perfil). 
        Misión prioritaria: Si no hay email visible, extraer el Username para enviar Mensaje Directo. 
        Entregar los resultados en un formato de lista estructurada.''',
        expected_output='Una lista de 10 prospectos calificados en la zona de Cañuelas/Buenos Aires con su vía de contacto y razón por la cual son buenos candidatos.',
        agent=agente_enjambre
    )

    tarea_redaccion = Task(
        description='''Tomar la lista de 10 prospectos generada por el Enjambre. Analizar su perfil y seleccionar los 5 leads con mayor probabilidad de compra (mayor liquidez aparente).
        Para estos 5 leads, redactar un correo o mensaje de contacto inicial. 
        El mensaje debe:
        1. Mencionar sutilmente que estás en la zona (Cañuelas/Buenos Aires).
        2. Aclarar que la Hilux SW4 está en estado impecable, destacando que eres contacto directo del segundo dueño, eliminando intermediarios y agencias.
        3. Invitar a una charla rápida o a ver el vehículo, sin presionar la venta directa.
        Guardar estos 5 textos listos para enviar.''',
        expected_output='5 borradores de mensajes/correos hiper-personalizados para los 5 mejores prospectos, listos para ser copiados y enviados.',
        agent=agente_profiler,
        output_file='data/borradores_sw4.txt'
    )

    # ==========================================
    # 4. ORQUESTACIÓN DEL ENJAMBRE
    # ==========================================
    equipo_synergy = Crew(
        agents=[agente_enjambre, agente_profiler],
        tasks=[tarea_extraccion, tarea_redaccion],
        verbose=True,
        process=Process.sequential
    )

    print(f"{CYAN}🚀 Iniciando Protocolo Synergy: Operación SW4 (Mapeo Geo-Especial: Cañuelas)...{RESET}")
    
    try:
        resultado = equipo_synergy.kickoff()
        print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
        print(f"{GREEN}{BOLD} ✅ Operación Finalizada. Bóveda de borradores generada en 'data/borradores_sw4.txt'.{RESET}")
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")
    except Exception as e:
        print(f"\n{RED}❌ Fricción crítica en la matriz de agentes: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_operacion_sw4()
