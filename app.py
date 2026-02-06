# app.py
# -------------------------------------------------------
# A premium, animated Streamlit portfolio for a final-year
# Data Scientist. Modern UI, glassmorphism, typing effect,
# project tags & charts, resume timeline, and polished contact.
# -------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import io
import base64
from datetime import datetime
import os

import streamlit as st
import base64

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
# Custom CSS
# =========================
CUSTOM_CSS = """
<style>
:root{
  --bg: #0b1020;
  --card: rgba(255,255,255,0.06);
  --card-border: rgba(255,255,255,0.12);
  --text: #E5E7EB;
  --muted: #9CA3AF;
  --brand: #34D399;
  --brand-2: #60A5FA;
  --shadow: 0 20px 60px rgba(0,0,0,0.35);
}

.stApp {
  background: radial-gradient(1200px 600px at 10% -10%, rgba(52,211,153,0.2), transparent 40%),
              radial-gradient(1200px 600px at 110% 10%, rgba(96,165,250,0.14), transparent 40%),
              linear-gradient(180deg, #0b1020 0%, #0a0f1b 100%);
  color: var(--text);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial;
}

.block-container {padding-top: 2rem;}
h1, h2, h3 { letter-spacing: -0.02em; }
.big-title { font-weight: 900; font-size: clamp(2rem, 6vw, 3.5rem); line-height: 1.05; }
.subhead { color: var(--muted); font-size: clamp(1rem, 2.2vw, 1.25rem); }

/* Cards */
.card {
  background: var(--card);
  border: 1px solid var(--card-border);
  border-radius: 20px;
  box-shadow: var(--shadow);
  backdrop-filter: blur(12px);
  padding: 1.2rem 1.3rem;
}
.card-hover:hover { transform: translateY(-4px); background: rgba(255,255,255,0.08); }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; gap: .6rem;
  padding: .7rem 1rem; border-radius: 14px;
  font-weight: 600; text-decoration: none !important;
  border: 1px solid var(--card-border); box-shadow: var(--shadow);
}
.btn-primary { background: linear-gradient(90deg, var(--brand), var(--brand-2)); color: #0a0f1b; border: none; }
.btn-ghost { background: var(--card); color: var(--text); }
.btn-ghost:hover { background: rgba(255,255,255,0.09); }

.hr { height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent); margin: 1.5rem 0; border: 0; }

.tags { display:flex; gap:.5rem; flex-wrap:wrap; }
.tag {
  font-size:.8rem; padding:.35rem .6rem; border-radius:999px;
  background: rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18);
}

[data-testid="stDecoration"], footer, header { display: none !important; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# =========================
# Typing Effect (JS)
# =========================
TYPING_HTML = """
<div id="typing" class="subhead"></div>
<script>
const roles = ["Data Scientist", "ML Engineer", "Computer Vision", "NLP & RAG", "Analytics & Dashboards"];
const el = window.parent.document.querySelector('#typing') || document.querySelector('#typing');
let i = 0, j = 0, deleting = false, delay = 70, pause = 900;

