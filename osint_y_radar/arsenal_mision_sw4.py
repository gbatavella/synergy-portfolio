# =====================================================================
# SYNERGY LABS: CEREBRO DE MISIÓN AISLADA B2C (PAYLOAD)
# Objetivo: Extracción y Contacto para Venta de Vehículo (Red Ampliada)
# =====================================================================

MISIONES = {
    "sw4": {
        "url_coto": "https://www.facebook.com/groups/1087114374978242/",
        
        "keywords": [
            "busco sw4", "compro toyota", "necesito camioneta", "busco camioneta", 
            "hilux srv usada", "dueño directo", "precio", "cuanto pedis", 
            "me interesa", "info", "te sirve permuta", "detalles"
        ],
        
        # Filtro heurístico estricto contra intermediarios y competidores
        "excluir": [
            "vendo", "agencia", "permuto", "concesionaria", "ofrezco"
        ],
        
        # Munición de contacto (Outbound Copy)
        "copy": "Hola, vi que buscás una SW4. Tengo una 3.0 radicada en Cañuelas, impecable. Soy segundo dueño, lista para transferir. Te paso un video donde muestro el motor encendido, el exterior impecable, la apertura de puertas..."
    }
}

# --- RUTINA DE VERIFICACIÓN (Solo se ejecuta si se llama al archivo directamente) ---
if __name__ == "__main__":
    # Códigos ANSI para telemetría visual
    BLUE = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    
    print(f"\n{BLUE}{BOLD}📡 SYNERGY B2C TARGETING MATRIX (SW4 SNIPER PAYLOAD){RESET}")
    print(f"{GREEN}[+] Matriz de misión cargada en memoria.{RESET}\n")
    
    for mision, datos in MISIONES.items():
        print(f"{YELLOW}   🎯 Misión Activa:{RESET} {mision.upper()}")
        print(f"      - Coto de Caza: {datos['url_coto']}")
        print(f"      - Vectores de Ataque: {len(datos['keywords'])} keywords")
        print(f"      - Filtros de Exclusión: {len(datos['excluir'])} keywords")
        print(f"      - Copy Cargado: Sí ({len(datos['copy'])} caracteres)\n")
    
    print(f"\n{GRAY}>> Bóveda lista para ser importada por los motores de extracción.{RESET}\n")
