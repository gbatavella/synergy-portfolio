import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
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

def iniciar_greeter():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 🌐 SYNERGY COMMUNITY GREETER (ONBOARDING BOT) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    # ==========================================
    # 1. CREDENCIALES Y BÚNKER (OPSEC)
    # ==========================================
    load_dotenv()
    # Define TELEGRAM_COMMUNITY_TOKEN en tu archivo .env
    TOKEN = os.getenv("TELEGRAM_COMMUNITY_TOKEN") 

    if not TOKEN:
        print(f"{RED}X [ERROR CRÍTICO] Falta TELEGRAM_COMMUNITY_TOKEN en la bóveda .env.{RESET}")
        print(f"{GRAY}>> Abortando ignición para prevenir fallos en el Long Polling.{RESET}\n")
        sys.exit(1)

    bot = telebot.TeleBot(TOKEN)

    # ==========================================
    # 2. PROTOCOLO DE INTERCEPCIÓN FRONT-END
    # ==========================================
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        nombre_prospecto = message.from_user.first_name
        print(f"{GREEN}[+] Nuevo ingreso en el embudo detectado: {BOLD}{nombre_prospecto}{RESET}")
        
        welcome_text = """
Welcome to the Synergy Humans & AI Agents Community! 🌐🤖

You’ve just stepped into the vanguard of High-Ticket Sales automation. We don't build chat-bots; we engineer Autonomous Sales Clones.

⚡️ **Your Next Steps:**
1. Secure your Complete AI Sales System below.

2. Join the Anglo Mastermind Group (Link provided inside).

The paradigm has shifted. Stop typing. Start closing. How can I assist your deployment today?
"""
        # Creación del botón interactivo (Call to Action)
        markup = InlineKeyboardMarkup()
        btn_gumroad = InlineKeyboardButton(
            text="🛒 Secure The System Now", 
            url="https://batavella.gumroad.com/l/synergyagents"
        )
        markup.add(btn_gumroad)

        bot.reply_to(message, welcome_text, parse_mode='Markdown', reply_markup=markup)

    # ==========================================
    # 3. IGNICIÓN DEL MOTOR DE ESCUCHA
    # ==========================================
    print(f"{GRAY}[*] [SYSTEM ONLINE] Synergy Community Bot desplegado y a la escucha...{RESET}\n")
    try:
        bot.infinity_polling()
    except KeyboardInterrupt:
        print(f"\n{YELLOW} Operación cancelada. Apagando servidor de comunidad...{RESET}\n")

if __name__ == "__main__":
    iniciar_greeter()
