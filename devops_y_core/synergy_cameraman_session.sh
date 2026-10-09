#!/bin/bash

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE="\033[96m"
GREEN="\033[92m"
YELLOW="\033[93m"
GRAY="\033[90m"
RESET="\033[0m"
BOLD="\033[1m"

# =====================================================================
# SYNERGY LABS: AGENTE CAMERAMAN (AUTOMATED SESSION RECORDER)
# =====================================================================

start_synergy_session() {
    echo -e "\n${BLUE}${BOLD}=================================================================${RESET}"
    echo -e "${BLUE}${BOLD} 🎥 SYNERGY AGENT CAMERAMAN (AUTOMATED SESSION RECORDER) ${RESET}"
    echo -e "${BLUE}${BOLD}=================================================================${RESET}\n"
    
    echo -e "${YELLOW}[*] Inicializando subsistema de captura visual (Kazam)...${RESET}"
    
    # Lanza Kazam en segundo plano desacoplado de la terminal principal
    if command -v kazam &> /dev/null; then
        kazam &
        PID_KAZAM=$!
        echo -e "${GRAY}   ↳ Instancia de grabación enlazada (PID: $PID_KAZAM).${RESET}"
    else
        echo -e "${YELLOW}⚠️ [ADVERTENCIA] Kazam no está instalado. Continuando sin grabación visual.{RESET}"
    fi
    
    echo -e "${GRAY}[*] Esperando estabilización del buffer gráfico (3s)...{RESET}"
    sleep 3 
    
    echo -e "${GREEN}[+] ¡Grabación lista! Iniciando Protocolo Ares (Engine Core)...${RESET}\n"
    
    # Ejecución del motor principal de la IA (Reemplazar 'python3 ares_engine.py' por tu script activo)
    python3 ares_engine.py 
    
    echo -e "\n${BLUE}[*] Sesión de ejecución finalizada. Conserve o detenga la grabación de video.${RESET}\n"
}

# Ejecución directa si se llama al script
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    start_synergy_session
fi
