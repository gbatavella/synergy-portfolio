import time
import sys
import csv
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
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

# MOCK DE ARSENAL (Para demostración en repositorio público)
MISIONES_DEMO = {
    "alpha": {
        "url_coto": "https://www.facebook.com/groups/ejemplo-ventas-b2c",
        "keywords": ["compro", "busco", "precio", "interesado", "info"]
    }
}

def configurar_blindaje():
    """Inyecta la cura WebRTC y DNS en el núcleo del navegador"""
    opciones = Options()
    
    # === TRASPLANTE DE IDENTIDAD (RUTA BLINDADA) ===
    # En producción, usar ruta exacta del perfil aislado
    perfil_path = os.getenv("FIREFOX_PROFILE_PATH", "/default/path/to/profile")
    if os.path.exists(perfil_path):
        opciones.add_argument("-profile")
        opciones.add_argument(perfil_path)
    
    # Sellado de Fugas (OPSEC)
    opciones.set_preference("media.peerconnection.enabled", False)
    opciones.set_preference("network.proxy.socks_remote_dns", True)
    opciones.set_preference("network.dns.disablePrefetch", True)
    return opciones

def iniciar_patrullaje(mision_id):
    print(f"\n{BLUE}{BOLD}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD} 🚀 SYNERGY B2C RADAR | MISIÓN: {mision_id.upper()} {RESET}")
    print(f"{BLUE}{BOLD}{'='*60}{RESET}\n")
    
    # Cargar datos del arsenal
    try:
        datos_mision = MISIONES_DEMO[mision_id]
        url_objetivo = datos_mision["url_coto"]
        palabras_clave = datos_mision["keywords"]
    except KeyError:
        print(f"{RED}❌ Error: Misión '{mision_id}' no encontrada en el arsenal.{RESET}")
        sys.exit(1)

    print(f"{GRAY}⏳ Desplegando motor Firefox blindado y con memoria inyectada...{RESET}")
    opciones = configurar_blindaje()
    driver = webdriver.Firefox(options=opciones)
    
    try:
        print(f"{YELLOW}📡 Infiltrando Coto de Caza: {url_objetivo}{RESET}")
        driver.get(url_objetivo)
        time.sleep(5) 

        print(f"{CYAN}⏬ Iniciando Human Scroll Profundo (Buscando leads asíncronos)...{RESET}")
        scrolls = 15 
        for i in range(scrolls):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(2) 
            sys.stdout.write(f"\r{GRAY}   [+] Scroll {i+1}/{scrolls} completado...{RESET}")
            sys.stdout.flush()
        
        caja_negra = f"caja_negra_{mision_id}.png"
        print(f"\n{BLUE}📸 [CAJA NEGRA] Tomando fotografía táctica del entorno...{RESET}")
        driver.save_screenshot(caja_negra)
        print(f"{GRAY}   [+] Evidencia visual guardada como: {caja_negra}{RESET}")

        print(f"{YELLOW}🔬 Escaneando señales de compradores con red ampliada...{RESET}")
        
        posts = driver.find_elements(By.CSS_SELECTOR, "div[role='article']")
        leads_encontrados = 0
        archivo_csv = f"botin_{mision_id}.csv"
        
        with open(archivo_csv, mode="a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            if archivo.tell() == 0:
                escritor.writerow(["Bloque de Identidad y Texto", "Fecha de Extraccion"])

            for post in posts:
                texto_completo = post.text
                texto_minuscula = texto_completo.lower()
                
                if any(keyword in texto_minuscula for keyword in palabras_clave):
                    resumen_terminal = texto_completo.replace('\n', ' - ')[:60]
                    print(f"{GREEN}   [!] LEAD DETECTADO:{RESET} {resumen_terminal}...")
                    
                    escritor.writerow([texto_completo, time.strftime("%Y-%m-%d %H:%M:%S")])
                    leads_encontrados += 1

        if leads_encontrados == 0:
            print(f"\n{RED}⚠️ [ALERTA] Visión nula. No hay posts visibles que coincidan o el grupo está bloqueado.{RESET}")
        else:
            print(f"\n{GREEN}{BOLD}✅ ¡COSECHA EXITOSA! {leads_encontrados} leads guardados en {archivo_csv}{RESET}")

    except Exception as e:
        print(f"\n{RED}❌ Error en la matriz: {e}{RESET}")
    finally:
        print(f"\n{GRAY}🏁 Patrullaje finalizado. Regresando a base.{RESET}")
        print(f"{GRAY}🔴 Soltando candado de perfil. Limpiando rastros temporales.{RESET}\n")
        driver.quit()

if __name__ == "__main__":
    # Si se pasa un argumento por consola, usa ese; si no, usa el demo "alpha"
    mision_target = sys.argv[1] if len(sys.argv) > 1 else "alpha"
    iniciar_patrullaje(mision_target)
