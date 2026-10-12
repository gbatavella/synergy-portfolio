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

def iniciar_reparacion_documental():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🛠️ SYNERGY AUTO-DOCUMENTER (SELF-HEALING DOC BUILDER) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    RUTA_README = "../README.md"

    if not os.path.exists(RUTA_README):
        print(f"{RED}X [ERROR] No se encuentra el archivo README.md en la ruta ../{RESET}")
        sys.exit(1)

    print(f"{GRAY}[*] Analizando integridad del archivo maestro README.md...{RESET}")

    # ==========================================
    # EL CATÁLOGO MAESTRO ESTERILIZADO (5 AL 10)
    # ==========================================
    bloque_perfecto = """### 5. Agente Manager (agente_manager/)
Orquestación cognitiva, ideación de infoproductos y estrategia de contenido B2B.

* **70. mision_investigador_ia.py**: Synergy Advanced Researcher (CrewAI Content Strategist). Orquestación Multi-Agente, Prompt Engineering y automatización de archivos.
* **71. agente_profiler.py**: Synergy Stealth Profiler (CrewAI Cold Email Forge). Búsqueda Semántica en Tiempo Real (SerperDev) y Pipeline I/O Dinámico.
* **72. enjambre_infoproducto.py**: Synergy Global Prospector (SaaS & High-Ticket Swarm). Google Dorking Avanzado y Structured Output Enforcement.
* **73. mision_sw4_ariel.py**: Synergy Asset Liquidator (SW4 Auto-Broker Swarm). Prompt Engineering (Psicología de Ventas) y Geofencing B2C.
* **79. agente_linkedin.py**: Synergy LinkedIn Generator (B2B Content Factory). Inbound Marketing, Direct API Integration (OpenRouter) y B2B Copywriting.
* **80. agente_planificador.py**: Synergy Operations Planner (COO Agent). Executive Accountability, System Prompts Estrictos y Bucle REPL.
* **81. agente_cerebro.py**: Synergy Market Brain (Gemini 2.5 Macro-Profiler). Ingesta cualitativa, Google GenAI SDK y Psicología del Consumidor.
* **94. forjador_blueprint.py**: Synergy Blueprint Forger (Lead Magnet Engine). Adopción de arquetipo "Trusted Advisor" y generación de activos Markdown.
* **99. manager.py**: Synergy Niche Manager (Trinity Web Investigator). Web scraping de SERPs en tiempo real para validación de mercado e ideación B2B.
* **100. memoria.py**: Synergy Frontal Lobe (ChromaDB Vector Memory). Bases de datos vectoriales persistentes y recuperación semántica (RAG Architecture).

### 6. Agentes Telegram (agentes_telegram/)
Operaciones de intercepción, análisis competitivo y social listening autónomo.

* **84. agente_trafficker.py**: Synergy Competitor X-Ray (Trafficker Agent V1.0). Growth Hacking, análisis de competencia y extracción estructurada (JSON).
* **85. ares_delta.py**: Synergy Ares Delta (Stealth OSINT Infiltrator). Evasión anti-bot (undetected-chromedriver) y parseo semántico de DOM.
* **86. ares_delta_v2.py**: Synergy Ares Delta V2.1 (Deep Extraction & Pain Vacuum). OSINT profundo y extracción masiva de PII por Regex.
* **90. ares_trafficker_v2.py**: Synergy Ares Trafficker V2 (Stateful OSINT Radar). Social Listening con gestión de estado en memoria y arquitectura desacoplada.
* **95. goalkeeper.py**: Synergy Goalkeeper (Telegram Sales & Support Agent). Intercepción BoFu, Long Polling 24/7 y cierre de ventas multilingüe.
* **101. mi_bot.py**: Synergy Community Greeter (Onboarding Bot). Lead Onboarding, Front-End Funnel y enrutamiento de tráfico B2B (Inline UI).

### 7. Outbound y Closers (outbound_y_closers/)
Infraestructura de ventas, higiene de datos y distribución de correo en frío.

* **76. agente_depurador_v2.py**: Synergy Bounce Scrubber (IMAP Data Cleanser). Higiene de Datos, IMAP Protocol Parsing y Pandas ETL.
* **77. agente_depurador_v3.py**: Synergy Lead Refiner (Heuristic Data Cleanser). Filtrado Heurístico, Pandas Data Wrangling y Blacklist I/O.
* **78. agente_depurador_v3_1.py**: Synergy Data Cleanser V3.1. Machine Auto-Learning, Whitelisting y Blacklist Dinámica.
* **96. hermes.py**: Synergy Hermes Sentinel (HITL SMTP Dispatcher). Despacho seguro de Cold Emails con autorización humana e integración TLS/SSL.
* **97. hermes_sniper.py**: Synergy Hermes Sniper (Autonomous Conditional Dispatcher). Copywriting dinámico, memoria de estado y cortafuegos Anti-Spam Trap.
* **98. hermes_vip.py**: Synergy Hermes VIP (High-Ticket HITL Dispatcher). Fricción táctica de entrega y validación de lazo cerrado para CEOs.

### 8. OSINT y Radar (osint_y_radar/)
Inteligencia de fuentes abiertas, dorking y detección de señales de mercado.

* **87. operacion_fantasma.py**: Synergy Ghost Navigator (HITL OSINT Scraper). Detección temprana de dolores SaaS y evasión WAF vía Human-In-The-Loop.
* **88. ares_hacker_news.py**: Synergy Ares Hacker News (Y Combinator OSINT Radar). Ingestión nativa por API REST y heurística de palabras clave.
* **89. ares_indiehackers.py**: Synergy Ares IndieHackers (Bootstrapper OSINT Radar). Spoofing de User-Agent e interceptación de intención comercial B2B.
* **91. ares_vip.py**: Synergy VIP Hound (HITL Dorking Scraper). Prospección High-Ticket automatizada mediante Google Dorks e infiltración híbrida.

### 9. DevOps y Core (devops_y_core/)
Ingeniería de confiabilidad (SRE), seguridad operativa (OPSEC) y monitoreo.

* **74. agente_centinela.py**: Synergy Sentinel Agent (UFW Active Firewall & IDS). Prevención de intrusos, Log Tailing y UFW Firewall Automation.
* **75. agente_custodio.py**: Synergy Custodian Agent (FinOps & Telegram Alerter). Monitoreo de infraestructura financiera y notificaciones Push.
* **82. agente_security.py**: Synergy Watchdog (IMAP Kill Switch). Protección de reputación de dominio, Process Isolation (pkill) y Telemetría.
* **83. agente_sombra.py**: Synergy Shadow Agent (Air-Gap Dead Man's Switch). Aislamiento de red de emergencia y Zero-Trust Air-Gapping.
* **102. builder_readme.py**: Synergy Auto-Documenter (Self-Healing File I/O). Automatización de documentación Markdown y reparación de catálogos.

### 10. Black Ops (black_ops/)
Operaciones especiales, recuperación de activos y consultoría de alta disponibilidad.

* **92. fenix_estratega.py**: Synergy Phoenix Strategist (Forensic Legal Agent). Consultoría legal/forense parametrizada para el marco jurídico corporativo argentino.
* **93. fenix_legal.py**: Synergy Phoenix Legal (High-Availability Counsel). Ruteo de inferencia en cascada (Claude/GPT-4o/LLaMA) para disponibilidad 100%.

---
*Todos los scripts en este repositorio han sido anonimizados, parametrizados dinámicamente y despojados de claves de API, payloads corporativos reales y credenciales de red para proteger la Propiedad Intelectual, los datos sensibles y el secreto comercial de la agencia operativa.*
"""

    try:
        # Leemos todo el contenido actual
        with open(RUTA_README, "r", encoding="utf-8") as f:
            contenido_original = f.read()

        # Encontramos el punto donde empieza el desorden (División 5)
        marcador = "### 5. Agente Manager (agente_manager/)"
        punto_corte = contenido_original.find(marcador)

        if punto_corte != -1:
            # Amputamos la parte rota y le pegamos el bloque perfecto
            contenido_limpio = contenido_original[:punto_corte]
            nuevo_contenido = contenido_limpio + bloque_perfecto

            # Sobrescribimos el archivo con la estructura sana
            with open(RUTA_README, "w", encoding="utf-8") as f:
                f.write(nuevo_contenido)
                
            print(f"{GREEN}✓ Operación quirúrgica exitosa. Bloque de catálogos 5-10 inyectado.{RESET}")
            print(f"{GREEN}✓ El archivo README.md ha sido reparado y ahora contiene 102 motores.{RESET}\n")
        else:
            print(f"{YELLOW}! No se encontró el marcador de la División 5. Verifica el archivo.{RESET}\n")

    except Exception as e:
        print(f"{RED}X Fallo de lectura/escritura en el sistema de archivos: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_reparacion_documental()
