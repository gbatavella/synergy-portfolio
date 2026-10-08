from google.cloud import texttospeech
import os
import time
import sys
from dotenv import load_dotenv

# --- SEGURIDAD Y CONFIGURACIÓN ---
load_dotenv()

# --- CÓDIGOS ANSI PARA TERMINAL ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def rapid_output(text, delay=0.02):
    print(text)
    time.sleep(delay)

def generar_audio(texto, nombre_archivo="entrenamiento_ventas_b2b.mp3"):
    print(f"\n{BLUE}{BOLD}{'='*60}{RESET}")
    print(f"{BLUE}{BOLD} 🎙️ SYNERGY SALES COACH (VOICE SYNTHESIS PROTOCOL) {RESET}")
    print(f"{BLUE}{BOLD}{'='*60}{RESET}\n")
    
    # Verificación de OPSEC: Comprobar credenciales de Google Cloud
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        rapid_output(f"{YELLOW}[!] ADVERTENCIA: Variable GOOGLE_APPLICATION_CREDENTIALS no detectada.{RESET}")
        rapid_output(f"{GRAY}>> El SDK de Google Cloud intentará usar la autenticación por defecto del sistema.{RESET}\n")

    rapid_output(f"{GRAY}[*] Iniciando cliente Google Cloud Text-to-Speech...{RESET}")
    
    try:
        # Instancia el cliente de GCP
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=texto)

        rapid_output(f"{GRAY}[*] Configurando modelo acústico (Serie Premium 'Journey')...{RESET}")
        # Configura la voz (Inglés US, voz masculina premium)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Journey-D" 
        )

        # Configura el archivo de salida (MP3) a velocidad conversacional
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=0.95 
        )

        rapid_output(f"{YELLOW}⏳ Compilando síntesis neuronal y descargando payload...{RESET}")
        # Ejecuta la solicitud a los servidores de Google
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Escribe los bytes en el archivo local
        with open(nombre_archivo, "wb") as out:
            out.write(response.audio_content)
            
        print(f"\n{GREEN}{BOLD}✅ EXTRACCIÓN EXITOSA: Archivo de audio generado.{RESET}")
        print(f"{BLUE}>> Ubicación: {os.path.abspath(nombre_archivo)}{RESET}\n")
        
    except Exception as e:
        print(f"\n{RED}❌ Error crítico de infraestructura GCP: {e}{RESET}")
        print(f"{GRAY}>> Verifica tu archivo credentials.json y tus permisos IAM.{RESET}\n")

if __name__ == "__main__":
    # Texto de entrenamiento (Manejo de Objeciones B2B)
    texto_practica = """
    Actually, David, our AI doesn't guess. If it faces a complex question, 
    it instantly queries your custom knowledge base in milliseconds. 
    The prospect gets a perfect, seamless answer, exactly as if they were talking to you. 
    We don't sell replacement, we sell Synergy.
    """
    
    generar_audio(texto_practica)
