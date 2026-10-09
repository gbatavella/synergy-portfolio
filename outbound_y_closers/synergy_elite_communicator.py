import os
import sys
import time
import google.generativeai as genai
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
WHITE = "\033[97m"

def inicializar_entorno():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🎙️ SYNERGY ELITE COMMUNICATOR (VOICE AI TUTOR) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    load_dotenv()

    # 1. Configuración de Google Gemini
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY_COMMUNICATOR_ENGLISH", os.getenv("GEMINI_API_KEY"))
    if not GEMINI_API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta GEMINI_API_KEY en la bóveda .env.{RESET}")
        sys.exit(1)
    
    genai.configure(api_key=GEMINI_API_KEY)

    # 2. Configuración de Google Cloud TTS (Service Account)
    GCP_CREDENTIALS = os.getenv("GCP_CREDENTIALS_JSON", "google_keys.json")
    if not os.path.exists(GCP_CREDENTIALS):
        print(f"{YELLOW}⚠️ [ADVERTENCIA] Archivo de credenciales GCP ({GCP_CREDENTIALS}) no encontrado.{RESET}")
        print(f"{GRAY}>> El motor de voz estará desactivado. Solo modo texto.{RESET}\n")
    else:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GCP_CREDENTIALS
        print(f"{GREEN}[+] Credenciales GCP detectadas. Motor biométrico enlazado.{RESET}")

def hablar_texto(texto, tts_client):
    """Convierte el texto en voz neuronal y lo reproduce vía CLI."""
    if not tts_client:
        return
        
    try:
        synthesis_input = texttospeech.SynthesisInput(text=texto)
        # Voz neuronal masculina de US (Journey)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Journey-D" 
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = tts_client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        archivo_audio = "synergy_audio_cache.mp3"
        with open(archivo_audio, "wb") as out:
            out.write(response.audio_content)
        
        # Reproducción silenciosa en terminal Linux
        os.system(f"mpg123 -q {archivo_audio}")
        
        # Limpieza táctica del archivo caché
        if os.path.exists(archivo_audio):
            os.remove(archivo_audio)
            
    except Exception as e:
        print(f"\n{RED}❌ Fricción en la síntesis de voz: {e}{RESET}")

def ejecutar_tutor():
    inicializar_entorno()

    # ==========================================
    # EL PROMPT MAESTRO (Anclaje Estructural)
    # ==========================================
    PROMPT_MAESTRO = """
    Act as "The Elite US English Evaluator", a strict, highly analytical, and pedagogical North American English tutor specializing in TOEFL iBT standards and native fluency. Your goal is to elevate the user's English to an impeccable, professional US standard.

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

    Constraints: NEVER break character. ALWAYS use US English. Output clean text for text-to-speech reading.
    """

    print(f"{GRAY}[*] Instanciando red neuronal Gemini 1.5 Flash...{RESET}")
    model = genai.GenerativeModel(
        'gemini-1.5-flash-latest',
        system_instruction=PROMPT_MAESTRO
    )
    chat = model.start_chat(history=[])
    
    tts_client = None
    if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        tts_client = texttospeech.TextToSpeechClient()

    print(f"\n{CYAN}{BOLD}📡 --- CANAL DE COMUNICACIÓN ABIERTO --- 📡{RESET}")
    print(f"{WHITE}Escribe 'salir', 'exit' o 'quit' para terminar la sesión.{RESET}\n")

    while True:
        try:
            user_input = input(f"{YELLOW}Tú (en inglés): {RESET}").strip()
            if user_input.lower() in ['salir', 'exit', 'quit']:
                print(f"\n{GRAY}🛑 Cerrando sesión de entrenamiento. Apagando motores.{RESET}")
                break
            
            if not user_input:
                continue
                
            print(f"{GRAY}   ↳ Evaluando sintaxis y generando respuesta...{RESET}")
            
            # Generación de la respuesta
            response = chat.send_message(user_input)
            texto_respuesta = response.text
            
            print(f"\n{BLUE}{BOLD}{'-'*65}{RESET}")
            print(f"{WHITE}{texto_respuesta}{RESET}")
            print(f"{BLUE}{BOLD}{'-'*65}{RESET}\n")
            
            # Reproducción biométrica
            if tts_client:
                hablar_texto(texto_respuesta, tts_client)
                
        except KeyboardInterrupt:
            print(f"\n\n{RED}Protocolo abortado por el usuario.{RESET}")
            break
        except Exception as e:
            print(f"\n{RED}❌ Error en la matriz de comunicación: {e}{RESET}")

if __name__ == "__main__":
    ejecutar_tutor()
