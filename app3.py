# app.py
# -------------------------------------------------------
# Premium Streamlit Portfolio for Data Scientist
# Modern UI with glassmorphism, smooth animations,
# interactive elements, and professional design
# -------------------------------------------------------

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64
import os
from datetime import datetime

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Ansh Kedia — Data Scientist Portfolio",
    page_icon="👨‍🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================
# Enhanced Custom CSS
# =========================
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

:root {
  --bg: #0a0e1a;
  --bg-secondary: #0f1419;
  --card: rgba(255,255,255,0.05);
  --card-hover: rgba(255,255,255,0.08);
  --card-border: rgba(255,255,255,0.1);
  --text: #e8eaed;
  --text-secondary: #a8b3cf;
  --muted: #6b7280;
  --brand: #34d399;
  --brand-2: #60a5fa;
  --brand-3: #a78bfa;
  --accent: #fbbf24;
  --shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
  --shadow-lg: 0 35px 60px -15px rgba(0,0,0,0.6);
}

* {
  scroll-behavior: smooth;
}

.stApp {
  background: 
    radial-gradient(ellipse 80% 50% at 50% -20%, rgba(52,211,153,0.15), transparent),
    radial-gradient(ellipse 60% 50% at -20% 80%, rgba(96,165,250,0.12), transparent),
    radial-gradient(ellipse 60% 50% at 120% 80%, rgba(167,139,250,0.1), transparent),
    linear-gradient(180deg, var(--bg) 0%, var(--bg-secondary) 100%);
  color: var(--text);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background-attachment: fixed;
}

.block-container {
  padding-top: 3rem;
  padding-bottom: 4rem;
  max-width: 1400px;
}

/* Typography */
h1, h2, h3, h4 {
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--text);
}

h1 { font-size: clamp(2.5rem, 5vw, 4rem); }
h2 { font-size: clamp(2rem, 4vw, 3rem); margin-bottom: 1.5rem; }
h3 { font-size: clamp(1.5rem, 3vw, 2rem); }

