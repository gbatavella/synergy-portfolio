import chromadb
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
WHITE = "\033[97m"

def iniciar_lobulo_frontal():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧠 SYNERGY FRONTAL LOBE (CHROMADB VECTOR MEMORY) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. ARQUITECTURA DE DISCO NEURONAL
    # ==========================================
    ruta_memoria = "./cerebro_synergy"
    print(f"{GRAY}[*] Inicializando clúster de memoria local en: {BOLD}{ruta_memoria}{RESET}")
    
    try:
        # Instanciando el cliente persistente
        cliente_chroma = chromadb.PersistentClient(path=ruta_memoria)
        
        # Crear o enlazar con la colección de recuerdos
        coleccion = cliente_chroma.get_or_create_collection(name="memoria_a_largo_plazo")
        print(f"{GREEN}[+] Hipocampo digital enlazado y listo para operaciones vectoriales.{RESET}\n")

        # ==========================================
        # 2. INYECCIÓN DE RECUERDOS FUNDACIONALES
        # ==========================================
        if coleccion.count() == 0:
            print(f"{YELLOW}⏳ Bóveda vacía detectada. Grabando recuerdos fundacionales (Seed Protocol)...{RESET}")
            coleccion.add(
                documents=[
                    "El CEO y Arquitecto del sistema es Gabriel Tavella.",
                    "El ecosistema principal se llama Synergy Human & AI Agents, y también incluye operaciones clasificadas como el Proyecto Fénix.",
                    "La base de operaciones corre sobre una arquitectura de hardware impulsada por un procesador Ryzen 7000 de alta eficiencia.",
                    "El objetivo táctico a largo plazo es escalar hacia la tecnología cuántica y el enrutamiento predictivo."
                ],
                ids=["id_perfil", "id_proyectos", "id_hardware", "id_vision"]
            )
            print(f"{GREEN}✓ Recuerdos fundacionales grabados a nivel físico en la matriz.{RESET}\n")
        else:
            print(f"{CYAN}✓ El lóbulo frontal ya se encuentra activo con {BOLD}{coleccion.count()}{RESET}{CYAN} recuerdos almacenados.{RESET}\n")

        # ==========================================
        # 3. PRUEBA DE RECUPERACIÓN SEMÁNTICA (RAG)
        # ==========================================
        pregunta_usuario = "¿Quién está al mando de los proyectos de IA y Fénix y en qué equipo se procesa?"
        
        print(f"{GRAY}[*] Ejecutando test de latencia y recuperación (RAG)...{RESET}")
        print(f"{WHITE}🗣️ Estímulo de entrada: {BOLD}'{pregunta_usuario}'{RESET}")
        print(f"{YELLOW}🔍 Escaneando distancias vectoriales multidimensionales...{RESET}")

        # Recuperación del N-Top 1 más relevante
        resultados = coleccion.query(
            query_texts=[pregunta_usuario],
            n_results=2 # Extraemos los 2 contextos más relevantes
        )

        print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
        print(f"{GREEN}{BOLD} 💡 BLOQUES DE MEMORIA RECUPERADOS (MAYOR SIMILITUD): {RESET}\n")
        
        for idx, documento in enumerate(resultados['documents'][0]):
            print(f"{CYAN}   Memoria {idx+1}:{RESET} {WHITE}{documento}{RESET}")
            
        print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")

    except Exception as e:
        print(f"\n{RED}X Falla estructural al inicializar ChromaDB: {e}{RESET}")
        print(f"{GRAY}>> Asegúrate de tener las dependencias correctas instaladas (pip install chromadb).{RESET}\n")

if __name__ == "__main__":
    iniciar_lobulo_frontal()
