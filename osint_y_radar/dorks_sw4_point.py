# =====================================================================
# SYNERGY LABS: PAYLOAD DE INTELIGENCIA (DORKS MATRIX)
# =====================================================================
# Módulo inyectable para motores OSINT. 
# Misión Logística: Ruta del Interior a Zona Sur PBA (Evitando CABA)
# =====================================================================

DORKS = [
    # 1. Dorks apuntando directo al centro de operaciones logísticas
    'site:facebook.com/groups ("necesito flete" OR "necesito mudanza" OR "presupuesto mudanza") ("Mina Clavero" OR "San Luis" OR "Merlo") ("Cañuelas" OR "Provincia de Buenos Aires" OR "Zona Sur") -ofrezco',
    
    # 2. Búsquedas de encomiendas, cargas menores y paquetería
    'site:facebook.com/groups "alguien viaja para" ("Cañuelas" OR "San Miguel del Monte" OR "Ezeiza") ("llevar una caja" OR "encomienda") ("Villa de las Rosas" OR "Traslasierra") -viajo',
    
    # 3. Retornos: Mudanzas desde la provincia hacia el interior (Consolidación de carga)
    'site:facebook.com/groups ("necesito mudanza" OR "busco flete") ("Cañuelas" OR "Lobos" OR "PBA") ("San Luis" OR "Córdoba") -viajo',
    
    # 4. Rutas transversales de media distancia
    'site:facebook.com/groups "flete" ("Junín" OR "La Carlota") "Cañuelas" -ofrezco'
]

# --- RUTINA DE VERIFICACIÓN (Solo se ejecuta si se llama al archivo directamente) ---
if __name__ == "__main__":
    BLUE = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    
    print(f"\n{BLUE}{BOLD}📡 SYNERGY TARGETING MATRIX (LOGISTICS PAYLOAD){RESET}")
    print(f"{GREEN}[+] Módulo de inteligencia cargado. {len(DORKS)} vectores de asalto configurados.{RESET}\n")
    
    for i, dork in enumerate(DORKS, 1):
        print(f"{YELLOW}   Vect-{i}:{RESET} {dork}")
    
    print(f"\n{GRAY}>> Listo para ser importado por el motor OSINT principal.{RESET}\n")
