import os
import sys
import re

# --- CÓDIGOS ANSI ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def inyectar_en_readme(numero, archivo, descripcion, id_categoria):
    ruta_readme = "../README.md"
    if not os.path.exists(ruta_readme):
        print(f"{RED}X Error: README.md no encontrado en la ruta ../{RESET}")
        sys.exit(1)

    with open(ruta_readme, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Mapeo exacto de las cabeceras de tu README
    categorias = {
        "5": "### 5. Agente Manager (agente_manager/)",
        "6": "### 6. Agentes Telegram (agentes_telegram/)",
        "7": "### 7. Outbound y Closers (outbound_y_closers/)",
        "8": "### 8. OSINT y Radar (osint_y_radar/)",
        "9": "### 9. DevOps y Core (devops_y_core/)",
        "10": "### 10. Black Ops (black_ops/)"
    }

    if id_categoria not in categorias:
        print(f"{RED}X Categoría inválida. Usa un número del 5 al 10.{RESET}")
        sys.exit(1)

    marcador_categoria = categorias[id_categoria]
    nueva_linea = f"* **{numero}. {archivo}**: {descripcion}\n"

    # Encontrar la categoría y añadir la línea al final de su bloque
    patron = re.compile(rf"({re.escape(marcador_categoria)}.*?(?=\n### |\n---))", re.DOTALL)
    
    if not patron.search(contenido):
        print(f"{RED}X No se encontró la sección '{marcador_categoria}' en el README.{RESET}")
        sys.exit(1)

    nuevo_contenido = patron.sub(lambda m: m.group(1).rstrip() + "\n" + nueva_linea + "\n", contenido)

    with open(ruta_readme, "w", encoding="utf-8") as f:
        f.write(nuevo_contenido)

    print(f"{GREEN}✓ Inyección exitosa: Motor {numero} añadido a la categoría {id_categoria}.{RESET}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(f"{YELLOW}Uso: python3 builder_readme.py <NUMERO> <ARCHIVO.PY> \"<DESCRIPCIÓN>\" <ID_CATEGORIA>{RESET}")
        print(f"{GRAY}Ejemplo: python3 builder_readme.py 104 nuevo_agente.py \"Synergy Agent. Hace X.\" 6{RESET}")
        sys.exit(1)

    _, num, arc, desc, cat = sys.argv
    inyectar_en_readme(num, arc, desc, cat)
