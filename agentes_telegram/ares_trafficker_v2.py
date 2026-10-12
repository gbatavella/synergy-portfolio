import requests
import json
import time
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def iniciar_operacion_v2():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} SYNERGY ARES TRAFFICKER V2 (STATEFUL OSINT RADAR) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # --- OPSEC Y CONFIGURACIÓN ---
    load_dotenv()
    CORREO_CONTACTO = os.getenv("ADMIN_EMAIL", "ceo.synergy@proton.me")
    
    HEADERS = {
        'User-Agent': f'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Synergy/AresDelta_Trafficker (Contact: {CORREO_CONTACTO})'
    }

    ARCHIVO_CONFIG = 'inteligencia_creadores.json'
    ARCHIVO_MEMORIA = 'memoria_ares.json'
    ARCHIVO_REPORTE = f'Botin_Creadores_{datetime.now().strftime("%Y-%m-%d_%H-%M")}.json'

    def cargar_memoria():
        if os.path.exists(ARCHIVO_MEMORIA):
            with open(ARCHIVO_MEMORIA, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def guardar_memoria(memoria_actualizada):
        with open(ARCHIVO_MEMORIA, 'w', encoding='utf-8') as f:
            json.dump(memoria_actualizada, f, indent=4)

    def cargar_inteligencia():
        try:
            with open(ARCHIVO_CONFIG, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"{RED}X [ERROR ESTRUCTURAL] No se encontró el manifiesto de configuración: {ARCHIVO_CONFIG}{RESET}")
            print(f"{GRAY}>> Crea el archivo JSON con los objetivos y palabras clave antes de iniciar.{RESET}\n")
            return None

    def analizar_texto(texto, palabras_clave, exclusiones):
        texto_min = str(texto).lower()
        
        # Capa 1: Filtro de Exclusión (Basura)
        for exc in exclusiones:
            if exc in texto_min:
                return False, []
                
        # Capa 2: Filtro de Inclusión (Oro)
        hits = [pc for pc in palabras_clave if pc in texto_min]
        if hits:
            return True, hits
            
        return False, []

    def infiltrar_reddit(url, palabras_clave, exclusiones, memoria):
        print(f"{GRAY}[*] Escaneando sub-matriz: {BOLD}{url.split('.com')[1][:40]}...{RESET}")
        oportunidades = []
        nuevas_urls = []
        
        try:
            respuesta = requests.get(url, headers=HEADERS, timeout=10)
            if respuesta.status_code != 200:
                print(f"{YELLOW}! Fricción en el perímetro: Status {respuesta.status_code}{RESET}")
                return oportunidades, nuevas_urls
                
            data = respuesta.json()
            posts = data.get('data', {}).get('children', [])
            
            for post in posts:
                post_data = post['data']
                url_post = f"https://www.reddit.com{post_data.get('permalink', '')}"
                
                # CONTROL DE MEMORIA (Zero-Duplication)
                if url_post in memoria:
                    continue
                    
                titulo = post_data.get('title', '')
                cuerpo = post_data.get('selftext', '')
                autor = post_data.get('author', '')
                
                contexto_completo = f"{titulo} {cuerpo}"
                es_oro, hits = analizar_texto(contexto_completo, palabras_clave, exclusiones)
                
                if es_oro:
                    oportunidades.append({
                        "objetivo": autor,
                        "dolor_detectado": hits,
                        "titulo": titulo,
                        "url": url_post,
                        "extracto": cuerpo[:200] + "..." if len(cuerpo) > 200 else cuerpo
                    })
                    nuevas_urls.append(url_post)
                    print(f"{GREEN}  🎯 ¡NUEVO ORO! Hit: {BOLD}{hits}{RESET}{GREEN} | {WHITE}{titulo[:50]}...{RESET}")
                    
        except Exception as e:
            print(f"{RED}X Anomalía de red durante el escaneo: {e}{RESET}")
            
        return oportunidades, nuevas_urls

    # --- EJECUCIÓN PRINCIPAL ---
    config = cargar_inteligencia()
    if not config: sys.exit(1)
    
    print(f"{CYAN}[+] Manifiesto táctico cargado con éxito.{RESET}")
    
    memoria_historica = cargar_memoria()
    print(f"{GRAY}[*] Memoria de estado inicializada ({len(memoria_historica)} registros previos).{RESET}\n")
    
    botin_total = []
    nuevas_entradas_memoria = []
    
    for objetivo in config.get('objetivos', []):
        resultados, urls_nuevas = infiltrar_reddit(
            objetivo, 
            config.get('palabras_clave_dolor', []), 
            config.get('filtros_exclusion', []), 
            memoria_historica
        )
        botin_total.extend(resultados)
        nuevas_entradas_memoria.extend(urls_nuevas)
        time.sleep(3) # Latencia para respetar los límites de la API
        
    print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
    if botin_total:
        with open(ARCHIVO_REPORTE, 'w', encoding='utf-8') as f:
            json.dump(botin_total, f, indent=4, ensure_ascii=False)
            
        # Actualización de memoria persistente
        guardar_memoria(memoria_historica + nuevas_entradas_memoria)
        
        print(f"{GREEN}✓ Operación finalizada. {BOLD}{len(botin_total)}{RESET}{GREEN} NUEVAS presas extraídas.{RESET}")
        print(f"{GREEN}✓ Memoria actualizada. Botín guardado en: {ARCHIVO_REPORTE}{RESET}")
    else:
        print(f"{YELLOW}! Radar limpio. No se detectaron anomalías nuevas en este ciclo.{RESET}")
    print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")

if __name__ == "__main__":
    iniciar_operacion_v2()
