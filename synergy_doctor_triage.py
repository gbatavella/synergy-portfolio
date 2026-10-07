import time
import sys
import os

# --- CÓDIGOS ANSI ---
BLUE = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
GRAY = "\033[90m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

def rapid_output(text, delay=0.05):
    print(text)
    time.sleep(delay)

if __name__ == "__main__":
    print("\n" * 2)
    rapid_output(f"{BLUE}{BOLD}=== SYNERGY DOCTOR: INFRASTRUCTURE IMMORTALITY (TRIAGE) ==={RESET}", 2)

    rapid_output(f"{GRAY}[*] Monitoring live vitals of 6 Active Autonomous Sales Reps...{RESET}", 2)

    rapid_output(f"\n{YELLOW}{BOLD}[!] INCOMING TELEMETRY ALERTS DETECTED:{RESET}", 1)
    rapid_output(f"{YELLOW}>> [1] Tech Payload: reCAPTCHA Bypass + DOM updates from SCIENTIST SCOUT.{RESET}", 1.5)
    rapid_output(f"{YELLOW}>> [2] Legal Payload: RFC-8058 Shield + GDPR constraints from LEGAL ORACLE.{RESET}", 2)

    rapid_output(f"\n{RED}{BOLD}[CRITICAL] FLEET DAMAGE DETECTED. INITIATING EMERGENCY TRIAGE...{RESET}", 1.5)
    time.sleep(1)

    # EL INFARTADO (Legal)
    rapid_output(f"\n{MAGENTA}{BOLD}>>> PATIENT 1: REP-02 (CARDIAC ARREST - GDPR TRAP DETECTED){RESET}", 1)
    rapid_output(f"{RED}   [!] Symptom: Caught in EU double opt-in honeypot. Imminent domain ban.{RESET}", 1.5)
    rapid_output(f"{GRAY}   >> Applying Defibrillator: Injecting Universal Legal Shield...{RESET}", 2)
    rapid_output(f"{GREEN}   [SUCCESS] Legal compliance restored. Domain reputation saved.{RESET}", 1)

    # EL QUEBRADO (Tech)
    rapid_output(f"\n{MAGENTA}{BOLD}>>> PATIENT 2: REP-03 (MULTIPLE FRACTURES - CLOUDFLARE BLOCK){RESET}", 1)
    rapid_output(f"{RED}   [!] Symptom: Extraction logic shattered by undocumented WAF update.{RESET}", 1.5)
    rapid_output(f"{GRAY}   >> Performing Orthopedic Surgery: Splicing new JS challenge bypass...{RESET}", 2)
    rapid_output(f"{GREEN}   [SUCCESS] DOM structure healed. Extraction capabilities restored.{RESET}", 1)

    # EL MUERTO (Resurrección)
    rapid_output(f"\n{MAGENTA}{BOLD}>>> PATIENT 3: REP-04 (FLATLINE - OFFLINE){RESET}", 1)
    rapid_output(f"{RED}   [!] Symptom: Banned by target authentication server. Pulse lost.{RESET}", 2)
    rapid_output(f"{GRAY}   >> Initiating Resurrection Protocol: Rotating Proxies and refreshing OAuth tokens...{RESET}", 2.5)
    rapid_output(f"{YELLOW}   >> Stand clear...{RESET}", 1)
    rapid_output(f"{GREEN}   [SUCCESS] Heartbeat detected. Rep-04 is back online.{RESET}", 1)

    # LA CAJA NEGRA (Prevención)
    rapid_output(f"\n{MAGENTA}{BOLD}>>> PREVENTATIVE CARE: REP-05 & REP-06{RESET}", 1)
    rapid_output(f"{GRAY}   >> Installing [BLACK BOX] Telemetry Modules...{RESET}", 1.5)
    rapid_output(f"{GREEN}   [!] BLACK BOX ACTIVE: Reps now feature auto-monitoring heuristics.{RESET}", 1.5)

    print("\n")
    rapid_output(f"{BLUE}{BOLD}[!] MOMENTO AHÁ: EMERGENCY TRIAGE COMPLETE.{RESET}", 1.5)
    rapid_output(f"{GREEN}[SUCCESS] All Autonomous Sales Reps discharged and fully operational.{RESET}", 1)
    rapid_output(f"{BLUE}{BOLD}=== SYSTEM INVULNERABILITY SECURED. INFINITE LIFE GRANTED. ==={RESET}\n", 1)
