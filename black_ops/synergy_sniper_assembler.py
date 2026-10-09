import pandas as pd
import os
import sys
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def prueba_francotirador():
    print(f"\n{RED}{BOLD}{'='*65}{RESET}")
    print(f"{RED}{BOLD} 🎯 SYNERGY SNIPER ASSEMBLER (PROMPT DRY RUN) {RESET}")
    print(f"{RED}{BOLD}{'='*65}{RESET}\n")
    
    # Abstracción segura de rutas
    load_dotenv()
    ruta_archivo = os.getenv("CSV_APOLLO_INPUT", "TARGETS_PRESIDENTS_B2B.csv")
    
    print(f"{GRAY}[*] Iniciando protocolo de calibración. Cargando mapa táctico...{RESET}")
    
    try:
        # 1. Ingesta y limpieza del mapa táctico
        df = pd.read_csv(ruta_archivo)
        columnas_clave = ['First Name', 'Last Name', 'Title', 'Company Name', 'Email']
        df_filtrado = df[columnas_clave].dropna(subset=['Email'])
        
        if df_filtrado.empty:
            print(f"{YELLOW}⚠️ La base de datos está vacía o carece de correos válidos.{RESET}")
            sys.exit(1)
        
        # 2. Aislar al Objetivo Alpha (Unit Test)
        objetivo_alpha = df_filtrado.iloc[0]
        
        nombre = objetivo_alpha.get('First Name', 'NA')
        apellido = objetivo_alpha.get('Last Name', 'NA')
        cargo = objetivo_alpha.get('Title', 'NA')
        empresa = objetivo_alpha.get('Company Name', 'NA')
        
        print(f"{CYAN}🔍 [BLANCO FIJADO]: {BOLD}{nombre} {apellido} | {cargo} en {empresa}{RESET}")
        print(f"{YELLOW}⚙️  [SISTEMA]: Ensamblando ojiva psicológica (Prompt Matrix)...{RESET}\n")
        
        # 3. La directiva maestra estructurada
        prompt_francotirador = f"""Actúa como un Closer de Ventas B2B de élite. 
Tu objetivo es redactar un correo en frío (Cold Email) brutalmente efectivo, corto y persuasivo para:

- Nombre del prospecto: {nombre} {apellido}
- Cargo: {cargo}
- Empresa: {empresa}

REGLAS DE INFILTRACIÓN (CUMPLE TODAS ESTRICTAMENTE):
1. Asunto: Corto, todo en minúsculas, que parezca un correo interno de un colega (ejemplo: "pregunta rápida sobre {empresa}").
2. Longitud máxima: 4 o 5 líneas. Un {cargo} no tiene tiempo para leer testamentos.
3. El Ángulo: Menciona que hemos desarrollado un Sistema de Agentes IA (Swarm Protocol) que automatiza la captura de clientes B2B sin fricción y sin contratar más personal.
4. Llamado a la Acción (CTA): De muy baja fricción. No pidas una reunión de 30 minutos. Pregunta algo como: "¿Estarías abierto a que te envíe un video de 2 minutos mostrando cómo funciona nuestra bóveda de prospectos?"
5. Tono: Directo, corporativo pero conversacional. Cero relleno.
"""
        
        print(f"{BLUE}{BOLD}{'='*65}{RESET}")
        print(f"{WHITE}{BOLD} CÓDIGO FUENTE DEL PROMPT (Input Inyectado al LLM):{RESET}")
        print(f"{BLUE}{BOLD}{'='*65}{RESET}")
        print(f"{WHITE}{prompt_francotirador}{RESET}")
        print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
        
        print(f"{GREEN}{BOLD}✅ Armado completo. Test de Inyección de Variables Exitoso.{RESET}")
        print(f"{GRAY}>> El motor de inferencia (Groq/OpenAI) está listo para procesar esta estructura.{RESET}\n")
        
    except FileNotFoundError:
        print(f"{RED}❌ [ERROR] Archivo origen no encontrado: {ruta_archivo}{RESET}")
    except Exception as e:
        print(f"{RED}❌ [ERROR CRÍTICO] Falla en la mira telescópica: {e}{RESET}")

if __name__ == "__main__":
    prueba_francotirador()
