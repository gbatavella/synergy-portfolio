import pandas as pd
import re
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

def iniciar_refineria():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧹 SYNERGY LEAD REFINER (HEURISTIC DATA CLEANSER V3) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    ARCHIVO_BLACKLIST = "blacklist_dominios.txt"
    ROLES_GENERICOS = ["admin", "info", "support", "contact", "sales", "hello", "test", "webmaster", "marketing"]

    # Auto-creación de Blacklist si no existe para evitar crashes
    if not os.path.exists(ARCHIVO_BLACKLIST):
        with open(ARCHIVO_BLACKLIST, "w") as f:
            f.write("dominio-enemigo.com\nspam-trap.org\n")
        print(f"{GRAY}[*] Archivo '{ARCHIVO_BLACKLIST}' generado por defecto.{RESET}")

    def cargar_blacklist_global():
        """Carga y normaliza el manifiesto de dominios prohibidos."""
        if os.path.exists(ARCHIVO_BLACKLIST):
            with open(ARCHIVO_BLACKLIST, "r", encoding="utf-8") as f:
                return [linea.strip().lower() for linea in f if linea.strip()]
        return []

    def es_correo_valido(correo, blacklist_dominios):
        """Filtro heurístico de 4 capas para validación de prospectos."""
        if not isinstance(correo, str):
            return False
            
        correo = correo.lower().strip()
        
        # 1. Filtro Estructural: Formato RFC básico
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            return False
            
        usuario, dominio = correo.split('@', 1)
        
        # 2. Heurística de Longitud: Correos demasiado cortos (ej. me@)
        if len(usuario) < 4:
            return False
            
        # 3. Heurística de Rol: Departamentos genéricos sin poder de decisión
        if usuario in ROLES_GENERICOS:
            return False
            
        # 4. Inteligencia de Red: Dominios en Lista Negra
        if dominio in blacklist_dominios:
            return False
            
        return True

    def refinar_botin(archivo_csv):
        print(f"{GRAY}[*] Iniciando proceso de refinamiento algorítmico en: {BOLD}{archivo_csv}{RESET}")
        
        blacklist = cargar_blacklist_global()
        print(f"{CYAN} ↳ Cargada Lista Negra Global ({len(blacklist)} dominios restringidos).{RESET}\n")
        
        try:
            df = pd.read_csv(archivo_csv)
            
            # Mapeo dinámico de columna (Agnóstico a mayúsculas/minúsculas)
            col_email = next((col for col in df.columns if col.lower() == 'email'), None)
            
            if not col_email:
                print(f"{RED}❌ [ERROR CRÍTICO] No se detectó columna de 'Email' en la matriz CSV.{RESET}\n")
                return

            total_original = len(df)
            print(f"{YELLOW}⏳ Aplicando filtros heurísticos y limpieza vectorial a {total_original} registros...{RESET}")
            
            # Ejecución de purga por función Lambda
            df_limpio = df[df[col_email].apply(lambda x: es_correo_valido(x, blacklist))]
            
            total_limpio = len(df_limpio)
            basura_eliminada = total_original - total_limpio
            
            # Serialización
            archivo_salida = archivo_csv.replace(".csv", "_V3_limpio.csv")
            df_limpio.to_csv(archivo_salida, index=False)
            
            print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
            print(f"{GREEN}{BOLD} ✅ REFINAMIENTO COMPLETADO CON ÉXITO.{RESET}")
            print(f"{GRAY} 📊 Registros Ingestados: {total_original}{RESET}")
            print(f"{RED} 🗑️ Basura/Trampas purgadas: {basura_eliminada}{RESET}")
            print(f"{GREEN} 💎 Botín Puro (High-Ticket) guardado en: {archivo_salida}{RESET}")
            print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")

        except Exception as e:
            print(f"\n{RED}❌ Falla estructural en la refinería de datos: {e}{RESET}\n")

    # Bucle de Interacción Principal
    archivo = input(f"{YELLOW}📁 Ingresa el archivo de inteligencia a depurar (ej. botin_ares.csv): {RESET}").strip()
    
    if os.path.exists(archivo):
        refinar_botin(archivo)
    else:
        print(f"\n{RED}❌ [ERROR DE SISTEMA] Archivo '{archivo}' no detectado en el perímetro local.{RESET}\n")

if __name__ == "__main__":
    iniciar_refineria()
