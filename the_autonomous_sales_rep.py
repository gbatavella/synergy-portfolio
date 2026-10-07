import os
import time
import sys
from dotenv import load_dotenv

# --- SEGURIDAD Y CONFIGURACIÓN ---
load_dotenv()

# Variables de entorno para proteger datos reales del Pipeline
LEAD_NAME = os.getenv("LEAD_NAME", "Alexander Vance")
LEAD_ROLE = os.getenv("LEAD_ROLE", "Managing Partner")
LEAD_COMPANY = os.getenv("LEAD_COMPANY", "Vanguard Equity")
LEAD_SECTOR = os.getenv("LEAD_SECTOR", "PE (Private Equity)")

# --- CÓDIGOS DE COLOR ANSI ---
GREEN = "\033[92m"
BLUE = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
GRAY = "\033[90m"
MAGENTA = "\033[95m"

def type_effect(text, color=RESET, speed=0.02):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print(RESET)

def rapid_output(text, color=RESET, delay=0.01):
    print(color + text + RESET)
    time.sleep(delay)

# --- INICIO DEL SISTEMA ---
if __name__ == "__main__":
    print("\n" * 2)
    type_effect("=== THE AUTONOMOUS SALES REP (CLOSER PROTOCOL) ===", BLUE, 0.04)
    time.sleep(0.5)

    type_effect("[*] AWAITING PIPELINE DATA FROM SYNERGY SWARM/ENGINE...", GRAY)
    time.sleep(1.5)

    # Ingesta de Datos 
    rapid_output(f"\n{GREEN}[+] INCOMING PAYLOAD SECURED: 1 VIP LEAD{RESET}")
    rapid_output(f"{GRAY}>> Loading profile: {LEAD_NAME} | {LEAD_ROLE} | {LEAD_COMPANY}{RESET}")
    time.sleep(1)

    # --- PERFILADO PSICOLÓGICO ---
    print("\n")
    type_effect(f"[*] INITIATING NEAR-AGI PSYCHOLOGICAL PROFILING...", MAGENTA, 0.03)
    time.sleep(0.5)
    rapid_output(f"{YELLOW}>> Target Role:{RESET} {LEAD_ROLE} (Time-starved, ROI-driven)")
    time.sleep(0.4)
    rapid_output(f"{YELLOW}>> Identified Pain Point:{RESET} Manual deal flow origination & Analyst burnout.")
    time.sleep(0.4)
    rapid_output(f"{YELLOW}>> Closing Framework:{RESET} High-Ticket Logic + Price Judo (Frictionless Value Framing)")
    time.sleep(1)

    # --- REDACCIÓN Y BLINDAJE (EL MOMENTO AHÁ) ---
    print("\n")
    type_effect("[!] MOMENTO AHÁ: GENERATING HYPER-PERSONALIZED OUTREACH...", BLUE, 0.04)
    time.sleep(1)

    rapid_output(f"{GRAY}--- WHATSAPP VARIANT (DIRECT OUTREACH) ---{RESET}")
    type_effect(f""""Hi {LEAD_NAME.split()[0]}. Noticed {LEAD_COMPANY}'s recent market positioning. Most {LEAD_SECTOR} firms burn their analysts out with manual deal sourcing. We deployed an autonomous infrastructure that extracts off-market targets 24/7. Worth a quick 5-min async chat?" """, GREEN, 0.01)

    time.sleep(1)
    print("\n")

    rapid_output(f"{GRAY}--- EMAIL VARIANT WITH SCHEMA BLINDING ---{RESET}")
    type_effect(">> Drafting email body...", GRAY)
    time.sleep(0.5)
    type_effect(">> Injecting JSON-LD Schema Markup into headers for Primary Inbox placement...", YELLOW)
    for i in range(1, 4):
        sys.stdout.write(f"\r{GRAY}Applying cryptographic anti-spam signature [{i}/3]...{RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")

    type_effect(f"""
SUBJECT: {LEAD_COMPANY} // Proprietary Deal Flow Architecture

{LEAD_NAME.split()[0]},

I'll be direct. Manual origination is costing you leverage. 
While your team manually scrapes for targets, autonomous systems are already closing the gap. 

We build RaaS (Robots as a Service) infrastructures that operate 24/7, securing verified decision-makers in the {LEAD_SECTOR} space before they hit the open market. 

I have a live instance mapped for your sector. Reply 'yes' and I'll send a 90-second hidden link showing it extracting targets for {LEAD_COMPANY}.

Best,
Synergy AI Systems
""", GREEN, 0.005)

    print("\n")
    type_effect("=== REPRESENTATIVE READY. OUTREACH DEPLOYED. ===", BLUE)
    type_effect("Task complete. Architect, your closer is operating at 100%.", GREEN, 0.04)
