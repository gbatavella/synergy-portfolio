# =====================================================================
# SYNERGY LABS: CEREBRO DE MISIONES B2C (OMNI-NICHE PAYLOAD)
# Objetivo: Centralización de Vectores de Asalto para Liquidación B2C
# =====================================================================

MISIONES = {
    "sw4": {
        "url_coto": "https://www.facebook.com/groups/1087114374978242/",
        "keywords": [r"busco sw4", r"compro toyota", r"necesito camioneta", r"busco camioneta", r"hilux srv usada", r"dueño directo"],
        "excluir": [r"vendo", r"agencia", r"permuto", r"concesionaria", r"ofrezco"],
        "copy": "Hola, vi que buscás una SW4. Tengo una 3.0 radicada en Cañuelas, impecable. Soy segundo dueño, lista para transferir. Te paso un video donde muestro el motor encendido, el exterior impecable, la apertura de puertas, el tablero y todo el interior desde todos los ángulos. Cero vueltas."
    },
    "fitness": {
        "url_coto": "https://www.facebook.com/groups/compraventafitnessargentina",
        "keywords": [r"aparato gimnasia", r"tonificador", r"clases step", r"gym casa", r"entrenamiento integral", r"aparato musculación"],
        "excluir": [r"vendo", r"clase zumba", r"suplementos", r"proteina", r"ofrezco"],
        "copy": "Hola, tengo el entrenador integral Body Fitness que te tonifica todo el cuerpo (incluidas piernas). Viene con el CD/video de clases de Step guiadas, ideal para entrenar en casa con método profesional. Si te sirve para tu espacio, escribime."
    },
    "tech": {
        "url_coto": "https://www.facebook.com/groups/compraventatecnologiacba",
        "keywords": [r"compro impresora", r"impresora wifi barata", r"samsung m2020w", r"impresora para estudio", r"impresora l[aá]ser"],
        "excluir": [r"vendo", r"cartuchos", r"reparacion", r"toner vacio", r"ofrezco", r"servicio tecnico"],
        "copy": "Vi que buscás impresora. Tengo la Samsung Xpress M2020W LÁSER con Wi-Fi. Ideal para imprimir volúmenes altos súper rápido y con tóner económico. Está como nueva, te paso fotos si te interesa."
    },
    "moda": {
        "url_coto": "https://www.facebook.com/groups/ropademarcaargentina",
        "keywords": [r"campera cuero xl", r"ropa guess original", r"campera napalan", r"cuero importado", r"busco campera xl"],
        "excluir": [r"vendo", r"zapatillas", r"imitacion", r"replica", r"ofrezco", r"mayorista"],
        "copy": "Hola, tengo una campera Guess de cuero Napalan legítimo, talle XL. Está impecable, calidad premium difícil de conseguir acá. Si buscás algo así de marca original, avisame y te paso medidas."
    }
}

# --- RUTINA DE DIAGNÓSTICO (Solo se ejecuta si se llama al archivo directamente) ---
if __name__ == "__main__":
    BLUE = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    GRAY = "\033[90m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    WHITE = "\033[97m"
    
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧠 SYNERGY OMNI-NICHE PAYLOAD (B2C MATRIX) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    print(f"{GREEN}[+] Bóveda central sincronizada. {len(MISIONES)} frentes de ataque activos.{RESET}\n")
    
    for mision, datos in MISIONES.items():
        print(f"{CYAN}🎯 NODO ESTRATÉGICO:{RESET} {WHITE}{BOLD}{mision.upper()}{RESET}")
        print(f"{GRAY}   ↳ Coto de Caza:{RESET} {datos['url_coto']}")
        print(f"{GRAY}   ↳ Firma Regex (Triggers):{RESET} {len(datos['keywords'])} patrones")
        print(f"{GRAY}   ↳ Escudos Anti-Ruido:{RESET} {len(datos['excluir'])} patrones")
        print(f"{GRAY}   ↳ Longitud del Payload:{RESET} {len(datos['copy'])} caracteres\n")
    
    print(f"{GRAY}>> Modulo listo para ser orquestado por el radar de Playwright.{RESET}\n")
