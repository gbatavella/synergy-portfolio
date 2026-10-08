import os
import time
import sys
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

# --- SEGURIDAD Y CONFIGURACIÓN ---
load_dotenv()

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def rapid_output(text, delay=0.03):
    print(text)
    time.sleep(delay)

def iniciar_agente_manager():
    print(f"\n{BLUE}{BOLD}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD} 🧠 SYNERGY MANAGER AGENT (PAIN-POINT SCOUT) {RESET}")
    print(f"{BLUE}{BOLD}{'='*60}{RESET}\n")

    # 1. SEGURIDAD: Carga y puenteo de llaves desde la bóveda (.env)
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")

    if not GEMINI_API_KEY or not SERPER_API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Faltan llaves de Gemini o Serper en el archivo .env.{RESET}")
        sys.exit(1)

    # Forzamos la lectura para las librerías internas de CrewAI/LiteLLM
    os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
    os.environ["SERPER_API_KEY"] = SERPER_API_KEY

    rapid_output(f"{GRAY}[*] Conexión establecida con Gemini 2.5 Flash y Serper Search...{RESET}")

    # --- VARIABLES DE BÚSQUEDA DINÁMICA ---
    print(f"\n{YELLOW}>> Configuración del Target Comercial{RESET}")
    nicho = input(f"{GREEN}🎯 Ingresa el nicho (ej. Clínicas de Estética): {RESET}").strip()
    ubicacion = input(f"{GREEN}📍 Ingresa la ubicación (ej. Lomas de Zamora): {RESET}").strip()

    if not nicho or not ubicacion:
        nicho, ubicacion = "Estudios Jurídicos", "Córdoba"
        print(f"{YELLOW}[!] Datos incompletos. Ejecutando objetivo de demostración: {nicho} en {ubicacion}{RESET}")

    # Nombre automático para el archivo de salida
    nombre_archivo = f'reporte_{nicho.replace(" ", "_").lower()}_{ubicacion.replace(" ", "_").lower()}.md'
    
    herramienta_busqueda = SerperDevTool()

    # 2. Crear el Agente Manager
    agente_manager = Agent(
        role='Agente Manager de Inteligencia Comercial',
        goal=f'Escudriñar la web para descubrir los dolores digitales y extraer datos de contacto completos de {nicho} en {ubicacion}.',
        backstory='Eres un investigador de mercado de élite. Tu misión es analizar la presencia online de negocios locales, identificar qué les falta (su dolor) y recopilar todos los medios de contacto posibles (WhatsApp, Email, Redes Sociales) para que el equipo de ventas les ofrezca un infoproducto (App/Web) a medida.',
        verbose=True,
        allow_delegation=False,
        tools=[herramienta_busqueda],
        llm="gemini/gemini-2.5-flash"
    )

    # 3. Asignar la Tarea con EXPORTACIÓN AUTOMÁTICA
    tarea_investigacion = Task(
        description=f'''
        Busca en internet a 3 {nicho} en {ubicacion}.
        Para cada negocio, debes investigar profundamente y extraer:
        1. Nombre del negocio.
        2. Teléfono o WhatsApp.
        3. Correo electrónico público.
        4. Enlace a sus redes sociales (Instagram/Facebook) para contactar por DM.
        5. DIAGNÓSTICO DEL DOLOR: Analiza su presencia digital y describe cuál es su mayor debilidad comercial (ej: no tienen sistema de reservas online, web desactualizada, no tienen catálogo digital, etc.).
        ''',
        expected_output=f'Un reporte estructurado en formato Markdown de 3 {nicho} en {ubicacion} con todos sus canales de contacto y un diagnóstico comercial de su dolor principal.',
        agent=agente_manager,
        output_file=nombre_archivo  # Guarda el resultado directamente
    )

    # 4. Ejecutar la Misión
    equipo = Crew(
        agents=[agente_manager],
        tasks=[tarea_investigacion]
    )

    print(f"\n{BLUE}🚀 Iniciando Protocolo Synergy: Desplegando Enjambre sobre {nicho} en {ubicacion}...{RESET}\n")
    
    try:
        resultado = equipo.kickoff()

        print(f"\n{GREEN}{BOLD}{'='*60}{RESET}")
        print(f"{GREEN}{BOLD} ✅ EXTRACCIÓN Y DIAGNÓSTICO COMPLETADOS {RESET}")
        print(f"{GREEN}{BOLD}{'='*60}{RESET}")
        print(f"{BLUE}>> El manifiesto táctico ha sido generado exitosamente en: {nombre_archivo}{RESET}")
        print(f"{GRAY}>> Listo para derivar el infoproducto al equipo de Closers.{RESET}\n")
        
    except Exception as e:
        print(f"\n{RED}❌ Fricción detectada durante el escrutinio: {e}{RESET}")

if __name__ == "__main__":
    iniciar_agente_manager()
