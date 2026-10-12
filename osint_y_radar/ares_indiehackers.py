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

def escanear_indiehackers():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} SYNERGY ARES INDIEHACKERS (BOOTSTRAPPER OSINT RADAR) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    # Evasión de Capa 7: Spoofing de identidad de navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    # Endpoint de la sección de Growth
    url_ih = "https://www.indiehackers.com/api/groups/growth/posts" 
    
    print(f"{GRAY}[*] Iniciando enlace HTTP con enmascaramiento de User-Agent...{RESET}")
    
    try:
        respuesta = requests.get(url_ih, headers=headers, timeout=10)
        
        if respuesta.status_code != 200:
            print(f"{RED}X [ACCESO DENEGADO] La plataforma está protegiendo sus datos (HTTP {respuesta.status_code}).{RESET}\n")
            sys.exit(1)
            
        posts = respuesta.json()
        botin = []
        
        print(f"{GREEN}[+] Enlace establecido. Escaneando la matriz de IndieHackers en tiempo real...{RESET}\n")
        
        for post in posts:
            # Concatenación defensiva (title + body)
            texto = (post.get('title', '') + " " + post.get('body', '')).lower()
            
            # Escáner heurístico de dolor
            hits = [kw for kw in KEYWORDS if kw in texto]
            
            if hits:
                item = {
                    "plataforma": "IndieHackers",
                    "dolor": hits,
                    "titulo": post.get('title', ''),
                    "url": f"https://www.indiehackers.com/post/{post.get('id', '')}"
                }
                botin.append(item)
                print(f"{GREEN}  🎯 ¡ORO EN IH! Hit: {BOLD}{hits}{RESET}{GREEN} | {WHITE}{item['titulo'][:60]}...{RESET}")
                
        if botin:
            archivo = f"Botin_IH_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.json"
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(botin, f, indent=4, ensure_ascii=False)
                
            print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
            print(f"{GREEN}✓ Extracción completada. {len(botin)} presas de alto valor aseguradas en: {archivo}{RESET}")
            print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")
        else:
            print(f"\n{YELLOW}! Radar limpio en IndieHackers. Sin anomalías detectadas en este ciclo.{RESET}\n")
            
    except requests.exceptions.RequestException as e:
        print(f"\n{RED}X Falla estructural al contactar con el endpoint: {e}{RESET}\n")
    except json.JSONDecodeError:
        print(f"\n{RED}X El servidor devolvió HTML en lugar de JSON. Posible bloqueo por WAF (Cloudflare).{RESET}\n")

if __name__ == "__main__":
    escanear_indiehackers()
