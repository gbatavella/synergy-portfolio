import csv
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

def iniciar_fragua_stealth():
    # ==========================================
    # 1. INICIALIZACIÓN DE LA FRAGUA
    # ==========================================
    load_dotenv()
    
    # Abstracción de OPSEC (Permite cambiar el modelo desde el .env si es necesario)
    modelo_directo = os.getenv("PROFILER_LLM_MODEL", "openrouter/anthropic/claude-3-haiku")
    
    # Validación de API Key de Serper
    if not os.getenv("SERPER_API_KEY"):
        print(f"{RED}❌ [ERROR CRÍTICO] Falta SERPER_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)
        
    herramienta_busqueda = SerperDevTool()

    # Auto-aprovisionamiento del directorio de salida
    directorio_salida = 'borradores_ataque'
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🕵️ SYNERGY STEALTH PROFILER (CREWAI COLD EMAIL FORGE) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 2. LECTURA DEL BOTÍN (CSV)
    # ==========================================
    archivo_csv = os.getenv("CSV_ELITE_TARGETS", "data/botin_elite_espectro_total.csv")
    
    if not os.path.exists(archivo_csv):
        print(f"{RED}❌ Error: El botín ({archivo_csv}) no existe.{RESET}")
        print(f"{GRAY}>> Ejecuta el Enjambre OSINT primero para nutrir el pipeline.{RESET}\n")
        sys.exit(1)

    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                empresa = row.get('Empresa', 'la empresa')
                url = row.get('URL', '')
                
                if not url:
                    continue
                    
                print(f"\n{CYAN}[+] Forjando lingote de persuasión para: {BOLD}{empresa}{RESET} ({url})...")

                # ==========================================
                # 3. LOS OPERADORES DE CONTACTO
                # ==========================================
                profiler = Agent(
                    role='Consultor Senior de Inteligencia B2B',
                    goal=f'Investigar a {empresa} usando su URL ({url}) y descubrir sus proyectos actuales.',
                    backstory="""Eres un estratega corporativo de élite. Buscas noticias recientes 
                    o el modelo de negocio del prospecto para encontrar un gancho conversacional.""",
                    verbose=False,
                    allow_delegation=False,
                    llm=modelo_directo,
                    tools=[herramienta_busqueda]
                )

                copywriter = Agent(
                    role='Copywriter B2B de Alta Etiqueta',
                    goal=f'Escribir un cold email corto, hiper-personalizado y elegante para {empresa}.',
                    backstory="""Eres un maestro de la persuasión sutil. NUNCA suenas como un robot. 
                    Usas la información del Profiler para hacer un cumplido profesional y luego ofreces 
                    nuestra tecnología de automatización asincrónica.""",
                    verbose=False,
                    allow_delegation=False,
                    llm=modelo_directo
                )

                # ==========================================
                # 4. TAREAS DEL BUCLE (CON FIRMA DE CEO)
                # ==========================================
                tarea_investigacion = Task(
                    description=f'Busca información clave sobre {empresa}. Extrae un dato interesante.',
                    expected_output='Un párrafo con un dato clave de la empresa.',
                    agent=profiler
                )

                tarea_redaccion = Task(
                    description=f'''Usando el dato investigado, escribe un cold email en INGLÉS.
                    Estructura:
                    1. Asunto corto y que genere curiosidad.
                    2. Apertura personalizada.
                    3. Conexión rápida con Agentes IA Asincrónicos para escalar operaciones.
                    4. Call to Action suave ("Open to a quick 5-min chat this week?").
                    
                    REGLA DE FIRMA: Firma el correo EXACTAMENTE así:
                    "Best regards,
                    Gabriel Tavella
                    CEO of Synergy Humans & AI Agents"
                    
                    No añadas notas adicionales al final del correo.''',
                    expected_output='Un borrador de correo B2B perfecto.',
                    agent=copywriter
                )

                # ==========================================
                # 5. EJECUCIÓN Y GUARDADO
                # ==========================================
                escuadron_tactico = Crew(
                    agents=[profiler, copywriter],
                    tasks=[tarea_investigacion, tarea_redaccion],
                    verbose=False,
                    process=Process.sequential
                )
                
                # Ejecución del enjambre
                borrador = escuadron_tactico.kickoff()
                
                # Sanitización del nombre del archivo y guardado seguro
                nombre_seguro = empresa.replace(' ', '_').replace('/', '').replace('\\', '')
                nombre_archivo = f"{directorio_salida}/email_{nombre_seguro}.txt"
                
                with open(nombre_archivo, 'w', encoding='utf-8') as f:
                    f.write(borrador.raw)
                    
                print(f" {GREEN}✅ Lingote asegurado:{RESET} {nombre_archivo}")

    except Exception as e:
        print(f"\n{RED}❌ Anomalía estructural durante la forja: {e}{RESET}")

    print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
    print(f"{GREEN}{BOLD} 🏁 FRAGUA DETENIDA. Revisa la bóveda '{directorio_salida}'.{RESET}")
    print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")

if __name__ == "__main__":
    iniciar_fragua_stealth()
