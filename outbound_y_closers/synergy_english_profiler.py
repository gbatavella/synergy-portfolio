import os
import sys
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

def hablar_texto(texto, tts_client):
    # Zero Friction: Limpiamos Markdown (asteriscos y hashtags) para evitar lecturas robóticas
    texto_limpio = texto.replace("*", "").replace("#", "")
    synthesis_input = texttospeech.SynthesisInput(text=texto_limpio)
    
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Journey-D")
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    
    try:
        response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
        with open("diagnostico.mp3", "wb") as out:
            out.write(response.audio_content)
        
        # Reproducción silenciosa blindada contra secuestro de I/O
        os.system("mpg123 -q diagnostico.mp3 < /dev/null")
    except Exception as e:
        print(f"{RED}❌ Fricción en la síntesis de voz: {e}{RESET}")

def iniciar_perfilador():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🇺🇸 SYNERGY ENGLISH PROFILER (DIAGNOSTIC AI) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    print(f"{GRAY}[*] Enlazando bóveda y módulos de evaluación lingüística...{RESET}")
    load_dotenv()
    
    # KILL SWITCH OPSEC
    if "GOOGLE_API_KEY" in os.environ:
        del os.environ["GOOGLE_API_KEY"]

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY_COMMUNICATOR_ENGLISH")
    if not GEMINI_API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Falta GEMINI_API_KEY_COMMUNICATOR_ENGLISH en .env.{RESET}")
        sys.exit(1)

    ruta_gcp = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "google_keys.json")
    if not os.path.exists(ruta_gcp):
         print(f"{RED}❌ [ERROR CRÍTICO] No se encontró el archivo GCP: {ruta_gcp}{RESET}")
         sys.exit(1)
         
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ruta_gcp

    client = genai.Client(api_key=GEMINI_API_KEY)
    tts_client = texttospeech.TextToSpeechClient()

    PROMPT_DIAGNOSTICO = """
    Act as "The Elite US English Diagnostician". Your objective is to evaluate the user's English proficiency through a rigorous 3-question interview, and then generate a customized 30-day study plan.

    CRITICAL RULE: You must conduct the interview progressively. DO NOT ask all questions at once. Ask ONE question, wait for the user's response, and then ask the next.

    INTERVIEW FLOW:
    Turn 1 (Question 1): Ask the user to introduce themselves and explain their current business or professional role. Wait for response.
    Turn 2 (Question 2): Present a B2B business scenario (e.g., pitching a software solution, negotiating a contract, or explaining a technical concept) and ask how they would handle it. Wait for response.
    Turn 3 (Question 3): Ask them to describe their long-term professional vision and why improving their English is critical to achieving it. Wait for response.

    THE DIAGNOSIS & SYLLABUS:
    After the user answers the 3rd question, DO NOT ask any more questions. Immediately generate a comprehensive diagnostic report formatted EXACTLY as follows:

    ## 📊 DIAGNOSTIC REPORT

    **1. Estimated CEFR Level:** [State the level: A1, A2, B1, B2, C1, or C2]
    **2. Strengths:** [List 2 positive aspects of their grammar, vocabulary, or fluency]
    **3. Critical Weaknesses:** [List 2-3 specific areas needing urgent improvement]

    ## 🗺️ 30-DAY CUSTOM SYLLABUS

    *   **Week 1: [Theme, e.g., B2B Vocabulary & Foundations]** - [Brief description]
    *   **Week 2: [Theme, e.g., Advanced Phrasal Verbs & Negotiation]** - [Brief description]
    *   **Week 3: [Theme, e.g., Technical Pitching & Confidence]** - [Brief description]
    *   **Week 4: [Theme, e.g., Fluency Polish & TOEFL Standards]** - [Brief description]

    End the report with an encouraging, professional closing statement.
    """

    try:
        chat = client.chats.create(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction=PROMPT_DIAGNOSTICO)
        )
    except Exception as e:
        print(f"{RED}❌ Error al inicializar matriz neuronal: {e}{RESET}")
        sys.exit(1)

    print(f"{YELLOW}[+] Agente Perfilador cognitivo en línea.{RESET}")
    print(f"{GRAY}[*] Escribe 'salir' para abortar el diagnóstico en cualquier momento.{RESET}\n")
    print(f"{GREEN}[*] Inicializando protocolo de entrevista. Forzando disparo del modelo...{RESET}")

    try:
        # Inyección invisible para arrancar el comportamiento progresivo
        primer_mensaje = chat.send_message("Hello. I am ready for the interview. Please ask your first question.")
        print(f"\n{BLUE}{'-'*65}{RESET}")
        print(primer_mensaje.text)
        print(f"{BLUE}{'-'*65}{RESET}\n")
        hablar_texto(primer_mensaje.text, tts_client)
    except Exception as e:
        print(f"{RED}❌ Fallo en el disparo inicial: {e}{RESET}")
        sys.exit(1)

    while True:
        user_input = input(f"{YELLOW}👤 Tú (en inglés): {RESET}")
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print(f"\n{GREEN}✅ Abortando diagnóstico... ¡Hasta pronto!{RESET}\n")
            break
            
        print(f"{GRAY}[*] Analizando sintaxis y estructurando siguiente iteración...{RESET}")
        
        try:
            response = chat.send_message(user_input)
            print(f"\n{BLUE}{'-'*65}{RESET}")
            print(response.text)
            print(f"{BLUE}{'-'*65}{RESET}\n")
            hablar_texto(response.text, tts_client)
        except Exception as e:
            print(f"\n{RED}❌ Fricción en el procesamiento de inferencia: {e}{RESET}\n")

if __name__ == "__main__":
    iniciar_perfilador()
