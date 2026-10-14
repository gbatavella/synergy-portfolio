import os
import sys
import json
import warnings
import telebot
import emoji
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from google import genai
from google.genai import types
from google.cloud import texttospeech
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

warnings.filterwarnings("ignore")

# ==========================================
# 1. CARGA DE BÚNKER Y CREDENCIALES
# ==========================================
def inicializar_entorno():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🤖 SYNERGY TELEGRAM COACH (VOICE AI & FUNNEL) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    print(f"{GRAY}[*] Enlazando bóveda y módulos de mensajería...{RESET}")
    load_dotenv()

    # KILL SWITCH OPSEC
    if "GOOGLE_API_KEY" in os.environ:
        del os.environ["GOOGLE_API_KEY"]

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY_COMMUNICATOR_ENGLISH")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN_ENGLISH_COACH")

    if not GEMINI_API_KEY or not TELEGRAM_TOKEN:
        print(f"{RED}❌ [ERROR CRÍTICO] Faltan API Keys (Gemini o Telegram) en .env.{RESET}")
        sys.exit(1)

    ruta_gcp = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "google_keys.json")
    if not os.path.exists(ruta_gcp):
         print(f"{RED}❌ [ERROR CRÍTICO] No se encontró el archivo GCP: {ruta_gcp}{RESET}")
         sys.exit(1)
         
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ruta_gcp
    return GEMINI_API_KEY, TELEGRAM_TOKEN

GEMINI_API_KEY, TELEGRAM_TOKEN = inicializar_entorno()

client = genai.Client(api_key=GEMINI_API_KEY)
bot = telebot.TeleBot(TELEGRAM_TOKEN)
tts_client = texttospeech.TextToSpeechClient()

ARCHIVO_HISTORIAL = "historial_telegram.json"
estados_onboarding = {}
respuestas_onboarding = {}

# ==========================================
# 2. PROMPTS MAESTROS
# ==========================================
PROMPT_DIAGNOSTICO = """
Actúa como un Coach de Inglés empático, fascinante y muy motivador. 
El usuario acaba de terminar un test de 3 preguntas. Tienes sus respuestas (pueden ser transcripciones de audio o texto).
Tu misión:
1. Analizar su nivel general (A1, A2, B1, B2, C1, C2) basándote en cómo respondió.
2. Hablarle 100% en español de forma súper cálida, usando muchos emojis.
3. Decirle su nivel estimado sin juzgarlo. ¡Felicítalo por dar el primer paso!
4. DALE PROYECCIÓN (ITINERARIO AUTOMÁTICO): Propónle inmediatamente un itinerario de 3 pasos a seguir a partir de hoy para mejorar sus puntos débiles. 
5. Invítalo a dar ese primer paso AHORA MISMO respondiendo a este mensaje con un texto o una NOTA DE VOZ.
NO HAGAS AUDITORÍAS ESTRICTAS AQUÍ. Solo dale un diagnóstico hermoso, su itinerario y motívalo a empezar. Párrafos cortos.
"""

PROMPT_MAESTRO = """
Act as "The Elite US English Evaluator" and empathetic language coach.
Your goal is to elevate the user's English to a professional US standard (TOEFL iBT), but you MUST
adapt your pedagogy, tone, and formatting to their current level.

CRITICAL UX RULES (Visuals & Psychology):
- Use emojis generously to break up text, make it visually appealing.
- Keep paragraphs SHORT (maximum 2-3 lines). NO "walls of text."
- Be warm, encouraging, and fascinating. Create a safe space for mistakes.
- IF THE USER SENDS AN AUDIO/VOICE NOTE: Evaluate their pronunciation, intonation, and fluidity explicitly!

For EVERY response, use this exact 3-part structure:

PART 1: THE CONVERSATION & EMPATHY
- Respond to the user naturally.
- IF the user is a beginner (Level 0/A1) or speaks in Spanish: Welcome them warmly. DO NOT mention "TOEFL" or "C1/C2" unless the user explicitly asks about it. 

### PART 2: THE STRICT AUDIT (Grammar, Diction & Pronunciation)
- Analyze the user's exact input (Text or Audio).
- Identify grammatical errors, non-native syntax, or pronunciation issues.
- Rewrite the sentence to sound native.
- If flawless, state: "Audit: Flawless"

### PART 3: TOEFL & NATIVE POLISH
- Upgrade 1 or 2 simple words to TOEFL-level (C1/C2). Explain them simply.
- Suggest 1 native US idiom fitting the context.
"""

