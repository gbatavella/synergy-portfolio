import streamlit as st

# ==========================================
# 1. ENTERPRISE BRAND CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Synergy AI | Global Autonomous Infrastructure", 
    page_icon="🌐", 
    layout="wide"
)

# CSS for High-Ticket Aesthetics
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 4px; height: 3.5em; font-weight: bold; transition: 0.3s; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 4px 15px rgba(0,82,255,0.4); }
    .main { background-color: #050505; }
    div[data-testid="stExpander"] { border: 1px solid #262730; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. HERO SECTION
# ==========================================
st.title("The Industrial Revolution of B2B Sales.")
st.markdown("### Deploy autonomous agent swarms that source, profile, and close deals while you sleep.")
st.divider()

# ==========================================
# 3. TIER SELECTION (CHECKOUT ROUTING)
# ==========================================
st.header("Select Your Deployment Level")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📦 STARTER")
    st.write("Perfect for solo consultants.")
    st.markdown("## **$197**")
    st.write("- Core Swarm Engine\n- Basic Profiler\n- Local Data Storage")
    st.link_button("GET STARTED", "https://lemon-squeezy-link-197.com", use_container_width=True)

with col2:
    st.markdown("### 🚀 PRO (Most Popular)")
    st.write("For growing agencies.")
    st.markdown("## **$497**")
    st.write("- **CRM Webhook Integration**\n- Advanced Evasion Protocols\n- Priority API Routing")
    st.link_button("DEPLOY PRO", "https://lemon-squeezy-link-497.com", use_container_width=True)

with col3:
    st.markdown("### 💎 PLATINUM")
    st.write("Enterprise-grade power.")
    st.markdown("## **$997**")
    st.write("- **Infinite Parallel Swarms**\n- **Neural Brand Voice Cloning**\n- **White-Label Reporting**")
    st.link_button("GO PLATINUM", "https://lemon-squeezy-link-997.com", use_container_width=True)

st.divider()

# ==========================================
# 4. HIGH-TICKET QUALIFICATION FUNNEL
# ==========================================
st.header("Custom Enterprise Solutions")
with st.expander("Apply for Full System Implementation ($5,000+)"):
    col_left, col_right = st.columns(2)
    with col_left:
        mrr = st.selectbox("Current Agency MRR:", ["$0 - $10k", "$10k - $50k", "$50k - $100k", "$100k+"])
    with col_right:
        niche = st.text_input("Target Market / Niche:")
    
    if st.button("REQUEST EXECUTIVE BRIEFING"):
        if mrr == "$0 - $10k":
            st.warning("We recommend starting with the Pro or Platinum scripts to scale your infrastructure first.")
        else:
            st.success("Profile Qualified. Our team will contact you for a technical assessment.")

st.caption("© 2026 Synergy Humans & Agents AI | Tier 1 Operations")
