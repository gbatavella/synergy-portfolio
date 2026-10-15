import os
import sys
import json
import subprocess
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

def iniciar_mcp_executor():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🧠 SYNERGY MCP EXECUTOR (NOTEBOOKLM SEARCHER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    load_dotenv()
    
    # OPSEC: Ruta del servidor MCP dinámica
    mcp_server_path = os.getenv("MCP_SERVER_PATH", "/usr/local/bin/notebooklm-mcp")

    # Inyección dinámica de búsqueda
    query = input(f"{YELLOW}🔎 Ingrese el término a buscar en NotebookLM (ej. infoproductos): {RESET}")
    if not query.strip():
        query = "infoproductos"

    print(f"{GRAY}[*] Abriendo túnel JSON-RPC con {mcp_server_path}...{RESET}")
    
    try:
        p = subprocess.Popen(
            [mcp_server_path], 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )
    except FileNotFoundError:
        print(f"{RED}❌ [ERROR CRÍTICO] Servidor MCP no encontrado en la ruta especificada.{RESET}\n")
        sys.exit(1)

    # 1. Handshake de Inicialización
    print(f"{GRAY}[*] Ejecutando Handshake de protocolo...{RESET}")
    init_req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "Synergy_Executor", "version": "1.0"}
        }
    }
    print(json.dumps(init_req), file=p.stdin, flush=True)
    
    # Lectura de confirmación
    while True:
        line = p.stdout.readline()
        if not line: break
        try:
            val = json.loads(line)
            if val.get("id") == 1:
                break
        except json.JSONDecodeError:
            pass
            
    # 2. Notificación de conexión establecida
    ack_req = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }
    print(json.dumps(ack_req), file=p.stdin, flush=True)

    # 3. Llamada a la herramienta (Tool Call)
    print(f"{GRAY}[*] Invocando herramienta 'search_notebooks' para el término: '{query}'...{RESET}")
    call_req = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "search_notebooks",
            "arguments": {"query": query}
        }
    }
    print(json.dumps(call_req), file=p.stdin, flush=True)

    # 4. Intercepción de Respuesta
    tools_res = ""
    while True:
        line = p.stdout.readline()
        if not line: break
        try:
            val = json.loads(line)
            if val.get("id") == 2:
                tools_res = json.dumps(val, indent=2)
                print(f"{GREEN}✓ Inferencia MCP completada con éxito.{RESET}")
                break
        except json.JSONDecodeError:
            pass

    print(f"\n{BLUE}{BOLD}--- 📄 PAYLOAD DEVUELTO POR NOTEBOOKLM ---{RESET}")
    print(f"{WHITE}{tools_res}{RESET}")
    print(f"{BLUE}{BOLD}{'-'*50}{RESET}\n")

    p.kill()

if __name__ == "__main__":
    iniciar_mcp_executor()
