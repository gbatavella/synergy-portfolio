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

cliente = OpenAI(api_key=API_KEY, base_url=BASE_URL)

MODELO_REDACTOR = "llama-3.3-70b-versatile" 
MODELO_AUDITOR = "llama-3.1-8b-instant" 

# ==========================================
# ESQUEMA: DEFINICIÓN DE LOS AGENTES
# ==========================================

def agente_redactor(nombre, apellido, cargo, empresa, feedback_previo=""):
    contexto = f"\n⚠️ EL AUDITOR RECHAZÓ TU INTENTO ANTERIOR POR ESTO: {feedback_previo}. ¡Corrige esto inmediatamente!" if feedback_previo else ""
    
    prompt = f"""
    Actúa como un Closer B2B de élite. Escribe un cold email para {nombre} {apellido}, {cargo} en {empresa}.
    PROPUESTA: Swarm Protocol (Agentes IA para ventas).
    
    REGLAS ESTRICTAS:
    1. ASUNTO: Escribe SOLO la frase en minúsculas. PROHIBIDO usar la palabra "Asunto:" o "Subject:".
    2. LONGITUD: Máximo 4 líneas de cuerpo. Ve al grano.
    3. CTA: Cierra preguntando si está abierto a ver un video de 2 min sobre nuestra bóveda de prospectos.
    {contexto}
    """
    try:
        respuesta = cliente.chat.completions.create(
            model=MODELO_REDACTOR,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"ERROR_REDACTOR: {e}"

def agente_auditor(correo_generado):
    prompt_auditoria = f"""
    Eres un Auditor de Control de Calidad B2B. Revisa este correo:
    ---
    {correo_generado}
    ---
    Verifica rápidamente:
    1. ¿Tiene 5 líneas o menos en total?
    2. ¿Ofrece el video de 2 minutos?
    
    No seas pedante con las mayúsculas al inicio de las oraciones. Evalúa la estructura.
    Si es un buen Cold Email, responde ÚNICAMENTE: APROBADO.
    Si es un desastre o es muy largo, responde RECHAZADO y explica en 1 sola línea por qué.
    """
    try:
        respuesta = cliente.chat.completions.create(
            model=MODELO_AUDITOR,
            messages=[{"role": "user", "content": prompt_auditoria}],
            temperature=0.1 
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return "RECHAZADO por fallo en la red."

# ==========================================
# CÓDIGO: EL BUCLE DE COBERTURA TOTAL
# ==========================================

def ejecutar_fuego_cobertura():
    print(f"\n{RED}{BOLD}{'='*65}{RESET}")
    print(f"{RED}{BOLD} 🔥 SYNERGY COVER FIRE (CALIBRATED EDITION) 🔥{RESET}")
    print(f"{RED}{BOLD}{'='*65}{RESET}\n")
    
    ruta_archivo = os.getenv("CSV_APOLLO_INPUT", "TARGETS_PRESIDENTS_B2B.csv")
    archivo_salida = os.getenv("CSV_ARSENAL_OUTPUT", "municion_lista_envio.csv")
    
    print(f"{GRAY}[*] Ingestando bases e iniciando calibración de enjambre...{RESET}")
    
    try:
        df = pd.read_csv(ruta_archivo)
        df_filtrado = df[['First Name', 'Last Name', 'Title', 'Company Name', 'Email']].dropna(subset=['Email'])
        total_objetivos = len(df_filtrado)
        resultados_arsenal = []
        df_filtrado = df_filtrado.reset_index(drop=True)
        
        print(f"{GREEN}[+] {total_objetivos} blancos fijados. Desplegando agentes Llama...{RESET}\n")
        
        for index, objetivo in df_filtrado.iterrows():
            nombre, apellido = objetivo['First Name'], objetivo['Last Name']
            cargo, empresa = objetivo['Title'], objetivo['Company Name']
            email = objetivo['Email']
            
            print(f"{CYAN}🎯 [Blanco {index + 1}/{total_objetivos}]: {BOLD}{nombre} {apellido} | {empresa}{RESET}")
            
            intentos_maximos = 3
            intento = 1
            feedback = ""
            correo_final = "FALLO EN GENERACIÓN (Requiere intervención manual)"
            
            while intento <= intentos_maximos:
                sys.stdout.write(f"   {GRAY}↳ Iteración {intento}: Generando...{RESET}")
                sys.stdout.flush()
                
                borrador = agente_redactor(nombre, apellido, cargo, empresa, feedback)
                auditoria = agente_auditor(borrador)
                
                if "APROBADO" in auditoria.upper():
                    if intento == 1:
                        print(f"\r   {GREEN}✅ One Shot, One Kill (Aprobado al primer intento).{RESET}")
                    else:
                        print(f"\r   {GREEN}✅ Auditoría superada en el intento {intento}.{RESET}")
                    correo_final = borrador
                    break
                else:
                    motivo_limpio = auditoria.replace('RECHAZADO', '').strip()
                    print(f"\r   {YELLOW}⚠️ Intento {intento} rechazado. Motivo: {motivo_limpio}{RESET}")
                    feedback = auditoria
                    intento += 1
            
            resultados_arsenal.append({
                "Nombre": f"{nombre} {apellido}", 
                "Cargo": cargo, 
                "Empresa": empresa, 
                "Email": email, 
                "Correo_Generado": correo_final
            })
            
            time.sleep(1.5)
            
        df_salida = pd.DataFrame(resultados_arsenal)
        df_salida.to_csv(archivo_salida, index=False, encoding='utf-8')
        
        print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
        print(f"{GREEN}{BOLD} 🎯 MISIÓN CUMPLIDA. Arsenal guardado en '{archivo_salida}'.{RESET}")
        print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
            
    except FileNotFoundError:
        print(f"{RED}❌ [ERROR] Archivo origen no encontrado: {ruta_archivo}{RESET}")
    except Exception as e:
        print(f"{RED}❌ [ERROR CRÍTICO] Falla sistémica: {e}{RESET}")

if __name__ == "__main__":
    ejecutar_fuego_cobertura()
