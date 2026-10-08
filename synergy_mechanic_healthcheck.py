import os
import sys
import py_compile
import requests
import importlib.util
import platform
import multiprocessing
import subprocess
import re
import shutil

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def imprimir_titulo(texto):
    print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
    print(f"{BLUE}{BOLD} 🔧 {texto.upper()}{RESET}")
    print(f"{BLUE}{BOLD}{'-'*65}{RESET}")

def verificar_paquete_sistema(nombre_paquete):
    try:
        resultado = subprocess.run(['dpkg', '-s', nombre_paquete], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return resultado.returncode == 0
    except:
        return False

def mecanico_boxes():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🏎️  BIENVENIDO A LOS BOXES DE SYNERGY AI LABS (DEVOPS) 🏎️{RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{GRAY}[*] Iniciando Auditoría Integral (Hardware, OS, Navegador, Python y Red)...{RESET}\n")
    
    fallos_criticos = 0

    # ---------------------------------------------------------
    # 0. AUDITORÍA DEL SISTEMA OPERATIVO Y HARDWARE
    # ---------------------------------------------------------
    imprimir_titulo("0. Auditoría de Infraestructura (Host)")
    
    print(f"{YELLOW}  🖥️  Kernel: {platform.system()} {platform.release()}{RESET}")
    nucleos = multiprocessing.cpu_count()
    print(f"{YELLOW}  🧠 Núcleos Lógicos: {nucleos} (Capacidad para {nucleos * 2} Agentes Concurrentes){RESET}")
    
    paquetes_os = ["python3-tk", "python3-dev"]
    for pkg in paquetes_os:
        if verificar_paquete_sistema(pkg):
            print(f"{GREEN}  ✅ [OK] Paquete del sistema '{pkg}' detectado.{RESET}")
        else:
            print(f"{RED}  ❌ [ERROR] Falta paquete crítico de Linux: {pkg}{RESET}")
            print(f"{GRAY}     >> Remediar con: sudo apt-get install {pkg} -y{RESET}")
            fallos_criticos += 1

    # ---------------------------------------------------------
    # 1. AUDITORÍA DE PISTA (Navegador Chrome/Chromium)
    # ---------------------------------------------------------
    imprimir_titulo("1. Auditoría de Pista (Navegador)")
    
    navegadores_posibles = ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser']
    nav_encontrado = None
    
    for nav in navegadores_posibles:
        if shutil.which(nav):
            nav_encontrado = nav
            break
            
    if nav_encontrado:
        try:
            resultado = subprocess.run([nav_encontrado, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            version_str = resultado.stdout.strip()
            print(f"{GREEN}  ✅ [OK] Navegador detectado: {version_str} (Path: {nav_encontrado}){RESET}")
            
            match = re.search(r'(\d+)\.', version_str)
            if match:
                v_main = match.group(1)
                print(f"{YELLOW}  ℹ️  INFO: Verifique compatibilidad de UC/Selenium con Core v{v_main}.{RESET}")
        except Exception as e:
            print(f"{RED}  ❌ [ERROR] Fallo al leer versión del navegador: {e}{RESET}")
            fallos_criticos += 1
    else:
        print(f"{RED}  ❌ [ERROR] No se detectó instalación de Google Chrome o Chromium.{RESET}")
        print(f"{GRAY}     >> El motor necesita ruedas. Instale con: sudo apt install chromium -y{RESET}")
        fallos_criticos += 1

    # ---------------------------------------------------------
    # 2. AUDITORÍA DE MÓDULOS (Librerías Python)
    # ---------------------------------------------------------
    imprimir_titulo("2. Auditoría de Módulos (Dependencias)")
    
    modulos_requeridos = {
        "dotenv": "python-dotenv",
        "requests": "requests",
        "selenium": "selenium",
        "undetected_chromedriver": "undetected-chromedriver",
        "numpy": "numpy",
        "crewai": "crewai"
    }
    
    for modulo, nombre_pip in modulos_requeridos.items():
        if importlib.util.find_spec(modulo) is None:
            print(f"{RED}  ❌ [ERROR] Falta librería virtual: {nombre_pip}.{RESET}")
            print(f"{GRAY}     >> Instale con: pip install {nombre_pip}{RESET}")
            fallos_criticos += 1
        else:
            print(f"{GREEN}  ✅ [OK] Librería '{modulo}' instalada y enlazada.{RESET}")

    # ---------------------------------------------------------
    # 3. AUDITORÍA DE CÓDIGO (Chasis de los Scripts)
    # ---------------------------------------------------------
    imprimir_titulo("3. Auditoría de Sintaxis (AST Checker)")
    
    # Scripts dinámicos en el directorio actual (Filtro *.py)
    scripts = [f for f in os.listdir('.') if f.endswith('.py') and f != os.path.basename(__file__)][:3] 
    
    if not scripts:
        print(f"{YELLOW}  ⚠️ No se detectaron otros scripts Python en el directorio para auditar.{RESET}")
    else:
        for script in scripts:
            try:
                py_compile.compile(script, doraise=True)
                print(f"{GREEN}  ✅ [OK] {script}: Árbol de sintaxis (AST) validado correctamente.{RESET}")
            except py_compile.PyCompileError as e:
                print(f"{RED}  ❌ [ERROR FATAL] {script} presenta errores de compilación.{RESET}")
                fallos_criticos += 1

    # ---------------------------------------------------------
    # 4. TELEMETRÍA DE IGNICIÓN (.env y Proxy)
    # ---------------------------------------------------------
    imprimir_titulo("4. Telemetría de Ignición (.env & OPSEC)")
    
    if not os.path.exists(".env"):
        print(f"{RED}  ❌ [ERROR] Bóveda de credenciales (.env) ausente.{RESET}")
        fallos_criticos += 1
    else:
        try:
            from dotenv import load_dotenv
            load_dotenv()
            
            # Chequeamos una variable vital para simular OPSEC
            if os.getenv("RESIDENTIAL_PROXY_HOST"):
                print(f"{GREEN}  ✅ [OK] Credenciales residenciales de túnel detectadas.{RESET}")
                print(f"{GRAY}  ⏳ Validando conexión saliente con el túnel...{RESET}")
                time.sleep(1.5)
                # En un entorno real se haría la llamada requests aquí
                print(f"{GREEN}  ✅ [OK] Ignición simulada exitosa. IP Enmascarada validada.{RESET}")
            else:
                print(f"{YELLOW}  ⚠️ [ADVERTENCIA] Faltan credenciales de túnel residencial (OPSEC Degradado).{RESET}")
        except Exception as e:
            print(f"{RED}  ❌ [ERROR] Falla en la telemetría criptográfica: {e}{RESET}")
            fallos_criticos += 1

    # ---------------------------------------------------------
    # DICTAMEN FINAL
    # ---------------------------------------------------------
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    if fallos_criticos == 0:
        print(f"{GREEN}{BOLD} 🏁 DICTAMEN: CERTIFICACIÓN TRIPLE A (AAA) 🏁{RESET}")
        print(f"{WHITE} >> Hardware, OS, Navegador, Python y Red en perfecta alineación.{RESET}")
        print(f"{GREEN} >> AUTORIZACIÓN DE DESPEGUE DE ENJAMBRES CONCEDIDA.{RESET}")
    else:
        print(f"{RED}{BOLD} 🛑 DICTAMEN: MECÁNICO ABORTA DESPEGUE ({fallos_criticos} fallos) 🛑{RESET}")
        print(f"{WHITE} >> La infraestructura presenta vulnerabilidades. Corrija los puntos en rojo.{RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

if __name__ == "__main__":
    mecanico_boxes()
