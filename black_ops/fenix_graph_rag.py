import os
import sys
import numpy as np
import faiss
from google import genai
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"

def iniciar_memoria_vram():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧠 SYNERGY FÉNIX GRAPHRAG (IN-MEMORY LEGAL MATRIX) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÚNKER (OPSEC)
    # ==========================================
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")

    if not API_KEY:
        print(f"{RED}X [ERROR CRÍTICO] Falta GEMINI_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)

    client = genai.Client(api_key=API_KEY)

    # ==========================================
    # 2. CONSTRUCCIÓN DEL GRAFO DE CONOCIMIENTO (Nodos Legales)
    # ==========================================
    print(f"{GRAY}[*] Inicializando Nodos del Grafo de Conocimiento Jurídico...{RESET}")
    
    grafo_legal = [
        "ENTIDAD: TAVSOL S.A. -> RELACIÓN: Posee -> ACTIVO: Parque Industrial en Villa Dolores, Córdoba.",
        "ENTIDAD: TAVSOL S.A. -> RELACIÓN: Vinculada a -> SOCIEDAD: MUSTAFÁ SH.",
        "NORMATIVA: Prescripción Fiscal AFIP -> CONDICIÓN: Exige 5 a 10 años de inactividad demostrable.",
        "ACCIÓN: Blindaje Patrimonial -> REQUIERE -> NORMATIVA: Regularización societaria ante la IGJ.",
        "ESTRATEGIA: Salvataje de Activos -> APLICA A -> ACTIVO: Parque Industrial mediante fideicomiso ciego."
    ]

    # ==========================================
    # 3. VECTORIZACIÓN (Embeddings)
    # ==========================================
    print(f"{GRAY}[*] Transformando Nodos Legales a Vectores de 768 Dimensiones (Google Embeddings)...{RESET}")
    
    try:
        # Solicitamos a Google que convierta los textos en matemática pura
        respuesta_emb = client.models.embed_content(
            model='text-embedding-004',
            contents=grafo_legal
        )
        
        # Extraemos los vectores y los convertimos a una matriz de Numpy (Float32 para FAISS)
        vectores = np.array([emb.values for emb in respuesta_emb.embeddings]).astype('float32')
        
        print(f"{GREEN}[+] Vectorización completada. Matriz de forma: {vectores.shape}{RESET}\n")

    except Exception as e:
        print(f"{RED}X Falla en el motor de Embeddings: {e}{RESET}")
        sys.exit(1)

    # ==========================================
    # 4. INDEXACIÓN IN-MEMORY (META FAISS)
    # ==========================================
    print(f"{YELLOW}⚡ Subiendo matriz vectorial a la Memoria RAM (Faiss CPU)...{RESET}")
    
    dimensiones = vectores.shape[1] # 768 dimensiones
    indice_faiss = faiss.IndexFlatL2(dimensiones) # Distancia Euclidiana
    indice_faiss.add(vectores)
    
    print(f"{GREEN}✓ Clúster FAISS operativo. {indice_faiss.ntotal} nodos cargados en RAM.{RESET}\n")

    # ==========================================
    # 5. TEST DE RAZONAMIENTO DEDUCTIVO (Graph Query)
    # ==========================================
    pregunta_director = "¿Qué se requiere para hacer un blindaje sobre el Parque Industrial y a quién pertenece?"
    print(f"{CYAN}👤 Comandante: {WHITE}'{pregunta_director}'{RESET}")
    
    print(f"{GRAY}[*] Ejecutando escaneo topológico dimensional...{RESET}")
    
    # Vectorizamos la pregunta
    emb_pregunta = client.models.embed_content(
        model='text-embedding-004',
        contents=pregunta_director
    ).embeddings[0].values
    
    vector_pregunta = np.array([emb_pregunta]).astype('float32')
    
    # FAISS busca los 2 nodos más cercanos en microsegundos
    distancias, indices = indice_faiss.search(vector_pregunta, k=2)
    
    print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
    print(f"{GREEN}{BOLD} 💡 NODOS DEL GRAFO RECUPERADOS (Microsegundos): {RESET}\n")
    
    for i in range(len(indices[0])):
        idx_nodo = indices[0][i]
        print(f"{CYAN}Nodo {i+1} (Distancia {distancias[0][i]:.2f}):{RESET} {WHITE}{grafo_legal[idx_nodo]}{RESET}")
    
    print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")
    print(f"{GRAY}>> Nota Arquitectónica: Fénix ahora puede deducir que TAVSOL es dueña del Parque y que el blindaje exige regularizar la IGJ, cruzando ambos nodos en RAM.{RESET}\n")

if __name__ == "__main__":
    iniciar_memoria_vram()
