import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time
import json
import re
import csv
import os
import sys

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def iniciar_extraccion():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} SYNERGY ARES DELTA V2.1 (DEEP EXTRACTION & PAIN VACUUM) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    ARCHIVO_COORDENADAS = "inteligencia_warrior.json"
    ARCHIVO_BOTIN = "botin_delta_bruto.csv"
    ARCHIVO_TEXTOS = "inteligencia_bruta_dolores.txt"

    if not os.path.exists(ARCHIVO_COORDENADAS):
        print(f"{RED}X [ERROR ESTRUCTURAL] No se encontró el mapa base: {ARCHIVO_COORDENADAS}{RESET}")
        print(f"{GRAY}>> Ejecuta Ares Delta V1 para generar las coordenadas primero.{RESET}\n")
        sys.exit(1)

    with open(ARCHIVO_COORDENADAS, "r", encoding="utf-8") as f:
        hilos = json.load(f)

    print(f"{GREEN}[+] Mapa táctico cargado. {BOLD}{len(hilos)}{RESET}{GREEN} coordenadas identificadas.{RESET}")
    print(f"{GRAY}[*] Iniciando máscara biométrica (undetected-chromedriver)...{RESET}")

    opciones = uc.ChromeOptions()
    opciones.binary_location = '/usr/bin/chromium'
    
    try:
        driver = uc.Chrome(options=opciones)
    except Exception as e:
        print(f"{RED}X Fricción al instanciar Chromium: {e}{RESET}")
        sys.exit(1)

    perlas_negras = []
    
    # Salto táctico: Omitir hilos fijados (reglas del foro)
    hilos_a_procesar = hilos[5:10] 

    try:
        for i, hilo in enumerate(hilos_a_procesar):
            url = hilo['enlace']
            titulo = hilo['titulo']
            
            if not url.startswith("http"):
                url = "https://www.warriorforum.com" + url

            print(f"\n{CYAN}🔗 Infiltrando trinchera {i+1}/{len(hilos_a_procesar)}: {BOLD}{titulo}{RESET}")
            driver.get(url)
            
            # Evasión heurística (Jittering)
            tiempo_pausa = 5 + (i % 3)
            print(f"{YELLOW}⏳ Leyendo el terreno ({tiempo_pausa}s de latencia evasiva)...{RESET}")
            time.sleep(tiempo_pausa)
            
            html_crudo = driver.page_source
            sopa = BeautifulSoup(html_crudo, 'html.parser')
            texto_puro = sopa.get_text(separator=' ', strip=True)

            # 1. Mira Láser para Correos (Regex)
            correos_encontrados = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', texto_puro)
            correos_encontrados = list(set(correos_encontrados)) 

            if correos_encontrados:
                print(f"{GREEN}  💎 ¡PERLAS ENCONTRADAS! {len(correos_encontrados)} correos extraídos.{RESET}")
                for correo in correos_encontrados:
                    perlas_negras.append({
                        "Email": correo,
                        "Dolor_Detectado": titulo,
                        "Plataforma_Origen": "warriorforum.com",
                        "Contexto": "Extracción profunda"
                    })
            else:
                print(f"{GRAY}  📝 Sin targets directos. Extrayendo transcripción para el Profiler...{RESET}")

            # 2. La Aspiradora de Dolor (Data Ingestion)
            with open(ARCHIVO_TEXTOS, "a", encoding="utf-8") as f_dolor:
                f_dolor.write(f"\n\n{'='*50}\n")
                f_dolor.write(f"HILO: {titulo}\n")
                f_dolor.write(f"URL: {url}\n")
                f_dolor.write(f"{'='*50}\n")
                f_dolor.write(texto_puro[:3000] + " [...]\n")

        # Serialización de botín (CSV)
        if perlas_negras:
            claves = perlas_negras[0].keys()
            modo = 'a' if os.path.exists(ARCHIVO_BOTIN) else 'w'
            with open(ARCHIVO_BOTIN, modo, newline='', encoding='utf-8') as f:
                escritor = csv.DictWriter(f, fieldnames=claves)
                if modo == 'w':
                    escritor.writeheader()
                escritor.writerows(perlas_negras)
            print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
            print(f"{GREEN}✓ Misión Cumplida. CRM actualizado en: {ARCHIVO_BOTIN}{RESET}")
        else:
            print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
            print(f"{YELLOW}! Misión Cumplida sin impactos PII.{RESET}")
            
        print(f"{GREEN}✓ Inteligencia cualitativa (Dolor) asegurada en: {ARCHIVO_TEXTOS}{RESET}")
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")

    except Exception as e:
        print(f"\n{RED}X Falla estructural en la matriz de extracción: {e}{RESET}\n")
    finally:
        print(f"{GRAY}💨 Ares Delta 2.1 cerrando túnel de infiltración...{RESET}\n")
        driver.quit()

if __name__ == "__main__":
    iniciar_extraccion()
