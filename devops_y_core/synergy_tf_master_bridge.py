import sys
import time
import os
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def estabilizar_matriz_tf():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🌉 SYNERGY TF MASTER BRIDGE (KERAS MONKEY PATCH) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")
    
    print(f"{GRAY}[*] Analizando integridad del espacio de nombres (Namespaces)...{RESET}")
    time.sleep(1)
    
    try:
        # Importamos la ruta antigua (puede estar vacía o depreciada en versiones nuevas)
        import keras.preprocessing.image
        # Importamos la ruta moderna (TensorFlow 2.x+)
        from tensorflow.keras.utils import img_to_array, array_to_img
        
        print(f"{YELLOW}>> Desincronización detectada. Aplicando Monkey Patching en caliente...{RESET}")
        time.sleep(0.5)
        
        # EL PUENTE MAESTRO: Asignación forzada en memoria
        keras.preprocessing.image.img_to_array = img_to_array
        keras.preprocessing.image.array_to_img = array_to_img
        
        print(f"{GREEN}{BOLD}✅ Puente Maestro de TensorFlow activado. Matriz estabilizada.{RESET}")
        print(f"{GRAY}>> Los módulos Legacy de Computer Vision operarán sin fricción algorítmica.{RESET}\n")
        
    except ImportError as e:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta dependencia estructural: {e}{RESET}")
        print(f"{GRAY}>> El puente requiere que TensorFlow esté instalado en el entorno virtual.{RESET}")
        print(f"{GRAY}>> Ejecute: pip install tensorflow{RESET}\n")
        sys.exit(1)
    except Exception as e:
        print(f"{RED}❌ [ANOMALÍA] Falla en la inyección de la matriz: {e}{RESET}\n")

if __name__ == "__main__":
    estabilizar_matriz_tf()
