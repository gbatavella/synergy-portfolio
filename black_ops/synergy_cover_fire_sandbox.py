import os
import sys
import time
from dotenv import load_dotenv
from openai import OpenAI

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

# ==========================================
# 1. SETUP DE INFRAESTRUCTURA MLOps
# ==========================================
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    print(f"{RED}❌ [ERROR CRÍTICO] Fuga de credenciales. GROQ_API_KEY no detectada.{RESET}")
    sys.exit(1)

# Túnel de inferencia de baja latencia
cliente = OpenAI(api_key=API_KEY, base_url="https://api.groq.com/openai/v1")
MODELO_REDACTOR = "llama-3.3-70b-versatile"
MODELO_AUDITOR = "llama-3.1-8b-instant"

# ==========================================
# 2. AGENTES (Aislamiento de Prompts)
# ==========================================
def agente_redactor(nombre, empresa):
    prompt = f"""
    Write a B2B cold email for {nombre} at {empresa}.
    USE EXACTLY THIS TEMPLATE:
    subject: [write a 2-4 word lowercase subject]

    Hi {nombre},
    We deployed a Swarm Protocol (autonomous AI agents) that handles 24/7 outbound prospecting for companies like {empresa}.
    Mind if I send a 2-min video showing how we fill your pipeline?
    """
    try:
        respuesta = cliente.chat.completions.create(
            model=MODELO_REDACTOR,
            messages=[
                {"role": "system", "content": "You are a raw output machine. Output ONLY the email text. NO preambles. NO 'Here is the email'."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"ERROR_API_REDACTOR: {e}"

def agente_auditor(correo_generado):
    prompt_auditoria = f"""
    Analyze this text:
    ---
    {correo_generado}
    ---
    RULE: The email MUST be 4 sentences or less.
    Respond ONLY with APPROVED or REJECTED: [Reason].
    """
    try:
        respuesta = cliente.chat.completions.create(
            model=MODELO_AUDITOR,
            messages=[{"role": "user", "content": prompt_auditoria}],
            temperature=0.0
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"ERROR_API_AUDITOR: {e}"

# ==========================================
# 3. SANDBOX (Modo Depuración)
# ==========================================
def ejecutar_sandbox():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🔬 SYNERGY COVER FIRE SANDBOX (MLOps DEBUGGER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    # Inyección de Mock Data para pruebas de latencia cero
    leads_prueba = [
        {"nombre": "Taylor", "empresa": "American Fintech Council"},
        {"nombre": "Jasmine", "empresa": "Risk Management Advisors"}
    ]
    
    print(f"{GRAY}[*] Iniciando entorno de pruebas aislado. Ejecutando {len(leads_prueba)} perfiles de diagnóstico...{RESET}\n")
    
    for lead in leads_prueba:
        print(f"{CYAN}▶️ PROCESANDO NODO DE PRUEBA: {BOLD}{lead['nombre']} | {lead['empresa']}{RESET}")
        time.sleep(0.5)
        
        # 1. Generar
        correo = agente_redactor(lead['nombre'], lead['empresa'])
        
        # 2. MOSTRAR LA CAJA NEGRA (Black Box Inspector)
        print(f"{GRAY}{'='*65}{RESET}")
        print(f"{WHITE}{BOLD}📝 PAYLOAD CRUDO EXACTO DEL REDACTOR (Llama-70b):{RESET}")
        print(f"{GRAY}{'='*65}{RESET}")
        print(f"{WHITE}{correo}{RESET}")
        print(f"{GRAY}{'='*65}{RESET}\n")
        
        # 3. Auditar
        auditoria = agente_auditor(correo)
        if "APPROVED" in auditoria.upper():
            print(f"   {GREEN}⚖️ VEREDICTO DEL AUDITOR (Llama-8b): {auditoria}{RESET}\n")
        else:
            print(f"   {RED}⚖️ VEREDICTO DEL AUDITOR (Llama-8b): {auditoria}{RESET}\n")
            
        print(f"{BLUE}{'-' * 65}{RESET}\n")

if __name__ == "__main__":
    ejecutar_sandbox()
