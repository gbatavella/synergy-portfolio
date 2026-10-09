import os
import re
import sys
import time

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def recalibrar_nucleo():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🔧 SYNERGY FAWKES CALIBRATOR (SOURCE CODE HOTFIX) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    print(f"{YELLOW}🔥 Iniciando protocolo de reparación autónoma (Self-Healing)...{RESET}")
    
    try:
        # Importación dinámica para localizar la ruta del paquete
        import fawkes
        fawkes_dir = os.path.dirname(fawkes.__file__)
    except ImportError:
        print(f"{RED}❌ [ERROR] La librería 'fawkes' no está instalada en este entorno virtual.{RESET}")
        print(f"{GRAY}>> Ejecute: pip install fawkes{RESET}\n")
        sys.exit(1)

    print(f"{GRAY}🔍 Escaneando directorio dinámico de dependencias:{RESET} {BOLD}{fawkes_dir}{RESET}\n")
    time.sleep(1)

    parche_aplicado = False

    # Escaneo profundo del árbol de directorios de la librería
    for root, dirs, files in os.walk(fawkes_dir):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Patrón de detección de la falla (MTCNN backward compatibility break)
                    if "min_face_size" in content and "MTCNN" in content:
                        print(f"{CYAN}⚙️ Falla estructural detectada en: {BOLD}{file}{RESET}")
                        print(f"{GRAY}   ↳ Aplicando mutación quirúrgica mediante Regex...{RESET}")
                        
                        # Expresión regular para extirpar el argumento defectuoso sin romper la sintaxis
                        content_patched = re.sub(r'min_face_size\s*=\s*[0-9A-Za-z_]+,?\s*', '', content)
                        
                        # Guardado del parche directamente en el código fuente de la librería
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content_patched)
                            
                        print(f"   {GREEN}✅ Código recalibrado con éxito en: {filepath}{RESET}")
                        parche_aplicado = True
                        time.sleep(0.5)
                        
                except PermissionError:
                    print(f"\n{RED}❌ [DENEGADO] Permisos insuficientes para modificar dependencias.{RESET}")
                    print(f"{GRAY}>> Vuelva a ejecutar el calibrador con privilegios de administrador (sudo).{RESET}\n")
                    sys.exit(1)
                except Exception as e:
                    print(f"   {RED}❌ Fricción al leer {file}: {e}{RESET}")

    print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
    if parche_aplicado:
        print(f"{GREEN}{BOLD}🚀 ¡PROTOCOLO COMPLETADO! Fawkes ha sido parcheado estructuralmente.{RESET}")
        print(f"{GRAY}>> El motor biométrico está listo para operar sin colapsos.{RESET}\n")
    else:
        print(f"{GREEN}{BOLD}✔️ SISTEMA ESTABLE.{RESET} {YELLOW}No se encontraron vectores defectuosos.{RESET}")
        print(f"{GRAY}>> La matriz ya se encuentra parcheada o la dependencia fue actualizada por el autor.{RESET}\n")

if __name__ == "__main__":
    recalibrar_nucleo()
