import time
import os
import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv

# --- CÓDIGOS ANSI PARA TERMINAL (LOGGING LOCAL) ---
BLUE = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

# --- 1. CONFIGURACIÓN OBLIGATORIA DE STREAMLIT (Debe ser el primer comando de ST) ---
st.set_page_config(
    page_title="Synergy AI | Autonomous Engine", 
    page_icon="🚀", 
    layout="wide"
)

load_dotenv()

# --- 2. 👁️ RADAR SYNERGY: Google Analytics 4 (Modo Invisible) ---
codigo_ga4 = """
<script async src="https://www.googletagmanager.com/gtag/js?id=G-T38CCXEWWK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-T38CCXEWWK');
</script>
"""
try:
    components.html(codigo_ga4, width=0, height=0)
except Exception:
    pass

# --- 3. INYECCIÓN DE ESTILOS CSS ELITE ---
st.markdown("""
<style>
    /* Fondo Limpio y Tipografía Corporativa */
    .stApp {
        background-color: #f8fafc;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    /* Tarjetas Blancas Elegantes */
    div[data-testid="column"] {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border: 1px solid #e2e8f0;
    }
    
    /* BOTONES CON GRADIENTE SYNERGY (Fucsia a Naranja) */
    .stButton>button, a[data-testid="stLinkButton"] {
        background: linear-gradient(135deg, #ff007f 0%, #ff5e00 100%) !important;
        color: white !important;
        font-weight: 800;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        width: 100%;
        text-align: center;
        transition: transform 0.2s, box-shadow 0.2s;
        text-decoration: none !important;
    }
    
    .stButton>button:hover, a[data-testid="stLinkButton"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(255, 94, 0, 0.4);
    }

    /* Encabezados Principales */
    .main-title {
        color: #0f172a;
        font-weight: 900;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    .sub-title {
        color: #475569;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    /* Ocultar barra de navegación lateral por defecto */
    [data-testid="collapsedControl"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. CONTROL DE ESTADO DEL SISTEMA (Memory Flow) ---
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"
if 'demo_consumed' not in st.session_state:
    st.session_state['demo_consumed'] = False
if 'last_report' not in st.session_state:
    st.session_state['last_report'] = None

# ==========================================
# PÁGINA 1: TERMINAL DE OPERACIONES (HOME)
# ==========================================
if st.session_state.current_page == "home":
    st.markdown("<div class='main-title'>Enterprise-Grade Sales Architecture</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Automate lead extraction, psychological profiling, and deal closing on the open web. Zero code required.</div>", unsafe_allow_html=True)

    # Manifiesto de Video (Asegúrate de cambiar la URL por tu recurso definitivo)
    st.video("https://www.youtube.com/watch?v=Rj6ahdmKGmA")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚡ Live Dynamic Extraction")
        st.write("Enter your niche. The swarm will extract real intelligence in 45 seconds.")
        
        niche = st.text_input("Enter your Target Niche:", placeholder="e.g., High-Ticket Coaches Miami", label_visibility="collapsed")
        
        if st.button("EXECUTE EXTRACTION (BETA)"):
            if st.session_state['demo_consumed']:
                st.warning("⚠️ Demo consumed. Your session footprint registers a previous extraction.")
                st.info("Here is your last generated report from the server cache:")
                st.markdown(st.session_state['last_report'])
                st.link_button("🔥 Unlock Unlimited Searches ($997)", "https://batavella.gumroad.com/l/gwesub")
            else:
                if niche:
                    with st.spinner(f"Connecting to the Swarm. Analyzing open web for '{niche}'..."):
                        progress_bar = st.progress(0)
                        for percent_complete in range(100):
                            time.sleep(0.04)
                            progress_bar.progress(percent_complete + 1)
                        
                        generated_report = f"""
                        ### 🎯 Intelligence Sample: {niche}
                        * **Target Level:** Tier 1 Providers
                        * **Decision Maker:** Founder / CEO
                        * **Vulnerability:** High Customer Acquisition Cost (CAC) / Low automation.
                        * **Synergy Tactic:** Deploy 'Goalkeeper' agent for stealth outreach demonstrating immediate ROI.
                        """
                        st.session_state['last_report'] = generated_report
                        st.session_state['demo_consumed'] = True
                        
                        st.success("Extraction and Profiling Complete.")
                        st.markdown(generated_report)
                        st.link_button("🚀 Deploy My Swarm Now ($97)", "https://batavella.gumroad.com/l/lccwzw")
                else:
                    st.error("Please enter a target niche for the agents to initiate the search.")

    with col2:
        st.subheader("🤖 For the Tech Visionary")
        st.write("Explore the engine. Simulate the infiltration. Discover AGI capabilities.")
        st.write("Enter the laboratory to see how our agents infiltrate high-ticket markets in real-time.")
        st.write("") 
        if st.button("ACCESS GEOLEPLEX EXPERIENCE"):
            st.session_state.current_page = "geoleplex"
            st.rerun()

    st.divider()
    st.markdown("<h3 style='text-align: center; color: #0f172a;'>Select Your Power Level</h3>", unsafe_allow_html=True)
    
    _, col_btn_2, _ = st.columns([1, 2, 1])
    with col_btn_2:
        st.link_button("🔥 FULL SWARM ACCESS ($997)", "https://batavella.gumroad.com/l/gwesub")

# ==========================================
# PÁGINA 2: LABORATORIO GEOLEPLEX (SIMULADOR)
# ==========================================
elif st.session_state.current_page == "geoleplex":
    if st.button("⬅ Return to Command Center"):
        st.session_state.current_page = "home"
        st.rerun()
        
    st.markdown("<div class='main-title'>🔬 GEOLEPLEX Lab</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Synergy Dynamic Infiltration Simulator</div>", unsafe_allow_html=True)

    col_sim1, col_sim2 = st.columns([1, 2])
    
    with col_sim1:
        st.subheader("Mission Parameters")
        scenario = st.selectbox("Infiltration Target:", ["Autonomous Tesla Fleet (Elon Mode)", "Dubai Real Estate (High-Ticket)"])
        ai_level = st.slider("Agent Autonomy Level:", min_value=1, max_value=10, value=5)
        mode = st.radio("Operation Mode:", ["Stealth Infiltration", "Mass Extraction Attack"])
        initiate = st.button("🚀 INITIATE SIMULATION")

    with col_sim2:
        st.subheader("Operations Console (War Room)")
        if initiate:
            st.success(f"Protocol activated: {scenario} | Mode: {mode}")
            st.code(f"[13:24:01] INITIATING PROTOCOL...\n[13:24:02] AI Level set to: {ai_level}/10\n[13:24:03] Sniper V5 deployed. Scanning open web...", language="bash")
            
            if scenario == "Autonomous Tesla Fleet (Elon Mode)":
                st.code("[13:24:05] Sniper V5: Corporate fleet bid detected.\n[13:24:06] Profiler: Analyzing psychology... 'Analytical-Conservative' confirmed.\n[13:24:10] Goalkeeper: Message drafted focusing on 5-year ROI. Sending...\n[13:24:12] CLOSING ALERT: Positive response received. Scheduling demo.", language="bash")
                if ai_level > 7:
                    st.warning("⚡ AGI LEVEL DETECTED: 3 hidden bids identified via patent cross-referencing.")
            else:
                st.code("[13:24:05] Sniper V5: Family Office interested in diversification identified.\n[13:24:06] Profiler: Extracting history. Preference for ultra-luxury beachfront.\n[13:24:10] Goalkeeper: Initiating outreach via private network.\n[13:24:12] CLOSING ALERT: Interest confirmed. Transfer to Closer initiated.", language="bash")
                if ai_level > 7:
                    st.warning("⚡ AGI LEVEL DETECTED: Price dynamically adapting to real-time liquidity.")
            
            st.metric(label="Estimated Revenue Potential (30 Days)", value=f"${ai_level * 125000:,.0f} USD", delta="+ Exponential Growth")
        else:
            st.info("Awaiting mission parameters. Configure the left panel and click Initiate Simulation.")

    st.divider()
    st.markdown("<p style='text-align: center; font-size: 1.2rem; font-weight: bold;'>Witnessed the power of the swarm?</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Connect with our top-tier concierge to profile your specific business model.</p>", unsafe_allow_html=True)
    
    _, col_t2, _ = st.columns([1, 2, 1])
    with col_t2:
        st.link_button("🤖 Initiate Triage with AI Manager", "https://t.me/SynergyCommunity_bot")