# ==========================================
# 3. MÓDULOS DE MEMORIA Y VOZ
# ==========================================
def cargar_historial_sdk(chat_id):
    if not os.path.exists(ARCHIVO_HISTORIAL):
        return [] 
    with open(ARCHIVO_HISTORIAL, "r") as f:
        data = json.load(f)
    str_chat_id = str(chat_id)
    if str_chat_id not in data:
        return [] 
        
    historial_formateado = []
    for item in data[str_chat_id]:
        part = types.Part.from_text(text=item["parts"][0])
        historial_formateado.append(types.Content(role=item["role"], parts=[part]))
    return historial_formateado

def guardar_interaccion(chat_id, texto_usuario, texto_modelo):
    if os.path.exists(ARCHIVO_HISTORIAL):
        with open(ARCHIVO_HISTORIAL, "r") as f:
            data = json.load(f)
    else:
        data = {}
    str_chat_id = str(chat_id)
    if str_chat_id not in data:
        data[str_chat_id] = []
    data[str_chat_id].append({"role": "user", "parts": [texto_usuario]})
    data[str_chat_id].append({"role": "model", "parts": [texto_modelo]})
    with open(ARCHIVO_HISTORIAL, "w") as f:
        json.dump(data, f, indent=4)

def generar_audio(texto, chat_id):
    texto_limpio = texto.replace("*", "").replace("#", "")
    texto_limpio = emoji.replace_emoji(texto_limpio, replace="")
    synthesis_input = texttospeech.SynthesisInput(text=texto_limpio)
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Journey-D")
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    archivo_salida = f"respuesta_{chat_id}.mp3"
    with open(archivo_salida, "wb") as out:
        out.write(response.audio_content)
    return archivo_salida

def enviar_cta_cafe(chat_id):
    markup = InlineKeyboardMarkup(row_width=1)
    boton_gumroad = InlineKeyboardButton("🌍 Aportar vía Gumroad (USD)", url="https://batavella.gumroad.com/")
    boton_whop = InlineKeyboardButton("🚀 Aportar vía Whop (USD)", url="https://whop.com/")
    boton_mp = InlineKeyboardButton("🇦🇷 Aportar vía Mercado Pago", url="https://link.mercadopago.com.ar/")
    markup.add(boton_gumroad, boton_whop, boton_mp)
    
    texto_cta = (
        "¡Tu aventura con el inglés comienza AHORA! 🎉\n\n"
        "Mi objetivo es democratizar el inglés de élite. Por eso, el pase para desbloquear **tu plan de estudio personalizado** "
        "y mantener tus auditorías ilimitadas activas es *a la gorra* (a voluntad, desde el valor de un cafecito). ☕\n\n"
        "Tú decides cuánto valor te aporta mi guía. ¡Elige tu plataforma preferida aquí abajo y envíame tu primer audio! 👇"
    )
    bot.send_message(chat_id, texto_cta, reply_markup=markup, parse_mode="Markdown")

