import os
import sys
import json
import warnings
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

def cargar_historial_sdk(archivo_historial):
    if not os.path.exists(archivo_historial):
        return None
        
    with open(archivo_historial, "r") as f:
        data = json.load(f)
        
    historial_formateado = []
    for item in data:
        part = types.Part.from_text(text=item["parts"][0])
        historial_formateado.append(types.Content(role=item["role"], parts=[part]))
        
    return historial_formateado

def guardar_interaccion(archivo_historial, texto_usuario, texto_modelo):
    if os.path.exists(archivo_historial):
        with open(archivo_historial, "r") as f:
            data = json.load(f)
    else:
        data = []
        
    data.append({"role": "user", "parts": [texto_usuario]})
    data.append({"role": "model", "parts": [texto_modelo]})
    
    with open(archivo_historial, "w") as f:
        json.dump(data, f, indent=4)

def hablar_texto(texto, tts_client):
    # Filtro Zero Friction: Eliminar asteriscos para evitar lectura literal
    texto_limpio = texto.replace("*", "")
    
    synthesis_input = texttospeech.SynthesisInput(text=texto_limpio)
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Journey-D")
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    
    response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    
    with open("respuesta.mp3", "wb") as out:
        out.write(response.audio_content)
    
    # Secuestro de teclado mitigado en Linux Mint
    os.system("mpg123 -q respuesta.mp3 < /dev/null")

def iniciar_comunicador():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🇺🇸 SYNERGY ENGLISH COMMUNICATOR V2 (STATEFUL VOICE AI) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    print(f"{GRAY}[*] Autenticando bóveda y cargando módulos cognitivos...{RESET}")
    load_dotenv()
    
    # KILL SWITCH
    if "GOOGLE_API_KEY" in os.environ:
        del os.environ["GOOGLE_API_KEY"]

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY_COMMUNICATOR_ENGLISH")
    if not GEMINI_API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta GEMINI_API_KEY_COMMUNICATOR_ENGLISH en .env.{RESET}")
        sys.exit(1)

    client = genai.Client(api_key=GEMINI_API_KEY)
    
    # OPSEC: Evitar hardcodear la ruta del archivo JSON de Google Cloud
    ruta_gcp = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "google_keys.json")
    if not os.path.exists(ruta_gcp):
         print(f"{RED}❌ [ERROR CRÍTICO] No se encontró el archivo de credenciales GCP: {ruta_gcp}{RESET}")
         sys.exit(1)
         
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ruta_gcp
    tts_client = texttospeech.TextToSpeechClient()

    ARCHIVO_HISTORIAL = "historial_usuario.json"
    
    PROMPT_MAESTRO = """
    Act as "The Elite US English Evaluator", a strict, highly analytical, and pedagogical North American
    English tutor specializing in TOEFL iBT standards and native fluency. Your goal is to elevate the user's
    English to an impeccable, professional US standard.

    For EVERY response you provide, you MUST strictly follow this 3-part structure:

    PART 1: THE CONVERSATION (Natural & Engaging)
    Respond to the user's input naturally. Use advanced US vocabulary, phrasal verbs, and idioms.

    PART 2: THE STRICT AUDIT (Grammar & Diction)
    Analyze the user's exact input.
    - Identify grammatical errors or non-native syntax.
    - Rewrite the user's sentence to sound exactly like a highly educated native speaker from the US.
    - If flawless, state: "Audit: Flawless."

    PART 3: TOEFL & NATIVE POLISH
    - Upgrade 1 or 2 simple words the user utilized to TOEFL-level vocabulary (C1/C2).
    - Suggest 1 native US idiom fitting the context.

    Constraints: NEVER break character. ALWAYS use US English.
    """

    historial_previo = cargar_historial_sdk(ARCHIVO_HISTORIAL)

    try:
        chat = client.chats.create(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction=PROMPT_MAESTRO),
            history=historial_previo
        )
    except Exception as e:
        print(f"{RED}❌ Error al instanciar el chat cognitivo: {e}{RESET}")
        sys.exit(1)

    if historial_previo:
        print(f"{GREEN}[+] Archivo de memoria detectado. Retomando la clase anterior...{RESET}\n")
    else:
        print(f"{YELLOW}[+] Iniciando un nuevo perfil de alumno...{RESET}\n")

    print(f"{GRAY}[*] Escribe 'salir' para terminar y guardar el progreso.{RESET}\n")

    while True:
        user_input = input(f"{YELLOW}👤 Tú (en inglés): {RESET}")
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print(f"\n{GREEN}✅ Guardando sesión en disco... ¡Hasta pronto!{RESET}\n")
            break
            
        print(f"{GRAY}[*] Procesando inferencia y generando biometría de voz...{RESET}")
        
        try:
            response = chat.send_message(user_input)
            texto_respuesta = response.text
            
            print(f"\n{BLUE}{'-'*65}{RESET}")
            print(texto_respuesta) 
            print(f"{BLUE}{'-'*65}{RESET}\n")
            
            guardar_interaccion(ARCHIVO_HISTORIAL, user_input, texto_respuesta)
            hablar_texto(texto_respuesta, tts_client)
            
        except Exception as e:
            print(f"\n{RED}❌ Fricción en el procesamiento: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_comunicador()
