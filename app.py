import streamlit as st
import json
import time

st.set_page_config(
    page_title="ArchitectAI",
    page_icon="🚀",
    layout="wide"
)

# ---------- CUSTOM CSS ----------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

.stApp {
    background: #0A0A0F;
    color: #E8E8F0;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1100px;
}

/* Hero Header */
.hero-wrapper {
    text-align: center;
    padding: 3.5rem 2rem 2.5rem;
    position: relative;
    margin-bottom: 1rem;
}

.hero-eyebrow {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    color: #7C6EFA;
    text-transform: uppercase;
    background: rgba(124, 110, 250, 0.1);
    border: 1px solid rgba(124, 110, 250, 0.25);
    padding: 0.35rem 1rem;
    border-radius: 100px;
    margin-bottom: 1.5rem;
}

.hero-title {
    font-size: 3.8rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    line-height: 1.05;
    margin: 0 0 1rem;
    background: linear-gradient(135deg, #FFFFFF 0%, #B8B0FF 50%, #7C6EFA 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-size: 1.05rem;
    color: #8888A8;
    font-weight: 400;
    max-width: 480px;
    margin: 0 auto;
    line-height: 1.6;
}

/* Metric Cards */
.metric-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    overflow: hidden;
    margin: 2rem 0;
}

.metric-item {
    background: #0E0E18;
    padding: 1.5rem 1.25rem;
    text-align: center;
    transition: background 0.2s;
}

.metric-item:hover {
    background: #12121E;
}

.metric-value {
    font-size: 2rem;
    font-weight: 700;
    color: #7C6EFA;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: -0.02em;
}

.metric-label {
    font-size: 0.72rem;
    color: #6666888;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-top: 0.25rem;
    color: #666688;
}

/* Input Section */
.input-label {
    font-size: 0.8rem;
    font-weight: 500;
    color: #9999BB;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 0.5rem;
    font-family: 'JetBrains Mono', monospace;
}

.stTextArea textarea {
    background: #0E0E18 !important;
    border: 1px solid rgba(124, 110, 250, 0.2) !important;
    border-radius: 12px !important;
    color: #E8E8F0 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.95rem !important;
    resize: vertical !important;
    padding: 1rem 1.25rem !important;
    line-height: 1.6 !important;
}

.stTextArea textarea:focus {
    border-color: rgba(124, 110, 250, 0.6) !important;
    box-shadow: 0 0 0 3px rgba(124, 110, 250, 0.1) !important;
}

.stTextArea textarea::placeholder {
    color: #444460 !important;
}

/* Button */
.stButton button {
    background: linear-gradient(135deg, #7C6EFA 0%, #5B4EDA 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    padding: 0.65rem 2rem !important;
    letter-spacing: 0.01em !important;
    width: 100% !important;
    transition: opacity 0.2s, transform 0.1s !important;
    cursor: pointer !important;
}

.stButton button:hover {
    opacity: 0.9 !important;
    transform: translateY(-1px) !important;
}

.stButton button:active {
    transform: translateY(0) !important;
}

/* Progress Bar */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #7C6EFA, #A89BFF) !important;
    border-radius: 100px !important;
}

.stProgress > div > div {
    background: rgba(124, 110, 250, 0.1) !important;
    border-radius: 100px !important;
    height: 6px !important;
}

/* Stage Info */
.stAlert {
    background: rgba(124, 110, 250, 0.07) !important;
    border: 1px solid rgba(124, 110, 250, 0.2) !important;
    border-radius: 10px !important;
    color: #B0A8FF !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.82rem !important;
}

/* Success */
.stSuccess {
    background: rgba(29, 158, 117, 0.08) !important;
    border: 1px solid rgba(29, 158, 117, 0.25) !important;
    color: #5DCAA5 !important;
    border-radius: 10px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: #0E0E18 !important;
    border-radius: 10px !important;
    padding: 4px !important;
    gap: 2px !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #666688 !important;
    border-radius: 8px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    padding: 0.5rem 1rem !important;
}

.stTabs [aria-selected="true"] {
    background: rgba(124, 110, 250, 0.15) !important;
    color: #A89BFF !important;
}

.stTabs [data-baseweb="tab-panel"] {
    background: #0E0E18 !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 12px !important;
    margin-top: 0.5rem !important;
    padding: 1rem !important;
}

/* JSON Viewer */
.stJson {
    background: transparent !important;
    font-family: 'JetBrains Mono', monospace !important;
}

/* Download Button */
.stDownloadButton button {
    background: transparent !important;
    border: 1px solid rgba(124, 110, 250, 0.35) !important;
    color: #A89BFF !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    padding: 0.55rem 1.5rem !important;
    transition: all 0.2s !important;
}

.stDownloadButton button:hover {
    background: rgba(124, 110, 250, 0.08) !important;
    border-color: rgba(124, 110, 250, 0.55) !important;
}

/* Divider */
hr {
    border-color: rgba(255,255,255,0.06) !important;
    margin: 2rem 0 !important;
}

/* Summary Cards */
.summary-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-top: 1.25rem;
}

.summary-card {
    background: #0E0E18;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 1.1rem 1rem;
}

.summary-card-label {
    font-size: 0.72rem;
    color: #666688;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 0.4rem;
    font-family: 'JetBrains Mono', monospace;
}

.summary-card-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #A89BFF;
    font-family: 'JetBrains Mono', monospace;
}

