import os
import sqlite3
import requests
import json
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

# --- CÓDIGOS ANSI PARA TERMINAL (LOGGING LOCAL) ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

# 1. CARGA DE BÓVEDA DE SEGURIDAD (OPSEC)
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
admin_password = os.getenv("ADMIN_PASSWORD", "SynergyMaster2026") 
DB_PATH = "synergy_vault.db"

# 2. ARQUITECTURA DE BASE DE DATOS (The Vault)
def init_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS leads 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      timestamp TEXT, 
                      niche TEXT, 
                      contact TEXT, 
                      hook TEXT)''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"{RED}❌ Error al inicializar el Vault SQLite: {e}{RESET}")

def save_lead(niche, contact, intelligence):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO leads (timestamp, niche, contact, hook) VALUES (?, ?, ?, ?)", 
                  (now, niche, contact, intelligence))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"{RED}❌ Error al guardar lead en la bóveda: {e}{RESET}")

init_db()

# 3. CONFIGURACIÓN DE UI & ESTÉTICA ELITE (CSS Injection)
st.set_page_config(page_title="Synergy AI | Autonomous Sales Engine", page_icon="🚀", layout="wide")

st.markdown("""
<style>
/* Botones Estándar - Fucsia a Naranja Corporativo */
div.stButton > button {
    background: linear-gradient(90deg, #FF0080 0%, #FF8C00 100%) !important;
    color: white !important; border: none !important; padding: 1.2rem 2rem !important; 
    font-size: 1.1rem !important; font-weight: 800 !important; border-radius: 50px !important;
    box-shadow: 0 10px 25px -5px rgba(255, 0, 128, 0.4) !important; transition: all 0.3s ease !important;
    text-transform: uppercase !important;
}
div.stButton > button:hover { transform: translateY(-3px) !important; box-shadow: 0 15px 35px -5px rgba(255, 0, 128, 0.6) !important; }

/* Botones de Gumroad / RaaS Deployment */
div.stLinkButton > a {
    background: linear-gradient(90deg, #FF0080 0%, #FF8C00 100%) !important;
    color: white !important; border: none !important; padding: 1.2rem 2rem !important; 
    font-size: 1.1rem !important; font-weight: 800 !important; border-radius: 50px !important;
    text-decoration: none !important; display: block; text-align: center;
    box-shadow: 0 10px 25px -5px rgba(255, 0, 128, 0.4) !important; transition: all 0.3s ease !important;
    text-transform: uppercase !important;
}
div.stLinkButton > a:hover { transform: translateY(-3px) !important; box-shadow: 0 15px 35px -5px rgba(255, 0, 128, 0.6) !important; }

.report-card {
    background: #ffffff; border-left: 10px solid #FF0080; padding: 35px; 
    border-radius: 20px; margin-top: 30px; box-shadow: 0 15px 45px rgba(0,0,0,0.07);
}
.metric-box {
    background: white; border-radius: 30px; padding: 35px; 
    text-align: center; border: 1px solid #f1f3f5; box-shadow: 0 8px 20px rgba(0,0,0,0.03);
}
.price-card {
    background: white; border-radius: 30px; padding: 50px; 
    text-align: center; border-top: 12px solid #FF0080; box-shadow: 0 20px 50px rgba(0,0,0,0.06);
}
</style>
""", unsafe_allow_html=True)

