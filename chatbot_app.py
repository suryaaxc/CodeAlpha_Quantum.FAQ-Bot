import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import urllib.request
import json
import time

# BRANDING PROTOCOLS
st.set_page_config(
    page_title="QUANTUM.FAQ BOT", 
    page_icon="🤖", 
    layout="centered"
)

# STYLE INJECTION: Immersive Minimalist Jarvis Matrix Environment
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght=800&family=Plus+Jakarta+Sans:wght=400;600;700&family=Space+Grotesk:wght=500;700&display=swap');
    
    html, body, .stApp, div, input, p, span, h1 { user-select: none !important; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stMainBlockContainer"] { background: transparent !important; }
    
    /* SYSTEM THEME ADAPTATION PROTOCOL WITH KINETIC GLOW BACKGROUNDS */
    @media (prefers-color-scheme: dark) {
        html, body {
            background: 
                radial-gradient(circle at 10% 20%, rgba(57, 255, 20, 0.04) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(255, 49, 49, 0.04) 0%, transparent 40%),
                background-color: #030101 !important;
            background-attachment: fixed !important;
        }
        .stylish-title { color: #ffffff !important; }
        .user-bubble { background: rgba(57, 255, 20, 0.02) !important; color: #ffffff !important; box-shadow: 0 0 15px rgba(57, 255, 20, 0.02); }
        .bot-bubble { background: rgba(255, 49, 49, 0.01) !important; color: #fff0f0 !important; box-shadow: 0 0 20px rgba(255, 49, 49, 0.02); }
        div[data-baseweb="input"] { background: rgba(8, 4, 4, 0.9) !important; }
        input { color: #ffffff !important; }
        .status-node { background: rgba(6, 4, 4, 0.7) !important; }
    }

    @media (prefers-color-scheme: light) {
        html, body {
            background: 
                radial-gradient(circle at 10% 20%, rgba(57, 255, 20, 0.05) 0%, transparent 45%),
                radial-gradient(circle at 90% 80%, rgba(255, 49, 49, 0.05) 0%, transparent 45%),
                background-color: #faf9f6 !important;
            background-attachment: fixed !important;
        }
        .stylish-title { color: #111111 !important; }
        .user-bubble { background: rgba(57, 255, 20, 0.03) !important; color: #111111 !important; }
        .bot-bubble { background: rgba(255, 49, 49, 0.03) !important; color: #221111 !important; }
        div[data-baseweb="input"] { background: rgba(255, 255, 255, 0.95) !important; border: 1px solid rgba(255, 49, 49, 0.3) !important; }
        input { color: #111111 !important; }
        .status-node { background: rgba(245, 244, 240, 0.9) !important; }
    }

    /* STRUCTURE CORE ELEMENTS & TRANSITIONS */
    .brand-core-wrapper { text-align: center; margin: 40px 0 10px 0; position: relative; z-index: 10; animation: fadeIn 1s ease-out; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
    
    .cyber-tech-logo { width: 60px; height: 60px; margin: 0 auto 25px auto; position: relative; display: flex; align-items: center; justify-content: center; }
    .logo-square { position: absolute; width: 100%; height: 100%; border: 2px solid #39ff14; border-radius: 12px; transform: rotate(45deg); box-shadow: 0 0 15px rgba(57, 255, 20, 0.2); animation: spinClockwise 12s linear infinite; }
    .logo-inner-core { position: absolute; width: 50%; height: 50%; border: 2px dashed #ff3131; border-radius: 6px; transform: rotate(-45deg); box-shadow: 0 0 10px rgba(255, 49, 49, 0.3); animation: spinCounter 8s linear infinite; }
    @keyframes spinClockwise { 0% { transform: rotate(45deg); } 100% { transform: rotate(405deg); } }
    @keyframes spinCounter { 0% { transform: rotate(-45deg); } 100% { transform: rotate(-405deg); } }
    
    .stylish-title { font-family: 'Cinzel', serif; font-weight: 800; font-size: 3.2rem; letter-spacing: 3px; text-transform: uppercase; }
    .gradient-accent { color: #ff3131; text-shadow: 0 0 10px rgba(255, 49, 49, 0.6); }
    
    /* QUANTUM CAPSULAR STATUS CHANNELS */
    .status-bar-container { display: flex; justify-content: center; gap: 14px; margin: 20px auto; font-family: 'Space Grotesk', sans-serif; font-size: 0.72rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; }
    .status-node { padding: 10px 18px; border-radius: 14px; backdrop-filter: blur(12px); display: inline-flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; min-width: 155px; line-height: 1.4; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
    .status-node:hover { transform: scale(1.03); box-shadow: 0 0 15px rgba(57, 255, 20, 0.15); }
    .node-green { color: #39ff14; border: 1px solid rgba(57, 255, 20, 0.35); }
    .status-pulse { display: inline-block; width: 6px; height: 6px; background: #39ff14; border-radius: 50%; margin-bottom: 4px; box-shadow: 0 0 8px #39ff14; animation: pulseAlpha 1.5s infinite; }
    .badge-subtext { font-size: 0.55rem; color: #777788; letter-spacing: 1px; margin-top: 3px; font-weight: 400; }
    @keyframes pulseAlpha { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }

    /* CHAT STREAM ARCHITECTURE WITH ANIMATION LAYERS */
    .chat-container { margin: 25px 0; position: relative; z-index: 10; }
    .user-bubble { border: 1px solid rgba(57, 255, 20, 0.2) !important; padding: 16px 20px; border-radius: 12px 12px 0px 12px; margin-left: 15%; margin-bottom: 18px; font-family: 'Plus Jakarta Sans', sans-serif; animation: slideLeft 0.4s cubic-bezier(0.1, 0.8, 0.3, 1); }
    .bot-bubble { border: 1px solid rgba(255, 49, 49, 0.25) !important; padding: 20px; border-radius: 12px 12px 12px 0px; margin-right: 15%; margin-bottom: 18px; font-family: 'Plus Jakarta Sans', sans-serif; line-height: 1.65; animation: slideRight 0.5s cubic-bezier(0.1, 0.8, 0.3, 1); position: relative; }
    
    @keyframes slideLeft { from { opacity: 0; transform: translateX(20px); } to { opacity: 1; transform: translateX(0); } }
    @keyframes slideRight { from { opacity: 0; transform: translateX(-20px); } to { opacity: 1; transform: translateX(0); } }
    
    /* Holographic Typewriter Cursor Node */
    .jarvis-cursor::after {
        content: '█';
        animation: blink 0.8s infinite;
        color: #ff3131;
        margin-left: 3px;
        font-size: 0.95rem;
    }
    @keyframes blink { 0%, 100% { opacity: 0; } 50% { opacity: 1; } }
    
    div[data-baseweb="input"] { border: 1px solid rgba(255, 49, 49, 0.25) !important; border-radius: 30px !important; transition: all 0.3s ease; }
    div[data-baseweb="input"]:focus-within { border-color: #39ff14 !important; box-shadow: 0 0 15px rgba(57, 255, 20, 0.15) !important; }
    input { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    </style>
""", unsafe_allow_html=True)

# AMBIENT JARVIS TERMINAL MATRIX CODE STREAM (Fades safely behind panels)
st.components.v1.html("""
    <canvas id="matrixStream" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 0; opacity: 0.15;"></canvas>
    <script>
    const canvas = document.getElementById('matrixStream'); const ctx = canvas.getContext('2d');
    function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
    resize(); window.addEventListener('resize', resize);
    
    const chars = '01'.split('');
    const fontSize = 14; const columns = canvas.width / fontSize;
    const drops = Array(Math.floor(columns)).fill(1);
    
    function drawMatrix() {
        ctx.fillStyle = 'rgba(3, 1, 1, 0.08)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#00ffcc'; ctx.font = fontSize + 'px monospace';
        for (let i = 0; i < drops.length; i++) {
            const text = chars[Math.floor(Math.random() * chars.length)];
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
    }
    setInterval(drawMatrix, 40);
    </script>
""", height=0, scrolling=False)

# DYNAMIC READOUT VARIABLES
live_hex = f"0x{random.randint(4096, 65535):X}"
live_ms = f"{random.uniform(0.12, 0.35):.2f}ms"

# CORE GRAPHICS HEADER
st.markdown(f"""
    <div class="brand-core-wrapper">
        <div class="cyber-tech-logo">
            <div class="logo-square"></div>
            <div class="logo-inner-core"></div>
        </div>
        <h1 class="stylish-title">QUANTUM.FAQ <span class="gradient-accent">BOT</span></h1>
        <div class="status-bar-container">
            <div class="status-node node-green">
                <div><span class="status-pulse"></span> SYSTEM CORE: ACTIVE</div>
                <div class="badge-subtext">CORE_ID: {live_hex}</div>
            </div>
            <div class="status-node node-green">
                <div>OFFLINE KNOWLEDGE MATRIX</div>
                <div class="badge-subtext">INDEX: COMPRESSED</div>
            </div>
            <div class="status-node node-green">
                <div>LOCAL HIGH-DIMENSIONAL TUNED</div>
                <div class="badge-subtext">LATENCY: {live_ms}</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

UNIVERSAL_DATA = {
    "queries": [
        "what is your name?", "who are you", "how does this chatbot work?", 
        "what is the stack of this project?", "what is tf-idf vectorization?", 
        "how to deploy a streamlit app?", "what is cosine similarity?", "what domain is this project?",
        "compare sql vs nosql databases based on scaling and schema flexibility",
        "sql vs nosql database scaling schema",
        "who won the latest icc t20 world cup",
        "what is rest api and how does it use http methods",
        "explain the ending of the movie inception in short",
        "what has keys but opens no locks space but no room",
        "interstellar movie plot space black holes",
        "python loops machine learning algorithms core coding definition",
        "curse of dimensionality", "event horizon", "cap theorem distributed systems", "turing test", "schrodingers cat paradox"
    ],
    "responses": [
        "I am Quantum Core, an automated conversational subroutine engineered for instant vector mapping calculations.",
        "I am Quantum Core, a hybrid NLP navigation assistant specialized in handling localized context datasets.",
        "I ingest raw text sequences, apply high-dimensional TF-IDF vectorization, and determine analytical match coefficients using Cosine Proximity formulas.",
        "This system architecture is engineered using Python 3.11, Streamlit UI Framework, and Scikit-Learn Matrix Tokenizer pipelines.",
        "TF-IDF (Term Frequency-Inverse Document Frequency) is a mathematical algorithm that transforms raw text tokens into a numerical matrix based on word importance.",
        "To deploy a Streamlit workspace, push source files to a public GitHub repository, initialize a requirements.txt file, and link the branch tree to Streamlit Community Cloud.",
        "It is a mathematical metric computing the angle cosine between two non-zero vectors inside an inner mathematical vector space to evaluate string proximity rules.",
        "This project cluster is built as a production-grade prototype for the Artificial Intelligence & Python Development Framework domain.",
        
        "📌 **SQL vs NoSQL Database Matrix Framework:**<br><br>"
        "⚖️ **Schema Flexibility:**<br>"
        "* **SQL:** Uses strict, predefined relational schemas (tables/rows). Altering schemas requires heavy database migrations.<br>"
        "* **NoSQL:** Uses dynamic, unstructured schemas (JSON documents, key-value, graphs). Allows unstructured schema flexibility on the fly.<br><br>"
        "📈 **Scaling Dynamics:**<br>"
        "* **SQL:** Scales **Vertically** (requires upgrading CPU, RAM, or SSD capabilities of a single hardware server unit).<br>"
        "* **NoSQL:** Scales **Horizontally** (distributes data load across thousands of decentralized commodity server clusters automatically).",
        
        "📌 **SQL vs NoSQL Database Matrix Framework:**<br><br>"
        "⚖️ **Schema Flexibility:**<br>"
        "* **SQL:** Strict relational schemas.<br>"
        "* **NoSQL:** Dynamic unstructured document models.<br><br>"
        "📈 **Scaling Dynamics:**<br>"
        "* **SQL:** Vertical scaling (Hardware upgrade).<br>"
        "* **NoSQL:** Horizontal scaling (Data splitting across nodes).",

        "🏆 **ICC T20 World Cup Matrix:** India captured the definitive T20 World Cup crown in a historic execution run, defeating South Africa in an intense final over finish.",
        
        "🌐 **REST API Execution Node:** REST (Representational State Transfer) is a stateless architectural protocol. It utilizes primary HTTP verbs to execute structural CRUD mechanics:<br>"
        "* **GET:** Retrieve specific target resource data.<br>"
        "* **POST:** Construct/Create new payload entries.<br>"
        "* **PUT:** Completely update existing data objects.<br>"
        "* **DELETE:** Erase target server array properties.",
        
        "🌀 **Inception Ending Matrix Decoded:** The spinning top keeps spinning in the final sequence, blurring the lines between reality and dream layers. Cobb doesn't wait to see it drop because his children are his absolute reality now—signifying emotional closure over objective status.",
        
        "🧩 **Logical Extraction Core:** The computational riddle solution is: **A Keyboard**. (Contains letter keys, spacebar, and the Enter sequence).",
        
        "🚀 **Interstellar Space Log:** Directed by Christopher Nolan, it tracks an astronaut team navigating a wormhole near Saturn to discover habitable worlds, utilizing real General Relativity equations, time dilation, and black hole dynamics (Gargantua).",
        
        "💻 **Core Engineering Scripts:** Python loops automate iterative traversal blocks. Machine Learning algorithms (like Linear Regression, DBSCAN, or Decision Trees) map high-dimensional statistical variations inside sample packets to make automated classifications.",

        "📊 **Curse of Dimensionality:** As data features (dimensions) increase inside machine learning spaces, the volume grows exponentially. This causes available training vectors to become extremely sparse, making distance-based cluster grouping (like KNN or DBSCAN) mathematically inefficient without dimensionality reduction.",
        
        "🌌 **Event Horizon Matrix:** The absolute geometric boundary surrounding a gravitational singularity (Black Hole) where the escape velocity strictly exceeds the speed of light. Zero data packets or electromagnetic sequences can escape once crossed.",
        
        "💻 **CAP Theorem Node:** Inside distributed data environments, a decentralized system can only simultaneously guarantee **two out of three** absolute properties: Consistency (identical data across nodes), Availability (every request receives a non-error response), and Partition Tolerance (system continues despite message drops).",
        
        "🧠 **Turing Test Architecture:** A cognitive benchmark proposed by Alan Turing. If a human evaluator cannot consistently distinguish machine textual outputs from a real human subject during blind natural conversations, the AI system passes the operational intelligence threshold.",
        
        "🧪 **Schrodinger's Cat Paradox:** A quantum mechanics thought experiment illustrating superposition. A cat inside a sealed box with a radioactive trigger exists in a simultaneous wave state of being **both alive and dead** until an outside measurement forces a quantum collapse."
    ]
}

EMOTION_KEYWORDS = ["sad", "low", "depressed", "stress", "upset", "lonely", "happy", "excited", "bored", "tension", "mood"]
EMOTION_RESPONSES = [
    "Bhai, tension mat le, plot twists hi toh kahani mazedaar banate hain. Ek gehri saans le, scene sahi ho jayega. Main yahi hoon.",
    "Listen to me, low phases are just temporary glitches in the matrix. Chal thoda chill kar, step back le aur restart maar. You got this, flex up!"
]

user_query = st.text_input("SHARE WHAT'S ON YOUR MIND OR ASK ANY QUESTION", placeholder="System awaiting vector transmission...")

if user_query:
    query_lower = user_query.lower().strip()
    bot_response = None
    response_type = ""
    
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown(f'<div class="user-bubble"><b>🧑‍💻 User Input Matrix:</b><br>{user_query}</div>', unsafe_allow_html=True)
    
    # LAYER 1: COMPANION ENGINE
    if any(word in query_lower for word in EMOTION_KEYWORDS):
        bot_response = random.choice(EMOTION_RESPONSES)
        response_type = "💚 Companion Core"

    # LAYER 2: LOCAL HIGH-DIMENSIONAL CLASSIFIER
    if not bot_response:
        compiled_queries = UNIVERSAL_DATA["queries"] + [user_query]
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(compiled_queries)
        
        similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]
        best_match_idx = similarity_scores.argmax()
        highest_score = similarity_scores[best_match_idx]
        
        if highest_score > 0.35:
            bot_response = UNIVERSAL_DATA["responses"][best_match_idx]
            response_type = "🏛️ Offline Knowledge Matrix"

    # LAYER 3: DYNAMIC SHORT STREAM CHANNELS
    if not bot_response:
        try:
            system_instruction = (
                "You are Jarvis. Explain the user query clearly in an extremely short, concise, "
                "and exam-ready format. Use bullet points or short bold headings if applicable. Max 100 words."
            )
            req = urllib.request.Request(
                "https://text.pollinations.ai/", 
                data=json.dumps({
                    "messages": [
                        {"role": "system", "content": system_instruction},
                        {"role": "user", "content": user_query}
                    ],
                    "model": "openai"
                }).encode("utf-8"),
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=8) as response:
                res_data = json.loads(response.read().decode("utf-8"))
            
            ai_out = res_data["choices"][0]["message"]["content"]
            if ai_out:
                bot_response = ai_out.strip()
                response_type = "🌐 Cognitive Intelligent Node"
        except Exception:
            pass

    # LAYER 4: FALLBACK NODE
    if not bot_response:
        bot_response = "Bhai, keyword parameters out-of-bounds chal rahe hain. Try checking your local gateway parameters."
        response_type = "⚠️ System Safe Fallback"

    # STREAMING ANIMATION GENERATOR (Jarvis Typewriter Module)
    formatted_response = bot_response.replace("'", "\\'").replace("\n", " ").replace("\r", "")
    unique_stream_id = f"jarvis_core_{int(time.time())}"
    
    st.markdown(f"""
        <div class="bot-bubble">
            <b>🤖 Matrix Engine ({response_type}):</b><br><br>
            <span id="{unique_stream_id}" class="jarvis-cursor"></span>
        </div>
        
        <script>
            (function() {{
                const el = document.getElementById('{unique_stream_id}');
                const textStr = '{formatted_response}';
                let idx = 0;
                
                function processStream() {{
                    if (idx < textStr.length) {{
                        if(textStr.substr(idx, 4) === '<br>') {{ el.innerHTML += '<br>'; idx += 4; }}
                        else if(textStr.substr(idx, 4) === '<li>') {{ el.innerHTML += '<li>'; idx += 4; }}
                        else if(textStr.substr(idx, 5) === '</li>') {{ el.innerHTML += '</li>'; idx += 5; }}
                        else {{ el.innerHTML += textStr.charAt(idx); idx++; }}
                        setTimeout(processStream, 12);
                    }} else {{
                        el.classList.remove('jarvis-cursor');
                    }}
                }}
                setTimeout(processStream, 300);
            }})();
        </script>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)