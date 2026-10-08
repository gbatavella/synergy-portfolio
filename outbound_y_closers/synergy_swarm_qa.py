import pandas as pd
import os
import time
import sys
from openai import OpenAI
from dotenv import load_dotenv

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

# ==========================================
# DATOS: CONFIGURACIÓN E INFRAESTRUCTURA
# ==========================================
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1"

if not API_KEY:
    print(f"{RED}❌ ERROR: GROQ_API_KEY no encontrada en el entorno .env.{RESET}")
    sys.exit()

cliente = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# Protocolo de cambio de modelos (Actualizado y Calibrado)
MODELO_REDACTOR = "llama-3.3-70b-versatile" 
MODELO_AUDITOR = "llama-3.1-8b-instant" 

# ==========================================
# ESQUEMA: DEFINICIÓN DE LOS AGENTES
# ==========================================

def agente_redactor(nombre, apellido, cargo, empresa, feedback_previo=""):
    """Agente encargado de redactar el correo inicial."""
    contexto = ""
    if feedback_previo:
        contexto = f"\nATENCIÓN, TU INTENTO ANTERIOR FALLÓ POR ESTO: {feedback_previo}. Corrige tu error ahora."

    prompt = f"""
    Actúa como un Closer B2B de élite. Escribe un cold email para {nombre} {apellido}, {cargo} en {empresa}.
    PROPUESTA: Swarm Protocol (Agentes IA para ventas).
    REGLAS:
    1. Asunto corto TODO en minúsculas.
    2. Máximo 4-5 líneas de cuerpo.
    3. CTA: ¿Abierto a un video de 2 min sobre nuestra bóveda de prospectos?
    {contexto}
    """
    
    respuesta = cliente.chat.completions.create(
        model=MODELO_REDACTOR,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )
    return respuesta.choices[0].message.content

def agente_auditor(correo_generado):
    """Agente encargado de verificar que el correo cumpla las reglas estrictas."""
    prompt_auditoria = f"""
    Eres un Auditor de Control de Calidad B2B. Revisa el siguiente correo:
    
    ---CORREO---
    {correo_generado}
    ---FIN CORREO---
    
    Verifica estrictamente:
    1. ¿El Asunto está completamente en minúsculas?
    2. ¿El cuerpo del correo es corto (5 líneas o menos)?
    3. ¿Incluye la pregunta sobre el video de 2 minutos?
    
    Si cumple TODO, responde ÚNICAMENTE con la palabra: APROBADO.
    Si falla en algo, responde con la palabra RECHAZADO y explica brevemente por qué.
    """
    
    respuesta = cliente.chat.completions.create(
        model=MODELO_AUDITOR,
        messages=[{"role": "user", "content": prompt_auditoria}],
        temperature=0.1 # Muy baja temperatura para decisiones lógicas
    )
    return respuesta.choices[0].message.content

# ==========================================
# CÓDIGO: EL BUCLE PRINCIPAL (MAIN LOOP)
# ==========================================

def ejecutar_swarm():
    print(f"\n{BLUE}{BOLD}=============================================================={RESET}")
    print(f"{BLUE}{BOLD}  🛡️  SYNERGY SWARM PROTOCOL: ACTOR-CRITIC (Llama 3 Core)  {RESET}")
    print(f"{BLUE}{BOLD}=============================================================={RESET}\n")
    
    ruta_archivo = os.getenv("APOLLO_CSV_PATH", 'apollo-contacts-exportUSA.csv')
    
    try:
        # Intenta leer el archivo real, si no existe, crea un Mock DataFrame para que el código no falle en repositorios públicos
        try:
            df = pd.read_csv(ruta_archivo)
            df_filtrado = df[['First Name', 'Last Name', 'Title', 'Company Name', 'Email']].dropna(subset=['Email'])
            objetivo = df_filtrado.iloc[0]
            rapid_output(f"{GRAY}[*] Base de datos B2B cargada exitosamente.{RESET}")
        except FileNotFoundError:
            rapid_output(f"{YELLOW}[!] Archivo CSV no encontrado. Generando target en memoria (Mock Mode)...{RESET}")
            data = {'First Name': ['Alexander'], 'Last Name': ['Vance'], 'Title': ['CEO'], 'Company Name': ['Vanguard Tech'], 'Email': ['alex@vanguard.com']}
            df = pd.DataFrame(data)
            objetivo = df.iloc[0]

        rapid_output(f"{GREEN}[+] Blanco fijado: {objetivo['First Name']} {objetivo['Last Name']} ({objetivo['Title']} en {objetivo['Company Name']}){RESET}")
        
        intentos_maximos = 3
        intento = 1
        feedback = ""
        correo_final = ""
        
        while intento <= intentos_maximos:
            rapid_output(f"\n{GRAY}⚙️ [Intento {intento}/3] Agente Redactor ({MODELO_REDACTOR}) escribiendo...{RESET}")
            borrador = agente_redactor(objetivo['First Name'], objetivo['Last Name'], objetivo['Title'], objetivo['Company Name'], feedback)
            
            rapid_output(f"{YELLOW}🔍 Agente Auditor ({MODELO_AUDITOR}) verificando calidad estricta...{RESET}")
            auditoria = agente_auditor(borrador)
            
            if "APROBADO" in auditoria.upper():
                rapid_output(f"{GREEN}{BOLD}✅ ¡AUDITORÍA SUPERADA! Output validado.{RESET}")
                correo_final = borrador
                break
            else:
                rapid_output(f"{RED}⚠️ RECHAZADO por el Auditor: {auditoria}{RESET}")
                rapid_output(f"{MAGENTA}>> Inyectando feedback al Redactor para auto-corrección...{RESET}")
                feedback = auditoria
                intento += 1
                time.sleep(1)
                
        if correo_final:
            print(f"\n{BLUE}======================================================================{RESET}")
            print(f"{WHITE}{BOLD}📨 PRODUCTO FINAL APROBADO Y LISTO PARA PIPELINE:{RESET}")
            print(f"{BLUE}======================================================================{RESET}")
            print(f"{WHITE}{correo_final}{RESET}")
            print(f"{BLUE}======================================================================{RESET}\n")
        else:
            print(f"\n{RED}❌ El Agente Redactor no logró superar la auditoría tras 3 intentos. Protocolo abortado para proteger reputación de dominio.{RESET}\n")
            
    except Exception as e:
        print(f"{RED}❌ Error crítico en la infraestructura: {e}{RESET}")

if __name__ == "__main__":
    ejecutar_swarm()
