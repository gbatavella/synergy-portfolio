import os
import sys
import telebot
import chromadb
from openai import OpenAI
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

def iniciar_ciborg():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🚀 PROTOCOLO SYNERGY: MODO CIBORG ACTIVADO (RAG TELEGRAM) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CARGA DEL BÚNKER (OPSEC)
    # ==========================================
    load_dotenv()
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") # O TELEGRAM_TOKEN según tu .env
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    if not TELEGRAM_TOKEN or not OPENROUTER_API_KEY:
        print(f"{RED}X [ERROR CRÍTICO] Faltan llaves de API en la bóveda .env.{RESET}")
        sys.exit(1)

    # ==========================================
    # 2. CONEXIÓN A LOS NÚCLEOS DE PROCESAMIENTO
    # ==========================================
    print(f"{GRAY}[*] Enlazando con el puente cognitivo OpenRouter (Trinity)...{RESET}")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )

    print(f"{GRAY}[*] Inicializando Lóbulo Frontal (ChromaDB) en ./cerebro_synergy...{RESET}")
    cliente_chroma = chromadb.PersistentClient(path="../agente_manager/cerebro_synergy") # Apunta al cerebro central
    coleccion = cliente_chroma.get_or_create_collection(name="memoria_a_largo_plazo")
    
    bot = telebot.TeleBot(TELEGRAM_TOKEN)
    
    print(f"{GREEN}[+] Enlaces estables. El Ciborg está a la escucha en Telegram.{RESET}\n")

    # ==========================================
    # 3. MOTOR DE INTERCEPCIÓN Y APRENDIZAJE
    # ==========================================
    @bot.message_handler(func=lambda message: True)
    def manejar_mensajes(message):
        nombre = message.from_user.first_name
        print(f"\n{CYAN}📩 Transmisión entrante de {BOLD}{nombre}{RESET}{CYAN}: {WHITE}{message.text}{RESET}")
        
        bot.send_chat_action(message.chat.id, 'typing')
        
        try:
            # --- FASE 1: RECORDAR (RAG) ---
            contexto_historico = ""
            if coleccion.count() > 0:
                print(f"{YELLOW}🔍 [Fase 1] Escaneando vectores dimensionales en busca de recuerdos...{RESET}")
                resultados = coleccion.query(
                    query_texts=[message.text],
                    n_results=2 
                )
                recuerdos = resultados['documents'][0]
                if recuerdos:
                    contexto_historico = "RECUERDOS DEL PASADO:\n" + "\n".join(recuerdos) + "\n\n"
                    print(f"{GREEN}🧠 [Memoria] Recuperados {len(recuerdos)} fragmentos históricos relevantes.{RESET}")

            # --- FASE 2: PENSAR (INFERENCIA) ---
            print(f"{GRAY}⚙️ [Fase 2] Procesando prompt enriquecido a través de Trinity...{RESET}")
            prompt_completo = contexto_historico + f"MENSAJE ACTUAL DEL USUARIO: {message.text}"
            
            response = client.chat.completions.create(
                extra_headers={"HTTP-Referer": "https://t.me", "X-Title": "Synergy Human & AI Agents"},
                model="arcee-ai/trinity-large-preview:free",
                messages=[
                    {"role": "system", "content": "Eres el Agente Synergy de 'El Ingeniero Autónomo'. Eres un estratega brillante. Usa los 'RECUERDOS DEL PASADO' proporcionados para responder con contexto, pero responde de forma natural, sin decir 'basado en mis recuerdos'."},
                    {"role": "user", "content": prompt_completo},
                ]
            )
            texto_respuesta = response.choices[0].message.content
            
            # --- FASE 3: RESPONDER ---
            bot.reply_to(message, texto_respuesta)
            print(f"{GREEN}✅ [Fase 3] Respuesta táctica enviada al usuario.{RESET}")

            # --- FASE 4: MEMORIZAR (CONTINUOUS LEARNING) ---
            nuevo_recuerdo = f"Usuario dijo: '{message.text}'. Synergy respondió: '{texto_respuesta}'"
            id_unico = f"msg_{message.chat.id}_{message.message_id}" 
            
            coleccion.add(
                documents=[nuevo_recuerdo],
                ids=[id_unico]
            )
            print(f"{BLUE}💾 [Fase 4] Nueva interacción consolidada en el disco duro vectorial.{RESET}")

        except Exception as e:
            print(f"\n{RED}🚨 Alerta de Sistema Operativo: {e}{RESET}")
            bot.reply_to(message, "⚠️ El nodo táctico está procesando un volumen anómalo de información. Redirigiendo ancho de banda, un momento por favor.")

    # ==========================================
    # 4. BUCLE DE EJECUCIÓN
    # ==========================================
    try:
        bot.infinity_polling()
    except KeyboardInterrupt:
        print(f"\n{YELLOW} Operación cancelada. Ciborg en modo hibernación.{RESET}\n")

if __name__ == "__main__":
    iniciar_ciborg()
