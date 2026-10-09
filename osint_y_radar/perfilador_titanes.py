import os
import csv
import time
import sys
from selenium.webdriver.common.by import By

# --- INYECCIÓN TÁCTICA: PROTOCOLO NORBERTO (DEV-OPS MODULE) ---
# Asegúrate de que el PYTHONPATH incluya la ruta raíz o el módulo esté accesible
try:
    from aislamiento_norberto import desplegar_norberto
except ImportError:
    # Fallback si se ejecuta desde otra ruta relativa
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../devops_y_core')))
    from aislamiento_norberto import desplegar_norberto

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def perfilador_titanes(archivo_entrada="titanes.txt", archivo_salida="perfiles_titanes.csv"):
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🤖 SYNERGY TITANS PROFILER (GUMROAD OSINT & NORBERTO CORE) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # Validación del archivo de entrada
    if not os.path.exists(archivo_entrada):
        print(f"{RED}❌ [ERROR CRÍTICO] No se encontró el archivo de objetivos: {archivo_entrada}{RESET}")
        print(f"{GRAY}>> Cree un archivo de texto plano con las URLs de los Titanes a perfilar.{RESET}\n")
        return

    try:
        with open(archivo_entrada, "r", encoding="utf-8") as f:
            urls = [linea.strip() for linea in f if linea.strip()]
    except Exception as e:
        print(f"{RED}❌ Error al leer el archivo {archivo_entrada}: {e}{RESET}")
        return

    if not urls:
        print(f"{YELLOW}⚠️ El archivo {archivo_entrada} está vacío. Ingrese objetivos válidos.{RESET}\n")
        return

    datos_extraidos = []

    # ---------------------------------------------------------
    # DESPLIEGUE DEL MOTOR AISLADO (Perfil Firefox Norberto)
    # ---------------------------------------------------------
    print(f"{GRAY}[*] Solicitando despliegue de instancia Firefox blindada (Norberto)...{RESET}")
    # modo_fantasma=True para ejecución desatendida en segundo plano
    driver = desplegar_norberto(modo_fantasma=True)

    if not driver:
        print(f"{RED}❌ [ERROR FATAL] No se pudo levantar el motor de navegación Firefox.{RESET}\n")
        return

    try:
        for i, url in enumerate(urls, 1):
            print(f"\n{CYAN}[{i}/{len(urls)}] 🎯 Analizando objetivo: {BOLD}{url}{RESET}")
            perfil = {
                "URL_Gumroad": url,
                "Nombre": "Desconocido",
                "Twitter_X": "",
                "Instagram": "",
                "YouTube": "",
                "Website": "",
                "Email": ""
            }

            try:
                driver.get(url)
                time.sleep(4) # Pausa táctica para asegurar renderizado completo del DOM

                # 1. Extracción del título de la página (Identidad del creador)
                titulo = driver.title
                if titulo:
                    perfil["Nombre"] = titulo.replace("— Gumroad", "").replace("Gumroad", "").strip()

                # 2. Extracción masiva de enlaces en el DOM
                elementos_a = driver.find_elements(By.TAG_NAME, "a")
                enlaces = [e.get_attribute("href") for e in elementos_a if e.get_attribute("href")]

                # 3. Clasificación Heurística de la Inteligencia Extraída
                for enlace in enlaces:
                    enlace_lower = enlace.lower()
                    if "twitter.com" in enlace_lower or "x.com" in enlace_lower:
                        if not perfil["Twitter_X"]: perfil["Twitter_X"] = enlace
                    elif "instagram.com" in enlace_lower:
                        if not perfil["Instagram"]: perfil["Instagram"] = enlace
                    elif "youtube.com" in enlace_lower:
                        if not perfil["YouTube"]: perfil["YouTube"] = enlace
                    elif "mailto:" in enlace_lower:
                        if not perfil["Email"]:
                            perfil["Email"] = enlace.replace("mailto:", "").replace("MAILTO:", "").strip()
                    
                    # Detección de sitio web personal (excluyendo plataformas de redes y la propia Gumroad)
                    elif (
                        "http" in enlace_lower 
                        and "gumroad.com" not in enlace_lower 
                        and "twitter.com" not in enlace_lower 
                        and "x.com" not in enlace_lower 
                        and "instagram.com" not in enlace_lower 
                        and "youtube.com" not in enlace_lower
                        and "facebook.com" not in enlace_lower
                        and "linkedin.com" not in enlace_lower
                    ):
                        if not perfil["Website"]: 
                            perfil["Website"] = enlace

                print(f"   {GREEN}✅ Inteligencia asegurada para: {BOLD}{perfil['Nombre']}{RESET}")
                datos_extraidos.append(perfil)

            except Exception as e:
                print(f"   {YELLOW}⚠️ Fricción al perfilar el objetivo {url}: {e}{RESET}")

    finally:
        print(f"\n{GRAY}[*] Destruyendo instancia de Norberto y liberando recursos del sistema...{RESET}")
        try:
            driver.quit()
        except Exception:
            pass

    # Consolidación del Reporte en formato Tabular (CSV)
    print(f"\n{GRAY}[*] Consolidando matriz de inteligencia en disco...{RESET}")
    
    if datos_extraidos:
        try:
            claves = datos_extraidos[0].keys()
            with open(archivo_salida, "w", newline="", encoding="utf-8") as f:
                dict_writer = csv.DictWriter(f, fieldnames=claves)
                dict_writer.writeheader()
                dict_writer.writerows(datos_extraidos)

            print(f"{BLUE}{BOLD}{'='*65}{RESET}")
            print(f"{GREEN}{BOLD} 🚀 EXTRACCIÓN COMPLETA. {len(datos_extraidos)} perfiles consolidados.{RESET}")
            print(f"{BLUE} 📂 Reporte exportado en: {archivo_salida}{RESET}")
            print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
        except Exception as e:
            print(f"{RED}❌ Error al escribir el archivo CSV: {e}{RESET}\n")
    else:
        print(f"{YELLOW}⚠️ 0 perfiles extraídos. Verifique la conectividad o la estructura del DOM.{RESET}\n")

if __name__ == "__main__":
    # Archivos por defecto para ejecución directa
    perfilador_titanes("titanes.txt", "perfiles_titanes.csv")