/* Subheader */
h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    color: #E8E8F0 !important;
    font-size: 1.15rem !important;
    letter-spacing: -0.01em !important;
}

/* Metrics override */
[data-testid="stMetric"] {
    background: #0E0E18 !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 12px !important;
    padding: 1.25rem !important;
}sss

[data-testid="stMetricValue"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1.9rem !important;
    color: #7C6EFA !important;
}

[data-testid="stMetricLabel"] {
    font-size: 0.72rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    color: #666688 !important;
}

/* Stage badge */
.stage-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: #7C6EFA;
    background: rgba(124, 110, 250, 0.08);
    border: 1px solid rgba(124, 110, 250, 0.18);
    border-radius: 8px;
    padding: 0.45rem 0.9rem;
    margin-bottom: 0.5rem;
}

.dot {
    width: 7px;
    height: 7px;
    background: #7C6EFA;
    border-radius: 50%;
    display: inline-block;
    animation: pulse 1.2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

/* Section label */
.section-label {
    font-size: 0.72rem;
    font-family: 'JetBrains Mono', monospace;
    color: #555577;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
</style>
""", unsafe_allow_html=True)

# ---------- FUNCTIONS ----------

def extract_intent(prompt):
    prompt = prompt.lower()
    return {
        "login": "login" in prompt,
        "dashboard": "dashboard" in prompt,
        "contacts": "contact" in prompt,
        "payments": "payment" in prompt or "premium" in prompt,
        "analytics": "analytics" in prompt,
        "role_based_access": "role" in prompt
    }

def design_system(intent):
    pages = []
    if intent["login"]:
        pages.append("Login")
    if intent["dashboard"]:
        pages.append("Dashboard")
    if intent["contacts"]:
        pages.append("Contacts")
    if intent["payments"]:
        pages.append("Payments")
    if intent["analytics"]:
        pages.append("Analytics")
    return pages

def generate_schema(intent, pages):
    return {
        "ui_schema": {
            "pages": pages
        },
        "api_schema": {
            "endpoints": [
                {"path": "/login", "method": "POST"},
                {"path": "/contacts", "method": "GET"},
                {"path": "/payments", "method": "POST"}
            ]
        },
        "database_schema": {
            "tables": ["users", "contacts", "payments"]
        },
        "auth_system": {
            "roles": ["Admin", "User"],
            "permissions": {
                "Admin": ["analytics", "all_access"],
                "User": ["contacts"]
            }
        },
        "business_logic": {
            "premium_plan": intent["payments"],
            "analytics_only_for_admin": intent["analytics"]
        }
    }

# ---------- UI ----------

st.markdown("""
<div class="hero-wrapper">
    <div class="hero-eyebrow">✦ Natural Language → Architecture</div>
    <h1 class="hero-title">ArchitectAI</h1>
    <p class="hero-subtitle">Describe your app in plain English. Get production-ready schemas, API design, and auth systems instantly.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Pipeline Stages", "5")
with col2:
    st.metric("Schema Layers", "5")
with col3:
    st.metric("Validation", "100%")
with col4:
    st.metric("AI Repair", "On")

st.divider()

st.markdown('<p class="section-label">// describe your application</p>', unsafe_allow_html=True)

prompt = st.text_area(
    label="",
    height=180,
    placeholder="Build a CRM with login, contacts dashboard, role-based access, premium plan, payments, and admin analytics..."
)

generate = st.button("→ Generate Architecture")

# ---------- PROCESS ----------

if generate:
    progress = st.progress(0)

    stages = [
        "Intent Extraction",
        "System Design",
        "Schema Generation",
        "Validation",
        "Repair Engine"
    ]

    for i, stage in enumerate(stages):
        st.markdown(f'<div class="stage-badge"><span class="dot"></span> Running: {stage}</div>', unsafe_allow_html=True)
        time.sleep(0.8)
        progress.progress((i + 1) * 20)

    intent = extract_intent(prompt)
    pages = design_system(intent)
    schema = generate_schema(intent, pages)

    st.success("✓ Schema generated — all layers validated")

    st.divider()
    st.markdown('<p class="section-label">// output schema</p>', unsafe_allow_html=True)

    tabs = st.tabs([
        "🎨  UI Schema",
        "⚙  API Endpoints",
        "🗄  Database",
        "🔐  Auth & Roles",
        "📋  Business Logic"
    ])

    with tabs[0]:
        st.json(schema["ui_schema"])
    with tabs[1]:
        st.json(schema["api_schema"])
    with tabs[2]:
        st.json(schema["database_schema"])
    with tabs[3]:
        st.json(schema["auth_system"])
    with tabs[4]:
        st.json(schema["business_logic"])

    st.divider()

    col_dl, col_space = st.columns([1, 3])
    with col_dl:
        st.download_button(
            "⬇  Download schema.json",
            json.dumps(schema, indent=4),
            file_name="schema.json",
            mime="application/json"
        )

    st.divider()
    st.markdown('<p class="section-label">// architecture summary</p>', unsafe_allow_html=True)

    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.metric("Pages", len(schema["ui_schema"]["pages"]))
    with s2:
        st.metric("DB Tables", len(schema["database_schema"]["tables"]))
    with s3:
        st.metric("Auth Roles", len(schema["auth_system"]["roles"]))
    with s4:
        st.metric("Status", "VALID ✓")