import os
import csv
import json
import time
import sys
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

# ==========================================
# CONFIGURACIÓN DEL BÚNKER (.env)
# ==========================================
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1"

if not API_KEY:
    print(f"{RED}❌ [ERROR CRÍTICO] GROQ_API_KEY no encontrada en la bóveda .env.{RESET}")
    sys.exit(1)

# Utilizamos el SDK de OpenAI pero enrutado a los clústeres ultrarrápidos de Groq
cliente = OpenAI(api_key=API_KEY, base_url=BASE_URL)
MODELO_REDACTOR = "llama-3.3-70b-versatile"
MODELO_AUDITOR = "llama-3.1-8b-instant"

# ==========================================
# AGENTES DEL ENJAMBRE (ACTOR-CRITIC)
# ==========================================

def agente_redactor(nombre, apellido, cargo, empresa, feedback_previo=""):
    contexto = f"\n⚠️ THE AUDITOR SAID: {feedback_previo}. FIX IT." if feedback_previo else ""
    prompt = f"""
    Write a B2B cold email for {nombre} at {empresa}.
    
    USE EXACTLY THIS TEMPLATE:
    subject: [write a 2-4 word lowercase subject]

    Hi {nombre},
    We deployed a Swarm Protocol (autonomous AI agents) that handles 24/7 outbound prospecting for companies like {empresa}.
    Mind if I send a 2-min video showing how we fill your pipeline?
    {contexto}
    """
    try:
        respuesta = cliente.chat.completions.create(
            model=MODELO_REDACTOR,
            messages=[
                {"role": "system", "content": "You are a raw output machine. Output ONLY the email text. NO preambles."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1 # Muy baja temperatura para evitar desviaciones del template
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"ERROR_REDACTOR: {e}"

def agente_auditor(correo_generado):
    prompt_auditoria = f"""
    Analyze this text:
    ---
    {correo_generado}
    ---
    RULE: The email MUST be 4 sentences or less (including the subject line).
    """
    try:
        respuesta = cliente.chat.completions.create(
            model=MODELO_AUDITOR,
            messages=[
                {"role": "system", "content": "You are a strict binary auditor. Output ONLY 'APPROVED' or 'REJECTED'."},
                {"role": "user", "content": prompt_auditoria}
            ],
            temperature=0.0 # Temperatura cero para un juicio determinista absoluto
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"REJECTED_BY_SYSTEM_ERROR"

# ==========================================
# EJECUCIÓN TÁCTICA 
# ==========================================

def ejecutar_fuego_cobertura():
    print(f"\n{RED}{BOLD}{'='*65}{RESET}")
    print(f"{RED}{BOLD} 🔥 SYNERGY COVER FIRE V3 (LLM ACTOR-CRITIC PIPELINE) {RESET}")
    print(f"{RED}{BOLD}{'='*65}{RESET}\n")

    # Archivos dinámicos para protección en GitHub
    archivo_entrada = os.getenv("CSV_CONTACTS_TARGET", "TARGETS_B2B_VIP.csv")
    archivo_salida = os.getenv("JSON_MUNICION_OUTPUT", "municion_aprobada_usa.json")
    
    firma_ejecutiva = "\n\nGabriel Tavella\nFounder & CEO | Synergy (Human & AI Agents)"
    municion_lista = []
    
    print(f"{GRAY}[*] Conectando a clústeres Groq (Llama-3.3-70B / Llama-3.1-8B)...{RESET}\n")
    
    try:
        with open(archivo_entrada, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            filas = list(reader)
            
            for i, row in enumerate(filas, 1):
                # Soporte para múltiples formatos de cabeceras B2B
                nombre = row.get('First Name', row.get('Nombre', ''))
                apellido = row.get('Last Name', row.get('Apellido', ''))
                cargo = row.get('Title', row.get('Cargo', ''))
                empresa = row.get('Company Name', row.get('Empresa', ''))
                
                if not nombre or not empresa:
                    continue
                    
                print(f"{CYAN}🎯 [Blanco {i}/{len(filas)}]: {BOLD}{nombre} | {empresa}{RESET}")
                
                intentos = 0
                aprobado = False
                correo_final = ""
                
                while intentos < 3 and not aprobado:
                    intentos += 1
                    sys.stdout.write(f"   {GRAY}↳ Iteración {intentos}: Generando y Auditando...{RESET}")
                    sys.stdout.flush()
                    
                    correo_generado = agente_redactor(nombre, apellido, cargo, empresa)
                    auditoria = agente_auditor(correo_generado)
                    
                    if "APPROVED" in auditoria.upper():
                        print(f"\r   {GREEN}✅ APPROVED - Firma inyectada. Listo para disparo.{RESET}")
                        aprobado = True
                        # INYECCIÓN PROGRAMÁTICA DE LA FIRMA (Evita gasto de tokens)
                        correo_final = correo_generado + firma_ejecutiva
                    else:
                        print(f"\r   {YELLOW}⚠️ REJECTED - Ajustando verbosidad (Intento {intentos}/3)...{RESET}")
                        time.sleep(1) # Límite de ráfaga para la API
                
                if aprobado:
                    municion_lista.append({
                        "nombre": nombre,
                        "apellido": apellido,
                        "empresa": empresa,
                        "cargo": cargo,
                        "mensaje_b2b": correo_final
                    })
                else:
                    print(f"   {RED}❌ ABORTADO - El prospecto no superó la auditoría.{RESET}")
                    
                time.sleep(0.5)

        with open(archivo_salida, 'w', encoding='utf-8') as f:
            json.dump(municion_lista, f, indent=4, ensure_ascii=False)
            
        print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
        print(f"{GREEN}{BOLD} 🎯 MISIÓN CUMPLIDA. {len(municion_lista)} payloads asegurados.{RESET}")
        print(f"{BLUE} 📂 Bóveda de munición: {archivo_salida}{RESET}\n")

    except FileNotFoundError:
        print(f"{RED}❌ [ERROR] No se encontró el arsenal de origen '{archivo_entrada}'.{RESET}")
        print(f"{YELLOW}>> Verifique que Apollo Extractor haya generado el archivo CSV.{RESET}\n")

if __name__ == "__main__":
    ejecutar_fuego_cobertura()
