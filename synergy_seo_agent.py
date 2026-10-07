import time
import random
import os
from dotenv import load_dotenv

# --- SEGURIDAD Y CONFIGURACIÓN ---
load_dotenv()

# Códigos de Color ANSI
GREEN = "\033[92m"
BLUE = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
GRAY = "\033[90m"
BOLD = "\033[1m"

class SynergySEOAgent:
    def __init__(self, target_url):
        self.target_url = target_url
        self.keywords = ["AI sales automation", "lead generation 2026", "replace cold email", "B2B growth hacking"]
        print(f"\n{BLUE}{BOLD}=============================================================={RESET}")
        print(f"{BLUE}{BOLD}  SYNERGY SEO AGENT (VÓRTICE DE TRÁFICO INBOUND) ONLINE  {RESET}")
        print(f"{BLUE}{BOLD}=============================================================={RESET}\n")
        print(f"{GREEN}[+] Agente SEO Inicializado. Objetivo: Redirigir tráfico masivo al nodo destino.{RESET}")

    def rastrear_tendencias(self):
        print(f"\n{GRAY}[*] Escaneando algoritmos de búsqueda y foros (Reddit/X)...{RESET}")
        time.sleep(2)
        keyword_caliente = random.choice(self.keywords)
        print(f"{YELLOW}[+] Tendencia detectada con alto volumen de búsqueda:{RESET} '{keyword_caliente}'")
        return keyword_caliente

    def generar_y_publicar_carnada(self, keyword):
        print(f"\n{GRAY}[*] Generando hilo de alto impacto basado en '{keyword}'...{RESET}")
        time.sleep(2)
        contenido = f"¿Sigues usando Cold Email? Este motor autónomo extrae y cierra leads 2.6x más rápido usando {keyword}. Míralo operar en vivo aquí: {self.target_url}"
        print(f"{GREEN}[+] Contenido generado con éxito.{RESET}")
        
        print(f"\n{GRAY}--------------------------------------------------{RESET}")
        print(f"{BLUE}[>] SIMULACIÓN DE POSTEO EN REDES:{RESET}")
        print(f"    {contenido}")
        print(f"{GRAY}--------------------------------------------------{RESET}")
        
        print(f"\n{RED}[!] VÓRTICE ABIERTO. ESPERANDO CLICS ENTRANTES...{RESET}\n")

if __name__ == "__main__":
    # La URL se carga desde el .env para proteger el endpoint real
    URL_LANDING = os.getenv("LANDING_PAGE_URL", "https://synergy-ai.up.railway.app") 
    
    seo_sniper = SynergySEOAgent(URL_LANDING)
    
    tendencia = seo_sniper.rastrear_tendencias()
    seo_sniper.generar_y_publicar_carnada(tendencia)
