import asyncio
import aiohttp
import os
from dotenv import load_dotenv

# --- INICIALIZACIÓN DE SEGURIDAD ---
load_dotenv()

# --- CÓDIGOS ANSI: TERMINAL ARCHITECT FERRARI ---
RED = '\033[91m'
WHITE = '\033[97m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

# 🔑 CREDENCIALES (Extracción segura)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    print(f"{RED}❌ [ERROR CRÍTICO] No se encontró TAVILY_API_KEY en el entorno (.env).{RESET}")
    print(f"{YELLOW}Asegúrate de configurar tus variables antes de iniciar el motor.{RESET}")
    exit(1)

async def investigar_dork(query):
    """Extracción de datos pura usando Tavily API (Modo Blindado)"""
    print(f"\n{RED}{BOLD}{'='*65}{RESET}")
    print(f"{WHITE}{BOLD}     🇺🇸 SYNERGY LABS: AGENTE SCIENTIST (NÚCLEO BLINDADO) 🇺🇸      {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    print(f"{RED}🔬 [SCIENTIST] Recibiendo directiva de búsqueda: {RESET}{query}")
    print(f"{CYAN}⚙️ [SISTEMA] Leyendo credenciales seguras. Iniciando enlace...{RESET}")
    
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "advanced",
        "include_answer": True,
        "max_results": 3
    }

    async with aiohttp.ClientSession() as session:
        print(f"{WHITE}🌐 [RED] Bypasseando buscadores comerciales. Conexión directa a API...{RESET}")
        async with session.post(url, json=payload) as response:
            if response.status == 200:
                print(f"{GREEN}✅ [ÉXITO] Datos extraídos en milisegundos. Desencriptando botín...{RESET}\n")
                data = await response.json()
                
                resultados = data.get("results", [])
                print(f"{RED}{BOLD}--- FUENTES DE EXTRACCIÓN (TOP 3) ---{RESET}")
                for i, res in enumerate(resultados, 1):
                    print(f"{WHITE}{i}. {res.get('title')}{RESET}")
                    print(f"{BLUE}   🔗 {res.get('url')}{RESET}")
                
                respuesta_directa = data.get("answer", "No se generó síntesis.")
                
                print(f"\n{CYAN}🔌 [SISTEMA] Cerrando enlace seguro...{RESET}")
                return respuesta_directa
            else:
                print(f"{RED}❌ [ERROR DE RED] Código de estado: {response.status}{RESET}")
                error_msg = await response.text()
                print(f"{YELLOW}Detalle: {error_msg}{RESET}")
                return "Fallo en la matriz de extracción."

# --- INTERFAZ INTERACTIVA DEL MOTOR ---
if __name__ == "__main__":
    print(f"\n{CYAN}{BOLD}📡 --- TERMINAL DE ENLACE SCIENTIST --- 📡{RESET}")
    
    objetivo_dinamico = input(f"{WHITE}🎯 Ingresa el Dork o tema a investigar: {RESET}").strip()
    
    if objetivo_dinamico:
        hipotesis_extraida = asyncio.run(investigar_dork(objetivo_dinamico))
        
        print(f"\n{GREEN}{BOLD}🏆 [REPORTE FINAL SCIENTIST]{RESET}")
        print(f"{WHITE}Hipótesis destilada. Lista para integración en pipeline:{RESET}")
        print(f"{YELLOW}> {hipotesis_extraida}{RESET}\n")
    else:
        print(f"{RED}⚠️ Directiva vacía. Abortando conexión.{RESET}")
