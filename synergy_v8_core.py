import re
import asyncio
import time
import sys

def auditar_fuga_datos(prompt_usuario):
    """
    Escudo Sentinel (DLP Middleware):
    Escanea patrones corporativos críticos antes de enviar el payload al LLM.
    """
    patron_tarjeta = r'\b(?:\d[ -]*?){13,16}\b'
    patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    if re.search(patron_tarjeta, prompt_usuario):
        return "[ALERTA CRÍTICA] Bloqueo Sentinel: Datos financieros detectados. Abortando envío a LLM."
    if re.search(patron_email, prompt_usuario):
        return "[ALERTA] Bloqueo Sentinel: Posible fuga de base de datos PII o correos."
    
    return "Limpio"

# --- CÓDIGOS ANSI: TERMINAL ARCHITECT FERRARI (USA EDITION) ---
RED = '\033[91m'
WHITE = '\033[97m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
GREEN = '\033[92m'

async def iniciar_consola():
    """Secuencia de arranque asíncrona con interfaz visual premium e interactiva."""
    print(f"\n{RED}======================================================{RESET}")
    print(f"{WHITE}{BOLD}        🇺🇸 SYNERGY LABS: ARCHITECT FERRARI TERMINAL 🇺🇸        {RESET}")
    print(f"{BLUE}======================================================{RESET}\n")

    print(f"{WHITE}Iniciando Secuencia de Ignición del Stack Avanzado...{RESET}")
    await asyncio.sleep(1) 

    # Carga simulada de submódulos asíncronos pesados
    print(f"{RED}⚡ [CARGANDO] Motor Asíncrono (asyncio + aiohttp)... OK{RESET}")
    await asyncio.sleep(0.5)

    print(f"{WHITE}🕷️  [CARGANDO] Exoesqueleto de Extracción (Playwright)... OK{RESET}")
    await asyncio.sleep(0.5)

    print(f"{BLUE}🧠 [CARGANDO] Orquestador de Agentes (CrewAI)... OK{RESET}")
    await asyncio.sleep(0.5)

    print(f"{RED}💾 [CARGANDO] Bóveda de Memoria Vectorial (ChromaDB)... OK{RESET}")
    await asyncio.sleep(1)

    print(f"\n{GREEN}{BOLD}✓ [SISTEMA EN LÍNEA] El Binomio Scientist-Auditor está listo para recibir órdenes.{RESET}\n")
    
    # --- MOTOR INTERACTIVO (Bucle REPL) ---
    while True:
        comando = input(f"{BLUE}Synergy-V8-Core:~${RESET} ").strip().lower()
        
        if comando in ['salir', 'exit', 'quit']:
            print(f"\n{RED}🔌 [APAGANDO] Desconectando enlaces neuronales... Sistema fuera de línea.{RESET}\n")
            break
        elif comando == "":
            continue
        elif comando in ['ayuda', 'help']:
             print(f"{WHITE}Comandos disponibles: {RESET}auditar, prospectar, analizar, salir")
        else:
            # --- ESCUDO SENTINEL (Invocación DLP) ---
            estado_seguridad = auditar_fuga_datos(comando)
            if estado_seguridad != "Limpio":
                print(f"\n{RED}{estado_seguridad}{RESET}\n")
                continue
            
            # Simulación de orquestación de IA si el prompt es seguro
            print(f"{WHITE}⏳ Orquestando enjambre de agentes para la directiva: '{comando}'...{RESET}")
            await asyncio.sleep(1.5)
            print(f"{GREEN}✓ Arquitectura de respuesta preparada. (Módulo de ejecución en desarrollo).{RESET}\n")

# --- PUNTO DE ENTRADA DEL MOTOR ASÍNCRONO ---
if __name__ == "__main__":
    try:
        asyncio.run(iniciar_consola())
    except KeyboardInterrupt:
        # Graceful shutdown ante cancelación manual
        print(f"\n\n{RED}🛑 Interrupción manual detectada (Ctrl+C). Apagando motores de emergencia.{RESET}\n")
        sys.exit()