function loop(){
  const word = roles[i % roles.length];
  if(!deleting){
    el.innerHTML = word.substring(0,j+1) + '<span class="cursor">▮</span>';
    j++;
    if(j === word.length){ deleting = true; setTimeout(loop, pause); return; }
  } else {
    el.innerHTML = word.substring(0,j-1) + '<span class="cursor">▮</span>';
    j--;
    if(j === 0){ deleting = false; i++; }
  }
  setTimeout(loop, deleting ? delay/2 : delay);
}
setTimeout(loop, 400);
</script>
"""

# =========================
# Helper: Image Loader
# =========================
def get_base64_image(image_file):
    try:
        with open(image_file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return ""

# =========================
# Hero Section
# =========================
import streamlit as st
import streamlit.components.v1 as components

# Hero Section
col1, col2 = st.columns([1.2, 1], gap="large")
with col1:
    st.markdown('<span class="badge">👨‍🔬 Data Science • AI Enthusiast</span>', unsafe_allow_html=True)
    st.markdown(
        '<div class="big-title">Hi 👋, I\'m <span style="background:linear-gradient(90deg,var(--brand),var(--brand-2)); -webkit-background-clip:text; color:transparent;">Ansh Kedia</span></div>',
        unsafe_allow_html=True
    )

    # ✅ FIXED TYPING EFFECT — runs JS safely
    components.html(
        """
        <div id="typing" style="color:#9CA3AF; font-size:1.25rem; margin-top:.3rem;"></div>
        <script>
        const roles = ["Data Scientist", "ML Engineer", "Computer Vision", "NLP & RAG", "Agentic Ai", "Analytics & Dashboards"];
        const el = document.getElementById('typing');
        let i = 0, j = 0, deleting = false, delay = 80, pause = 800;

        function loop(){
          const word = roles[i % roles.length];
          if(!deleting){
            el.innerHTML = word.substring(0,j+1) + '<span style="opacity:.5">▮</span>';
            j++;
            if(j === word.length){ deleting = true; setTimeout(loop, pause); return; }
          } else {
            el.innerHTML = word.substring(0,j-1) + '<span style="opacity:.5">▮</span>';
            j--;
            if(j === 0){ deleting = false; i++; }
          }
          setTimeout(loop, deleting ? delay/2 : delay);
        }
        setTimeout(loop, 500);
        </script>
        """,
        height=60,
    )

    st.markdown(
    """
    <div class="subhead" style="margin-top: 1rem;">
    <b>2026 CSE Graduate</b> | <b>AI & ML Enthusiast</b> | <b>Python Developer</b>.
    <br>
    Building the future of tech with <b>clean code</b> and <b>intelligent algorithms</b>.
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================
# About Section
# =========================
ab_col1, ab_col2 = st.columns([1.4, 1])
with ab_col1:
    st.markdown(
        """
        <div class="card card-hover">
          <h3>Quick Peek</h3>
          <p style="color:var(--muted)">
          Final-year Data Science student passionate about building intelligent systems that bridge the gap between data and decision-making.
          Experienced in designing and deploying AI solutions with a focus on performance and interpretability.
          </p>
          <div class="tags">
            <span class="tag">Python</span>
            <span class="tag">TensorFlow</span>
            <span class="tag">scikit-learn</span>
            <span class="tag">OpenCV</span>
            <span class="tag">Transformers</span>
            <span class="tag">SQL</span>
            <span class="tag">Plotly</span>
            <span class="tag">Streamlit</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with ab_col2:
    st.markdown(
        """
        <div class="card card-hover">
          <h3>Connect Instantly</h3>
          <div style="line-height:1.9;">
            <strong>Email:</strong> anshkedia.04@gmail.com<br>
            <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/ansh-kedia-249843266/" target="_blank">linkedin.com/in/anshkedia</a><br>
            <strong>GitHub:</strong> <a href="https://github.com/anshkedia-04" target="_blank">github.com/anshkedia</a><br>
          </div>
          <div style="margin-top: .8rem;">
            <a class="btn btn-ghost" href="mailto:anshkedia.04@gmail.com">Email Me</a>
            <a class="btn btn-primary" href="https://github.com/anshkedia-04" target="_blank">GitHub</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)


# =========================
# Skills Section
# =========================
st.markdown("## Skills & Expertise")
st.caption("A glance at my technical stack.")

