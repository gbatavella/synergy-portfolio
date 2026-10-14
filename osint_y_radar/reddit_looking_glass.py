import sys
try:
    from duckduckgo_search import DDGS
except ImportError:
    print("❌ Error: Falta la librería. Ejecuta: pip install duckduckgo-search --break-system-packages")
    sys.exit(1)

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def escanear_foros(palabra_clave):
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🕵️‍♂️ SYNERGY LOOKING GLASS (OSINT REDDIT CAPTADOR) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    print(f"{GRAY}[*] Antenas desplegadas. Looking Glass encendido.{RESET}")
    print(f"{GRAY}[*] Buscando corderos con el dolor: {WHITE}'{palabra_clave}'{GRAY}...{RESET}\n")
    
    try:
        radar = DDGS()
        busqueda_exacta = f'{palabra_clave} site:reddit.com'
        
        # Extraemos los resultados limitados a 5
        resultados = list(radar.text(busqueda_exacta, max_results=5))

        if not resultados:
            print(f"{YELLOW}🛑 La red está vacía. Prueba otra carnada o cambia el dolor.{RESET}\n")
            return

        for i, prospecto in enumerate(resultados, 1):
            print(f"{GREEN}{BOLD}🚨 CORDERO DETECTADO #{i}{RESET}")
            print(f"{BLUE}🏷️ Título:{RESET} {WHITE}{prospecto.get('title')}{RESET}")
            print(f"{YELLOW}🗣️ Dolor:{RESET} {WHITE}{prospecto.get('body')[:200]}...{RESET}") # Truncamos a 200 caracteres para no desbordar pantalla
            print(f"{GRAY}🔗 Enlace:{RESET} {WHITE}{prospecto.get('href')}{RESET}\n")
            print(f"{GRAY}{'-' * 65}{RESET}\n")
            
    except Exception as e:
        print(f"{RED}❌ Fricción en la Looking Glass:{RESET} {e}")

if __name__ == "__main__":
    # Puedes cambiar el dolor a buscar aquí
    dolor_a_buscar = 'no puedo vender mi producto digital'
    escanear_foros(dolor_a_buscar)
