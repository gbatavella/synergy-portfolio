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
CYAN = "\033[96m"
WHITE = "\033[97m"

def iniciar_gestor_meta():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🌐 SYNERGY META GROUP ROUTER (LOCAL TARGETING DB) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # OPSEC: Permite abstraer el nombre del archivo vía entorno, o usar el por defecto
    nombre_archivo = os.getenv("META_GROUPS_DB", "mis_grupos.txt")
    print(f"{GRAY}[*] Inicializando motor de ingesta de datos locales...{RESET}")

    # Carga de datos profesional con protección de codificación
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                base_de_datos_meta = [linea.strip() for linea in archivo if linea.strip()]
            print(f"{GREEN}✓ Bóveda cargada. {len(base_de_datos_meta)} nodos indexados.{RESET}")
        except Exception as e:
            print(f"{RED}❌ [ERROR] Fallo al leer la bóveda: {e}{RESET}")
            sys.exit(1)
    else:
        print(f"{RED}❌ [ERROR CRÍTICO] No se encontró el archivo base: {nombre_archivo}{RESET}")
        sys.exit(1)

    def buscador_ingenieril(busqueda, ubicacion):
        # Algoritmo de captura por raíz semántica (4 caracteres)
        prefijo = busqueda[:4].lower()
        resultados = []
        for grupo in base_de_datos_meta:
            nombre_min = grupo.lower()
            # Filtro de ruido de metadatos de la plataforma
            if "última visita" in nombre_min:
                continue
            # Cruce de raíz semántica + Geofencing
            if prefijo in nombre_min and ubicacion.lower() in nombre_min:
                resultados.append(grupo)
        return resultados[:9]

    # --- Bucle REPL de Interfaz de Usuario ---
    while True:
        print(f"\n{GRAY}{'-'*65}{RESET}")
        que_buscas = input(f"{YELLOW}🎯 ¿Qué nicho buscas? (ej: Auto, Casa) o 'salir': {RESET}")
        
        if que_buscas.lower() in ['salir', 'exit', 'quit']:
            print(f"\n{GREEN}✅ Apagando Meta Group Router. ¡Buena caza!{RESET}\n")
            break
            
        donde = input(f"{YELLOW}📍 ¿En qué ubicación? (ej: Cordoba, Cañuelas): {RESET}")
        
        print(f"{GRAY}[*] Escaneando matriz de nodos en memoria RAM...{RESET}")
        mis_grupos = buscador_ingenieril(que_buscas, donde)
        
        if mis_grupos:
            print(f"\n{CYAN}💡 Encontré {len(mis_grupos)} zonas de impacto para despliegue táctico:{RESET}")
            for i, g in enumerate(mis_grupos, 1):
                print(f" {WHITE}{i}. {g}{RESET}")
        else:
            print(f"{RED}❌ Sin coincidencias. Amplía el radio geográfico o cambia la raíz de búsqueda.{RESET}")

if __name__ == "__main__":
    iniciar_gestor_meta()
