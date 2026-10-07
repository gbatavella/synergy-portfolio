import json
import pywhatkit
import time
import re
import os
from dotenv import load_dotenv

# Cargar variables de entorno (El archivo .env NO se sube a GitHub)
load_dotenv()

print("🔥 Iniciando Sistema Outbound B2B...")

# 1. Conexión a la base de datos (Archivo dummy para el repo)
archivo_leads = os.getenv("LEADS_FILE", "dummy_leads.json")
print(f"📂 Cargando prospectos desde {archivo_leads}...")

try:
    with open(archivo_leads, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    print(f"❌ Error: Asegúrate de tener tu archivo de leads configurado.")
    exit()

empresas = datos.get("empresas_target", [])

# Filtro de palabras clave abstractas (Se cargan desde un config o .env)
# En el repo público, mostramos una lista de ejemplo genérica.
palabras_prohibidas = os.getenv("BLACKLIST_KEYWORDS", "competidor,spam,no_contactar").split(",")

# 2. Ignición de la secuencia de mensajería
for empresa_data in empresas:
    empresa = empresa_data.get("content", empresa_data)
    
    telefono = empresa.get("telefono", "NA")
    nombre = empresa.get("nombre_empresa", "Empresa")
    rubro = empresa.get("rubro", "").lower()
    
    if telefono == "NA" or not telefono:
        continue
        
    if any(palabra.strip() in rubro for palabra in palabras_prohibidas):
        print(f" 🚫 Omitiendo {nombre}: Rubro filtrado.")
        continue

    # Lógica de Normalización de Teléfonos (Tu IP técnica, esto SÍ se muestra porque prueba tu nivel)
    telefono_aislado = str(telefono).split('/')[0].split('y')[0]
    num_limpio = re.sub(r'\D', '', telefono_aislado) 
    
    if num_limpio.startswith("549"):
        numero_formateado = "+" + num_limpio
    elif num_limpio.startswith("54"):
        numero_formateado = "+549" + num_limpio[2:]
    else:
        if num_limpio.startswith("0"): num_limpio = num_limpio[1:]
        if num_limpio.startswith("11"): num_limpio = num_limpio[2:]
        if num_limpio.startswith("15"): num_limpio = num_limpio[2:]
        numero_formateado = "+54911" + num_limpio[-8:] 
    
    # 2.3 El Mensaje Estratégico oculto en variable de entorno
    # Si no hay variable, usa un mensaje genérico de placeholder
    mensaje_template = os.getenv("OUTBOUND_MESSAGE", "Hola equipo de {nombre}. Nos contactamos para explorar sinergias comerciales.")
    mensaje = mensaje_template.format(nombre=nombre)
    
    print(f"📱 Intentando enviar a: {numero_formateado}...")
    
    try:
        pywhatkit.sendwhatmsg_instantly(numero_formateado, mensaje, 15, True, 3)
        print("✅ Mensaje despachado.")
        time.sleep(15) # Pausa anti-spam
    except Exception as e:
        print(f"❌ Fricción: {e}")