.big-title {
  font-weight: 900;
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  line-height: 1.1;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, var(--text) 0%, var(--text-secondary) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.gradient-text {
  background: linear-gradient(90deg, var(--brand), var(--brand-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.subhead {
  color: var(--text-secondary);
  font-size: clamp(1.1rem, 2vw, 1.4rem);
  line-height: 1.6;
  font-weight: 400;
}

/* Badge */
.badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: rgba(52,211,153,0.1);
  border: 1px solid rgba(52,211,153,0.3);
  border-radius: 50px;
  color: var(--brand);
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  letter-spacing: 0.5px;
}

/* Cards */
.card {
  background: var(--card);
  border: 1px solid var(--card-border);
  border-radius: 24px;
  box-shadow: var(--shadow);
  backdrop-filter: blur(20px);
  padding: 2rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
}

.card-hover {
  cursor: pointer;
}

.card-hover:hover {
  transform: translateY(-8px);
  background: var(--card-hover);
  box-shadow: var(--shadow-lg);
  border-color: rgba(255,255,255,0.2);
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.875rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none !important;
  border: 1px solid transparent;
  transition: all 0.3s ease;
  cursor: pointer;
  white-space: nowrap;
}

.btn-primary {
  background: linear-gradient(135deg, var(--brand), var(--brand-2));
  color: var(--bg);
  box-shadow: 0 10px 25px rgba(52,211,153,0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 15px 35px rgba(52,211,153,0.4);
}

.btn-ghost {
  background: var(--card);
  color: var(--text);
  border: 1px solid var(--card-border);
}

.btn-ghost:hover {
  background: var(--card-hover);
  border-color: rgba(255,255,255,0.3);
}

/* Divider */
.hr {
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
  margin: 4rem 0;
  border: 0;
}

/* Tags */
.tags {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.tag {
  font-size: 0.8rem;
  padding: 0.4rem 0.8rem;
  border-radius: 8px;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  color: var(--text-secondary);
  font-weight: 500;
  transition: all 0.2s ease;
}

.tag:hover {
  background: rgba(255,255,255,0.1);
  border-color: rgba(255,255,255,0.2);
  transform: translateY(-2px);
}

/* Project Cards */
.project-card {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.project-cover {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 16px;
  margin-bottom: 1.2rem;
  transition: transform 0.3s ease;
}

.project-card:hover .project-cover {
  transform: scale(1.05);
}

/* Skills Grid */
.skill-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.2rem;
  background: var(--card);
  border: 1px solid var(--card-border);
  border-radius: 12px;
  margin-bottom: 0.75rem;
  transition: all 0.3s ease;
}

.skill-item:hover {
  background: var(--card-hover);
  border-color: rgba(255,255,255,0.2);
  transform: translateX(8px);
}

.skill-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
}

/* Timeline */
.timeline {
  position: relative;
  padding-left: 2rem;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(180deg, var(--brand), var(--brand-2), var(--brand-3));
}

.timeline-item {
  position: relative;
  margin-bottom: 1.5rem;
  padding-left: 1.5rem;
}

.timeline-item::before {
  content: '';
  position: absolute;
  left: -2.5rem;
  top: 1.5rem;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--brand);
  border: 3px solid var(--bg);
  box-shadow: 0 0 0 4px rgba(52,211,153,0.2);
}

/* Footer */
.footer {
  text-align: center;
  padding: 2rem 0;
  color: var(--muted);
  font-size: 0.9rem;
  border-top: 1px solid var(--card-border);
  margin-top: 4rem;
}

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fadeIn 0.6s ease-out;
}

/* Hide Streamlit Elements */
[data-testid="stDecoration"],
footer,
header,
#MainMenu,
.stDeployButton {
  display: none !important;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: var(--bg);
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, var(--brand), var(--brand-2));
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(180deg, var(--brand-2), var(--brand));
}

/* Responsive */
@media (max-width: 768px) {
  .block-container {
    padding-top: 2rem;
  }
  
  .card {
    padding: 1.5rem;
  }
  
  .timeline {
    padding-left: 1rem;
  }
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# =========================
# Helper Functions
# =========================
def get_base64_image(image_file):
    try:
        with open(image_file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return ""

def render_timeline_item(it):
    """Renders a single timeline item"""
    logo_html = ""
    try:
        if os.path.exists(it["logo"]):
            with open(it["logo"], "rb") as f:
                logo_b64 = base64.b64encode(f.read()).decode()
                logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="width:48px;height:48px;object-fit:contain;border-radius:12px;border:1px solid rgba(255,255,255,0.15);background:rgba(255,255,255,0.03);padding:4px;" />'
        else:
            logo_html = '<div style="width:48px;height:48px;border-radius:12px;background:rgba(255,255,255,0.05);display:flex;align-items:center;justify-content:center;font-size:1.2rem;color:var(--brand);border:1px solid var(--card-border);">📄</div>'
    except Exception:
        logo_html = '<div style="width:48px;height:48px;border-radius:12px;background:rgba(255,255,255,0.05);display:flex;align-items:center;justify-content:center;font-size:1.2rem;color:var(--brand);border:1px solid var(--card-border);">📄</div>'
    
    st.markdown(
        f"""
        <div class="timeline-item card-hover" style="display:flex; gap:1.2rem; align-items:flex-start; padding:1.5rem; border-radius:16px; background:var(--card); border:1px solid var(--card-border);">
          {logo_html}
          <div style="flex:1;">
            <div style="color:var(--brand); font-weight:600; font-size:0.85rem; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:0.5rem;">{it['when']}</div>
            <div style="font-weight:700; font-size:1.1rem; margin-bottom:0.3rem; color:var(--text);">{it['title']}</div>
            <div style="color:var(--text-secondary); font-size:0.95rem; font-weight:500; margin-bottom:0.5rem;">{it['where']}</div>
            <div style="color:var(--muted); font-size:0.9rem; line-height:1.5;">{it['detail']}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_timeline(items):
    """Renders the entire timeline"""
    st.markdown('<div class="timeline">', unsafe_allow_html=True)
    for it in items:
        render_timeline_item(it)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# Hero Section
# =========================
st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)

col1, col2 = st.columns([1.3, 1], gap="large")

with col1:
    st.markdown(
        '<span class="badge">👨‍🔬 Data Science • AI Enthusiast</span>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="big-title">Hi 👋, I\'m <span class="gradient-text">Ansh Kedia</span></div>',
        unsafe_allow_html=True
    )
    
    # Typing Effect
    components.html(
        """
        <div id="typing" style="color:#a8b3cf; font-size:1.4rem; margin:0.8rem 0; min-height:45px; font-weight:500;"></div>
        <script>
        const roles = ["Data Scientist", "ML Engineer", "Computer Vision Expert", "NLP Specialist", "Agentic AI Developer", "Analytics Wizard"];
        const el = document.getElementById('typing');
        let i = 0, j = 0, deleting = false, delay = 70, pause = 1200;
        
        function loop(){
          const word = roles[i % roles.length];
          if(!deleting){
            el.innerHTML = word.substring(0,j+1) + '<span style="opacity:.4; margin-left:2px;">▮</span>';
            j++;
            if(j === word.length){ deleting = true; setTimeout(loop, pause); return; }
          } else {
            el.innerHTML = word.substring(0,j-1) + '<span style="opacity:.4; margin-left:2px;">▮</span>';
            j--;
            if(j === 0){ deleting = false; i++; }
          }
          setTimeout(loop, deleting ? delay/2 : delay);
        }
        setTimeout(loop, 500);
        </script>
        """,
        height=65,
    )
    
    st.markdown(
        """
        <div class="subhead" style="margin-top:1.5rem; line-height:1.8;">
        <b>2026 CSE Graduate</b> | Passionate about transforming data into actionable insights
        <br>
        Specializing in <b>Machine Learning</b>, <b>Deep Learning</b>, and <b>AI-powered Solutions</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div style="margin-top:2rem; display:flex; gap:1rem; flex-wrap:wrap;">
          <a class="btn btn-primary" href="#projects" style="text-decoration:none;">
            🚀 View Projects
          </a>
          <a class="btn btn-ghost" href="#contact" style="text-decoration:none;">
            💬 Get in Touch
          </a>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card" style="text-align:center; padding:2.5rem;">
          <div style="width:180px; height:180px; margin:0 auto 1.5rem auto; border-radius:50%; background:linear-gradient(135deg, var(--brand), var(--brand-2)); display:flex; align-items:center; justify-content:center; font-size:5rem; box-shadow:0 20px 60px rgba(52,211,153,0.3);">
            👨‍💻
          </div>
          <h3 style="margin-bottom:1rem; color:var(--text);">Currently Available</h3>
          <p style="color:var(--text-secondary); margin-bottom:1.5rem;">
            Open to full-time opportunities in Data Science and AI/ML roles
          </p>
          <div style="display:flex; gap:0.8rem; justify-content:center; flex-wrap:wrap;">
            <span class="tag" style="background:rgba(52,211,153,0.1); border-color:rgba(52,211,153,0.3); color:var(--brand);">💼 Job Ready</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =========================
# About Section
# =========================
st.markdown("## About Me 👨‍🎓")
st.caption("Get to know me better")

ab_col1, ab_col2 = st.columns([1.5, 1])

with ab_col1:
    st.markdown(
        """
        <div class="card">
          <h3 style="margin-bottom:1rem;">Who I Am</h3>
          <p style="color:var(--text-secondary); line-height:1.8; font-size:1rem;">
          I'm a final-year Computer Science student with a passion for artificial intelligence and data science. 
          My journey in tech has been driven by curiosity and a desire to solve real-world problems using intelligent systems.
          </p>
          <p style="color:var(--text-secondary); line-height:1.8; font-size:1rem; margin-top:1rem;">
          I specialize in building end-to-end machine learning pipelines, from data preprocessing to model deployment. 
          My experience spans across computer vision, natural language processing, and creating AI-powered applications 
          that deliver tangible business value.
          </p>
          <div class="tags" style="margin-top:1.5rem;">
            <span class="tag">🐍 Python</span>
            <span class="tag">🤖 TensorFlow</span>
            <span class="tag">📊 scikit-learn</span>
            <span class="tag">👁️ OpenCV</span>
            <span class="tag">🔤 Transformers</span>
            <span class="tag">💾 SQL</span>
            <span class="tag">📈 Plotly</span>
            <span class="tag">⚡ Streamlit</span>
            <span class="tag">🦜 LangChain</span>
            <span class="tag">🔥 PyTorch</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with ab_col2:
    st.markdown(
        """
        <div class="card">
          <h3 style="margin-bottom:1.5rem;">Quick Connect</h3>
          <div style="line-height:2.2;">
            <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.8rem;">
              <span style="font-size:1.5rem;">📧</span>
              <div>
                <div style="font-size:0.8rem; color:var(--muted); text-transform:uppercase; letter-spacing:0.5px;">Email</div>
                <div style="color:var(--text-secondary); font-weight:500;">anshkedia.04@gmail.com</div>
              </div>
            </div>
            <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.8rem;">
              <span style="font-size:1.5rem;">💼</span>
              <div>
                <div style="font-size:0.8rem; color:var(--muted); text-transform:uppercase; letter-spacing:0.5px;">LinkedIn</div>
                <a href="https://www.linkedin.com/in/ansh-kedia-249843266/" target="_blank" style="color:var(--brand); text-decoration:none; font-weight:500;">linkedin.com/in/anshkedia</a>
              </div>
            </div>
            <div style="display:flex; align-items:center; gap:0.8rem;">
              <span style="font-size:1.5rem;">💻</span>
              <div>
                <div style="font-size:0.8rem; color:var(--muted); text-transform:uppercase; letter-spacing:0.5px;">GitHub</div>
                <a href="https://github.com/anshkedia-04" target="_blank" style="color:var(--brand); text-decoration:none; font-weight:500;">github.com/anshkedia-04</a>
              </div>
            </div>
          </div>
          <div style="margin-top:1.8rem; display:flex; gap:0.8rem;">
            <a class="btn btn-primary" href="mailto:anshkedia.04@gmail.com" style="flex:1; text-decoration:none; justify-content:center;">
              Email Me
            </a>
            <a class="btn btn-ghost" href="https://github.com/anshkedia-04" target="_blank" style="flex:1; text-decoration:none; justify-content:center;">
              GitHub
            </a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =========================
# Skills Section
# =========================
st.markdown("## Skills & Expertise 🎯")
st.caption("My technical arsenal across different domains")

skill_categories = {
    "Programming Languages": [
        ("Python", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"),
        ("Java", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"),
        ("SQL", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"),
        ("Git", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"),
    ],
    "Data Science & Analytics": [
        ("Pandas", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"),
        ("NumPy", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg"),
        ("Scikit-learn", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg"),
    ],
    "Deep Learning Frameworks": [
        ("TensorFlow", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg"),
        ("PyTorch", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg"),
        ("Keras", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/keras/keras-original.svg"),
    ],
    "Computer Vision": [
        ("OpenCV", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg"),
        ("MediaPipe", "https://imgs.search.brave.com/fzKrZ13dBAhof8JjX-t39wbArWfq_8znKIhuG7Gp6go/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/aWNvbnNjb3V0LmNv/bS9pY29uL3ByZW1p/dW0vcG5nLTI1Ni10/aHVtYi9uZXVyYWwt/bmV0d29yay1sb2dv/LWljb24tc3ZnLXBu/Zy1kb3dubG9hZC0x/NTM1MTMwLnBuZz9m/PXdlYnAmdz0xMjg"),
    ],
    "NLP & LLMs": [
        ("LangChain", "https://imgs.search.brave.com/IgPYZP9QFG0iiIPnFZzQuNSHM7zTYelvbt3DfhT2eYA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9yZWdp/c3RyeS5ucG1taXJy/b3IuY29tL0Bsb2Jl/aHViL2ljb25zLXN0/YXRpYy1wbmcvbGF0/ZXN0L2ZpbGVzL2Rh/cmsvbGFuZ3NtaXRo/LnBuZw"),
        ("Hugging Face", "https://huggingface.co/front/assets/huggingface_logo-noborder.svg"),
        ("Transformers", "https://huggingface.co/front/assets/huggingface_logo-noborder.svg"),
    ],
    "Data Visualization": [
        ("Streamlit", "https://streamlit.io/images/brand/streamlit-mark-color.png"),
        ("Tableau", "https://cdn.worldvectorlogo.com/logos/tableau-software.svg"),
        ("Power BI", "https://imgs.search.brave.com/p94jLqUg8ptH4YJkAAkACVma2gKzLJBw_JK-1h3oZzc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly8xMDAw/bG9nb3MubmV0L3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIyLzA4/L01pY3Jvc29mdC1Q/b3dlci1CSS1Mb2dv/LTUwMHgyODEucG5n"),
    ]
}

col1, col2 = st.columns(2)

for i, (category, skills) in enumerate(skill_categories.items()):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"### {category}")
        for name, icon_url in skills:
            icon_html = f'<img src="{icon_url}" alt="{name}" style="width:32px;height:32px;object-fit:contain;">'
            st.markdown(
                f"""
                <div class="skill-item">
                    <div class="skill-icon">
                        {icon_html}
                    </div>
                    <span style="font-size:1rem; font-weight:500; color:var(--text);">{name}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =========================
# Projects Section
# =========================
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.markdown("## Featured Projects 🚀")
st.caption("Explore my latest work in AI, ML, and Data Science")

PROJECTS = [
    {
        "title": "🔮 LifePulse",
        "desc": "An AI synthesis engine that reasons across environment signals to intelligently guide your next actions.",
        "tags": ["FastAPI", "React", "PostgreSQL", "Reasoning AI"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/LifePulse.png?raw=true",
        "repo": None,
        "demo": None,
        "status": "🚧 In Progress"
    },
    {
        "title": "✈️ VoyageAI",
        "desc": "AI-powered travel planner generating personalized itineraries based on preferences and real-time data.",
        "tags": ["FastAPI", "LangChain", "Groq", "Streamlit"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/Voyage_AI.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/VoyageAI-Smart-Travel-Assistant",
        "demo": "https://voyageai-smart-travel-assistant-pkrk9xcpwhhynq4h3eylis.streamlit.app/",
        "status": "✅ Live"
    },
    {
        "title": "🏥 MedAssist-XR",
        "desc": "Virtual healthcare assistant for symptom analysis, lab report interpretation, and health insights.",
        "tags": ["FastAPI", "LangChain", "Groq", "RAG"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/MedAssist.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/VoyageAI-Smart-Travel-Assistant",
        "demo": None,
        "status": "✅ Complete"
    },
    {
        "title": "😷 Facemask 360",
        "desc": "Comprehensive facial recognition solution for attendance marking with mask detection capabilities.",
        "tags": ["FaceNet", "OpenCV", "Deep Learning", "Streamlit"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/FaceMask.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/Smart_Attend",
        "demo": None,
        "status": "✅ Complete"
    },
    {
        "title": "🏡 BrickWise",
        "desc": "Bangalore house price prediction with advanced regression, feature engineering, and hyperparameter tuning.",
        "tags": ["Regression", "EDA", "Feature Engineering", "Streamlit"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/Brickwise.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/House-Price-Prediction-",
        "demo": "https://bengaluru-housepriceprediction.streamlit.app/",
        "status": "✅ Live"
    },
    {
        "title": "☕ BrewBot",
        "desc": "Intelligent FAQ chatbot for cafés using embeddings and semantic search for accurate responses.",
        "tags": ["LangChain", "HuggingFace", "NLP", "Streamlit"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/BrewBot.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/BrewBot",
        "demo": None,
        "status": "✅ Complete"
    },
    {
        "title": "🖱️ VisionMouse",
        "desc": "Control mouse cursor with hand gestures using computer vision and gesture recognition.",
        "tags": ["MediaPipe", "OpenCV", "Computer Vision"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/VisionMouse.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/Gesture_Mouse_Control",
        "demo": None,
        "status": "✅ Complete"
    },
    {
        "title": "🔊 AirTune",
        "desc": "Gesture-based volume controller using hand tracking and real-time computer vision.",
        "tags": ["MediaPipe", "OpenCV", "Hand Tracking"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/AirTune.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/AirTune",
        "demo": None,
        "status": "✅ Complete"
    }
]

# Tag filter
all_tags = ["All"] + sorted({t for p in PROJECTS for t in p["tags"]})
ft_col1, ft_col2 = st.columns([0.7, 0.3])

with ft_col1:
    active_tag = st.segmented_control("Filter by Technology", options=all_tags, default="All", key="tag_filter")

with ft_col2:
    search = st.text_input("🔍 Search", placeholder="Search projects...", label_visibility="collapsed")

# Filter projects
rows = []
for p in PROJECTS:
    if active_tag != "All" and active_tag not in p["tags"]:
        continue
    if search and (search.lower() not in p["title"].lower() and search.lower() not in p["desc"].lower()):
        continue
    rows.append(p)

# Display projects
if not rows:
    st.info("🔍 No projects match your filter. Try adjusting your search criteria.")
else:
    for i in range(0, len(rows), 3):
        cols = st.columns(3, gap="large")
        batch = rows[i:i+3]
        for c, p in zip(cols, batch):
            with c:
                status_colors = {
                    "✅ Live": "rgba(52,211,153,0.15)",
                    "✅ Complete": "rgba(96,165,250,0.15)",
                    "🚧 In Progress": "rgba(251,191,36,0.15)"
                }
                status_border = {
                    "✅ Live": "rgba(52,211,153,0.4)",
                    "✅ Complete": "rgba(96,165,250,0.4)",
                    "🚧 In Progress": "rgba(251,191,36,0.4)"
                }
                
                st.markdown(
                    f"""
                    <div class="card card-hover project-card">
                      <img src="{p['img']}" class="project-cover"/>
                      <div style="background:{status_colors.get(p.get('status', ''), 'rgba(255,255,255,0.05)')}; border:1px solid {status_border.get(p.get('status', ''), 'rgba(255,255,255,0.1)')}; padding:0.4rem 0.8rem; border-radius:8px; display:inline-block; font-size:0.8rem; font-weight:600; margin-bottom:0.8rem;">
                        {p.get('status', '✅ Complete')}
                      </div>
                      <h3 style="margin:0 0 0.5rem 0; font-size:1.3rem;">{p['title']}</h3>
                      <p style="color:var(--text-secondary); margin:0 0 1rem 0; line-height:1.6; font-size:0.95rem;">{p['desc']}</p>
                      <div class="tags">
                        {''.join([f'<span class="tag">{t}</span>' for t in p['tags']])}
                      </div>
                      <div style="display:flex; gap:0.8rem; margin-top:1.5rem;">
                        {"<a href='"+p['repo']+"' target='_blank' class='btn btn-primary' style='flex:1; text-decoration:none; justify-content:center;'>📂 Code</a>" if p['repo'] else "<span class='btn btn-ghost' style='flex:1; opacity:0.5; cursor:not-allowed; justify-content:center;'>🔒 Private</span>"}
                        {"<a href='"+p['demo']+"' target='_blank' class='btn btn-ghost' style='flex:1; text-decoration:none; justify-content:center;'>🚀 Demo</a>" if p['demo'] else ""}
                      </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =========================
# Resume Timeline Section
# =========================
st.markdown("## Professional Journey 📜")
st.caption("Education, experience, and certifications")

education_items = [
    {
        "when": "2022 — 2026",
        "title": "B.Tech in Computer Science & Engineering",
        "where": "Parul University",
        "detail": "Specialized in Data Science, ML, DL, Computer Vision, NLP, and Database Management Systems.",
        "logo": "logos/parul.png"
    },
    {
        "when": "2020 — 2022",
        "title": "Senior Secondary Education (Science)",
        "where": "Green Valley High School",
        "detail": "Focused on Physics, Chemistry, and Mathematics with distinction.",
        "logo": "logos/greenValley.webp"
    },
    {
        "when": "Till 2020",
        "title": "Secondary Education",
        "where": "Tree House High School",
        "detail": "Strong foundation in Science and Mathematics.",
        "logo": "logos/tree_house.webp"
    },
]

internship_items = [
    {
        "when": "May 2025 — July 2025",
        "title": "Data Science Summer Intern",
        "where": "Celebal Technologies Pvt. Ltd.",
        "detail": "Working on ML pipelines, A/B testing, and production-ready AI solutions.",
        "logo": "logos/celebal.png"
    },
    {
        "when": "Jan 2025 — Apr 2025",
        "title": "Machine Learning Intern",
        "where": "Unified Mentor Pvt. Ltd.",
        "detail": "Hands-on experience with Python, Scikit-learn, TensorFlow, and model deployment.",
        "logo": "logos/unified.png"
    },
    {
        "when": "Summer 2024",
        "title": "Data Science Intern",
        "where": "SkillForge E-Learning Solutions",
        "detail": "Data analytics, visualization, and machine learning model development.",
        "logo": "logos/skillforge.png"
    },
]

certification_items = [
    {
        "when": "2025",
        "title": "Career Essentials in Generative AI",
        "where": "Microsoft & LinkedIn",
        "detail": "Microsoft Copilot, Responsible AI, Prompt Engineering, and AI for Business.",
        "logo": "logos/microsoft.png"
    },
    {
        "when": "2025",
        "title": "Introduction to Generative AI",
        "where": "Google Cloud",
        "detail": "Fundamentals of LLMs, transformer architecture, and practical applications.",
        "logo": "logos/google.png"
    },
    {
        "when": "2024",
        "title": "Microsoft Cloud & AI Certification",
        "where": "Ignite Edition Challenge",
        "detail": "Cloud computing, Azure AI services, and Microsoft development tools.",
        "logo": "logos/microsoft.png"
    },
    {
        "when": "2024",
        "title": "Python Essentials",
        "where": "Cisco Networking Academy",
        "detail": "Advanced Python programming, data structures, and object-oriented design.",
        "logo": "logos/cisco.png"
    },
    {
        "when": "2024",
        "title": "Introduction to Data Science",
        "where": "Cisco Networking Academy",
        "detail": "Data science fundamentals, statistical analysis, and visualization techniques.",
        "logo": "logos/cisco.png"
    },
]

cL, cR = st.columns([1.4, 1])

with cL:
    tab1, tab2, tab3 = st.tabs(["🎓 Education", "💼 Experience", "🏆 Certifications"])
    
    with tab1:
        render_timeline(education_items)
    
    with tab2:
        render_timeline(internship_items)
    
    with tab3:
        render_timeline(certification_items)

with cR:
    # Resume download card
    try:
        with open("Resume.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            pdf_available = True
    except FileNotFoundError:
        pdf_bytes = b''
        pdf_available = False
    
    st.markdown(
        """
        <div class="card" style="text-align:center; padding:3rem 2rem; background:linear-gradient(135deg, rgba(52,211,153,0.1), rgba(96,165,250,0.1)); border:2px solid rgba(52,211,153,0.3);">
          <div style="font-size:4rem; margin-bottom:1rem;">📄</div>
          <h3 style="color:var(--text); margin-bottom:0.8rem; font-size:1.8rem;">Download Resume</h3>
          <p style="color:var(--text-secondary); margin-bottom:2rem; font-size:1rem; line-height:1.6;">
            Get a comprehensive overview of my skills, experience, and achievements in a professionally designed format.
          </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if pdf_available:
        st.download_button(
            "⬇️ Download PDF Resume",
            data=pdf_bytes,
            file_name="Ansh_Kedia_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.error("Resume.pdf not found in the directory")

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =========================
# Contact Section
# =========================
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align:center; margin:4rem 0 3rem 0;">
      <h2 style="font-size:clamp(2rem, 4vw, 3rem); margin-bottom:1rem;">Let's Build Something Amazing Together 🚀</h2>
      <p style="color:var(--text-secondary); font-size:1.2rem; max-width:700px; margin:0 auto; line-height:1.8;">
        Whether you have a project in mind, want to discuss opportunities, or just want to chat about AI and data science,
        I'm always excited to connect with like-minded professionals.
      </p>
    </div>
    """,
    unsafe_allow_html=True
)

_, col_center, _ = st.columns([1, 2.5, 1])

with col_center:
    st.markdown(
        """
        <div class="card" style="padding:3rem; text-align:center; background:linear-gradient(135deg, rgba(52,211,153,0.05), rgba(96,165,250,0.05)); border:1px solid rgba(255,255,255,0.15);">
          
          <div style="margin-bottom:2.5rem;">
            <p style="font-size:1rem; text-transform:uppercase; letter-spacing:2px; color:var(--muted); margin-bottom:1rem; font-weight:600;">
              Preferred Contact
            </p>
            <div style="background:rgba(255,255,255,0.08); padding:1.5rem 2rem; border-radius:16px; display:inline-block; border:1px solid rgba(255,255,255,0.15);">
              <span style="font-family:monospace; font-size:1.4rem; font-weight:600; color:var(--brand); letter-spacing:0.5px;">
                📧 anshkedia.04@gmail.com
              </span>
            </div>
          </div>
          
          <div style="display:flex; justify-content:center; gap:1.2rem; flex-wrap:wrap; margin-bottom:2.5rem;">
            <a class="btn btn-primary" href="mailto:anshkedia.04@gmail.com" style="text-decoration:none; padding:1rem 2rem;">
              <span style="font-size:1.2rem;">📧</span> Email Me
            </a>
            <a class="btn btn-ghost" href="https://www.linkedin.com/in/ansh-kedia-249843266/" target="_blank" style="text-decoration:none; padding:1rem 2rem;">
              <span style="font-size:1.2rem;">💼</span> LinkedIn
            </a>
            <a class="btn btn-ghost" href="https://github.com/anshkedia-04" target="_blank" style="text-decoration:none; padding:1rem 2rem;">
              <span style="font-size:1.2rem;">💻</span> GitHub
            </a>
          </div>
          
          <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:1.5rem; margin-top:1.5rem;">
            <div style="display:flex; align-items:center; justify-content:center; gap:0.8rem; color:var(--text-secondary);">
              <span style="font-size:1.5rem;">📍</span>
              <span style="font-size:1rem;">Based in Vadodara, Gujarat, India</span>
            </div>
            <p style="color:var(--muted); font-size:0.9rem; margin-top:0.8rem;">
              Open to opportunities worldwide
            </p>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# Footer
# =========================
st.markdown(
    f"""
    <div class="footer">
      <p style="font-size:1rem; margin-bottom:0.5rem;">
        © {datetime.now().year} Ansh Kedia
      </p>
      <p style="font-size:0.85rem; color:var(--muted);">
        Transforming data into intelligent solutions.
      </p>
    </div>
    """,
    unsafe_allow_html=True
)