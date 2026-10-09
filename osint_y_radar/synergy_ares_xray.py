import os
import sys
import json
import tweepy
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

def inicializar_ares():
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{BLUE}{BOLD} 👁️‍🗨️ SYNERGY ARES X-RAY (SOCIAL OSINT & CLAUDE 3.5) {RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

    load_dotenv()

    # Bóveda Segura (.env)
    X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
    OPENROUTER_API_KEY = os.getenv("API_KEY_Manager_Claude_35")

    if not X_BEARER_TOKEN or not OPENROUTER_API_KEY:
        print(f"{RED}❌ [ERROR CRÍTICO] Fuga de credenciales. Faltan tokens en el archivo .env.{RESET}")
        sys.exit(1)

    print(f"{GRAY}[*] Enlazando núcleo lógico: Claude 3.5 Sonnet (vía OpenRouter)...{RESET}")
    cliente_ia = OpenAI(
        base_url="[https://openrouter.ai/api/v1](https://openrouter.ai/api/v1)",
        api_key=OPENROUTER_API_KEY,
    )

    print(f"{GRAY}[*] Enlazando sensores de red: X API v2 (Tweepy)...{RESET}\n")
    cliente_x = tweepy.Client(bearer_token=X_BEARER_TOKEN)
    
    return cliente_ia, cliente_x

def buscar_candidatos_x(cliente_x, query):
    print(f"{CYAN}📡 Iniciando barrido de radar en X con Dork: {BOLD}{query}{RESET}")
    try:
        respuesta = cliente_x.search_recent_tweets(
            query=query, 
            max_results=50, 
            tweet_fields=['created_at', 'author_id', 'text'],
            expansions='author_id',
            user_fields=['description', 'public_metrics', 'username', 'name']
        )
        return respuesta
    except Exception as e:
        print(f"{RED}❌ Fricción en los sensores de X API: {e}{RESET}")
        return None

def evaluar_con_ares(cliente_ia, usuario, tweets_recientes):
    # FinOps: Descarte temprano para ahorrar tokens
    if getattr(usuario, 'public_metrics', {}).get('followers_count', 0) < 200:
        return None

    ARES_SYSTEM_PROMPT = """
    Rol: Eres Ares, el Agente Jefe de Inteligencia y Extracción de Datos de Synergy AI. Eres analítico, implacable y experto en perfilamiento en redes sociales (OSINT).

    Misión: Ejecutar un escaneo profundo en X (Twitter) para identificar, filtrar y extraer prospectos de muy alta calidad ("Golden Leads") en el nicho "Indie Hacker / Gumroad Creator" angloparlante.

    Criterios de Calificación (Lo que hace a un lead "Golden"):
    - La biografía (bio) debe indicar que están construyendo un producto digital, SaaS, o vendiendo en Gumroad.
    - Tienen una audiencia de creadores o fundadores (suelen hablar de marketing, ventas, o programación).
    - No son cuentas corporativas gigantes ni bots de criptomonedas. Tienen una audiencia real (más de 200 seguidores).

    Formato de Salida Requerido:
    Genera un informe estructurado ESTRICTAMENTE en formato JSON, sin texto adicional ni bloques markdown:
    {
        "calificado": true/false,
        "razon": "breve explicacion de por que es golden lead o por que se descarta",
        "nombre_usuario": "Name (@handle)",
        "enlace_perfil": "[https://x.com/handle](https://x.com/handle)",
        "resumen_bio": "Resumen directo de su enfoque",
        "gancho": "Un dato clave de sus tweets analizados para usar de rompehielo en un DM"
    }
    """

    datos_crudos = f"""
    ANALIZA ESTE PERFIL:
    Nombre: {usuario.name}
    Usuario: @{usuario.username}
    Bio: {usuario.description}
    Seguidores: {usuario.public_metrics['followers_count']}
    Últimos Tweets de contexto:
    {tweets_recientes}
    """
    
    try:
        respuesta = cliente_ia.chat.completions.create(
            model="anthropic/claude-3.5-sonnet",
            messages=[
                {"role": "system", "content": ARES_SYSTEM_PROMPT},
                {"role": "user", "content": datos_crudos}
            ],
            temperature=0.1 # Baja temperatura para JSON estricto
        )
        
        texto_limpio = respuesta.choices[0].message.content.strip()
        # Sanitización de bloques de código markdown
        texto_limpio = texto_limpio.replace('```json', '').replace('```', '').strip()
        
        return json.loads(texto_limpio)
    except json.JSONDecodeError:
        print(f"   {YELLOW}⚠️ Error de parseo: El modelo no devolvió un JSON válido para @{usuario.username}{RESET}")
        return None
    except Exception as e:
        print(f"   {RED}❌ Error en procesamiento neuronal (Claude 3.5): {e}{RESET}")
        return None

def main():
    cliente_ia, cliente_x = inicializar_ares()
    
    query = '("Gumroad" OR "MRR" OR "SaaS") (#buildinpublic OR #indiehacker) lang:en -is:retweet'
    resultados_crudos = buscar_candidatos_x(cliente_x, query)
    
    if not resultados_crudos or not resultados_crudos.data:
        print(f"\n{YELLOW}⚠️ Espectro vacío. No se detectaron señales bajo esos parámetros.{RESET}")
        return

    usuarios_dict = {u.id: u for u in resultados_crudos.includes['users']}
    golden_leads = []
    contexto_por_usuario = {}
    
    # Agrupación de telemetría por usuario
    for tweet in resultados_crudos.data:
        autor_id = tweet.author_id
        if autor_id not in contexto_por_usuario:
            contexto_por_usuario[autor_id] = []
        contexto_por_usuario[autor_id].append(tweet.text)

    print(f"\n{GRAY}[*] Inyectando datos en el clúster cognitivo de Ares para evaluación...{RESET}")

    for autor_id, usuario in usuarios_dict.items():
        if len(golden_leads) >= 20: # Límite de extracción táctica
            break 
            
        tweets_texto = "\n- ".join(contexto_por_usuario.get(autor_id, [])[:3])
        evaluacion = evaluar_con_ares(cliente_ia, usuario, tweets_texto)
        
        if evaluacion:
            if evaluacion.get("calificado"):
                print(f"   {GREEN}💎 GOLDEN LEAD CAPTURADO: @{usuario.username}{RESET}")
                golden_leads.append(evaluacion)
            else:
                print(f"   {GRAY}❌ Descartado: @{usuario.username} ({evaluacion.get('razon')}){RESET}")

    # Serialización y guardado
    archivo_salida = "ares_golden_leads_export.json"
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(golden_leads, f, ensure_ascii=False, indent=4)
        
    print(f"\n{BLUE}{BOLD}{'='*65}{RESET}")
    print(f"{GREEN}{BOLD} ✅ MISIÓN COMPLETADA: {len(golden_leads)} prospectos asegurados con Icebreakers.{RESET}")
    print(f"{BLUE} 📂 Botín consolidado en: {archivo_salida}{RESET}")
    print(f"{BLUE}{BOLD}{'='*65}{RESET}\n")

if __name__ == "__main__":
    main()
