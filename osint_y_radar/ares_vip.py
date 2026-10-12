from playwright.sync_api import sync_playwright
import re
import time
import csv
import sys
from datetime import datetime

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def iniciar_sabueso_vip():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} SYNERGY VIP HOUND (HITL DORKING SCRAPER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    # EL CARGADOR MÚLTIPLE
    redes_objetivo = ["instagram.com", "linkedin.com", "facebook.com"]

    # EL FILTRO HIGH-TICKET Y LA LISTA NEGRA
    terminos_vip = '(CEO OR Director OR Dueño OR Fundador OR Inversor OR "Socio Gerente")'
    lista_negra = '-gratis -ong -voluntario -comunista -wok -diversidad -"sin fines de lucro"'
    base_correo = '"@gmail.com"'

    prospectos = set()
    patron_correo = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    with sync_playwright() as p:
        print(f"{GRAY}[*] Iniciando motor Chromium (Modo Headful para soporte HITL)...{RESET}")
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        
        paginas_a_minar_por_red = 3 # Perfil bajo para evadir rate limits
        
        for red in redes_objetivo:
            print(f"\n{CYAN}{BOLD}{'-'*40}{RESET}")
            print(f"{CYAN}{BOLD} 🌐 CAMBIANDO OBJETIVO VIP: Apuntando a {red.upper()} {RESET}")
            print(f"{CYAN}{BOLD}{'-'*40}{RESET}")
            
            # Construcción del Dork Avanzado para Google
            query = f"site:{red} {terminos_vip} {base_correo} {lista_negra}"
            
            for i in range(paginas_a_minar_por_red):
                salto = i * 10
                url_google = f"https://www.google.com/search?q={query}&start={salto}"
                
                print(f"\n{GRAY}[*] 🚀 Infiltrando Página {i+1} de {red} (Dorking)...{RESET}")
                page.goto(url_google)
                
                # --- EL FRENO DE MANO TÁCTICO PARA EL COMANDANTE (HITL) ---
                print(f"\n{RED}{BOLD} [!] PAUSA TÁCTICA ACTIVA (HITL) {RESET}")
                input(f"{YELLOW} 👉 Revisa el navegador. Resuelve el CAPTCHA de Google si lo hay y PRESIONA ENTER AQUÍ para continuar...{RESET}")
                
                print(f"{GREEN}[+] Orden de extracción recibida. Barriendo el DOM...{RESET}")
                texto_visible = page.inner_text("body")
                correos = re.findall(patron_correo, texto_visible)
                
                nuevos_encontrados = 0
                for c in correos:
                    c_low = c.lower()
                    # Filtros heurísticos de limpieza
                    if "google" not in c_low and ".png" not in c_low and "w3.org" not in c_low:
                        if c_low not in [p[0] for p in prospectos]:
                            prospectos.add((c_low, red))
                            nuevos_encontrados += 1
                            print(f"{GREEN}  💎 TARGET HIGH-TICKET ({red}): {BOLD}{c_low}{RESET}")
                
                print(f"{GRAY}✅ Página {i+1} completada: {nuevos_encontrados} targets VIP asegurados.{RESET}")

        print(f"\n{GRAY}💨 Matriz completa barrida. Cerrando Navegador y borrando rastro...{RESET}\n")
        time.sleep(2)
        browser.close()

    # --- SERIALIZACIÓN DE BOTÍN ---
    print(f"{BLUE}{BOLD}{'='*65}{RESET}")
    if len(prospectos) > 0:
        fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"Botin_VIP_Synergy_{fecha_actual}.csv"
        
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow(["Correo Electrónico", "Nicho", "Fuente"]) 
            for correo, fuente in prospectos:
                escritor.writerow([correo, "High-Ticket VIP", fuente])
                
        print(f"{GREEN}{BOLD} 🏆 BOTÍN VIP RECOLECTADO: {len(prospectos)} prospectos de alta rentabilidad.{RESET}")
        print(f"{GREEN} ✓ Súper-Mochila asegurada en: {nombre_archivo}{RESET}")
    else:
        print(f"{YELLOW} ⚠️ La mochila VIP está vacía. Filtros muy estrictos o sin resultados.{RESET}")
        
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

if __name__ == "__main__":
    iniciar_sabueso_vip()
