import os
import csv
import time
import random
import smtplib
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

# Configuración de red y credenciales desde la bóveda segura (.env)
REMITENTE = os.getenv("SMTP_USER", "ceo@agentpruebaai.online")
PASSWORD = os.getenv("SMTP_PASSWORD", "Gat197069#$")
CORREO_PRUEBA = os.getenv("ADMIN_EMAIL", "gbatavella@gmail.com")
HISTORIAL_FILE = "disparos_realizados.txt"

def cargar_historial():
    """Lee el archivo de historial para saber a qué destinatarios ya se les disparó."""
    if not os.path.exists(HISTORIAL_FILE):
        return set()
    try:
        with open(HISTORIAL_FILE, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())
    except Exception as e:
        print(f"{YELLOW}⚠️ Error al leer el historial: {e}{RESET}")
        return set()

def guardar_historial(email):
    """Sella el email en la memoria histórica tras un disparo exitoso."""
    try:
        with open(HISTORIAL_FILE, 'a', encoding='utf-8') as f:
            f.write(email + '\n')
    except Exception as e:
        print(f"{RED}❌ Error al escribir en el historial: {e}{RESET}")

def enviar_correo(remitente, password, destinatario, asunto, cuerpo):
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

    try:
        # Conexión cifrada STARTTLS al servidor SMTP
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
    print(f"{BLUE}{BOLD} 🚀 SYNERGY TRAFFICKER V5 (AUTONOMOUS COLD EMAIL ENGINE) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    # Cargador de leads (Parámetro configurable o variable de entorno)
    archivo_csv = os.getenv("OUTBOUND_CSV_SOURCE", "apollo_india_realestate_directors_08MAY.csv")
    
    if not os.path.exists(archivo_csv):
        print(f"{RED}❌ [ERROR CRÍTICO] No se encontró el archivo de munición: {archivo_csv}{RESET}")
        print(f"{GRAY}>> Verifique que el CSV esté alojado en la ruta de ejecución.{RESET}\n")
        return

    historial = cargar_historial()
    firma = "\n\n--\nGabriel Tavella\nFounder & CEO | Synergy (Human & AI Agents)\nAgendar Consultoría: https://calendar.app.google/1BqKtUmMijJJNLN4A"
    
    try:
        municiones_disponibles = []
        print(f"{GRAY}[*] Analizando cargador tabular ({archivo_csv})...{RESET}")
        
        with open(archivo_csv, mode='r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                email = fila.get('Email', '').strip()
                if email and email not in historial:
                    municiones_disponibles.append(fila)

        print(f"{GREEN}[+] Cargador analizado.{RESET} {BOLD}{len(municiones_disponibles)}{RESET} {GRAY}leads NUEVOS listos para operar.{RESET}\n")

        if len(municiones_disponibles) == 0:
            print(f"{YELLOW}🏁 OPERACIÓN FINALIZADA. Todos los objetivos de este CSV ya fueron impactados.{RESET}\n")
            return

        # =========================================================
        # FASE 1: CALIBRACIÓN Y PRUEBA HUMANA (HITL)
        # =========================================================
        print(f"{CYAN}=== FASE 1: CALIBRACIÓN DE COPY & ENTREGABILIDAD ==={RESET}")
        lead_ejemplo = municiones_disponibles[0]
        nombre_ej = lead_ejemplo.get('First Name', 'there')
        empresa_ej = lead_ejemplo.get('Company Name', 'your company')
        
        asunto_prueba = "real estate buyer pipeline"
        cuerpo_base = (
            f"Hi {nombre_ej},\n\n"
            f"We deployed a Swarm Protocol (autonomous AI agents) that handles 24/7 lead qualification "
            f"and outbound prospecting for real estate firms like {empresa_ej}.\n"
            f"Instead of your team wasting time on unqualified inquiries, our agents filter buyers and book site visits on autopilot.\n"
            f"Mind if I send a 2-min video showing how we fill your pipeline?"
        )
        cuerpo_prueba = cuerpo_base + firma

        print(f"{GRAY}>> Enviando correo de calibración de prueba hacia: {BOLD}{CORREO_PRUEBA}{RESET}")
        exito_prueba, msj_prueba = enviar_correo(REMITENTE, PASSWORD, CORREO_PRUEBA, asunto_prueba, cuerpo_prueba)
        print(f"   {msj_prueba}")

        confirmacion = input(f"\n{YELLOW}⚠️ ¿El correo llegó correctamente a tu bandeja de Gmail? (s/n): {RESET}")
        if confirmacion.lower() != 's':
            print(f"{RED}🛑 Calibración rechazada por el operador. Abortando misión.{RESET}\n")
            return

        # =========================================================
        # FASE 2: FUEGO REAL AUTORIZADO (GOTEO DIARIO MÁX 10)
        # =========================================================
        print(f"\n{GREEN}{BOLD}=== FASE 2: FUEGO REAL AUTORIZADO (MAX 10 OBJETIVOS) ==={RESET}\n")

        for i, lead in enumerate(municiones_disponibles[:10], 1):
            nombre = lead.get('First Name', 'there')
            empresa = lead.get('Company Name', 'your company')
            destinatario_real = lead.get('Email', '').strip()

            asunto = "real estate buyer pipeline"
            cuerpo = (
                f"Hi {nombre},\n\n"
                f"We deployed a Swarm Protocol (autonomous AI agents) that handles 24/7 lead qualification "
                f"and outbound prospecting for real estate firms like {empresa}.\n"
                f"Instead of your team wasting time on unqualified inquiries, our agents filter buyers and book site visits on autopilot.\n"
                f"Mind if I send a 2-min video showing how we fill your pipeline?"
            ) + firma

            print(f"[{i}/10] 🎯 Disparando hacia objetivo: {BOLD}{destinatario_real}{RESET} ({empresa})...")

            intentos = 0
            exito = False
            while intentos < 3 and not exito:
                exito, msj_resultado = enviar_correo(REMITENTE, PASSWORD, destinatario_real, asunto, cuerpo)
                print(f"      {msj_resultado}")
                if exito:
                    guardar_historial(destinatario_real) # Sella la memoria permanente
                else:
                    intentos += 1
                    print(f"      {YELLOW}⚠️ Reintentando conexión ({intentos}/3)...{RESET}")
                    time.sleep(5)

            # Pausa táctica estocástica entre envíos para proteger la IP/Dominio
            if i < 10 and i < len(municiones_disponibles):
                tiempo_espera = random.randint(120, 300)
                print(f"   {GRAY}⏱️ Pausa táctica de seguridad: {tiempo_espera // 60}m {tiempo_espera % 60}s...{RESET}\n")
                time.sleep(tiempo_espera)

        print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
        print(f"{GREEN}{BOLD} 🏁 GOTEO DIARIO COMPLETADO CON ÉXITO.{RESET}")
        print(f"{BLUE} 📂 El registro de memoria fue actualizado en '{HISTORIAL_FILE}'.{RESET}")
        print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    except Exception as e:
        print(f"\n{RED}❌ [ERROR CRÍTICO EN TRAFFICKER]: {e}{RESET}\n")

if __name__ == "__main__":
    agente_trafficker()
