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

def iniciar_depuracion_v3():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧠 SYNERGY DATA CLEANSER V3.1 (SELF-LEARNING HEURISTICS) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    ARCHIVO_DOMINIOS = "blacklist_dominios.txt"
    ARCHIVO_DEMONIOS = "blacklist_demonios.txt"
    ROLES_GENERICOS = ["admin", "info", "support", "contact", "sales", "hello", "test", "webmaster", "marketing"]

    # 🛡️ EL CHALECO ANTIBALAS DE LA IA (Whitelist)
    DOMINIOS_INTOCABLES = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "proton.me", "icloud.com", "live.com"]

    def cargar_lista(archivo):
        """Lee y normaliza el archivo plano en un Set estructurado."""
        if os.path.exists(archivo):
            with open(archivo, "r", encoding="utf-8") as f:
                return set(linea.strip().lower() for linea in f if linea.strip())
        return set()

    def agregar_a_lista(archivo, item, lista_cargada):
        """Inyecta un nuevo registro a la base de datos en tiempo de ejecución."""
        if item not in lista_cargada:
            with open(archivo, "a", encoding="utf-8") as f:
                f.write(item + "\n")
            lista_cargada.add(item)
            return True
        return False

    def procesar_botin(archivo_csv):
        print(f"{GRAY}[*] Iniciando escrutinio algorítmico profundo en: {BOLD}{archivo_csv}{RESET}")
        
        # Carga de Bóvedas de Inteligencia Histórica
        dominios_prohibidos = cargar_lista(ARCHIVO_DOMINIOS)
        demonios_conocidos = cargar_lista(ARCHIVO_DEMONIOS)
        
        # Inyección de Exclusión Manual (Hardcoded Target)
        target_aislado = "lispaydaypro@gmail.com"
        if agregar_a_lista(ARCHIVO_DEMONIOS, target_aislado, demonios_conocidos):
            print(f"{RED}🎯 Objetivo hostil priorizado (Manual Injection): {target_aislado}{RESET}")

        try:
            df = pd.read_csv(archivo_csv)
            # Resolución dinámica de la columna (Case-insensitive)
            col_email = next((col for col in df.columns if col.lower() == 'email'), None)
            
            if not col_email:
                print(f"\n{RED}❌ [ERROR CRÍTICO] La matriz de datos carece de la columna 'Email'.{RESET}\n")
                return

            total_original = len(df)
            demonios_cazados = []
            indices_validos = []

            print(f"{YELLOW}⏳ Aplicando matrices heurísticas y escudos de auto-aprendizaje a {total_original} registros...{RESET}\n")

            # Bucle de Auditoría Heurística
            for index, row in df.iterrows():
                correo = str(row[col_email]).lower().strip()
                
                # 1. Filtro Estructural Básico (RFC)
                if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
                    demonios_cazados.append(f"{correo} [Razón: Estructura Inválida]")
                    continue
                    
                usuario, dominio = correo.split('@', 1)
                es_valido = True
                razon_bloqueo = ""

                # 2. Filtro de Bóveda: Individuos Restringidos
                if correo in demonios_conocidos:
                    es_valido = False
                    razon_bloqueo = "Target en Blacklist Específica"
                    
                # 3. Filtro de Bóveda: Corporaciones Restringidas
                elif dominio in dominios_prohibidos:
                    es_valido = False
                    razon_bloqueo = "Dominio en Blacklist Global"
                    
                # 4. Inteligencia Táctica (Sentido Común + Auto-Aprendizaje)
                elif len(usuario) < 4 or usuario in ROLES_GENERICOS:
                    es_valido = False
                    razon_bloqueo = "Rol Genérico o Sospechoso"
                    
                    # 🛡️ PARCHE DE SEGURIDAD V3.1 (Aislamiento de Chaleco Antibalas)
                    if dominio not in DOMINIOS_INTOCABLES:
                        if agregar_a_lista(ARCHIVO_DOMINIOS, dominio, dominios_prohibidos):
                            print(f"{CYAN} ⚡ [AUTO-LEARNING] Nueva amenaza corporativa aprendida y bloqueada: {BOLD}{dominio}{RESET}")

                if es_valido:
                    indices_validos.append(index)
                else:
                    demonios_cazados.append(f"{correo} [Razón: {razon_bloqueo}]")

            # Extracción del Botín Validado (Matriz Filtrada)
            df_limpio = df.loc[indices_validos]
            archivo_salida = archivo_csv.replace(".csv", "_V3_puro.csv")
            df_limpio.to_csv(archivo_salida, index=False)
            
            # Generación Forense (Reporte de Exclusión)
            archivo_informe = archivo_csv.replace(".csv", "_REPORTE_DEMONIOS.txt")
            with open(archivo_informe, "w", encoding="utf-8") as f:
                f.write("--- SYNERGY AI: REPORTE FORENSE DE DEMONIOS CAZADOS ---\n\n")
                for demonio in demonios_cazados:
                    f.write(f"- {demonio}\n")

            print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
            print(f"{GREEN}{BOLD} ✅ PROTOCOLO DE AUTO-APRENDIZAJE COMPLETADO.{RESET}")
            print(f"{GRAY} 📊 Originales Ingestados: {total_original}{RESET}")
            print(f"{RED} 🗑️ Amenazas / Trampas purgadas: {len(demonios_cazados)}{RESET}")
            print(f"{GREEN} 💎 Botín de High-Ticket (Puro): {len(df_limpio)}{RESET}")
            print(f"{BLUE} 📝 Inteligencia forense compilada en: {archivo_informe}{RESET}")
            print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")

        except Exception as e:
            print(f"\n{RED}❌ Falla crítica en la infraestructura de refinería: {e}{RESET}\n")

    # Inicialización de Flujo
    archivo = input(f"{YELLOW}📁 Ingresa la ruta del archivo de inteligencia a depurar: {RESET}").strip()
    
    if os.path.exists(archivo):
        procesar_botin(archivo)
    else:
        print(f"\n{RED}❌ [ERROR DE ARCHIVO] Ruta no encontrada en el perímetro local.{RESET}\n")

if __name__ == "__main__":
    iniciar_depuracion_v3()
