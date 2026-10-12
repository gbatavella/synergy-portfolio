import requests
import json
import os
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

# Matrices de Dolor B2B/SaaS
KEYWORDS = ["conversion", "pricing", "stripe", "india", "latam", "purchasing power", "sales dropped", "churn"]

def escanear_hacker_news():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} SYNERGY ARES HACKER NEWS (Y COMBINATOR OSINT RADAR) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    # Endpoint de Firebase oficial de HN
    url_top = "https://hacker-news.firebaseio.com/v0/newstories.json"
    
    print(f"{GRAY}[*] Conectando a los servidores centrales de Hacker News (Firebase API)...{RESET}")
    
    try:
        respuesta = requests.get(url_top, timeout=10)
        
        if respuesta.status_code != 200:
            print(f"{RED}X [ERROR DE RED] Fricción al conectar con la API de HN (HTTP {respuesta.status_code}).{RESET}\n")
            sys.exit(1)
            
        # Extracción del lote de IDs más recientes
        ids_posts = respuesta.json()[:100] 
        botin = []
        
        print(f"{GREEN}[+] Enlace establecido. Escaneando {BOLD}{len(ids_posts)}{RESET}{GREEN} hilos técnicos en tiempo real...{RESET}\n")
        
        for post_id in ids_posts:
            url_post = f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json"
            
            try:
                post_data = requests.get(url_post, timeout=10).json()
            except requests.exceptions.RequestException:
                continue # Ignorar latencias individuales y seguir avanzando
            
            if not post_data or 'title' not in post_data: 
                continue
                
            texto_completo = (post_data.get('title', '') + " " + post_data.get('text', '')).lower()
            
            # Escáner heurístico de dolor
            hits = [kw for kw in KEYWORDS if kw in texto_completo]
            
            if hits:
                item = {
                    "plataforma": "Hacker News",
                    "dolor": hits,
                    "titulo": post_data.get('title', ''),
                    "url": f"https://news.ycombinator.com/item?id={post_id}"
                }
                botin.append(item)
                print(f"{GREEN}  🎯 ¡ORO EN HN! Hit: {BOLD}{hits}{RESET}{GREEN} | {WHITE}{item['titulo'][:60]}...{RESET}")
                
        if botin:
            archivo = f"Botin_HN_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.json"
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(botin, f, indent=4, ensure_ascii=False)
                
            print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
            print(f"{GREEN}✓ Extracción completada. {len(botin)} presas de alto valor aseguradas en: {archivo}{RESET}")
            print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")
        else:
            print(f"\n{YELLOW}! Radar limpio en Hacker News. Sin anomalías detectadas en este ciclo.{RESET}\n")
            
    except requests.exceptions.RequestException as e:
        print(f"\n{RED}X Falla estructural al contactar con Firebase: {e}{RESET}\n")

if __name__ == "__main__":
    escanear_hacker_news()