# ==========================================
# 4. RUTAS Y ONBOARDING TELEGRAM
# ==========================================
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chat_id = message.chat.id
    nombre_usuario = message.from_user.first_name
    estados_onboarding[chat_id] = 0 
    
    markup = InlineKeyboardMarkup()
    boton_inicio = InlineKeyboardButton("➡️ ¡Sí, quiero descubrir mi nivel!", callback_data="iniciar_test")
    markup.add(boton_inicio)
    
    mensaje_bienvenida = (
        f"¡Hola, {nombre_usuario}! 👋 Qué alegría verte por aquí.\n\n"
        "¿Sabías que los profesionales que dominan el inglés ganan en promedio un *40% más*? 🚀\n\n"
        "Soy tu English Coach personal. Para armar tu ruta ideal, he preparado un test de 3 preguntitas rápidas. 🎯"
    )
    bot.send_message(chat_id, mensaje_bienvenida, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "iniciar_test":
        chat_id = call.message.chat.id
        bot.answer_callback_query(call.id)
        estados_onboarding[chat_id] = 1
        respuestas_onboarding[chat_id] = []
        
        pregunta_1 = "¡Excelente actitud! 🚀\n\n*Pregunta 1 de 3:*\nImagina que estás en una reunión y quieres decir 'Estoy de acuerdo contigo'. ¿Cómo lo dirías en inglés? (Texto o **AUDIO**) 👇"
        bot.send_message(chat_id, pregunta_1, parse_mode="Markdown")

@bot.message_handler(content_types=['text', 'voice'])
def manejar_mensaje(message):
    chat_id = message.chat.id
    nombre_usuario = message.from_user.first_name
    estado_actual = estados_onboarding.get(chat_id, 0)
    
    if message.content_type == 'voice':
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, "🎧 Escuchando tu nota de voz...")
        
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        audio_part = types.Part.from_bytes(data=downloaded_file, mime_type='audio/ogg')
        
        if estado_actual in [1, 2, 3]:
            mensaje_a_gemini = [audio_part, "Transcribe brevemente lo que el usuario dijo en este audio."]
            user_input = "[Audio interceptado en Onboarding]"
        else:
            mensaje_a_gemini = [audio_part, "El usuario acaba de enviar esta nota de voz. Por favor, transcribe lo que dijo, evalúa su pronunciación y fluidez, y responde siguiendo tu estructura habitual."]
            user_input = "[El usuario envió una nota de voz para evaluar su pronunciación]"
    else:
        mensaje_a_gemini = message.text
        user_input = message.text

    if estado_actual in [1, 2, 3]:
        if message.content_type == 'voice':
             chat_transcription = client.chats.create(model="gemini-2.5-flash")
             try:
                 response_transcription = chat_transcription.send_message(mensaje_a_gemini)
                 texto_para_guardar = response_transcription.text
             except:
                 texto_para_guardar = "El usuario envió un audio pero falló la transcripción."
        else:
             texto_para_guardar = user_input

        if estado_actual == 1:
            respuestas_onboarding[chat_id].append(texto_para_guardar)
            estados_onboarding[chat_id] = 2
            bot.send_message(chat_id, "¡Anotado! 📝\n\n*Pregunta 2 de 3:*\nEstás en un viaje y necesitas pedir 'un café con leche, por favor'. ¿Cómo lo pedirías en inglés? (Texto o Audio) ☕👇", parse_mode="Markdown")
            return
            
        elif estado_actual == 2:
            respuestas_onboarding[chat_id].append(texto_para_guardar)
            estados_onboarding[chat_id] = 3
            bot.send_message(chat_id, "¡Perfecto! Ya casi terminamos. 🎉\n\n*Pregunta 3 de 3:*\n¿Por qué te gustaría mejorar tu inglés? (Ej: viajar, trabajo, estudios). 🎯👇", parse_mode="Markdown")
            return
            
        elif estado_actual == 3:
            respuestas_onboarding[chat_id].append(texto_para_guardar)
            estados_onboarding[chat_id] = 0 
            
            bot.send_message(chat_id, "¡Genial! Dame un segundito que estoy analizando tus respuestas... 🧠⚙️")
            bot.send_chat_action(chat_id, 'typing')
            
            respuestas = respuestas_onboarding[chat_id]
            input_diagnostico = f"El usuario {nombre_usuario} ha terminado su test. Q1: '{respuestas[0]}'. Q2: '{respuestas[1]}'. Q3: '{respuestas[2]}'. Evalúa su nivel, dale su itinerario automático y anímalo."
            
            chat = client.chats.create(model="gemini-2.5-flash", config=types.GenerateContentConfig(system_instruction=PROMPT_DIAGNOSTICO))
            
            try:
                response = chat.send_message(input_diagnostico)
                texto_respuesta = response.text
                
                bot.send_chat_action(chat_id, 'record_voice')
                archivo_audio = generar_audio(texto_respuesta, chat_id)
                with open(archivo_audio, 'rb') as audio:
                    bot.send_voice(chat_id, audio)
                os.remove(archivo_audio)
                
                bot.send_message(chat_id, texto_respuesta)
                enviar_cta_cafe(chat_id)
                return
            except Exception as e:
                bot.send_message(chat_id, "Hubo un pequeño error procesando tu nivel, ¡pero ya podemos empezar a practicar!")
                print(f"{RED}Error Diagnóstico: {e}{RESET}")
                return

    # MODO NORMAL
    print(f"{GREEN}[+] Procesando inferencia para: {nombre_usuario} (ID: {chat_id}){RESET}")
    historial = cargar_historial_sdk(chat_id)
    
    kwargs = {"model": "gemini-2.5-flash", "config": types.GenerateContentConfig(system_instruction=PROMPT_MAESTRO)}
    if historial:
        kwargs["history"] = historial
        
    chat = client.chats.create(**kwargs)
    
    try:
        response = chat.send_message(mensaje_a_gemini)
        texto_respuesta = response.text
        guardar_interaccion(chat_id, user_input, texto_respuesta)
        
        bot.send_chat_action(chat_id, 'record_voice')
        archivo_audio = generar_audio(texto_respuesta, chat_id)
        
        with open(archivo_audio, 'rb') as audio:
            bot.send_voice(chat_id, audio)
        os.remove(archivo_audio)
        
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, texto_respuesta)
        
        historial_actualizado = cargar_historial_sdk(chat_id)
        if len(historial_actualizado) == 2:
            enviar_cta_cafe(chat_id)
            
    except Exception as e:
        bot.send_message(chat_id, "Sorry, I encountered an error. Please try again.")
        print(f"{RED}[-] Error en Modo Normal: {e}{RESET}")

if __name__ == "__main__":
    print(f"{YELLOW}[*] El bot de Telegram está ONLINE. Esperando interacciones...{RESET}")
    bot.infinity_polling()
