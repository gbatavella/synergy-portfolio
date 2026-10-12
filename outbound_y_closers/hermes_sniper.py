import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import os
import time
import random
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

def iniciar_sniper():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🎯 SYNERGY HERMES SNIPER V1.3 (AUTONOMOUS CONDITIONAL DISPATCHER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CREDENCIALES Y CONFIGURACIÓN DEL ARMA (OPSEC)
    # ==========================================
    load_dotenv()
    REMITENTE = os.getenv("SMTP_USER", "gbatavella@gmail.com")
    PASSWORD = os.getenv("SMTP_APP_PASSWORD") 
    CORREO_CEO = os.getenv("ADMIN_EMAIL", "ceo.synergy@proton.me")

    if not PASSWORD:
        print(f"{RED}X [ERROR CRÍTICO] Falta SMTP_APP_PASSWORD en la bóveda .env.{RESET}")
        sys.exit(1)

    # RADARES DE SEGURIDAD
    TRAMPAS_SPAM = ["myname", "account1", "account2", "test", "fake", "admin", "info", "business", "support", "xxxx", "example"]
    ENLACE_GUMROAD = "https://batavella.gumroad.com/l/gjxthn"
    
    ARCHIVO_CSV = input(f"{YELLOW}📁 Ingresa el archivo CSV a atacar (ej. botin_incursion_depurado.csv): {RESET}").strip()
    ARCHIVO_REGISTRO = "registro_enviados.txt" 

    if not os.path.exists(ARCHIVO_CSV):
        print(f"\n{RED}⚠️ ERROR: No se encuentra el botín de datos '{ARCHIVO_CSV}' en el perímetro.{RESET}\n")
        sys.exit(1)

    # ==========================================
    # 2. FUNCIONES DE MEMORIA
    # ==========================================
    def cargar_memoria():
        if os.path.exists(ARCHIVO_REGISTRO):
            with open(ARCHIVO_REGISTRO, 'r') as f:
                return set(line.strip().lower() for line in f)
        return set()

    def registrar_impacto(correo):
        with open(ARCHIVO_REGISTRO, 'a') as f:
            f.write(correo.lower() + "\n")

    # ==========================================
    # 3. MOTOR DE COPYWRITING DINÁMICO
    # ==========================================
    def generar_payload(correo_destino, dolor_crudo, plataforma):
        asunto = f"saw your post on {plataforma}"
        dolor = str(dolor_crudo).lower()
        plataforma = str(plataforma).lower()
        
        # Árbol de Decisión Heurístico
        if "blackhat" in plataforma:
            if "pdf" in dolor or "video" in dolor:
                frase_empatia = "I saw you venting about another useless PDF. You have every right to be pissed off. 99% of the 'gurus' on that forum are selling recycled garbage."
            elif "setup" in dolor or "install" in dolor or "hard" in dolor:
                frase_empatia = "I saw you fighting with that complicated setup. Most of the 'tools' pushed there require a computer science degree just to barely work."
            elif "support" in dolor or "refund" in dolor or "scam" in dolor:
                frase_empatia = "I saw your post. It's frustrating how many scammers sell recycled junk and then completely ghost you."
            else:
                frase_empatia = "I saw you looking for a real solution and hitting a wall with tools that just don't deliver."
        else:
            if "pdf" in dolor or "video" in dolor:
                frase_empatia = "I noticed you were tired of buying $47 text files when you actually need a step-by-step video tutorial."
            elif "setup" in dolor or "install" in dolor or "hard" in dolor:
                frase_empatia = "I saw you were fighting with that complicated setup. It shouldn't be that hard."
            elif "support" in dolor or "refund" in dolor or "scam" in dolor:
                frase_empatia = "I saw your post. It's incredibly frustrating when creators ghost you after taking your money."
            else:
                frase_empatia = "I saw you were looking for a reliable solution to scale your systems."

        cuerpo = f"""Hey,

{frase_empatia}

The market is full of creators who sell useless PDFs and disappear. That's exactly why I built 'The Complete AI Sales System'.

It's not a text file. It's a complete video vault where I show you the exact architecture, click-by-click. You get the blueprints in both English and Spanish.

And if you get stuck? You actually get direct support from me.

If you want a system that actually works (and a creator who shows up), check the blueprint here:
👉 {ENLACE_GUMROAD}

Best,

Gabriel Tavella
CEO, Synergy Human & AI Agents
{CORREO_CEO}"""
        return asunto, cuerpo

    # ==========================================
    # 4. EL GATILLO (MOTOR SMTP)
    # ==========================================
    def motor_envio(destinatario, asunto, cuerpo):
        try:
            msg = MIMEMultipart()
            msg['From'] = REMITENTE
            msg['To'] = destinatario
            msg['Subject'] = asunto
            msg.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(REMITENTE, PASSWORD)
            server.sendmail(REMITENTE, destinatario, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(f"{RED}  X FALLO SMTP: {destinatario} | Error: {e}{RESET}")
            return False

    # ==========================================
    # 5. CICLO DE DISPARO AUTÓNOMO
    # ==========================================
    memoria_impactos = cargar_memoria()
    print(f"\n{GRAY}[*] Abriendo botín: {BOLD}{ARCHIVO_CSV}{RESET}")
    print(f"{GREEN}[+] Bóveda de memoria cargada: {len(memoria_impactos)} objetivos previamente neutralizados.{RESET}\n")
    
    try:
        with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Tolerancia a variaciones de columnas del OSINT
                email_objetivo = fila.get('Email') or fila.get('email', '')
                dolor_objetivo = fila.get('Dolor_Detectado') or fila.get('Dolor') or fila.get('dolor', '')
                plataforma_objetivo = fila.get('Plataforma_Origen') or fila.get('Plataforma') or fila.get('plataforma', 'the forum')
                
                if email_objetivo:
                    email_limpio = email_objetivo.lower().strip()
                    
                    # 🛡️ 1. Verificar Memoria (Zero-Duplication)
                    if email_limpio in memoria_impactos:
                        print(f"{GRAY}  ⏭️ SALTANDO: {email_limpio} (En caché de memoria){RESET}")
                        continue

                    # 🛡️ 2. Súper Cortafuegos Heurístico
                    email_sin_puntos = email_limpio.replace(".", "")
                    es_trampa = any(trampa in email_sin_puntos for trampa in TRAMPAS_SPAM)
                    
                    if es_trampa:
                        print(f"{YELLOW}  🛡️ CORTAFUEGOS: Trampa SpamTrap detectada ({email_objetivo}). Abortando.{RESET}")
                        registrar_impacto(email_limpio) 
                        continue 
                    
                    # 🔫 3. Ensamblaje Dinámico y Disparo
                    print(f"{CYAN}  🎯 EN LA MIRA: {BOLD}{email_limpio}{RESET}")
                    asunto_final, cuerpo_final = generar_payload(email_limpio, dolor_objetivo, plataforma_objetivo)
                    
                    exito = motor_envio(email_limpio, asunto_final, cuerpo_final)
                    
                    if exito:
                        print(f"{GREEN}  ✓ IMPACTO CONFIRMADO.{RESET}")
                        registrar_impacto(email_limpio)
                        
                        # Evasión Estocástica de Rate Limits
                        pausa = random.randint(15, 35)
                        print(f"{GRAY}  ⏳ Recargando Sniper. Enfriamiento de cañones ({pausa}s)...{RESET}\n")
                        time.sleep(pausa)

        print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
        print(f"{GREEN}{BOLD}🏁 MISIÓN FINALIZADA. El dron de artillería regresa a la base.{RESET}")
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")
        
    except Exception as e:
        print(f"\n{RED}X Falla crítica durante la secuencia de fuego: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_sniper()
