import time
import sys
import csv
import re
import os
from dotenv import load_dotenv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# --- SEGURIDAD Y CONFIGURACIÓN ---
load_dotenv()

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def configurar_sabueso():
    opciones = uc.ChromeOptions()
    # Inyección de Proxy desde entorno para proteger la infraestructura del usuario
    PROXY_SERVER = os.getenv("PROXY_SERVER")
    if PROXY_SERVER:
        opciones.add_argument(f'--proxy-server={PROXY_SERVER}')
    opciones.add_argument('--disable-popup-blocking')
    return opciones

def extraer_telefonos(texto):
    # Regex calibrado para cazar números de contacto B2B/B2C en LATAM/Global
    patron_tel = r'(?:(?:\+?54|0054|11|[23]\d{2,3})[\s.-]?)?\d{3,4}[\s.-]?\d{4}'
    telefonos = re.findall(patron_tel, texto)
    return list(set(telefonos)) if telefonos else []

def mision_sabueso():
    print(f"\n{BLUE}{BOLD}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD} 🐺 SYNERGY INTENT HOUND (PROXY-ROUTED OSINT V4.2) {RESET}")
    print(f"{BLUE}{BOLD}    Objetivo: Interceptación de Demanda Activa{RESET}")
    print(f"{BLUE}{BOLD}{'='*60}{RESET}\n")
    
    print(f"{GRAY}[*] Iniciando Secuencia de Evasión Binaria...{RESET}")
    driver = uc.Chrome(options=configurar_sabueso())
    driver.set_page_load_timeout(45)

    try:
        # Validación de IP (Prueba de Búnker)
        driver.get('https://api.ipify.org')
        ip_actual = driver.find_element(By.TAG_NAME, "body").text.strip()
        print(f"{GREEN}✅ [OPSEC] Búnker sellado. IP Operativa (Proxy): {ip_actual}{RESET}\n")

        print(f"{YELLOW}[>] Accediendo a los nodos de búsqueda global...{RESET}")
        driver.get("https://www.google.com")
        time.sleep(3)

        # Comando OSINT (Dork) extraído del entorno para proteger el nicho
        dork_busqueda = os.getenv("INTENT_DORK", '("busco software b2b" OR "necesito automatizacion") ("whatsapp" OR "celular") -vende')
        
        print(f"{RED}{BOLD}[!] PUNTO DE CONTROL TÁCTICO: Observa la pantalla del navegador.{RESET}")
        input(f"{GREEN}>> Presiona ENTER para inyectar el código de rastreo...{RESET}")

        caja_busqueda = driver.find_element(By.NAME, "q")
        for letra in dork_busqueda:
            caja_busqueda.send_keys(letra)
            time.sleep(0.05)
            
        caja_busqueda.send_keys(Keys.RETURN)
        
        print(f"{GRAY}⏳ [SISTEMA] Analizando resultados... (Esperando renderizado asíncrono){RESET}")
        time.sleep(6)

        # Malla de extracción reforzada: Apunta directo a los Títulos H3
        titulos_h3 = driver.find_elements(By.TAG_NAME, "h3")
        print(f"\n{YELLOW}[!] Analizando posibles rastros en pantalla. Extrayendo oro...{RESET}\n")

        archivo_salida = "interceptacion_demanda.csv"
        with open(archivo_salida, mode="a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            if archivo.tell() == 0:
                escritor.writerow(["Origen", "Telefonos", "Enlace"])

            hallazgos = 0
            for h3 in titulos_h3:
                try:
                    titulo_texto = h3.text
                    if not titulo_texto: continue
                    
                    # DOM Climbing: Subimos al contenedor padre para sacar el texto completo
                    contenedor = h3.find_element(By.XPATH, "./ancestor::div[contains(@class, 'g') or @data-sokoban-container][1]")
                    texto_completo = contenedor.text
                    
                    enlace_elem = h3.find_element(By.XPATH, "./ancestor::a | ./parent::a")
                    enlace = enlace_elem.get_attribute("href")
                    
                    telefonos_encontrados = extraer_telefonos(texto_completo)
                    
                    hallazgos += 1
                    print(f"{BLUE}[+] ALERTA DE COMPRADOR #{hallazgos}:{RESET}")
                    print(f"     > Origen:  {titulo_texto}")
                    
                    if telefonos_encontrados:
                        print(f"     > {GREEN}{BOLD}¡BINGO! TELÉFONOS DETECTADOS:{RESET} {telefonos_encontrados}")
                    else:
                        print(f"     > {GRAY}Rastro sin número. Entrar al link para investigar.{RESET}")
                        
                    print(f"     > Enlace:  {enlace[:70]}...\n")
                    
                    escritor.writerow([titulo_texto, " | ".join(telefonos_encontrados), enlace])
                    
                    # Mimetismo Biométrico: Scroll visual para el Show
                    driver.execute_script("window.scrollBy(0, 150);")
                    time.sleep(1.5)
                    
                except Exception as e:
                    pass # Evita romper la ejecución por ads o fragmentos anómalos

        print(f"{BLUE}{BOLD}{'='*50}{RESET}")
        print(f"{GREEN}{BOLD}✅ EXTRACCIÓN EXITOSA: {hallazgos} prospectos procesados en {archivo_salida}{RESET}")
        print(f"{BLUE}{BOLD}{'='*50}{RESET}")

    finally:
        time.sleep(4)
        print(f"\n{GRAY}🔌 Apagando motor. Limpiando caché de proxy.{RESET}")
        driver.quit()

if __name__ == "__main__":
    mision_sabueso()
