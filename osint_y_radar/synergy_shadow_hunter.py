import csv
import os
import time
import sys
from dotenv import load_dotenv

# --- SEGURIDAD Y CONFIGURACIÓN ---
load_dotenv()

# Variables de entorno para monetización (Protege tus endpoints de pago)
CRYPTO_WALLET = os.getenv("USDT_WALLET", "0x7ccF6f628b230241C223170e9402C58EeF0BB1e0")
PREMIUM_URL = os.getenv("PREMIUM_LICENSE_URL", "whop.com/synergy-labs")

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def rapid_output(text, delay=0.02):
    print(text)
    time.sleep(delay)

def generar_permutaciones(nombre_completo, dominio):
    partes = nombre_completo.lower().strip().split()
    if not partes:
        return []
    
    nombre = partes[0]
    apellido = partes[-1] if len(partes) > 1 else ""

    # Si solo hay un nombre sin apellido
    if not apellido:
        return [f"{nombre}@{dominio}"]

    # Algoritmos de alta probabilidad (Wall Street / Fortune 500)
    patrones = [
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
    return patrones

if __name__ == "__main__":
    print(f"\n{BLUE}{BOLD}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD} 🕵️‍♂️ SYNERGY: THE SHADOW HUNTER (CORPORATE PERMUTATOR) {RESET}")
    print(f"{BLUE}{BOLD}{'='*60}{RESET}\n")
    rapid_output(f"{GRAY}[*] Iniciando motor de permutaciones corporativas...{RESET}")

    # --- ENTRADA DINÁMICA DEL USUARIO ---
    dominio_objetivo = input(f"{YELLOW}🌐 Ingresa el dominio objetivo (ej. dresnerco.com): {RESET}").strip().lower()
    nombres_input = input(f"{YELLOW}🎯 Ingresa nombres clave separados por coma (ej. Andres Remezzano, John Kinney): {RESET}")

    # Procesar los nombres quitando espacios extra
    nombres = [n.strip() for n in nombres_input.split(",") if n.strip()]

    if not dominio_objetivo or not nombres:
        print(f"\n{RED}❌ Error: Faltan datos para iniciar la caza. Operación abortada.{RESET}")
    else:
        print(f"\n{GREEN}⚙️ Generando coordenadas de ataque para el dominio: {dominio_objetivo}{RESET}\n")
        
        resultados = []
        limite_alcanzado = False
        
        for nombre in nombres:
            if limite_alcanzado:
                break
                
            print(f"{GRAY}🔎 Combinaciones para [{nombre}]:{RESET}")
            correos = generar_permutaciones(nombre, dominio_objetivo)
            
            for correo in correos:
                # 1. El Limitador Freemium (Frena en 30 exactos)
                if len(resultados) >= 30:
                    limite_alcanzado = True
                    break
                    
                # Guardamos para el CSV
                resultados.append({"Nombre Original": nombre, "Email Sugerido": correo})
                # Mostramos en pantalla
                print(f"{BLUE}  [+] {correo}{RESET}")
                time.sleep(0.01)
                
            print(f"{GRAY}{'-' * 45}{RESET}")
            
            # 2. El Mensaje de Cobro / Gorra
            if limite_alcanzado:
                print(f"\n{RED}{BOLD}{'='*60}{RESET}")
                print(f"{RED}{BOLD} 🛑 LÍMITE DE VERSIÓN GRATUITA ALCANZADO (30 LEADS) 🛑{RESET}")
                print(f"{WHITE}Para extraer listados masivos sin límites y apoyar el código,")
                print(f"invítanos un café virtual en USDT (BEP20 / BSC):{RESET}")
                print(f"{GREEN}{BOLD}👉 {CRYPTO_WALLET}{RESET}")
                print(f"{WHITE}O adquiere la Licencia Elite en: {BLUE}{PREMIUM_URL}{RESET}")
                print(f"{RED}{BOLD}{'='*60}{RESET}")
                break 
        
        # --- EXPORTACIÓN AUTOMÁTICA A CSV ---
        nombre_archivo = f"botin_sombra_{dominio_objetivo.split('.')[0]}.csv"
        
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            campos = ["Nombre Original", "Email Sugerido"]
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
            
            escritor.writeheader()
            escritor.writerows(resultados)
            
        print(f"\n{GREEN}{BOLD}✅ Caza finalizada. El botín se ha exportado exitosamente a: {nombre_archivo}{RESET}")
        print(f"{GRAY}TIP: Abre el archivo .csv para copiar y pegar los correos en tu verificador masivo SMTP.{RESET}\n")