# Define skill categories
skill_categories = {
    "Programming": [
        (" Python", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"),
        (" Java", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"),
        (" SQL", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"),
        (" Git", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"),
    ],
    "Data Science": [
        ("Pandas", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"),
        ("NumPy", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg"),
        ("Scikit-learn", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg"),
    ],
    "Deep Learning": [
        ("TensorFlow", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg"),
        ("PyTorch", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg"),
        ("CNN", "https://imgs.search.brave.com/fzKrZ13dBAhof8JjX-t39wbArWfq_8znKIhuG7Gp6go/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/aWNvbnNjb3V0LmNv/bS9pY29uL3ByZW1p/dW0vcG5nLTI1Ni10/aHVtYi9uZXVyYWwt/bmV0d29yay1sb2dv/LWljb24tc3ZnLXBu/Zy1kb3dubG9hZC0x/NTM1MTMwLnBuZz9m/PXdlYnAmdz0xMjg"),
    ],
    "Computer Vision": [
        ("OpenCV", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg"),
    ],
    "Natural Language Processing": [
        ("LangChain", "https://imgs.search.brave.com/IgPYZP9QFG0iiIPnFZzQuNSHM7zTYelvbt3DfhT2eYA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9yZWdp/c3RyeS5ucG1taXJy/b3IuY29tL0Bsb2Jl/aHViL2ljb25zLXN0/YXRpYy1wbmcvbGF0/ZXN0L2ZpbGVzL2Rh/cmsvbGFuZ3NtaXRo/LnBuZw"),
        ("LangGraph", "https://imgs.search.brave.com/IgPYZP9QFG0iiIPnFZzQuNSHM7zTYelvbt3DfhT2eYA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9yZWdp/c3RyeS5ucG1taXJy/b3IuY29tL0Bsb2Jl/aHViL2ljb25zLXN0/YXRpYy1wbmcvbGF0/ZXN0L2ZpbGVzL2Rh/cmsvbGFuZ3NtaXRo/LnBuZw"),
        ("Hugging Face", "https://huggingface.co/front/assets/huggingface_logo-noborder.svg"),
    ],
    "Visualization": [
        ("Streamlit", "https://streamlit.io/images/brand/streamlit-mark-color.png"),
        ("Plotly", "https://images.plot.ly/logo/plotly-logo-color.png"),
        ("Tableau", "https://cdn.worldvectorlogo.com/logos/tableau-software.svg"),
        ("PowerBI", "https://imgs.search.brave.com/p94jLqUg8ptH4YJkAAkACVma2gKzLJBw_JK-1h3oZzc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly8xMDAw/bG9nb3MubmV0L3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIyLzA4/L01pY3Jvc29mdC1Q/b3dlci1CSS1Mb2dv/LTUwMHgyODEucG5n"),
    ]
}

# Layout: 2 columns
col1, col2 = st.columns(2)

for i, (category, skills) in enumerate(skill_categories.items()):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"### {category}")
        for name, icon_url in skills:
            # Use an external icon if available, otherwise use a placeholder with the first letter
            icon_html = f'<img src="{icon_url}" alt="{name}" width="28" style="margin-right:10px;">' if "http" in icon_url else f'<div style="width:28px;height:28px;border-radius:50%;background:var(--brand);color:var(--bg);display:flex;align-items:center;justify-content:center;font-weight:bold;font-size:.8rem;margin-right:10px;">{name[1][0]}</div>'
            st.markdown(
                f"""
                <div style="display:flex; align-items:center; margin-bottom:10px;" class="card card-hover">
                    {icon_html}
                    <span style="font-size:16px;">{name}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# =========================
# Projects Section
# =========================
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.markdown("## Projects 🧑🏻‍💻")
st.caption("Filter by tag and explore interactive demos.")


PROJECTS = [
    {
        "title": "LifePulse (Currently working on it!)",
        "desc": "“An AI synthesis engine that reasons across environment signals to tell you what to do next.",
        "tags": ["FastAPI", "React", "PostgreSQL", "Reasoning Model"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/LifePulse.png?raw=true",
        "repo": None,
        "demo": None
    },
    {
        "title": "VoyageAI: Travel Planner",
        "desc": "An AI-powered travel planner that generates personalized itineraries based on user preferences.",
        "tags": ["FastAPI", "Langchain", "Groq", "Streamlit"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/Voyage_AI.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/VoyageAI-Smart-Travel-Assistant",
        "demo": "https://voyageai-smart-travel-assistant-pkrk9xcpwhhynq4h3eylis.streamlit.app/"
    },
    {
        "title": "MedAssist-XR",
        "desc": "MedAssist XR is an AI-driven virtual healthcare assistant that helps users analyze symptoms, interpret lab reports, find nearby doctors or hospitals, and get health insights — all through a chat-based interface.",
        "tags": ["FastAPI", "Langchain", "Groq", "Streamlit"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/MedAssist.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/VoyageAI-Smart-Travel-Assistant",
        "demo": None
    },
    {
        "title": "🧑🏻‍💻 Facemask 360",
        "desc": "A comprehensive solution for marking attendance using facial recognition.",
        "tags": ["Classification", "Facenet", "OpenCV", "Streamlit"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/FaceMask.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/Smart_Attend",
        "demo": None
    },
    {
        "title": "🏡 BrickWise: Bengaluru Price Prediction",
        "desc": "Regression pipeline with cross-validation, feature selection, and hyperparameter tuning.",
        "tags": ["ML", "Regression", "EDA","Streamlit"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/Brickwise.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/House-Price-Prediction-",
        "demo": "https://bengaluru-housepriceprediction.streamlit.app/"
    },
    {
        "title": "🤖 BrewBot",
        "desc": "Cafe FAQ Chatbot is an intelligent, open-source chatbot designed specifically for small cafés.",
        "tags": ["Langchain","HuggingFace","Streamlit"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/BrewBot.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/BrewBot",
        "demo": None
    },
    {
        "title": "🖱️ VisionMouse: Mouse Controller",
        "desc": "A deep learning project that uses computer vision to control the mouse cursor with hand movements.",
        "tags": ["MediaPipe", "OpenCV", "Streamlit"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/VisionMouse.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/Gesture_Mouse_Control",
        "demo": None
    },
    {
        "title": "🔊 AirTune: Volume Controller",
        "desc": "A deep learning project that uses computer vision to control the system volume with simple hand gestures.",
        "tags": ["MediaPipe", "OpenCV", "Streamlit"],
        "img": "https://github.com/anshkedia-04/Portfolio_Streamlit/blob/main/Project_images/AirTune.jpg?raw=true",
        "repo": "https://github.com/anshkedia-04/AirTune",
        "demo": None
    }
]

# Tag filter
all_tags = ["All"] + sorted({t for p in PROJECTS for t in p["tags"]})
ft_col1, ft_col2 = st.columns([.7, .3])
with ft_col1:
    active_tag = st.segmented_control("Filter by Tag", options=all_tags, default="All", key="tag_filter")
with ft_col2:
    search = st.text_input("Search", placeholder="Search by title or description")

# Filtered project rows
rows = []
for p in PROJECTS:
    if active_tag != "All" and active_tag not in p["tags"]:
        continue
    if search and (search.lower() not in p["title"].lower() and search.lower() not in p["desc"].lower()):
        continue
    rows.append(p)

# Display grid
if not rows:
    st.info("No projects match your filter. Try clearing search/tags.")
else:
    for i in range(0, len(rows), 3):
        cols = st.columns(3, gap="large")
        batch = rows[i:i+3]
        for c, p in zip(cols, batch):
            with c:
                st.markdown(
                    f"""
                    <div class="card card-hover" style="padding:1rem; border-radius:1rem; box-shadow:0 4px 15px rgba(0,0,0,0.15); background-color:var(--background-color);">
                      <img src="{p['img']}" class="project-cover" style="width:100%; border-radius:0.8rem; margin-bottom:0.7rem;"/>
                      <h3 style="margin:.6rem 0 0 0;">{p['title']}</h3>
                      <p style="color:var(--muted); margin:.25rem 0 .6rem 0;">{p['desc']}</p>
                      <div class="tags" style="margin-bottom:.7rem;">
                        {''.join([f'<span class="tag" style="display:inline-block; background:linear-gradient(135deg, #007bff, #00b4d8); color:white; padding:0.25rem 0.7rem; border-radius:0.6rem; margin:0.15rem; font-size:0.85rem; font-weight:500;">{t}</span>' for t in p['tags']])}
                      </div>
                      <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.8rem;">
                        <a href="{p['repo']}" target="_blank" class="btn btn-primary" style="text-decoration:none; background:#007bff; color:white; padding:0.4rem 0.9rem; border-radius:0.5rem; font-weight:500;">Repo</a>
                        {"<a href='"+p['demo']+"' target='_blank' class='btn btn-ghost' style='text-decoration:none; background:#f5f5f5; color:#007bff; padding:0.4rem 0.9rem; border-radius:0.5rem; font-weight:500;'>Demo</a>" if p['demo'] else ""}
                      </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)


# =========================
# Resume (Timeline - Separated into Tabs) - REVISED
# =========================

def render_timeline_item(it):
    """Renders a single timeline item using st.markdown with unsafe_allow_html."""
    
    # 1. Base64 conversion
    logo_html = ""
    try:
        # Check if the logo file exists
        if os.path.exists(it["logo"]):
            with open(it["logo"], "rb") as f:
                logo_b64 = base64.b64encode(f.read()).decode()
                logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="width:40px;height:40px;object-fit:contain;border-radius:8px;border:1px solid rgba(255,255,255,0.2);" />'
        else:
            # Placeholder for missing logo
            logo_html = '<div style="width:40px;height:40px;border-radius:8px;background:rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;font-size:.8rem;color:gray;">N/A</div>'
    except Exception:
         logo_html = '<div style="width:40px;height:40px;border-radius:8px;background:rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;font-size:.8rem;color:gray;">N/A</div>'

    # 2. Render the item HTML
    st.markdown(
        f"""
        <div class="timeline-item card-hover" style="display:flex; gap:1rem; align-items:center; padding:.9rem 1rem; border-radius:16px;">
          {logo_html}
          <div>
            <div style="color:#86efac; font-weight:700; font-size:.85rem;">{it['when']}</div>
            <div style="font-weight:700; margin-top:.15rem;">{it['title']}</div>
            <div style="color:var(--muted); font-size:.9rem;">{it['where']}</div>
            <div style="color:var(--muted); margin-top:.25rem; font-size:.9rem;">{it['detail']}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_timeline(items):
    """Renders the entire timeline structure."""
    st.markdown('<div class="timeline">', unsafe_allow_html=True)
    for it in items:
        render_timeline_item(it)
    st.markdown('</div>', unsafe_allow_html=True)


# Data remains the same... (Education, Internships, Certifications)
education_items = [
    {
        "when": "2022 — Present",
        "title": "B.Tech (Final Year) — Computer Science and Engineering",
        "where": "Parul University",
        "detail": "Coursework in: ML, DL, CV, NLP, DSA, DBMS.",
        "logo": "logos/parul.png"
    },
    {
        "when": "2020 — 2022",
        "title": "Senior Secondary Education — Science Stream",
        "where": "Green Valley High School",
        "detail": "Coursework in: Physics, Chemistry, Mathematics.",
        "logo": "logos/greenValley.webp"
    },
    {
        "when": "Till 2020",
        "title": "Secondary Education",
        "where": "Tree House High School",
        "detail": "Completed high school with a focus on Science and Mathematics.",
        "logo": "logos/tree_house.webp"
    },
]

internship_items = [
    # {
    #     "when": "Nov'25 - July'25",
    #     "title": "AI Intern",
    #     "where": "MyOnSite Healthcare Pvt. Ltd.",
    #     "detail": "Not started yet.",
    #     "logo": "logos/myonsite.jpg"
    # },
    {
        "when": "Summer 2025",
        "title": "Data Science Summer Intern",
        "where": "Celebal Technologies Pvt. Ltd.",
        "detail": "Shipped ML features with A/B tested improvements.",
        "logo": "logos/celebal.png"
    },
    {
        "when": "Jan 2025 - Apr 2025",
        "title": "Machine Learning Intern",
        "where": "Unified Mentor Pvt. Ltd.",
        "detail": "Gained hands-on experience with Python, Scikit-learn and Tensorflow",
        "logo": "logos/unified.png"
    },
    {
        "when": "Summer 2024",
        "title": "Data Science Intern",
        "where": "SkillForge E-Learning Solutions Pvt. Ltd.",
        "detail": "Hands-on experience in python, analytics and machine learning",
        "logo": "logos/skillforge.png"
    },
]

certification_items = [
    {
        "when": "2025",
        "title": "Career Essentials in Generative AI",
        "where": "Microsfoft and LinkedIn",
        "detail": "Microsoft Copilot, Responsible AI, Generative AI, AI for Business, Prompt Engineering",
        "logo": "logos/microsoft.png"
    },
    {
        "when": "2025",
        "title": "Introduction to Generative AI",
        "where": "Google Cloud",
        "detail": "Fundamentals of Generative AI, Large Language Models, and their applications.",
        "logo": "logos/google.png"
    },
    {
        "when": "2024",
        "title": "Microsoft Certification",
        "where": "Ignite Edition Challenge",
        "detail": "Explored cloud computing concepts, AI integration, and Microsoft tools.",
        "logo": "logos/microsoft.png"
    },
    {
        "when": "2024",
        "title": "Cisco Certification",
        "where": "Python Essentials",
        "detail": "Built a strong foundation in Python programming, data structures, and scripting.",
        "logo": "logos/cisco.png"
    },
    {
        "when": "2024",
        "title": "Cisco Certification",
        "where": "Introduction to Data Science",
        "detail": "Gained foundational knowledge in data science concepts, tools, and techniques.",
        "logo": "logos/cisco.png"
    },
]
# --- REVISED STREAMLIT DISPLAY LOGIC ---
st.markdown("## Highlights 📜")
st.caption("Education, internships, and certifications organized by timeline.")

cL, cR = st.columns([1.3, 1])
with cL:
    tab1, tab2, tab3 = st.tabs(["Education", "Internships", "Certifications"])
    
    with tab1:
        # 🔑 FIX: Direct Python rendering of each item inside the timeline container
        render_timeline(education_items) 

    with tab2:
        # 🔑 FIX: Direct Python rendering of each item inside the timeline container
        render_timeline(internship_items)
        
    with tab3:
        # 🔑 FIX: Direct Python rendering of each item inside the timeline container
        render_timeline(certification_items)

# The resume download card (cR) remains the same
# ... (Resume download code here) ...

with cR:
    # Resume PDF download (assuming 'Resume.pdf' is available)
    try:
        with open("Resume.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            pdf_available = True
    except FileNotFoundError:
        pdf_bytes = b''
        pdf_available = False

    st.markdown(
        """
        <style>
        .resume-card {
            background: linear-gradient(135deg, #1f2937, #111827);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            color: white;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            transition: transform 0.2s ease-in-out;
            margin-bottom: 1.5rem;
        }
        .resume-card:hover {
            transform: scale(1.03);
        }
        .resume-title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #facc15; /* gold */
        }
        .resume-desc {
            font-size: 16px;
            color: #d1d5db;
            margin-bottom: 20px;
        }
        div.stDownloadButton > button {
            background: linear-gradient(90deg, #3b82f6, #06b6d4);
            color: white;
            border-radius: 12px;
            padding: 10px 18px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
            font-weight: 600;
        }
        div.stDownloadButton > button:hover {
            background: linear-gradient(90deg, #06b6d4, #3b82f6);
            transform: translateY(-3px);
            box-shadow: 0px 8px 15px rgba(0,0,0,0.3);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="resume-card">
            <h3 class="resume-title">📄 My Resume</h3>
            <p class="resume-desc">Download a concise, elegant 1-page resume to know more about my journey.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if pdf_available:
        st.download_button("⬇️ Download Resume", data=pdf_bytes, file_name="Resume.pdf", mime="application/pdf", use_container_width=True)
    else:
        st.error("Resume.pdf file not found in the current directory.")


st.markdown('<div class="hr"></div>', unsafe_allow_html=True)


# =========================
# Final Contact Section
# =========================
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)

# 1. Header Area
st.markdown(
    """
    <div style="text-align: center; margin-top: 3rem; margin-bottom: 2rem;">
        <h2>Let's Connect 🤝</h2>
        <p style="color:var(--muted); font-size: 1.1rem; max-width: 600px; margin: 0 auto;">
            I’m actively looking for new opportunities in <b>AI/ML</b> and <b>Data Science</b>. 
            Whether you have a question, a project idea, or just want to discuss the latest in tech, 
            my inbox is always open!
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 2. The "Contact Card"
_, col_center, _ = st.columns([1, 2, 1])

with col_center:
    st.markdown(
        """
        <div class="card" style="text-align: center; padding: 2.5rem; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; background: rgba(255,255,255,0.02);">
            
            <div style="margin-bottom: 2rem;">
                <p style="font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; color: var(--muted); margin-bottom: 0.5rem;">
                    Drop me an email at
                </p>
                <div style="background: rgba(255, 255, 255, 0.08); padding: 12px 20px; border-radius: 8px; display: inline-block;">
                    <span style="font-family: monospace; font-size: 1.3rem; font-weight: bold; color: #fff;">
                        anshkedia.04@gmail.com
                    </span>
                </div>
            </div>

            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a class="btn btn-primary" href="https://www.linkedin.com/in/ansh-kedia-249843266/" target="_blank" style="text-decoration: none;">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" width="20" height="20" style="vertical-align: middle; margin-right: 8px;">
                    LinkedIn
                </a>
                <a class="btn btn-ghost" href="https://github.com/anshkedia-04" target="_blank" style="text-decoration: none; border: 1px solid rgba(255,255,255,0.2);">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="20" height="20" style="vertical-align: middle; margin-right: 8px;">
                    GitHub
                </a>
            </div>
            
            <div style="margin-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 1rem;">
                <p style="font-size: 0.85rem; color: var(--muted);">Based in Vadodara, India 🇮🇳</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
# =========================
# Footer
# =========================
st.write("")
st.markdown(
    f"""
    <div class="footer" style="text-align:center; margin:2rem 0 1rem 0;">
      © {datetime.now().year} Ansh Kedia • Built with Streamlit & ❤️
    </div>
    """,
    unsafe_allow_html=True
)