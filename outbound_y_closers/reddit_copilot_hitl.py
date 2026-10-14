import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
MAGENTA = "\033[95m"

def iniciar_copiloto():
    print(f"\n{MAGENTA}{BOLD}{'='*65}{RESET}")
    print(f"{MAGENTA}{BOLD} 🛡️ SYNERGY COPILOT HITL (CONTROL DUAL PARA REDDIT) {RESET}")
    print(f"{MAGENTA}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÚNKER (OPSEC)
    # ==========================================
    load_dotenv()
    
    # KILL SWITCH: Purga llaves globales del SO
    if "GOOGLE_API_KEY" in os.environ:
        del os.environ["GOOGLE_API_KEY"]
        
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta GEMINI_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    print(f"{GRAY}[*] Motor cognitivo enlazado. Cargando gemini-2.5-flash...{RESET}\n")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    # ==========================================
    # 2. BUCLE OPERATIVO (HUMAN-IN-THE-LOOP)
    # ==========================================
    while True:
        dolor_entrada = input(f"{YELLOW}🗣️ PEGA EL TEXTO DEL PROSPECTO (o 'salir'): {RESET}")
        
        if dolor_entrada.lower() == 'salir':
            print(f"\n{GRAY}[*] Apagando Copiloto. Buen trabajo.{RESET}\n")
            break

        print(f"\n{GRAY}🔍 Analizando vibración y riesgo ético del mensaje...{RESET}")
        check_prompt = f"Analiza si este texto es un dolor de NEGOCIOS/VENTAS o un problema de SALUD/PERSONAL GRAVE: '{dolor_entrada}'. Responde solo la palabra: NEGOCIO o SALUD."
        
        try:
            clasificacion = model.generate_content(check_prompt).text.strip()

            if "SALUD" in clasificacion.upper():
                print(f"{RED}⚠️ ALERTA ÉTICA: Se detectó un tema sensible de salud o personal. Bloqueando ruteo comercial.{RESET}\n")
                print(f"{BLUE}{'-'*65}{RESET}\n")
                continue

            print(f"{GREEN}✅ Vía libre. Forjando vector de conversión...{RESET}")
            
            prompt_ventas = f"""
            CONTEXTO: Eres Gabriel Alejandro Tavella, autor de 'EL INGENIERO AUTÓNOMO'.
            ESTADO: Estás operando en Reddit.
            TU MISIÓN: Analizar este texto de un usuario: '{dolor_entrada}' y elegir el modo de respuesta adecuado.

            --- MODO A: INFILTRACIÓN (Si es un post general, opinión, debate o noticia) ---
            - Objetivo: Ganar Upvotes (Karma) y autoridad.
            - Acción: Valida su punto y escribe un comentario ingenioso, breve y con sabiduría práctica de ingeniería.
            - REGLA: NO vendas nada aquí. Solo sé el usuario más brillante del hilo. No pongas links.

            --- MODO B: MISIL (Si es un dolor específico de ventas, negocio, tiempo o frustración comercial) ---
            - Objetivo: Conversión directa.
            - Acción: 
              1. GANCHO: Valida su dolor con empatía.
              2. EL GIRO: Explícale que el problema es usar 'tracción humana' en un mundo impulsado por 'IA'.
              3. LA SOLUCIÓN: Preséntale 'EL CLON VENDEDOR'.
            - CTA: https://batavella.gumroad.com/l/synergyagents
            
            REGLA CRÍTICA UNIVERSAL PARA AMBOS MODOS: 
            1. NUNCA uses corchetes [] ni paréntesis (). 
            2. Si usas el CTA, escribe la URL limpia y plana: https://batavella.gumroad.com/l/synergyagents
            3. No uses formato Markdown para los enlaces.
            """
            
            respuesta = model.generate_content(prompt_ventas)
            
            print(f"\n{BLUE}{BOLD}--- 📝 BORRADOR PROPUESTO (LISTO PARA PEGAR) ---{RESET}")
            print(f"{WHITE}{respuesta.text}{RESET}")
            print(f"{BLUE}{BOLD}{'-'*50}{RESET}")

            confirmacion = input(f"\n{MAGENTA}🚀 ¿ACTIVAR EMISIÓN FINAL EN REDDIT? (s/n): {RESET}")

            if confirmacion.lower() == 's':
                print(f"{GREEN}✅ RESPUESTA VALIDADA. Copia el texto superior, pégalo en el foro y escala tu negocio.{RESET}\n")
            else:
                print(f"{RED}❌ EMISIÓN CANCELADA. Borrador descartado.{RESET}\n")
            
        except Exception as e:
            print(f"{RED}❌ Error en la conexión al clúster cognitivo: {e}{RESET}\n")
        
        print(f"{BLUE}{'='*65}{RESET}\n")

if __name__ == "__main__":
    iniciar_copiloto()
