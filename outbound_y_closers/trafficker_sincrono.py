import os
import json
import time
import random
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Cargar variables de entorno (El archivo .env NO se sube a GitHub)
load_dotenv()

# --- INYECCIÓN TÁCTICA: PROTOCOLO NORBERTO (Modulo Externo) ---
# from aislamiento_norberto import desplegar_norberto
# ---------------------------------------------

def extraer_email_rayos_x(lead_dict):
    """Escanea todo el registro del prospecto y extrae el primer email que encuentre."""
    lead_str = json.dumps(lead_dict)
    match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', lead_str)
    if match:
        return match.group(0)
    return None

def enviar_correo(remitente, password, destinatario, asunto, cuerpo, smtp_server, smtp_port):
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

    try:
        servidor = smtplib.SMTP(smtp_server, smtp_port)
        servidor.starttls()
        servidor.login(remitente, password)
        servidor.send_message(msg)
        servidor.quit()
        return True, "✅ Aceptado por el servidor."
    except Exception as e:
        return False, f"❌ Falla de entrega: {e}"

def trafficker_sincrono():
    print("🚀 INICIANDO TRAFFICKER SÍNCRONO V2.3 (FRANCOTIRADOR) 🚀\n")
    
    # ---------------------------------------------------------
    # DESPLIEGUE DEL MOTOR AISLADO (Perfil Firefox Norberto)
    # ---------------------------------------------------------
    # print("  ⏳ Levantando navegador Firefox (Norberto) en espera...")
    # driver = desplegar_norberto(modo_fantasma=True) 

    # Carga de Secretos y Configuración desde el Entorno Local (.env)
    remitente = os.getenv("SMTP_USER", "usuario_seguro@dominio.com")
    password = os.getenv("SMTP_PASS", "TU_CLAVE_AQUI")
    smtp_server = os.getenv("SMTP_SERVER", "mail.privateemail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    
    archivo_municion = os.getenv("LEADS_FILE", "municion_aprobada_usa.json")
    correo_prueba = os.getenv("TEST_EMAIL", "tu_correo@gmail.com")
    
    firma_template = os.getenv("SIGNATURE_TEMPLATE", "\n\n{name}\n{title} | {company}")
    firma = firma_template.format(
        name=os.getenv("SIGNATURE_NAME", "Tu Nombre"),
        title=os.getenv("SIGNATURE_TITLE", "Director"),
        company=os.getenv("SIGNATURE_COMPANY", "Tu Empresa")
    )
    
    try:
        with open(archivo_municion, 'r', encoding='utf-8') as f:
            municiones = json.load(f)

        print(f"📦 Cargador conectado. {len(municiones)} leads listos.\n")

        # --- FASE 1: PRUEBA DE CALIBRACIÓN ---
        print("=== FASE 1: CALIBRACIÓN ===")
        texto_crudo_prueba = municiones[0]['mensaje_b2b']
        lineas_prueba = texto_crudo_prueba.split('\n')
        asunto_prueba = "[PRUEBA] " + lineas_prueba[0].replace("subject:", "").replace("Subject:", "").strip()
        cuerpo_prueba = '\n'.join(lineas_prueba[1:]).strip() + firma

        print(f"Enviando correo a {correo_prueba}...")
        exito_prueba, msj_prueba = enviar_correo(remitente, password, correo_prueba, asunto_prueba, cuerpo_prueba, smtp_server, smtp_port)
        print(msj_prueba)

        if not exito_prueba:
            print("🛑 FALLA EN PRUEBA. Revisa tu configuración SMTP.")
            return

        confirmacion = input(f"\n⚠️ Revisa tu Inbox ({correo_prueba}). ¿Llegó bien y con firma? (s/n): ")
        if confirmacion.lower() != 's':
            print("🛑 CANCELADO POR EL OPERADOR.")
            return

        # --- FASE 2: FUEGO REAL (Bucle Estocástico) ---
        print("\n=== FASE 2: FUEGO REAL AUTORIZADO ===")
        # Limitado a 4 para este despliegue de ejemplo
        for i, lead in enumerate(municiones[:4], 1):
            nombre = lead.get('nombre', 'Contacto')
            destinatario_real = extraer_email_rayos_x(lead)

            if not destinatario_real:
                print(f"[{i}/4] ⚠️ SALTANDO: No se encontró email para {nombre}.")
                continue

            texto_crudo = lead['mensaje_b2b']
            lineas = texto_crudo.split('\n')
            asunto = lineas[0].replace("subject:", "").replace("Subject:", "").strip()
            cuerpo = '\n'.join(lineas[1:]).strip() + firma

            print(f"[{i}/4] 🎯 Disparando a: {destinatario_real}...")
            
            intentos = 0
            exito = False
            while intentos < 3 and not exito:
                exito, msj_resultado = enviar_correo(remitente, password, destinatario_real, asunto, cuerpo, smtp_server, smtp_port)
                print(f"  {msj_resultado}")
                if not exito:
                    intentos += 1
                    time.sleep(5)

            if i < 4:
                # Pausa táctica antispam entre 2 y 5 minutos
                tiempo_espera = random.randint(120, 300)
                print(f"  ⏱️ Pausa táctica (Anti-Spam) de {tiempo_espera // 60}m {tiempo_espera % 60}s...\n")
                time.sleep(tiempo_espera)

        print("\n🏁 OPERACIÓN FINALIZADA.")

    except Exception as e:
        print(f"❌ ERROR CRÍTICO: {e}")
    finally:
        pass

if __name__ == "__main__":
    trafficker_sincrono()