# 4. SECCIÓN HERO (Propuesta de Valor RaaS)
st.markdown("<h1 style='text-align: center; font-size: 4.2rem; font-weight: 900;'>Scale Your Sales To <span style='color: #FF0080;'>Autopilot.</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.5rem; color: #4b5563;'>The World's First <b>Robots-as-a-Service (RaaS)</b> Ecosystem for High-Ticket Closers.</p>", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# MÉTRICAS CLAVE DE INFRAESTRUCTURA
m1, m2, m3 = st.columns(3)
with m1: st.markdown('<div class="metric-box"><h2 style="color:#FF0080; font-size:3.5rem; margin:0;">2.6x</h2><p style="font-weight:700; color:#6b7280; text-transform:uppercase;">ROI Boost</p></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric-box"><h2 style="color:#FF0080; font-size:3.5rem; margin:0;">+10k</h2><p style="font-weight:700; color:#6b7280; text-transform:uppercase;">Leads/Hr</p></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric-box"><h2 style="color:#FF0080; font-size:3.5rem; margin:0;">100%</h2><p style="font-weight:700; color:#6b7280; text-transform:uppercase;">Autonomy</p></div>', unsafe_allow_html=True)

st.write("<br><br>", unsafe_allow_html=True)

# 5. DEMO EN VIVO: TACTICAL INTELLIGENCE SNIPER
st.markdown("<h2 style='text-align: center; font-weight: 800;'>🔴 LIVE DEMO: Tactical Intelligence Sniper</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280; font-size: 1.1rem;'>Enter your niche to extract a <b>High-Value Intelligence Dossier</b> on top-tier targets.</p>", unsafe_allow_html=True)

_, col_demo, _ = st.columns([1, 2, 1])

with col_demo:
    target_niche = st.text_input("🎯 Target Market Niche", placeholder="e.g. Luxury Real Estate in Dubai")
    user_contact = st.text_input("📧 Business Email or WhatsApp (To receive report)", placeholder="e.g. founder@agency.com")
    
    if st.button("🚀 DEPLOY DATA SNIPER", use_container_width=True):
        if target_niche and user_contact:
            if not api_key:
                st.error("❌ [ERROR] Falta la clave GROQ_API_KEY en el entorno.")
            else:
                with st.spinner("Infiltrating market data... Deploying LPU Swarm..."):
                    try:
                        client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=api_key)
                        
                        sniper_prompt = f"""Act as an Elite AI Data Sniper. The user is targeting: '{target_niche}'. 
                        Generate a 'High-Value Intelligence Dossier' for 3 premium targets.
                        For each target, provide a structured profile:
                        - Target Name: (Plausible high-end business in the niche)
                        - Probable Decision Maker: (e.g., CEO, Founder, Head of Sales)
                        - Estimated Lead Value: (e.g., $15,000 - $60,000)
                        - Critical Vulnerability: (e.g., 'Inefficient ad spend', 'Slow mobile response time', 'Fragmented social authority')
                        
                        Conclude with a punchy, aggressive sentence on how the 'Swarm Evolution Protocol' exploits these gaps automatically to dominate.
                        Tone: Professional, High-Ticket, and Urgent. Language: English."""
                        
                        completion = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[{"role": "user", "content": sniper_prompt}]
                        )
                        
                        dossier = completion.choices[0].message.content
                        save_lead(target_niche, user_contact, dossier)
                        
                        st.markdown(f"""
                        <div class="report-card">
                            <h3 style="color: #FF0080; margin-top: 0; font-weight: 800;">🧬 TACTICAL DOSSIER: {target_niche.upper()}</h3>
                            <div style="white-space: pre-wrap; color: #111827; line-height: 1.7; font-size: 1.1rem;">{dossier}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        st.success("Target Intel Acquired. Encrypted and secured in the Vault.")
                    except Exception as e:
                        st.error(f"Intelligence extraction failed: {e}")
        else:
            st.warning("⚠️ Access Denied: Please provide both Target Niche and Contact Info.")

st.write("<br><br>", unsafe_allow_html=True)

# 6. PRECIOS GLOBALES & DESPLIEGUE COMERCIAL
st.markdown("<h2 style='text-align: center; font-weight: 800;'>Select Your Power Level</h2>", unsafe_allow_html=True)
p1, p2 = st.columns(2)

with p1:
    st.markdown("""<div class="price-card"><h3>📦 SYNERGY PRO ENGINE</h3><h1 style="font-size:4rem; margin: 10px 0;">$497</h1><p style="font-size: 1.1rem; color: #4b5563;">5 Autonomous Extraction Agents<br>90-Day Evolution Protocol Included</p></div><br>""", unsafe_allow_html=True)
    st.link_button("🚀 START PRO DEPLOYMENT", "https://batavella.gumroad.com/l/lccwzw", use_container_width=True)

with p2:
    st.markdown("""<div class="price-card" style="border-top-color: #FF8C00;"><h3>💎 SYNERGY ELITE SWARM</h3><h1 style="font-size:4rem; margin: 10px 0;">$997</h1><p style="font-size: 1.1rem; color: #4b5563;">20 Agents + Central Manager<br>Lifetime Access + Full Automation Stack</p></div><br>""", unsafe_allow_html=True)
    st.link_button("⚡ UNLOCK ELITE SWARM", "https://batavella.gumroad.com/l/gwesub", use_container_width=True)

# 7. LEGAL & CUMPLIMIENTO
st.write("<br><hr>", unsafe_allow_html=True)
l1, l2 = st.columns(2)
with l1:
    with st.expander("⚖️ Terms of Service"):
        st.write("All autonomous agents operate under strict RaaS compliance. Data is processed in real-time through the Evolution Protocol.")
with l2:
    with st.expander("🛡️ Data Protection Policy"):
        st.write("Leads are encrypted and stored in local Vaults. We adhere to top-tier security standards for High-Ticket operations.")

st.caption("© 2026 Synergy Humans & AI Agents. Built for the New Sovereign Economy. ClickBank & Gumroad Certified.")

# 8. BÓVEDA DE ADMINISTRACIÓN CIFRADA
st.write("<br><br><br><br>", unsafe_allow_html=True)
with st.expander("🔐 Secure Admin Vault Access (Architects Only)"):
    st.write("Enter your Encryption Key to unlock and download captured intelligence.")
    
    access_key = st.text_input("Vault Key:", type="password")
    
    if access_key:
        if access_key == admin_password:
            st.success("Access Granted. Vault Decrypted.")
            try:
                conn = sqlite3.connect(DB_PATH)
                df = pd.read_sql_query("SELECT * FROM leads", conn)
                conn.close()
                
                if not df.empty:
                    csv_data = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 DOWNLOAD INTELLIGENCE VAULT (CSV)",
                        data=csv_data,
                        file_name='synergy_intelligence_vault.csv',
                        mime='text/csv',
                    )
                else:
                    st.info("The Vault is currently empty. Waiting for targets.")
            except Exception as e:
                st.error(f"Vault decryption error: {e}")
        else:
            st.error("❌ Invalid Encryption Key. Intrusion attempt logged.")
