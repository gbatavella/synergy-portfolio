import time
import sys
import os
from dotenv import load_dotenv

# --- SEGURIDAD Y BLINDAJE ---
load_dotenv()

# Variables de entorno para proteger los leads reales del sector M&A
LEAD_1_NAME = os.getenv("EEP_LEAD_1_NAME", "James M. | M&A Operations | Apex Advisors")
LEAD_1_EMAIL = os.getenv("EEP_LEAD_1_EMAIL", "info@apexadvisors.com")

LEAD_2_NAME = os.getenv("EEP_LEAD_2_NAME", "David R. | Analyst | Horizon Partners")
LEAD_2_EMAIL = os.getenv("EEP_LEAD_2_EMAIL", "david.r@horizonpartners.com")

LEAD_3_NAME = os.getenv("EEP_LEAD_3_NAME", "Robert K. | Mandate Origination | Horizon Co.")
LEAD_3_EMAIL = os.getenv("EEP_LEAD_3_EMAIL", "rkinney@horizonco.com")

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
    type_effect("=== SYNERGY ENGINE PROTOCOL v4.2 ===", BLUE, 0.05)
    time.sleep(0.5)
    target_niche = input(YELLOW + "[ACTION REQUIRED] Enter your Target Niche (e.g., 'M&A Advisors, Investment Banking'): " + RESET)

    if not target_niche:
        target_niche = "M&A Advisors & Finance"

    print("\n")
    type_effect(f"[*] INITIALIZING RaaS: >Synergy AI: Engine Evolution Protocol (EEP)", BLUE)
    time.sleep(1)

    type_effect(f"[+] Deploying 5 Dedicated Hunting Bots...", GREEN)
    for i in range(1, 6):
        sys.stdout.write(f"\r{GRAY}Bot {i} - Status: ACTIVE RECONNAISSANCE [██████████] ONLINE{RESET}")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n")

    # --- EXTRACCIÓN Y EL MOMENTO AHÁ ---

    # Éxito inicial
    rapid_output(f"{GRAY}[Hunting Bot 1] Scanning target nodes...{RESET}")
    time.sleep(0.5)
    rapid_output(f"{GREEN}[SUCCESS] {LEAD_1_NAME}{RESET}")
    rapid_output(f"{BLUE}[DATA VERIFIED] Contact info secured: {LEAD_1_EMAIL}{RESET}")
    print(GRAY + "-" * 60 + RESET)
    time.sleep(1)

    # EL BLOQUEO (DOLOR DEL CLIENTE)
    rapid_output(f"{GRAY}[Hunting Bot 2] Scanning target nodes...{RESET}")
    time.sleep(0.8)
    rapid_output(f"{RED}[CRITICAL ERROR 403] Target Web Architecture Updated (LinkedIn/Google Algorithm Change).{RESET}")
    rapid_output(f"{RED}[!] TRADITIONAL SCRAPERS DEFEATED. CONNECTION DROPPED.{RESET}")
    time.sleep(1.5)

    # EL MOMENTO AHÁ: EVOLUCIÓN EN CALIENTE
    rapid_output(f"\n{YELLOW}>>> INITIATING ENGINE EVOLUTION PROTOCOL (EEP)...{RESET}")
    time.sleep(1)
    rapid_output(f"{GRAY}>> Connecting to Synergy Central Server for dynamic patches...{RESET}")
    time.sleep(0.5)

    # Barra de carga de parche
    sys.stdout.write(YELLOW + ">> Downloading & Injecting DOM bypass patch: " + RESET)
    for i in range(1, 101, 15):
        sys.stdout.write(f"\r{YELLOW}>> Downloading & Injecting DOM bypass patch: [{i}%]{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write(f"\r{YELLOW}>> Downloading & Injecting DOM bypass patch: [100%]{RESET}\n")

    time.sleep(0.5)
    rapid_output(f"{GREEN}[HOTFIX SUCCESSFUL] Engine adapted to new algorithm in real-time. User Maintenance: ZERO.{RESET}\n")
    time.sleep(1)

    # Resurrección y continuación
    rapid_output(f"{GRAY}[Hunting Bot 2] Resuming scan with new logic...{RESET}")
    time.sleep(0.5)
    rapid_output(f"{GREEN}[SUCCESS] {LEAD_2_NAME}{RESET}")
    rapid_output(f"{BLUE}[DATA VERIFIED] Contact info secured: {LEAD_2_EMAIL}{RESET}")
    print(GRAY + "-" * 60 + RESET)
    time.sleep(0.8)

    rapid_output(f"{GRAY}[Hunting Bot 3] Scanning target nodes...{RESET}")
    time.sleep(0.5)
    rapid_output(f"{GREEN}[SUCCESS] {LEAD_3_NAME}{RESET}")
    rapid_output(f"{BLUE}[DATA VERIFIED] Contact info secured: {LEAD_3_EMAIL}{RESET}")
    print(GRAY + "-" * 60 + RESET)
    time.sleep(1)

    # --- REPORTE FINAL ---
    print("\n")
    type_effect("[!] COMPILING DATA PIPELINE...", YELLOW, 0.05)
    time.sleep(0.5)

    type_effect(f"""
    {{
      "system_health": "100% OPERATIONAL",
      "eep_interventions": 1,
      "niche_target": "{target_niche}",
      "maintenance_required": false,
      "results": [
        {{ "name": "{LEAD_1_NAME.split(' |')[0]}", "email": "{LEAD_1_EMAIL}", "verified": true }},
        {{ "name": "{LEAD_2_NAME.split(' |')[0]}", "email": "{LEAD_2_EMAIL}", "verified": true, "note": "Post-EEP Extraction" }},
        {{ "name": "{LEAD_3_NAME.split(' |')[0]}", "email": "{LEAD_3_EMAIL}", "verified": true, "note": "Post-EEP Extraction" }}
      ]
    }}
    """, GREEN, 0.005)

    type_effect("=== THE ENGINE NEVER SLEEPS. THE ENGINE ALWAYS EVOLVES. ===", BLUE)
    type_effect("Task complete. Architect, your pipeline is secure.", GREEN, 0.04)
