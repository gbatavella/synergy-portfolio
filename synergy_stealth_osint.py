import time
import sys
import re
import random
import datetime
import os
from dotenv import load_dotenv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from weasyprint import HTML

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

# MOCK DE ARSENAL (Reemplaza la importación privada de dorks_sw4_point)
DORKS_DEMO = os.getenv("OSINT_DORKS", 'site:facebook.com "logistica" "contacto", site:instagram.com "transporte" "whatsapp"').split(',')

def configurar_sabueso():
    """Configura el driver indetectable sin proxy para latencia óptima en DDG."""
    opciones = uc.ChromeOptions()
    # Modo headless puede ser detectado por DDG a veces; se recomienda mantener ventana
    return opciones

def extraer_telefonos(texto):
    """Aplica Regex avanzado para extraer teléfonos B2B (Foco LATAM/ARG)."""
    patron_tel = r'(?:(?:\+?54|0054|11|[23]\d{2,3})[\s.-]?)?\d{3,4}[\s.-]?\d{4}'
    telefonos_crudos = re.findall(patron_tel, texto)
    telefonos_reales = []
    
    for tel in telefonos_crudos:
        solo_numeros = re.sub(r'\D', '', tel)
        # Filtro de falsos positivos (evita capturar años como 2024, 2025)
        if len(solo_numeros) >= 8 and not re.match(r'^20[12]\d20[12]\d$', solo_numeros):
            telefonos_reales.append(tel)
            
    return list(set(telefonos_reales))

def generar_pdf_prospectos(leads):
    ahora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    html_content = f'''
    <html><head><style>
        @page {{ size: A4 landscape; margin: 15mm; background-color: #f0f2f5; }}
        body {{ font-family: sans-serif; color: #1c1e21; }}
        .header {{ background: #00599C; color: white; padding: 20px; text-align: center; border-radius: 5px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: white; }}
        th {{ background: #004070; color: white; padding: 12px; text-align: left; font-size: 10pt; }}
        td {{ padding: 10px; border-bottom: 1px solid #ddd; font-size: 9pt; }}
        .hot {{ color: #d32f2f; font-weight: bold; background: #ffebee; padding: 4px; border-radius: 3px; }}
        .url-link {{ color: #1976d2; text-decoration: none; font-size: 8pt; }}
    </style></head><body>
        <div class="header"><h1>SYNERGY AI LABS - EXTRACCIÓN OSINT (TARGET ACQUISITION)</h1></div>
        <table><thead><tr><th width="30%">Origen / Entidad</th><th width="15%">Contacto</th><th width="15%">Estado</th><th width="40%">Enlace</th></tr></thead><tbody>
    '''
    for lead in leads:
        status = '<span class="hot">CARGA CALIENTE</span>' if lead['tel'] else 'Investigar URL'
        html_content += f"<tr><td>{lead['titulo']}</td><td><b>{lead['tel']}</b></td><td>{status}</td><td><a class='url-link' href='{lead['url']}'>{lead['url']}</a></td></tr>"
    
    html_content += f"</tbody></table><div class='footer'><br>Synergy AI Agents | {ahora}</div></body></html>"
    
    nombre_salida = "BOTIN_OSINT_SYNERGY.pdf"
    HTML(string=html_content).write_pdf(nombre_salida)
    return nombre_salida

def mision_sabueso():
    print(f"\n{BLUE}{BOLD}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD} 🦅 SYNERGY STEALTH OSINT (DUCKDUCKGO & PDF COMPILER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*60}{RESET}\n")
    
    print(f"{YELLOW}[SISTEMA] Motor V6.1 Activado - Inyectando Evasión Binaria...{RESET}")
    driver = uc.Chrome(options=configurar_sabueso())
    todos_los_leads = []

    try:
        for dork in DORKS_DEMO:
            dork = dork.strip()
            print(f"\n{GRAY}[>] Explorando Ruta en DuckDuckGo: {dork[:50]}...{RESET}")
            driver.get("https://duckduckgo.com/")
            
            # ESPERA INTELIGENTE Y UNIVERSAL
            try:
                caja = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@type='text' or @type='search']"))
                )
            except:
                print(f"{RED}[!!!] ERROR: No se detectó la caja de búsqueda. Posible WAF activo.{RESET}")
                continue

            caja.clear()
            print(f"{CYAN}  [+] Simulando mimetismo biométrico (Tipeo humano)...{RESET}")
            for letra in dork:
                caja.send_keys(letra)
                time.sleep(random.uniform(0.02, 0.08)) 
            caja.send_keys(Keys.RETURN)
            
            time.sleep(6) # Tiempo para carga de SERP

            results = driver.find_elements(By.CSS_SELECTOR, "div.result__body, article")
            
            if not results:
                print(f"{YELLOW}  [-] Sin resultados visibles. Pasando a la siguiente ruta...{RESET}")
                continue

            for res in results[:6]: 
                try:
                    titulo_elem = res.find_element(By.CSS_SELECTOR, "h2 a, a[data-testid='result-title-a']")
                    titulo_texto = titulo_elem.text
                    url_enlace = titulo_elem.get_attribute("href")
                    
                    try:
                        snippet_elem = res.find_element(By.CSS_SELECTOR, "div.result__snippet, div[data-testid='result-snippet']")
                        texto_analizar = snippet_elem.text
                    except:
                        texto_analizar = titulo_texto
                    
                    tels = extraer_telefonos(texto_analizar)
                    
                    todos_los_leads.append({
                        'titulo': titulo_texto[:70] + "...", 
                        'tel': " | ".join(tels),
                        'url': url_enlace
                    })
                    print(f"{GREEN}  [+] Pista asegurada:{RESET} {titulo_texto[:40]}...")
                except: continue
                
            time.sleep(random.uniform(3.0, 6.0)) 
        
        print(f"\n{BLUE}[SISTEMA] Redada completada. Compilando manifiesto...{RESET}")
        driver.quit() 
        
        if todos_los_leads:
            print(f"{GRAY}  [+] Renderizando HTML/CSS a PDF corporativo...{RESET}")
            archivo_pdf = generar_pdf_prospectos(todos_los_leads)
            print(f"\n{GREEN}{BOLD}✅ EXTRACCIÓN FINALIZADA: Reporte generado en {archivo_pdf}{RESET}\n")
        else:
            print(f"\n{YELLOW}⚠️ Finalizado sin datos cálidos extraíbles.{RESET}\n")
            
    except Exception as e:
        print(f"\n{RED}❌ Error crítico en el núcleo Stealth: {e}{RESET}")
        driver.quit()

if __name__ == "__main__":
    mision_sabueso()
