import time
import os
from dotenv import load_dotenv

# Carga de entorno para ocultar estrategias comerciales locales
load_dotenv()

# --- CÓDIGOS ANSI PARA TERMINAL ---
GREEN = "\033[92m"
BLUE = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

class SynergyGeoAgent:
    def __init__(self):
        print(f"\n{BLUE}{BOLD}=============================================================={RESET}")
        print(f"{BLUE}{BOLD}  SYNERGY GEO AGENT (FRANCOTIRADOR OUTBOUND) EN LÍNEA  {RESET}")
        print(f"{BLUE}{BOLD}=============================================================={RESET}\n")
        print(f"{GREEN}[+] Agente GEO Inicializado. Calibrando satélites de extracción...{RESET}")

    def fijar_coordenadas(self, ciudad, nicho):
        self.ciudad = ciudad
        self.nicho = nicho
        print(f"\n{YELLOW}[*] Coordenadas fijadas: {self.ciudad} | Objetivo: {self.nicho}{RESET}")
        time.sleep(1.5)

    def ejecutar_barrido_local(self):
        print(f"{GRAY}[*] Iniciando barrido en directorios locales y APIs geoespaciales...{RESET}")
        time.sleep(2)
        
        # Simulación de extracción estructurada
        leads_encontrados = [
            {"empresa": f"{self.nicho} Elite Group", "ubicacion": f"Centro Financiero, {self.ciudad}", "liquidez_estimada": "Alta"},
            {"empresa": f"Premium {self.nicho} Partners", "ubicacion": f"Zona Norte, {self.ciudad}", "liquidez_estimada": "Muy Alta"}
        ]
        
        print(f"{GREEN}[+] Barrido completado. {len(leads_encontrados)} objetivos localizados en {self.ciudad}.{RESET}")
        
        for lead in leads_encontrados:
            print(f"    {BLUE}-> {lead['empresa']} ({lead['ubicacion']}) [Liquidez: {lead['liquidez_estimada']}]{RESET}")
            time.sleep(0.5)
            
        print(f"\n{RED}[!] Exportando lista al Enjambre Principal para ataque automatizado...{RESET}\n")

if __name__ == "__main__":
    geo_sniper = SynergyGeoAgent()
    
    # Inyección de coordenadas y nicho desde entorno (.env)
    # Valores por defecto para mantener la demo funcional en GitHub
    target_city = os.getenv("GEO_TARGET_CITY", "Miami, Florida")
    target_niche = os.getenv("GEO_TARGET_NICHE", "Real Estate Agencies")
    
    geo_sniper.fijar_coordenadas(target_city, target_niche)
    geo_sniper.ejecutar_barrido_local()
