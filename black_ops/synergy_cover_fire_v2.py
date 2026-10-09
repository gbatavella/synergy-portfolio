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

# ==========================================
# DATOS: CONFIGURACIÓN E INFRAESTRUCTURA
# ==========================================
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1"

if not API_KEY:
    print(f"{RED}❌ [ERROR CRÍTICO] GROQ_API_KEY no encontrada en la bóveda .env.{RESET}")
    sys.exit(1)

# Túnel de alta velocidad Groq
cliente = OpenAI(api_key=API_KEY, base_url=BASE_URL)

MODELO_REDACTOR = "llama-3.3-70b-versatile" 
MODELO_AUDITOR = "llama-3.1-8b-instant" 

# ==========================================
# ESQUEMA: DEFINICIÓN DE LOS AGENTES
# ==========================================

def agente_redactor(nombre, apellido, cargo, empresa, feedback_previo=""):
    # Bucle de auto-reflexión inyectado en el contexto
    contexto = f"\n⚠️ ERROR ANTERIOR A CORREGIR: {feedback_previo}" if feedback_previo else ""
    
    prompt = f"""
    Eres un Closer B2B nivel experto. Redacta un correo para {nombre} {apellido}, {cargo} en {empresa}.
    
    ESTRUCTURA OBLIGATORIA:
    1. Una frase de asunto en minúsculas (ej: pregunta para {empresa}).
    2. Un saludo hiper-corto (ej: Hola {nombre},).
    3. Una sola idea: Swarm Protocol (Agentes IA que prospectan por ti).
    4. CTA: "¿Te envío un video de 2 min sobre nuestra bóveda de prospectos?".
    
    REGLAS DE ORO:
    - No uses la palabra 'Asunto:'. Solo escribe el texto.
    - Prohibido pasar de 60 palabras. 
    - Sé directo, sin rellenos.
    {contexto}
    """
    try:
        respuesta = cliente.chat.completions.create(
            model=MODELO_REDACTOR,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"ERROR_REDACTOR: {e}"

def agente_auditor(correo_generado):
    prompt_auditoria = f"""
    Eres un Director Comercial evaluando el trabajo de un vendedor.
    Revisa este correo:
    ---
    {correo_generado}
    ---
    CRITERIOS DE APROBACIÓN:
    1. ¿Es corto y se lee en menos de 10 segundos?
    2. ¿El tono es profesional y no parece spam barato?
    3. ¿Tiene la pregunta del video de 2 minutos?

    Si es aceptable para un VP o Presidente, responde ÚNICAMENTE: APROBADO.
    Si es basura o muy largo, responde RECHAZADO y dime el motivo breve.
    """
    try:
        respuesta = cliente.chat.completions.create(
            model=MODELO_AUDITOR,
            messages=[{"role": "user", "content": prompt_auditoria}],
            temperature=0.1 
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return "RECHAZADO por fallo de red."

# ==========================================
# CÓDIGO: EL BUCLE DE COBERTURA TOTAL
# ==========================================

def ejecutar_fuego_cobertura():
    print(f"\n{RED}{BOLD}{'='*65}{RESET}")
    print(f"{RED}{BOLD} 🔥 SYNERGY COVER FIRE V2 (PANDAS & SELF-REFLECTION) {RESET}")
    print(f"{RED}{BOLD}{'='*65}{RESET}\n")
    
    ruta_archivo = os.getenv("CSV_APOLLO_INPUT", "TARGETS_PRESIDENTS_B2B.csv")
    archivo_salida = os.getenv("CSV_ARSENAL_OUTPUT", "municion_lista_envio.csv")
    
    print(f"{GRAY}[*] Ingestando matriz de datos vía Pandas DataFrame...{RESET}")
    
    try:
        df = pd.read_csv(ruta_archivo)
        # Limpieza estructural de datos (Data Wrangling)
        df_filtrado = df[['First Name', 'Last Name', 'Title', 'Company Name', 'Email']].dropna(subset=['Email'])
        total_objetivos = len(df_filtrado)
        resultados_arsenal = []
        df_filtrado = df_filtrado.reset_index(drop=True)
        
        print(f"{GREEN}[+] Base sanitizada. {total_objetivos} objetivos listos para procesamiento.{RESET}\n")
        
        for index, objetivo in df_filtrado.iterrows():
            nombre, apellido = objetivo['First Name'], objetivo['Last Name']
            cargo, empresa = objetivo['Title'], objetivo['Company Name']
            email = objetivo['Email']
            
            print(f"{CYAN}🎯 [Blanco {index + 1}/{total_objetivos}]: {BOLD}{nombre} {apellido} | {empresa}{RESET}")
            
            intentos_maximos = 3
            intento = 1
            feedback = ""
            correo_final = "REQUERIDA INTERVENCIÓN MANUAL"
            
            while intento <= intentos_maximos:
                borrador = agente_redactor(nombre, apellido, cargo, empresa, feedback)
                auditoria = agente_auditor(borrador)
                
                if "APROBADO" in auditoria.upper():
                    print(f"    {GREEN}✅ APROBADO (Intento {intento}){RESET}")
                    correo_final = borrador
                    break
                else:
                    motivo = auditoria.replace('RECHAZADO', '').strip()
                    print(f"    {YELLOW}⚠️ Rechazo en capa {intento}. Motivo del Director: {motivo}{RESET}")
                    feedback = auditoria # Carga el error en la memoria del redactor
                    intento += 1
            
            resultados_arsenal.append({
                "Nombre": f"{nombre} {apellido}", 
                "Cargo": cargo, 
                "Empresa": empresa, 
                "Email": email, 
                "Correo_Generado": correo_final
            })
            
            time.sleep(1) # Límite de ráfaga para Groq LPU
            
        # Exportación masiva desde DataFrame a CSV
        df_salida = pd.DataFrame(resultados_arsenal)
        df_salida.to_csv(archivo_salida, index=False, encoding='utf-8')
        
        print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
        print(f"{GREEN}{BOLD} 🎯 MISIÓN CUMPLIDA. {len(resultados_arsenal)} proyectiles almacenados.{RESET}")
        print(f"{BLUE} 📂 DataFrame exportado a: {archivo_salida}{RESET}")
        print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
            
    except Exception as e:
        print(f"\n{RED}❌ Error crítico en el pipeline de Pandas: {e}{RESET}")

if __name__ == "__main__":
    ejecutar_fuego_cobertura()
