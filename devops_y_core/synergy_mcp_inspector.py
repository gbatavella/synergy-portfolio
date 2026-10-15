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

def iniciar_inspector_mcp():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🔌 SYNERGY MCP INSPECTOR (TOOL CAPABILITY EXTRACTOR) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    load_dotenv()
    
    # OPSEC: Rutas dinámicas. Si no existen en el .env, usa los valores por defecto.
    mcp_server_path = os.getenv("MCP_SERVER_PATH", "/usr/local/bin/notebooklm-mcp")
    output_file = os.getenv("MCP_TOOLS_OUTPUT", "tools_mcp.json")

    print(f"{GRAY}[*] Iniciando túnel JSON-RPC con el servidor MCP: {mcp_server_path}{RESET}")
    
    try:
        p = subprocess.Popen(
            [mcp_server_path], 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )
    except FileNotFoundError:
        print(f"{RED}❌ [ERROR CRÍTICO] No se encontró el ejecutable MCP en la ruta especificada.{RESET}\n")
        sys.exit(1)

    print(f"{GRAY}[*] Enviando paquete de inicialización (Protocolo 2024-11-05)...{RESET}")
    init_req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "Synergy_Inspector", "version": "1.0"}
        }
    }
    print(json.dumps(init_req), file=p.stdin, flush=True)

    # Esperar respuesta de inicialización
    while True:
        line = p.stdout.readline()
        if not line: break
        try:
            val = json.loads(line)
            if val.get("id") == 1:
                print(f"{GREEN}✓ Conexión establecida. Handshake completado.{RESET}")
                break
        except:
            pass

    # Enviar Acknowledgment (Notificación de inicializado)
    ack_req = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }
    print(json.dumps(ack_req), file=p.stdin, flush=True)

    print(f"{YELLOW}[*] Solicitando matriz de herramientas (tools/list)...{RESET}")
    call_req = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {}
    }
    print(json.dumps(call_req), file=p.stdin, flush=True)

    tools_res = ""
    while True:
        line = p.stdout.readline()
        if not line: break
        try:
            val = json.loads(line)
            if val.get("id") == 2:
                tools_res = json.dumps(val, indent=2)
                print(f"{GREEN}✓ Catálogo de herramientas interceptado con éxito.{RESET}")
                break
        except:
            pass

    print(f"{GRAY}[*] Escribiendo payload en disco: {output_file}{RESET}")
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(tools_res)
        print(f"\n{BLUE}{BOLD}>>> OPERACIÓN EXITOSA. Bóveda de herramientas MCP guardada.{RESET}\n")
    except Exception as e:
        print(f"{RED}❌ [ERROR] Fallo al escribir el archivo: {e}{RESET}\n")
        
    p.kill()

if __name__ == "__main__":
    iniciar_inspector_mcp()
