import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import urllib.request
import json
import random

# BRANDING PROTOCOLS
st.set_page_config(
    page_title="QUANTUM.FAQ BOT", 
    page_icon="🤖", 
    layout="centered"
)

# 1. BULLETPROOF MASTER STYLE INJECTION: Force Nebula Background & High-Tech Overlays
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Plus+Jakarta+Sans:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap');
    
    /* 🔥 ANTI-COPY CORE PROTECTION MATRIX: Disable absolute selection across DOM layers */
    html, body, .stApp, div, input, p, span, h1 {
        -webkit-user-select: none !important;  /* Safari */
        -moz-user-select: none !important;     /* Firefox */
        -ms-user-select: none !important;      /* IE 10+ */
        user-select: none !important;          /* Standard Syntax */
    }
    
    /* BACKGROUND ULTRA FORCE FIX */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stMainBlockContainer"] { 
        background: transparent !important;
    }
    
    /* Immersive Space Fog Environment */
    html, body {
        background: 
            radial-gradient(circle at 15% 25%, rgba(57, 255, 20, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 85% 75%, rgba(255, 49, 49, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 50% 30%, #110303 0%, #050000 65%, #000000 100%) !important;
        background-attachment: fixed !important;
        height: 100vh;
        margin: 0;
    }
    
    .brand-core-wrapper {
        text-align: center;
        margin: 40px 0 10px 0;
        position: relative;
        z-index: 10;
    }
    
    /* GEOMETRIC CORE TECH LOGO */
    .cyber-tech-logo {
        width: 60px;
        height: 60px;
        margin: 0 auto 25px auto;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .logo-square {
        position: absolute;
        width: 100%; height: 100%;
        border: 2px solid #39ff14;
        border-radius: 12px;
        transform: rotate(45deg);
        box-shadow: 0 0 15px rgba(57, 255, 20, 0.3);
        animation: spinClockwise 8s linear infinite;
    }
    .logo-inner-core {
        position: absolute;
        width: 50%; height: 50%;
        border: 2px dashed #ff3131;
        border-radius: 6px;
        transform: rotate(-45deg);
        box-shadow: 0 0 10px rgba(255, 49, 49, 0.4);
        animation: spinCounter 6s linear infinite;
    }
    @keyframes spinClockwise { 0% { transform: rotate(45deg); } 100% { transform: rotate(405deg); } }
    @keyframes spinCounter { 0% { transform: rotate(-45deg); } 100% { transform: rotate(-405deg); } }
    
    /* CLEAN CLASSIC OLD FONT */
    .stylish-title { 
        font-family: 'Cinzel', serif; 
        font-weight: 800; 
        font-size: 3.2rem; 
        color: #ffffff; 
        letter-spacing: 3px; 
        text-transform: uppercase;
        position: relative;
        display: inline-block;
        padding: 5px 0;
        margin-bottom: 15px;
        text-shadow: 0 0 5px rgba(255,255,255,0.4);
    }
    
    .gradient-accent { color: #ff3131; text-shadow: 0 0 8px rgba(255, 49, 49, 0.5); }
    
    /* HIGH-TECH FIXED STATUS BAR COMPONENTS */
    .status-bar-container {
        display: flex;
        justify-content: center;
        gap: 12px;
        margin: 15px auto 10px auto;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
    }
    .status-node {
        padding: 6px 14px;
        border-radius: 20px;
        background: rgba(10, 5, 5, 0.7);
        backdrop-filter: blur(5px);
        display: inline-flex;
        align-items: center;
    }
    .node-green {
        color: #39ff14;
        border: 1px solid rgba(57, 255, 20, 0.25);
    }
    .node-red {
        color: #ff3131;
        border: 1px solid rgba(255, 49, 49, 0.25);
    }
    .status-pulse {
        display: inline-block;
        width: 6px; height: 6px;
        background: #39ff14;
        border-radius: 50%;
        margin-right: 8px;
        box-shadow: 0 0 8px #39ff14;
        animation: pulseAlpha 1.5s infinite;
    }
    @keyframes pulseAlpha { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }

    .chat-container { margin: 25px 0; position: relative; z-index: 10; }
    
    /* Bubble Interactivity Mappings */
    .user-bubble { 
        background: rgba(57, 255, 20, 0.02) !important; border: 1px solid rgba(57, 255, 20, 0.15) !important; 
        padding: 16px 20px; border-radius: 12px 12px 0px 12px; color: #ffffff; margin-left: 15%; margin-bottom: 18px; 
        font-family: 'Plus Jakarta Sans', sans-serif; transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .user-bubble:hover { transform: translateY(-3px); border-color: #39ff14 !important; background: rgba(57, 255, 20, 0.06) !important; box-shadow: 0 8px 20px rgba(57, 255, 20, 0.15); }
    
    .bot-bubble { 
        background: rgba(255, 49, 49, 0.02) !important; border: 1px solid rgba(255, 49, 49, 0.15) !important; 
        padding: 16px 20px; border-radius: 12px 12px 12px 0px; color: #fff0f0; margin-right: 15%; margin-bottom: 18px; 
        font-family: 'Plus Jakarta Sans', sans-serif; transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .bot-bubble:hover { transform: translateY(-3px); border-color: #ff3131 !important; background: rgba(255, 49, 49, 0.06) !important; box-shadow: 0 8px 20px rgba(255, 49, 49, 0.15); }
    
    div[data-baseweb="input"] { background: rgba(10, 3, 3, 0.85) !important; border: 1px solid rgba(255, 49, 49, 0.2) !important; border-radius: 30px !important; }
    div[data-baseweb="input"]:focus-within, div[data-baseweb="input"]:hover { border-color: #39ff14 !important; box-shadow: 0 0 15px rgba(57, 255, 20, 0.2) !important; }
    input { color: #ffffff !important; font-family: 'Plus Jakarta Sans', sans-serif !important; }
    </style>
""", unsafe_allow_html=True)

# 2. CANVAS ENGINE: Native 60FPS Ambient Floating Glowing Particles
st.components.v1.html("""
    <canvas id="particleCanvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 0;"></canvas>
    <script>
    const canvas = document.getElementById('particleCanvas'); const ctx = canvas.getContext('2d');
    function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
    resize(); window.addEventListener('resize', resize);
    
    const particles = [];
    for(let i=0; i<65; i++) {
        particles.push({
            x: Math.random() * window.innerWidth,
            y: Math.random() * window.innerHeight,
            radius: Math.random() * 2 + 0.8,
            vx: (Math.random() - 0.5) * 0.7,
            vy: (Math.random() - 0.5) * 0.7,
            color: Math.random() > 0.5 ? 'rgba(57, 255, 20, ' : 'rgba(255, 49, 49, ',
            alpha: Math.random() * 0.4 + 0.1
        });
    }
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for(let i=0; i<65; i++) {
            let p = particles[i];
            ctx.beginPath(); ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = p.color + p.alpha + ')'; ctx.fill();
            p.x += p.vx; p.y += p.vy;
            if(p.x < 0 || p.x > canvas.width) p.vx *= -1;
            if(p.y < 0 || p.y > canvas.height) p.vy *= -1;
        }
        requestAnimationFrame(animate);
    }
    animate();
    </script>
""", height=0, scrolling=False)

# 🔥 ANTI-COPY JAVASCRIPT INJECTION: Kill Right-Click, F12, and Control Shortcuts
st.components.v1.html("""
    <script>
    // 1. Suppress Right Click (Context Menu Frame)
    document.addEventListener('contextmenu', event => event.preventDefault());

    // 2. Suppress Engineering Inspection Combinations
    document.onkeydown = function(e) {
        // Prevent F12 Dev Tools
        if(e.keyCode == 123) { return false; }
        
        // Prevent Ctrl+Shift+I (Inspect)
        if(e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) { return false; }
        
        // Prevent Ctrl+Shift+C (Element Selector)
        if(e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0)) { return false; }
        
        // Prevent Ctrl+Shift+J (Console Node logs)
        if(e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) { return false; }
        
        // Prevent Ctrl+U (Raw Resource Source Payload View)
        if(e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) { return false; }
    };
    </script>
""", height=0, scrolling=False)

# CORE STRUCTURAL LAYOUT FIXED
st.markdown("""
    <div class="brand-core-wrapper">
        <div class="cyber-tech-logo">
            <div class="logo-square"></div>
            <div class="logo-inner-core"></div>
        </div>
        <h1 class="stylish-title">QUANTUM.FAQ <span class="gradient-accent">BOT</span></h1>
        <div class="status-bar-container">
            <div class="status-node node-green"><span class="status-pulse"></span>SYSTEM CORE: ACTIVE</div>
            <div class="status-node node-red">SECURITY SECURE</div>
            <div class="status-node node-green">NLP HYBRID CONNECTED</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# TECHNICAL DATA MATRIX
TECH_DATA = {
    "queries": [
        "what is your name?", "who are you", "how does this chatbot work?", 
        "what is the stack of this project?", "what is tf-idf vectorization?", 
        "how to deploy a streamlit app?", "what is cosine similarity?", "what domain is this project?"
    ],
    "responses": [
        "I am Quantum Core, an automated conversational sub-routine engineered for instant vector mapping calculations.",
        "I am Quantum Core, a hybrid NLP navigation assistant specialized in handling local context datasets and open-domain searches.",
        "I ingest raw text sequences, apply high-dimensional TF-IDF vectorization, and determine analytical match coefficients using Cosine Similarity.",
        "This system architecture is engineered using Python 3.11, Streamlit Framework, Scikit-Learn (TfidfVectorizer), and Open Knowledge API Core Protocols.",
        "TF-IDF (Term Frequency-Inverse Document Frequency) is a mathematical algorithm that transforms raw text tokens into a numerical matrix based on word importance.",
        "To deploy a Streamlit workspace, push your source files to a public GitHub repository, initialize a requirements file, and link the tree terminal to Streamlit Community Cloud.",
        "It is a mathematical formula computing the angle cosine between two non-zero vectors inside an inner mathematical vector space to evaluate string similarity.",
        "This project cluster is built as a production-grade prototype for the Artificial Intelligence & Python Development Framework domain."
    ]
}

EMOTION_KEYWORDS = ["sad", "low", "depressed", "stress", "upset", "lonely", "happy", "excited", "bored", "tension", "mood"]
EMOTION_RESPONSES = [
    "Bhai, tension mat le, plot twists hi toh kahani mazedaar banate hain. Ek gehri saans le, scene sahi ho jayega. Main yahi hoon.",
    "Listen to me, low phases are just temporary glitches in the matrix. Chal thoda chill kar, step back le aur restart maar. You got this, flex up!",
    "Bhai load mat le, life me up-down chalta rehta hai. Koi badhiya music sun ya doston se baat kar, deep zones se bahar nikalna hai apan ko."
]

user_query = st.text_input("SHARE WHAT'S ON YOUR MIND OR ASK ANY QUESTION", placeholder="Ask me anything in the world...")

if user_query:
    query_lower = user_query.lower()
    bot_response = None
    response_type = ""
    
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown(f'<div class="user-bubble"><b>🧑‍💻 Input Layer:</b><br>{user_query}</div>', unsafe_allow_html=True)
    
    is_factual_search = any(trigger in query_lower for trigger in ["who is", "ceo", "president", "capital", "population", "weather", "score", "versus", "vs", "founder", "meaning of", "age of", "born", "movie", "toy story", "tell me about"])
    
    # Node 1: Emotion Engine Mappings
    if not is_factual_search and any(word in query_lower for word in EMOTION_KEYWORDS):
        bot_response = random.choice(EMOTION_RESPONSES)
        response_type = "💚 Companion Core"

    # Node 2: Matrix Mathematical NLP FAQ Scoring
    if not bot_response:
        compiled_queries = TECH_DATA["queries"] + [user_query]
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(compiled_queries)
        similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]
        
        best_match_idx = similarity_scores.argmax()
        highest_score = similarity_scores[best_match_idx]
        
        if highest_score > 0.45:
            bot_response = TECH_DATA["responses"][best_match_idx]
            response_type = f"⚙️ Tech Node (Match: {highest_score:.2f})"

    # Node 3: Open-Knowledge REST Endpoints
    if not bot_response:
        with st.spinner("🚀 Querying global open knowledge framework..."):
            try:
                formatted_query = urllib.parse.quote(user_query)
                wiki_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{formatted_query}"
                
                req = urllib.request.Request(wiki_url, headers={'User-Agent': 'QuantumBot/1.0 (portfolio project)'})
                with urllib.request.urlopen(req) as response:
                    data = json.loads(response.read().decode())
                    
                if "extract" in data:
                    bot_response = data["extract"]
                    source_url = data.get("content_urls", {}).get("desktop", {}).get("page", "https://wikipedia.org")
                    response_type = "🌐 Global Matrix Node"
                    bot_response += f"<br><br><a href='{source_url}' target='_blank' style='color: #ff3131; text-decoration: none; font-weight: 700;'>🔗 VIEW FULL DATA METADATA</a>"
            except:
                pass

    # Node 4: Fallback Search Mechanics
    if not bot_response:
        try:
            search_url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(user_query)}&limit=1&namespace=0&format=json"
            with urllib.request.urlopen(search_url) as response:
                search_data = json.loads(response.read().decode())
            if len(search_data) > 3 and search_data[3]:
                title = search_data[1][0]
                source_url = search_data[3][0]
                
                wiki_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(title)}"
                req = urllib.request.Request(wiki_url, headers={'User-Agent': 'QuantumBot/1.0'})
                with urllib.request.urlopen(req) as resp:
                    data = json.loads(resp.read().decode())
                bot_response = data.get("extract", "No explicit definition package found.")
                response_type = "🌐 Global Matrix Node"
                bot_response += f"<br><br><a href='{source_url}' target='_blank' style='color: #ff3131; text-decoration: none; font-weight: 700;'>🔗 VIEW FULL DATA METADATA</a>"
        except:
            pass

    # Final Security Fallback Layer
    if not bot_response:
        bot_response = "Bhai, phrase context isolated ajeeb hai. Try rephrasing with direct nouns (e.g. 'Toy Story movie', 'Elon Musk')."
        response_type = "⚠️ System Fallback"

    st.markdown(f'<div class="bot-bubble"><b>🤖 Matrix Engine ({response_type}):</b><br>{bot_response}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)