import os
import sys
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"

def iniciar_laboratorio_sap():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 💼 SYNERGY SAP SALES REP (IN-MEMORY ERP GRAPH) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CARGA DE BÚNKER (OPSEC)
    # ==========================================
    print(f"{GRAY}[*] Autenticando bóveda y cargando módulos...{RESET}")
    load_dotenv()
    
    if "GOOGLE_API_KEY" in os.environ:
        del os.environ["GOOGLE_API_KEY"]
        
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta GEMINI_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    # ==========================================
    # 2. MOTOR DE EMBEDDINGS LOCAL Y FAISS
    # ==========================================
    print(f"{GRAY}[*] Iniciando motor de Embeddings Local (Hugging Face MiniLM - Costo $0)...{RESET}")
    modelo_emb = SentenceTransformer('all-MiniLM-L6-v2')

    print(f"{GRAY}[*] Inicializando Nodos del Grafo ERP (Inventario SAP Simulado)...{RESET}")
    # Inventario corporativo: SKU, Nombre, Especificación Técnica y Dolor que resuelve
    inventario_sap = [
        "SKU: SRV-X900 | PRODUCTO: Servidor Synergy X900 | ESPECIFICACIONES: 128GB RAM, NVMe 4TB | SOLUCIÓN: Ideal para empresas cuyas bases de datos colapsan por picos de tráfico. Soporta alta concurrencia.",
        "SKU: CLD-SEC5 | PRODUCTO: Firewall Cloud Sentinel 5 | ESPECIFICACIONES: Zero-Trust, DPI en tiempo real | SOLUCIÓN: Perfecto para corporaciones que han sufrido brechas de seguridad o ataques ransomware recientes.",
        "SKU: AUT-RaaS | PRODUCTO: Robots as a Service (RaaS) | ESPECIFICACIONES: Enjambre de agentes LLM, automatización 24/7 | SOLUCIÓN: Resuelve la fatiga operativa, el alto costo de nómina de ventas y los embudos manuales lentos.",
        "SKU: NET-MESH | PRODUCTO: Malla de Red Inteligente | ESPECIFICACIONES: SD-WAN, Enrutamiento dinámico | SOLUCIÓN: Elimina la latencia y las caídas de conexión entre sucursales distribuidas geográficamente."
    ]

    print(f"{GRAY}[*] Transformando Inventario ERP a Vectores y subiendo a VRAM...{RESET}")
    vectores_sap = modelo_emb.encode(inventario_sap)
    dimensiones = vectores_sap.shape[1]
    indice_faiss = faiss.IndexFlatL2(dimensiones)
    indice_faiss.add(vectores_sap)
    print(f"{GREEN}✓ Clúster FAISS operativo. Catálogo SAP indexado en memoria.{RESET}\n")

    # ==========================================
    # 3. INTERCEPCIÓN DEL PROSPECTO Y CIERRE
    # ==========================================
    while True:
        dolor_prospecto = input(f"{YELLOW}👤 Dolor del Prospecto (o 'salir'): {RESET}")
        
        if dolor_prospecto.lower() in ['salir', 'exit']:
            print(f"\n{GREEN}✅ Apagando Laboratorio SAP.{RESET}\n")
            break

        print(f"{GRAY}[*] Escaneo semántico en VRAM buscando coincidencia exacta de SKU...{RESET}")
        vector_pregunta = modelo_emb.encode([dolor_prospecto])
        distancias, indices = indice_faiss.search(vector_pregunta, k=1)
        
        sku_detectado = inventario_sap[indices[0][0]]
        print(f"{CYAN}💡 Producto detectado en milisegundos: {BOLD}{sku_detectado}{RESET}\n")

        print(f"{GRAY}[*] Derivando a Gemini 2.5 para redactar el Pitch de Venta High-Ticket...{RESET}")
        
        prompt_ventas = f"""
        Eres un Closer de Ventas B2B de élite operando para Synergy.
        
        El cliente expresó este problema: "{dolor_prospecto}"
        
        Nuestro sistema interno (SAP) determinó que el producto exacto para él es este: 
        "{sku_detectado}"
        
        REDACTA UN PITCH DE VENTA CORTO (Máximo 3 párrafos):
        1. Empatiza con su problema sin rodeos.
        2. Presenta el producto y sus especificaciones técnicas de forma elegante.
        3. Cierra preguntando si tienen disponibilidad para una llamada técnica esta semana.
        
        Tono: Corporativo, directo, sin rogar. Usa Markdown.
        """
        
        try:
            respuesta_closer = model.generate_content(prompt_ventas)
            print(f"\n{BLUE}{BOLD}--- 📝 PITCH GENERADO POR EL SALES REP ---{RESET}")
            print(f"{WHITE}{respuesta_closer.text}{RESET}")
            print(f"{BLUE}{BOLD}{'-'*50}{RESET}\n")
        except Exception as e:
            print(f"{RED}❌ Error al generar el Pitch de ventas: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_laboratorio_sap()
