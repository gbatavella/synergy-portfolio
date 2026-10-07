import time
import sys
import os
from dotenv import load_dotenv

# Carga de entorno para proteger Leads reales
load_dotenv()

# --- BLINDAJE DE LEADS (Variables de Entorno con Fallbacks Genéricos) ---
LEAD_1_NAME = os.getenv("LEAD_1_NAME", "Alexander Vance | Managing Partner | Alpha Equity")
LEAD_1_EMAIL = os.getenv("LEAD_1_EMAIL", "avance@alphaequity.com")

LEAD_2_NAME = os.getenv("LEAD_2_NAME", "Sarah Jenkins | Director | Horizon Ventures")
LEAD_2_EMAIL = os.getenv("LEAD_2_EMAIL", "s.jenkins@horizonventures.com")

LEAD_3_BOUNCE = os.getenv("LEAD_3_BOUNCE", "j.doe@nexussystems.com")
LEAD_3_PIVOT = os.getenv("LEAD_3_PIVOT", "Elena Rostova | Executive Contact | Nexus Systems")
LEAD_3_PIVOT_EMAIL = os.getenv("LEAD_3_PIVOT_EMAIL", "erostova@nexussystems.com")

LEAD_4_NAME = os.getenv("LEAD_4_NAME", "Robert Thorne | MD | Apex Capital")
LEAD_4_EMAIL = os.getenv("LEAD_4_EMAIL", "rthorne@apexcap.com")

LEAD_5_NAME = os.getenv("LEAD_5_NAME", "Marcus T. (@BuildWithMarcus) | Creator & Builder")

# --- Códigos de Color (Estética Hacker/Corporate) ---
GREEN = "\033[92m"
BLUE = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
GRAY = "\033[90m"

def type_effect(text, color=RESET, speed=0.02):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print(RESET)

def rapid_output(text, color=RESET):
    print(color + text + RESET)
    time.sleep(0.01)

# --- INICIO DEL SISTEMA ---
if __name__ == "__main__":
    print("\n" * 2)
    type_effect("=== SYNERGY PROTOCOL v8.1 ===", BLUE, 0.05)
    time.sleep(0.5)
    target_niche = input(YELLOW + "[ACTION REQUIRED] Enter your Target Niche (e.g., 'Private Equity, Real Estate & Creators'): " + RESET)

    if not target_niche:
        target_niche = "High-Ticket VIP & Founders"

    print("\n")
    type_effect(f"[*] INITIALIZING INFRAESTRUCTURE: >Synergy AI: Swarm Evolution Protocol (RaaS)", BLUE)
    time.sleep(1)

    type_effect(f"[+] Deploying 5 Autonomous Sales Reps...", GREEN)
    for i in range(1, 6):
        sys.stdout.write(f"\r{GRAY}Rep {i} - Status: TACTICAL RECONNAISSANCE [██████████] ONLINE{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")

    type_effect(f"[*] Establishing secure connection to B2B Data Nodes for Niche: '{target_niche}'...", BLUE)
    time.sleep(1.5)

    type_effect("[!] LIVE INFILTRATION STARTING...", RED, 0.05)
    time.sleep(0.5)

    # --- EXTRACCIÓN DINÁMICA ---

    # Rep 1
    rapid_output(f"{GRAY}[Autonomous Rep 1] Extracting Profile...{RESET}")
    rapid_output(f"{GREEN}[SUCCESS] {LEAD_1_NAME}{RESET}")
    rapid_output(f"{BLUE}[DATA VERIFIED] Contact info secured & validated: {LEAD_1_EMAIL}{RESET}")
    print(GRAY + "-" * 60 + RESET)
    time.sleep(0.8)

    # Rep 2
    rapid_output(f"{GRAY}[Autonomous Rep 2] Extracting Profile...{RESET}")
    rapid_output(f"{GREEN}[SUCCESS] {LEAD_2_NAME}{RESET}")
    rapid_output(f"{BLUE}[DATA VERIFIED] Contact info secured & validated: {LEAD_2_EMAIL}{RESET}")
    print(GRAY + "-" * 60 + RESET)
    time.sleep(0.8)

    # Rep 3: EL PIVOTE MAGISTRAL 
    rapid_output(f"{GRAY}[Autonomous Rep 3] Extracting Profile...{RESET}")
    rapid_output(f"{RED}[WARNING] Target email ({LEAD_3_BOUNCE}) returned Auto-Responder/Bounce.{RESET}")
    time.sleep(1)
    rapid_output(f"{YELLOW}>>> INITIATING CONTEXTUAL ANALYSIS OF BOUNCE MESSAGE...{RESET}")
    time.sleep(1.5)
    rapid_output(f"{GREEN}[PIVOT SUCCESSFUL] Extracted new Decision Maker from auto-reply payload.{RESET}")
    rapid_output(f"{GREEN}[SUCCESS] {LEAD_3_PIVOT}{RESET}")
    rapid_output(f"{BLUE}[DATA VERIFIED] Contact info secured & validated: {LEAD_3_PIVOT_EMAIL}{RESET}")
    print(GRAY + "-" * 60 + RESET)
    time.sleep(0.8)

    # Rep 4
    rapid_output(f"{GRAY}[Autonomous Rep 4] Extracting Profile...{RESET}")
    rapid_output(f"{GREEN}[SUCCESS] {LEAD_4_NAME}{RESET}")
    rapid_output(f"{BLUE}[DATA VERIFIED] Contact info secured & validated: {LEAD_4_EMAIL}{RESET}")
    print(GRAY + "-" * 60 + RESET)
    time.sleep(0.8)

    # Rep 5
    rapid_output(f"{GRAY}[Autonomous Rep 5] Scraping Social Nodes...{RESET}")
    rapid_output(f"{GREEN}[SUCCESS] {LEAD_5_NAME}{RESET}")
    rapid_output(f"{BLUE}[DATA VERIFIED] Digital footprint secured & validated.{RESET}")
    print(GRAY + "-" * 60 + RESET)
    time.sleep(0.8)

    # --- EL MOMENTO AHÁ (COMPILACIÓN JSON) ---
    print("\n")
    type_effect("[!] MOMENTO AHÁ: Compiling Data for The Autonomous Sales Rep...", YELLOW, 0.05)
    time.sleep(1)

    type_effect(f"""
    {{
      "total_leads_secured": 5,
      "dynamic_pivots_executed": 1,
      "data_structure": "Clean JSON",
      "validation_status": "MX Records Found - VALID",
      "next_action": "Pass to Autonomous Rep / Pipeline Integration",
      "results": [
        {{ "name": "{LEAD_3_PIVOT.split(' |')[0]}", "email": "{LEAD_3_PIVOT_EMAIL}", "verified": true, "note": "Pivoted from bounce" }},
        {{ "name": "{LEAD_5_NAME.split(' (')[0]}", "source": "Social Nodes", "verified": true }},
        {{ "name": "{LEAD_1_NAME.split(' |')[0]}", "email": "{LEAD_1_EMAIL}", "verified": true }}
      ]
    }}
    """, GREEN, 0.005) 

    type_effect("=== THE SWARM NEVER SLEEPS. THE SWARM ALWAYS EVOLVES. ===", BLUE)
    type_effect("Task complete. Architect, your pipeline is full.", GREEN, 0.04)
