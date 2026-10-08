import csv
import os
import time
import sys
from dotenv import load_dotenv

# =======================================================
# CONFIGURACIÓN SYNERGY LABS - VERSIÓN LITE (RECON EDITION)
# =======================================================
load_dotenv()

MAX_LEADS_LITE = 5
# Protege el enlace de tu pasarela de pago o landing page
LINK_DE_COMPRA = os.getenv("PRO_LICENSE_URL", "https://whop.com/synergy-labs/")

# Colores corporativos para la terminal
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def efecto_tipeo(texto, retraso=0.015):
    """Genera el efecto visual de escritura en la terminal."""
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(retraso)
    print()

def generar_permutaciones(nombre_completo, dominio):
    partes = nombre_completo.lower().strip().split()
    if not partes:
        return []
    nombre = partes[0]
    apellido = partes[-1] if len(partes) > 1 else ""

    if not apellido:
        return [f"{nombre}@{dominio}"]

    return [
        f"{nombre}@{dominio}",
        f"{nombre}{apellido}@{dominio}",
        f"{nombre}.{apellido}@{dominio}",
        f"{nombre[0]}{apellido}@{dominio}",
        f"{nombre[0]}.{apellido}@{dominio}",
        f"{nombre}_{apellido}@{dominio}",
        f"{nombre}{apellido[0]}@{dominio}",
        f"{apellido}{nombre}@{dominio}",
        f"{apellido}.{nombre}@{dominio}",
        f"{apellido}@{dominio}"
    ]

def ejecutar_shadow_hunter_lite():
    print(f"\n{CYAN}{BOLD}================================================={RESET}")
    print(f"{CYAN}{BOLD}  SHADOW HUNTER : RECON EDITION (LITE) - SYNERGY {RESET}")
    print(f"{CYAN}{BOLD}================================================={RESET}\n")
    
    efecto_tipeo(f"{YELLOW}[SISTEMA] Iniciando motor de permutaciones corporativas...{RESET}")
    time.sleep(0.5)
    
    dominio_objetivo = input(f"\n{GREEN}🌐 V8-Core:~ $ Ingresa el dominio objetivo (ej. dresnerco.com): {RESET}").strip().lower()
    nombres_input = input(f"{GREEN}🎯 V8-Core:~ $ Ingresa nombres clave (ej. Andres Remezzano): {RESET}")
    
    nombres = [n.strip() for n in nombres_input.split(",") if n.strip()]

    if not dominio_objetivo or not nombres:
        print(f"\n{RED}❌ Error: Faltan datos para iniciar la caza. Operación abortada.{RESET}")
        return

    print(f"\n{CYAN}⚙️ Generando coordenadas de ataque para el dominio: {dominio_objetivo}{RESET}\n")
    time.sleep(1)
    
    resultados = []
    leads_encontrados = 0
    limite_alcanzado = False
    
    for nombre in nombres:
        if limite_alcanzado:
            break
            
        print(f"{BOLD}🔎 Combinaciones para [{nombre}]:{RESET}")
        correos = generar_permutaciones(nombre, dominio_objetivo)
        
        for correo in correos:
            if leads_encontrados >= MAX_LEADS_LITE:
                limite_alcanzado = True
                break
                
            # Guardamos para el CSV
            resultados.append({"Nombre Original": nombre, "Email Sugerido": correo})
            leads_encontrados += 1
            print(f"  {GREEN}[+]{RESET} {correo}")
            time.sleep(0.2) # Efecto de procesamiento asíncrono
            
        print("-" * 35)
    
    # --- EXPORTACIÓN AUTOMÁTICA A CSV ---
    nombre_archivo = f"botin_sombra_LITE_{dominio_objetivo.split('.')[0]}.csv"
    
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        campos = ["Nombre Original", "Email Sugerido"]
        escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)
        
    print(f"\n{GREEN}✅ Caza finalizada. El botín de muestra se ha exportado a: {nombre_archivo}{RESET}")

    # --- EL CHOQUE COMERCIAL (Fricción Natural) ---
    print(f"\n{RED}{BOLD}============================================================{RESET}")
    efecto_tipeo(f"{RED}[ALERTA DE SISTEMA] LÍMITE DE VERSIÓN LITE ALCANZADO.{RESET}")
    print(f"{RED}{BOLD}============================================================{RESET}")
    print(f"{YELLOW}El motor ha extraído {MAX_LEADS_LITE} correos permutados de muestra exitosamente.{RESET}")
    print(f"{CYAN}Para generar permutaciones ilimitadas, procesar listas masivas{RESET}")
    print(f"{CYAN}y acceder al código fuente abierto, adquiere la Licencia Pro en:{RESET}")
    print(f"{BOLD}{LINK_DE_COMPRA}{RESET}\n")

if __name__ == "__main__":
    try:
        ejecutar_shadow_hunter_lite()
    except KeyboardInterrupt:
        print(f"\n\n{RED}Protocolo abortado por el usuario.{RESET}")
        sys.exit()
