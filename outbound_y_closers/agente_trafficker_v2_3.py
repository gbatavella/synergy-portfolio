import os
import json
import time
import random
import smtplib
import re
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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

load_dotenv()

# Configuración de credenciales desde la bóveda segura (.env)
REMITENTE = os.getenv("SMTP_USER", "ceo@agentpruebaai.online")
PASSWORD = os.getenv("SMTP_PASSWORD", "Gat197069#$")
CORREO_PRUEBA = os.getenv("ADMIN_EMAIL", "gbatavella@gmail.com")

def extraer_email_rayos_x(lead_dict):
    """Escanea todo el registro del prospecto (JSON volcado a texto) y extrae el primer email válido."""
    lead_str = json.dumps(lead_dict)
    # Patrón universal optimizado para detección de correos electrónicos
    match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', lead_str)
    if match:
        return match.group(0)
    return None

def enviar_correo(remitente, password, destinatario, asunto, cuerpo):
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

    try:
        servidor = smtplib.SMTP('mail.privateemail.com', 587, timeout=15)
        servidor.starttls()
        servidor.login(remitente, password)
        servidor.send_message(msg)
        servidor.quit()
        return True, "✅ Aceptado por el servidor SMTP."
    except Exception as e:
        return False, f"❌ Falla de entrega en red: {e}"

def agente_trafficker():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🚀 SYNERGY TRAFFICKER V2.3 (JSON X-RAY & DRIP ENGINE) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    archivo_municion = os.getenv("JSON_MUNITION_SOURCE", "municion_aprobada_usa.json")
    firma = "\n\nGabriel Tavella\nFounder & CEO | Synergy (Human & AI Agents)"
    
    if not os.path.exists(archivo_municion):
        print(f"{RED}❌ [ERROR CRÍTICO] No se encontró el archivo de munición: {archivo_municion}{RESET}")
        print(f"{GRAY}>> Verifique que el archivo JSON esté alojado en la ruta de ejecución.{RESET}\n")
        return

    try:
        print(f"{GRAY}[*] Ingestando cargador JSON ({archivo_municion})...{RESET}")
        with open(archivo_municion, 'r', encoding='utf-8') as f:
            municiones = json.load(f)

        print(f"{GREEN}[+] Cargador conectado.{RESET} {BOLD}{len(municiones)}{RESET} {GRAY}leads listos para procesar.{RESET}\n")
        
        if len(municiones) == 0:
            print(f"{YELLOW}⚠️ El archivo de munición está vacío.{RESET}\n")
            return

        # =========================================================
        # FASE 1: CALIBRACIÓN Y PRUEBA HUMANA (HITL)
        # =========================================================
        print(f"{CYAN}=== FASE 1: CALIBRACIÓN DE COPY & ENTREGABILIDAD ==={RESET}")
        
        lead_prueba = municiones[0]
        texto_crudo_prueba = lead_prueba.get('mensaje_b2b', 'Subject: Test\nHi there, testing system.')
        lineas_prueba = texto_crudo_prueba.split('\n')
        
        asunto_prueba = "[PRUEBA] " + lineas_prueba[0].replace("subject:", "").replace("Subject:", "").strip()
        cuerpo_prueba = '\n'.join(lineas_prueba[1:]).strip() + firma

        print(f"{GRAY}>> Enviando correo de prueba hacia: {BOLD}{CORREO_PRUEBA}{RESET}")
        exito_prueba, msj_prueba = enviar_correo(REMITENTE, PASSWORD, CORREO_PRUEBA, asunto_prueba, cuerpo_prueba)
        print(f"   {msj_prueba}")

        if not exito_prueba:
            print(f"{RED}🛑 [FALLA EN PRUEBA] El servidor rechazó las credenciales. Revise la bóveda .{RESET}\n")
            return

        confirmacion = input(f"\n{YELLOW}⚠️ Revisa tu Gmail ({CORREO_PRUEBA}). ¿Llegó bien y con formato de firma? (s/n): {RESET}")
        if confirmacion.lower() != 's':
            print(f"{RED}🛑 Operación cancelada por el operador.{RESET}\n")
            return

        # =========================================================
        # FASE 2: FUEGO REAL AUTORIZADO (LOTE DE PROSPECCIÓN)
        # =========================================================
        print(f"\n{GREEN}{BOLD}=== FASE 2: FUEGO REAL AUTORIZADO (LOTE DE OBJETIVOS) ==={RESET}\n")
        
        for i, lead in enumerate(municiones[:10], 1):
            nombre = lead.get('nombre', 'Contacto')
            empresa = lead.get('empresa', 'Empresa')
            
            # Extracción universal por Rayos X (Regex)
            destinatario_real = extraer_email_rayos_x(lead)
            
            if not destinatario_real:
                print(f"[{i}/10] {YELLOW}⚠️ SALTANDO: No se detectó ninguna dirección de correo válida para {nombre}.{RESET}")
                continue

            texto_crudo = lead.get('mensaje_b2b', '')
            lineas = texto_crudo.split('\n')
            asunto = lineas[0].replace("subject:", "").replace("Subject:", "").strip() if lineas else "Business Opportunity"
            
            cuerpo = '\n'.join(lineas[1:]).strip() + firma

            print(f"[{i}/10] 🎯 Disparando hacia objetivo: {BOLD}{destinatario_real}{RESET} ({empresa})...")
            
            intentos = 0
            exito = False
            while intentos < 3 and not exito:
                exito, msj_resultado = enviar_correo(REMITENTE, PASSWORD, destinatario_real, asunto, cuerpo)
                print(f"      {msj_resultado}")
                if not exito:
                    intentos += 1
                    print(f"      {YELLOW}⚠️ Reintentando conexión ({intentos}/3)...{RESET}")
                    time.sleep(5)
            
            if i < 10 and i < len(municiones):
                tiempo_espera = random.randint(120, 300)
                print(f"   {GRAY}⏱️ Pausa táctica de seguridad: {tiempo_espera // 60}m {tiempo_espera % 60}s...{RESET}\n")
                time.sleep(tiempo_espera)

        print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
        print(f"{GREEN}{BOLD} 🏁 OPERACIÓN DE FLUJO JSON COMPLETADA CON ÉXITO.{RESET}")
        print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    except Exception as e:
        print(f"\n{RED}❌ [ERROR CRÍTICO EN FLUJO X-RAY]: {e}{RESET}\n")

if __name__ == "__main__":
    agente_trafficker()
