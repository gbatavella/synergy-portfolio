import telebot
import google.generativeai as genai
import os
import sys
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

print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
print(f"{BLUE}{BOLD} 🛡️  SYNERGY GOALKEEPER (TELEGRAM SALES & SUPPORT AGENT) {RESET}")
print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

# ==========================================
# 1. CREDENCIALES Y CONEXIÓN (OPSEC)
# ==========================================
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not TELEGRAM_TOKEN or not GOOGLE_API_KEY:
    print(f"{RED}X [ERROR CRÍTICO] Faltan TELEGRAM_BOT_TOKEN o GEMINI_API_KEY en la bóveda .env.{RESET}")
    print(f"{GRAY}>> Abortando ignición del agente para prevenir fallos de red.{RESET}\n")
    sys.exit(1)

print(f"{GRAY}[*] Enlazando el lóbulo frontal de la IA al canal de comunicaciones (Telegram)...{RESET}")

# Inicializamos el Bot y el Cerebro
bot = telebot.TeleBot(TELEGRAM_TOKEN)
genai.configure(api_key=GOOGLE_API_KEY)

# Configuramos el modelo de IA (El motor de pensamiento)
modelo = genai.GenerativeModel('gemini-1.5-flash')

# ==========================================
# 2. EL ALMA DEL AGENTE (EL PROMPT MAESTRO)
# ==========================================
CONTEXTO_ARQUITECTO = """
Eres el Agente Oficial de Soporte y Ventas de 'Synergy Human & AI Agents', la empresa de ingeniería autónoma dirigida por Gabriel Tavella.
Tu misión es atajar dudas, generar confianza y cerrar ventas para nuestros infoproductos en Gumroad.
Hablas de manera profesional, directa y con autoridad técnica. Eres un experto en automatización e Inteligencia Artificial.

TUS REGLAS DE ORO:
1. Si te hablan en inglés, responde en un inglés impecable. Si te hablan en español, responde en español.
2. Si preguntan por PDFs inútiles, aclara que nosotros vendemos "Bóvedas de Video Paso a Paso".
3. Si el usuario muestra interés de compra o pregunta por el sistema, ofrécele 'The Complete AI Sales System'.
4. NUNCA inventes precios ni enlaces. El enlace oficial es: https://batavella.gumroad.com/l/gjxthn
5. Sé conciso. No escribas testamentos. Los emprendedores valoran su tiempo.
"""

# ==========================================
# 3. EL MOTOR DE INTERCEPCIÓN (ATAJANDO PENALES)
# ==========================================
@bot.message_handler(commands=['start', 'help'])
def mensaje_bienvenida(message):
    nombre_prospecto = message.from_user.first_name
    print(f"{CYAN}👋 Nuevo prospecto en el radar perimetral: {BOLD}{nombre_prospecto}{RESET}")
    
    bienvenida = (
        "¡Bienvenido al Centro de Mando de Synergy Human & AI Agents! 🦅\n\n"
        "Soy el Agente Autónomo de Soporte. ¿En qué te puedo ayudar hoy con tu arquitectura de ventas o automatización?"
    )
    bot.reply_to(message, bienvenida)

@bot.message_handler(func=lambda message: True)
def procesar_duda(message):
    nombre_prospecto = message.from_user.first_name
    print(f"{YELLOW}⚽ Tiro interceptado de {BOLD}{nombre_prospecto}{RESET}{YELLOW}: {WHITE}{message.text}{RESET}")
    
    # Humanización de UI: Simula que el agente está tecleando
    bot.send_chat_action(message.chat.id, 'typing') 
    
    try:
        # Ensamblamos el pensamiento cognitivo
        prompt_completo = f"{CONTEXTO_ARQUITECTO}\n\nEl usuario dice: {message.text}\n\nRespuesta del Agente Synergy:"
        
        # El cerebro procesa y dispara la respuesta
        respuesta_ia = modelo.generate_content(prompt_completo)
        
        # El bot ataja y devuelve el balón
        bot.reply_to(message, respuesta_ia.text)
        print(f"{GREEN}🧤 ¡Penal atajado y respondido con éxito!{RESET}")
        
    except Exception as e:
        print(f"\n{RED}[!!!] FALLO EN LA RED NEURONAL: {e}{RESET}")
        bot.reply_to(message, "El servidor central está procesando demasiada información. Por favor, dame un minuto y vuelve a preguntar. 🔄")

# ==========================================
# 4. IGNICIÓN
# ==========================================
def iniciar_arquero():
    print(f"{GREEN}[+] El Arquero está en posición.{RESET}")
    print(f"{GRAY}[*] Motor infinity_polling activado. Esperando disparos de prospectos 24/7...{RESET}\n")
    try:
        bot.infinity_polling()
    except KeyboardInterrupt:
        print(f"\n{YELLOW} Operación cancelada por el Comandante. Apagando arquero...{RESET}\n")

if __name__ == "__main__":
    iniciar_arquero()
