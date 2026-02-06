# app.py
# -------------------------------------------------------
# Professional Streamlit Portfolio for Ansh Kedia
# Data Scientist | AI/ML Engineer | Final Year CSE Student
# Modern UI with glassmorphism, smooth animations, and clean architecture
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
# Page Configuration
# =========================
st.set_page_config(
    page_title="Ansh Kedia — AI/ML Portfolio",
    page_icon="🚀",
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
  --bg-primary: #0a0e1a;
  --bg-secondary: #0f1624;
  --card-bg: rgba(255, 255, 255, 0.04);
  --card-border: rgba(255, 255, 255, 0.08);
  --text-primary: #ffffff;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --brand-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --accent-cyan: #06b6d4;
  --accent-purple: #8b5cf6;
  --accent-green: #10b981;
  --shadow-lg: 0 20px 60px rgba(0, 0, 0, 0.4);
  --shadow-xl: 0 25px 80px rgba(0, 0, 0, 0.5);
}

* {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.stApp {
  background: 
    radial-gradient(ellipse 1400px 800px at 20% 10%, rgba(102, 126, 234, 0.15), transparent),
    radial-gradient(ellipse 1200px 600px at 80% 90%, rgba(139, 92, 246, 0.12), transparent),
    linear-gradient(180deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
  color: var(--text-primary);
}

.block-container {
  padding: 3rem 2rem 2rem 2rem;
  max-width: 1400px;
}

/* Typography */
h1, h2, h3, h4 {
  font-weight: 700;
  letter-spacing: -0.025em;
  color: var(--text-primary);
}

.hero-title {
  font-size: clamp(2.5rem, 7vw, 4.5rem);
  font-weight: 900;
  line-height: 1.1;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: clamp(1.1rem, 2.5vw, 1.4rem);
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 2rem;
}

.section-title {
  font-size: clamp(1.8rem, 4vw, 2.5rem);
  margin-bottom: 0.5rem;
  position: relative;
  display: inline-block;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 0;
  width: 60px;
  height: 4px;
  background: var(--brand-gradient);
  border-radius: 2px;
}

/* Badge */
.badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.3);
  border-radius: 50px;
  font-size: 0.875rem;
  font-weight: 600;
  color: #c4b5fd;
  margin-bottom: 1.5rem;
}

/* Cards */
.card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 24px;
  padding: 2rem;
  backdrop-filter: blur(20px);
  box-shadow: var(--shadow-lg);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  height: 100%;
}

.card-hover {
  cursor: pointer;
}

.card-hover:hover {
  transform: translateY(-8px);
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(255, 255, 255, 0.15);
  box-shadow: var(--shadow-xl);
}

.card h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: var(--text-primary);
}

.card p {
  color: var(--text-secondary);
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

/* Project Cards */
.project-card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 20px;
  overflow: hidden;
  backdrop-filter: blur(20px);
  transition: all 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.project-card:hover {
  transform: translateY(-10px);
  border-color: rgba(139, 92, 246, 0.4);
  box-shadow: 0 25px 80px rgba(139, 92, 246, 0.3);
}

.project-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-bottom: 1px solid var(--card-border);
}

.project-content {
  padding: 1.5rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.project-title {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
  color: var(--text-primary);
}

.project-desc {
  color: var(--text-secondary);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 1rem;
  flex-grow: 1;
}

/* Tags */
.tags {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 1.5rem;
}

.tag {
  padding: 0.4rem 0.9rem;
  background: rgba(139, 92, 246, 0.12);
  border: 1px solid rgba(139, 92, 246, 0.25);
  border-radius: 50px;
  font-size: 0.8rem;
  font-weight: 600;
  color: #c4b5fd;
  white-space: nowrap;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
}

.btn-primary {
  background: var(--brand-gradient);
  color: white;
  box-shadow: 0 8px 20px rgba(139, 92, 246, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 28px rgba(139, 92, 246, 0.4);
}

.btn-secondary {
  background: var(--card-bg);
  color: var(--text-primary);
  border: 1px solid var(--card-border);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.2);
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
  background: linear-gradient(180deg, var(--accent-purple), var(--accent-cyan));
}

.timeline-item {
  position: relative;
  margin-bottom: 1.5rem;
  padding: 1.5rem;
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 16px;
  backdrop-filter: blur(20px);
  transition: all 0.3s ease;
}

.timeline-item::before {
  content: '';
  position: absolute;
  left: -2.5rem;
  top: 2rem;
  width: 12px;
  height: 12px;
  background: var(--accent-purple);
  border-radius: 50%;
  border: 3px solid var(--bg-primary);
  box-shadow: 0 0 20px rgba(139, 92, 246, 0.6);
}

.timeline-item:hover {
  transform: translateX(8px);
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(139, 92, 246, 0.3);
}

.timeline-period {
  color: var(--accent-green);
  font-weight: 700;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 0.5rem;
}

.timeline-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
}

.timeline-org {
  color: var(--text-secondary);
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.timeline-detail {
  color: var(--text-muted);
  font-size: 0.9rem;
  line-height: 1.6;
}

/* Skill Pills */
.skill-category {
  margin-bottom: 2rem;
}

.skill-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 1rem;
}

.skill-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.25rem;
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 12px;
  backdrop-filter: blur(20px);
  transition: all 0.3s ease;
}

.skill-item:hover {
  transform: translateY(-4px);
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(139, 92, 246, 0.4);
  box-shadow: 0 8px 25px rgba(139, 92, 246, 0.2);
}

.skill-icon {
  width: 32px;
  height: 32px;
  object-fit: contain;
  filter: drop-shadow(0 0 8px rgba(139, 92, 246, 0.3));
}

.skill-name {
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--text-primary);
}

/* Divider */
.divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--card-border), transparent);
  margin: 4rem 0;
  border: none;
}

/* Contact Section */
.contact-card {
  text-align: center;
  padding: 3rem 2rem;
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 24px;
  backdrop-filter: blur(20px);
}

.contact-email {
  display: inline-block;
  padding: 1rem 2rem;
  background: rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.3);
  border-radius: 12px;
  font-family: 'Courier New', monospace;
  font-size: 1.2rem;
  font-weight: 700;
  color: #c4b5fd;
  margin: 1.5rem 0;
}

/* Footer */
.footer {
  text-align: center;
  padding: 2rem 0;
  color: var(--text-muted);
  font-size: 0.9rem;
  border-top: 1px solid var(--card-border);
  margin-top: 4rem;
}

/* Hide Streamlit Elements */
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stDecoration"] {display: none;}

/* Responsive */
@media (max-width: 768px) {
  .block-container {
    padding: 2rem 1rem;
  }
  
  .timeline {
    padding-left: 1.5rem;
  }
  
  .skill-grid {
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  }
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# =========================
# Helper Functions
# =========================
def get_base64_image(image_path):
    """Convert image to base64 string"""
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return None

def render_typing_effect():
    """Animated typing effect for roles"""
    components.html(
        """
        <div id="typing-container" style="min-height: 50px;">
            <div id="typing" style="color: #94a3b8; font-size: 1.3rem; font-weight: 500;"></div>
        </div>
        <script>
        const roles = [
            "Data Scientist 📊",
            "ML Engineer 🤖",
            "Computer Vision Expert 👁️",
            "NLP Specialist 💬",
            "Agentic AI Developer 🔗",
            "Full-Stack Developer 💻"
        ];
        
        const el = document.getElementById('typing');
        let roleIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        const typingSpeed = 80;
        const deletingSpeed = 40;
        const pauseDuration = 1500;
        
        function type() {
            const currentRole = roles[roleIndex];
            
            if (!isDeleting) {
                el.textContent = currentRole.substring(0, charIndex + 1);
                charIndex++;
                
                if (charIndex === currentRole.length) {
                    isDeleting = true;
                    setTimeout(type, pauseDuration);
                    return;
                }
            } else {
                el.textContent = currentRole.substring(0, charIndex - 1);
                charIndex--;
                
                if (charIndex === 0) {
                    isDeleting = false;
                    roleIndex = (roleIndex + 1) % roles.length;
                }
            }
            
            setTimeout(type, isDeleting ? deletingSpeed : typingSpeed);
        }
        
        setTimeout(type, 500);
        </script>
        """,
        height=60
    )

# =========================
# Data Definitions
# =========================

# Skills Data
SKILLS = {
    "Programming & Tools": [
        ("Python", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"),
        ("Java", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"),
        ("SQL", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"),
        ("Git", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"),
    ],
    "Data Science & ML": [
        ("Pandas", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"),
        ("NumPy", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg"),
        ("Scikit-learn", "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg"),
        ("TensorFlow", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg"),
        ("PyTorch", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg"),
    ],
    "AI & Deep Learning": [
        ("OpenCV", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg"),
        ("LangChain", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"),
        ("Hugging Face", "https://huggingface.co/front/assets/huggingface_logo-noborder.svg"),
    ],
    "Visualization": [
        ("Streamlit", "https://streamlit.io/images/brand/streamlit-mark-color.png"),
        ("Plotly", "https://images.plot.ly/logo/new-branding/plotly-logomark.png"),
        ("Tableau", "https://cdn.worldvectorlogo.com/logos/tableau-software.svg"),
        ("Power BI", "https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg"),
    ]
}

# Projects Data
PROJECTS = [
    {
        "title": "🌍 LifePulse",
        "desc": "An AI reasoning engine that synthesizes environmental signals to provide intelligent, context-aware recommendations for daily actions.",
        "tags": ["FastAPI", "React", "PostgreSQL", "Reasoning AI"],
        "img": "https://raw.githubusercontent.com/anshkedia-04/Portfolio_Streamlit/main/Project_images/LifePulse.png",
        "repo": None,
        "demo": None,
        "status": "🚧 In Development"
    },
    {
        "title": "✈️ VoyageAI",
        "desc": "AI-powered travel planner generating personalized itineraries based on user preferences using LLM technology.",
        "tags": ["FastAPI", "LangChain", "Groq", "Streamlit"],
        "img": "https://raw.githubusercontent.com/anshkedia-04/Portfolio_Streamlit/main/Project_images/Voyage_AI.jpg",
        "repo": "https://github.com/anshkedia-04/VoyageAI-Smart-Travel-Assistant",
        "demo": "https://voyageai-smart-travel-assistant-pkrk9xcpwhhynq4h3eylis.streamlit.app/",
        "status": None
    },
    {
        "title": "🏥 MedAssist-XR",
        "desc": "AI-driven virtual healthcare assistant for symptom analysis, lab report interpretation, and health insights via chat interface.",
        "tags": ["FastAPI", "LangChain", "Groq", "RAG"],
        "img": "https://raw.githubusercontent.com/anshkedia-04/Portfolio_Streamlit/main/Project_images/MedAssist.jpg",
        "repo": "https://github.com/anshkedia-04/MedAssist-XR",
        "demo": None,
        "status": None
    },
    {
        "title": "😷 FaceMask 360",
        "desc": "Comprehensive facial recognition solution for automated attendance tracking with real-time detection capabilities.",
        "tags": ["FaceNet", "OpenCV", "Deep Learning"],
        "img": "https://raw.githubusercontent.com/anshkedia-04/Portfolio_Streamlit/main/Project_images/FaceMask.jpg",
        "repo": "https://github.com/anshkedia-04/Smart_Attend",
        "demo": None,
        "status": None
    },
    {
        "title": "🏡 BrickWise",
        "desc": "ML-based house price prediction system with advanced regression techniques and comprehensive EDA.",
        "tags": ["ML", "Regression", "Feature Engineering"],
        "img": "https://raw.githubusercontent.com/anshkedia-04/Portfolio_Streamlit/main/Project_images/Brickwise.jpg",
        "repo": "https://github.com/anshkedia-04/House-Price-Prediction-",
        "demo": "https://bengaluru-housepriceprediction.streamlit.app/",
        "status": None
    },
    {
        "title": "🤖 BrewBot",
        "desc": "Intelligent FAQ chatbot designed for cafés, powered by open-source LLMs and retrieval-augmented generation.",
        "tags": ["LangChain", "HuggingFace", "RAG"],
        "img": "https://raw.githubusercontent.com/anshkedia-04/Portfolio_Streamlit/main/Project_images/BrewBot.jpg",
        "repo": "https://github.com/anshkedia-04/BrewBot",
        "demo": None,
        "status": None
    },
    {
        "title": "🖱️ VisionMouse",
        "desc": "Computer vision system for hands-free mouse control using real-time hand gesture recognition.",
        "tags": ["MediaPipe", "OpenCV", "CV"],
        "img": "https://raw.githubusercontent.com/anshkedia-04/Portfolio_Streamlit/main/Project_images/VisionMouse.jpg",
        "repo": "https://github.com/anshkedia-04/Gesture_Mouse_Control",
        "demo": None,
        "status": None
    },
    {
        "title": "🔊 AirTune",
        "desc": "Gesture-based volume controller using computer vision for touchless system audio management.",
        "tags": ["MediaPipe", "OpenCV", "CV"],
        "img": "https://raw.githubusercontent.com/anshkedia-04/Portfolio_Streamlit/main/Project_images/AirTune.jpg",
        "repo": "https://github.com/anshkedia-04/AirTune",
        "demo": None,
        "status": None
    }
]

# Experience Data
EXPERIENCES = {
    "education": [
        {
            "period": "2022 — 2026",
            "title": "B.Tech in Computer Science & Engineering",
            "organization": "Parul University",
            "detail": "Specialization in AI/ML • Relevant Coursework: Machine Learning, Deep Learning, Computer Vision, NLP, Data Structures & Algorithms",
            "logo": "logos/parul.png"
        },
        {
            "period": "2020 — 2022",
            "title": "Senior Secondary Education (12th Grade)",
            "organization": "Green Valley High School",
            "detail": "Science Stream • Physics, Chemistry, Mathematics • Achieved strong academic performance",
            "logo": "logos/greenValley.webp"
        }
    ],
    "internships": [
        {
            "period": "Summer 2025",
            "title": "Data Science Intern",
            "organization": "Celebal Technologies Pvt. Ltd.",
            "detail": "Developed ML features with A/B testing • Improved model performance metrics • Collaborated on production deployments",
            "logo": "logos/celebal.png"
        },
        {
            "period": "Jan 2025 — Apr 2025",
            "title": "Machine Learning Intern",
            "organization": "Unified Mentor Pvt. Ltd.",
            "detail": "Built end-to-end ML pipelines • Worked with scikit-learn, TensorFlow • Implemented classification and regression models",
            "logo": "logos/unified.png"
        },
        {
            "period": "Summer 2024",
            "title": "Data Science Intern",
            "organization": "SkillForge E-Learning Solutions Pvt. Ltd.",
            "detail": "Conducted exploratory data analysis • Built predictive models • Created interactive dashboards for insights",
            "logo": "logos/skillforge.png"
        }
    ],
    "certifications": [
        {
            "period": "2025",
            "title": "Career Essentials in Generative AI",
            "organization": "Microsoft & LinkedIn",
            "detail": "Microsoft Copilot • Responsible AI • Prompt Engineering • AI for Business",
            "logo": "logos/microsoft.png"
        },
        {
            "period": "2025",
            "title": "Introduction to Generative AI",
            "organization": "Google Cloud",
            "detail": "Fundamentals of Gen AI • Large Language Models • Practical applications and use cases",
            "logo": "logos/google.png"
        },
        {
            "period": "2024",
            "title": "Python Essentials",
            "organization": "Cisco Networking Academy",
            "detail": "Python programming fundamentals • Data structures • Object-oriented programming concepts",
            "logo": "logos/cisco.png"
        },
        {
            "period": "2024",
            "title": "Introduction to Data Science",
            "organization": "Cisco Networking Academy",
            "detail": "Data science fundamentals • Statistical analysis • Data visualization techniques",
            "logo": "logos/cisco.png"
        }
    ]
}

# =========================
# Hero Section
# =========================
st.markdown('<div style="margin-bottom: 4rem;">', unsafe_allow_html=True)

hero_col1, hero_col2 = st.columns([1.5, 1], gap="large")

with hero_col1:
    st.markdown('<span class="badge">🚀 AI Engineer • Data Scientist • Problem Solver</span>', unsafe_allow_html=True)
    st.markdown(
        '''
        <h1 class="hero-title">
            Hi, I'm <span style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Ansh Kedia</span>
        </h1>
        ''',
        unsafe_allow_html=True
    )
    
    render_typing_effect()
    
    st.markdown(
        '''
        <p class="hero-subtitle">
            Final-year <strong>CSE student</strong> passionate about building intelligent systems that solve real-world problems. 
            Experienced in <strong>Machine Learning</strong>, <strong>Computer Vision</strong>, <strong>NLP</strong>, and <strong>Full-Stack Development</strong>.
            <br><br>
            Currently seeking opportunities to apply AI/ML skills in impactful projects and innovative teams.
        </p>
        ''',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '''
        <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
            <a href="#projects" class="btn btn-primary" style="text-decoration: none;">
                View Projects 🚀
            </a>
            <a href="mailto:anshkedia.04@gmail.com" class="btn btn-secondary" style="text-decoration: none;">
                Get in Touch 📧
            </a>
        </div>
        ''',
        unsafe_allow_html=True
    )

with hero_col2:
    st.markdown(
        '''
        <div class="card">
            <h3 style="margin-bottom: 1.5rem;">🔗 Connect With Me</h3>
            <div style="line-height: 2.2;">
                <div style="margin-bottom: 0.75rem;">
                    <strong style="color: #c4b5fd;">📧 Email:</strong><br>
                    <a href="mailto:anshkedia.04@gmail.com" style="color: #94a3b8; text-decoration: none;">
                        anshkedia.04@gmail.com
                    </a>
                </div>
                <div style="margin-bottom: 0.75rem;">
                    <strong style="color: #c4b5fd;">💼 LinkedIn:</strong><br>
                    <a href="https://www.linkedin.com/in/ansh-kedia-249843266/" target="_blank" 
                       style="color: #94a3b8; text-decoration: none;">
                        linkedin.com/in/ansh-kedia
                    </a>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <strong style="color: #c4b5fd;">💻 GitHub:</strong><br>
                    <a href="https://github.com/anshkedia-04" target="_blank" 
                       style="color: #94a3b8; text-decoration: none;">
                        github.com/anshkedia-04
                    </a>
                </div>
            </div>
            <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                <a href="https://www.linkedin.com/in/ansh-kedia-249843266/" target="_blank" 
                   class="btn btn-secondary" style="text-decoration: none; flex: 1; min-width: 120px;">
                    LinkedIn
                </a>
                <a href="https://github.com/anshkedia-04" target="_blank" 
                   class="btn btn-primary" style="text-decoration: none; flex: 1; min-width: 120px;">
                    GitHub
                </a>
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# =========================
# About Section
# =========================
st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: var(--text-secondary); font-size: 1.1rem; margin-bottom: 2rem;">Building the future with AI, one project at a time</p>', unsafe_allow_html=True)

about_col1, about_col2 = st.columns([1.3, 1], gap="large")

with about_col1:
    st.markdown(
        '''
        <div class="card">
            <h3>👨‍💻 My Journey</h3>
            <p>
                I'm a final-year <strong>Computer Science Engineering student</strong> at Parul University, 
                specializing in <strong>Artificial Intelligence</strong> and <strong>Machine Learning</strong>.
            </p>
            <p>
                My passion lies in developing <strong>intelligent systems</strong> that bridge the gap between 
                complex data and actionable insights. From building <strong>computer vision applications</strong> 
                to creating <strong>conversational AI agents</strong>, I focus on solutions that are both 
                innovative and practical.
            </p>
            <p style="margin-bottom: 0;">
                Currently, I'm exploring <strong>Agentic AI</strong>, <strong>RAG systems</strong>, and 
                <strong>reasoning models</strong> while actively seeking internship opportunities to apply 
                my skills in real-world scenarios.
            </p>
        </div>
        ''',
        unsafe_allow_html=True
    )

with about_col2:
    st.markdown(
        '''
        <div class="card">
            <h3>🎯 What I Do Best</h3>
            <ul style="line-height: 2; color: var(--text-secondary); list-style: none; padding-left: 0;">
                <li>✅ <strong>Machine Learning:</strong> Predictive modeling & optimization</li>
                <li>✅ <strong>Deep Learning:</strong> Neural networks & computer vision</li>
                <li>✅ <strong>NLP & RAG:</strong> Conversational AI & document QA</li>
                <li>✅ <strong>Data Analytics:</strong> EDA, visualization & insights</li>
                <li>✅ <strong>Full-Stack:</strong> End-to-end application development</li>
            </ul>
        </div>
        ''',
        unsafe_allow_html=True
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# =========================
# Skills Section
# =========================
st.markdown('<h2 class="section-title">Technical Skills</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: var(--text-secondary); font-size: 1.1rem; margin-bottom: 2.5rem;">Technologies and tools I work with</p>', unsafe_allow_html=True)

for category, skills in SKILLS.items():
    st.markdown(f'<h3 style="margin-bottom: 1rem; font-size: 1.2rem;">{category}</h3>', unsafe_allow_html=True)
    
    cols = st.columns(min(len(skills), 4), gap="medium")
    for idx, (name, icon_url) in enumerate(skills):
        with cols[idx % len(cols)]:
            st.markdown(
                f'''
                <div class="skill-item">
                    <img src="{icon_url}" class="skill-icon" alt="{name}">
                    <span class="skill-name">{name}</span>
                </div>
                ''',
                unsafe_allow_html=True
            )
    st.markdown('<div style="margin-bottom: 2rem;"></div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# =========================
# Projects Section
# =========================
st.markdown('<a id="projects"></a><h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: var(--text-secondary); font-size: 1.1rem; margin-bottom: 2rem;">Explore my work in AI, ML, and software development</p>', unsafe_allow_html=True)

# Filter controls
filter_col1, filter_col2 = st.columns([2, 1])

with filter_col1:
    all_tags = ["All"] + sorted(list(set(tag for project in PROJECTS for tag in project["tags"])))
    selected_tag = st.segmented_control("Filter by Technology", options=all_tags, default="All")

with filter_col2:
    search_query = st.text_input("🔍 Search projects", placeholder="Type to search...", label_visibility="collapsed")

# Filter projects
filtered_projects = []
for project in PROJECTS:
    if selected_tag != "All" and selected_tag not in project["tags"]:
        continue
    if search_query and search_query.lower() not in project["title"].lower() and search_query.lower() not in project["desc"].lower():
        continue
    filtered_projects.append(project)

# Display projects
if not filtered_projects:
    st.info("🔍 No projects match your filter. Try different criteria!")
else:
    for i in range(0, len(filtered_projects), 3):
        cols = st.columns(3, gap="large")
        for idx, project in enumerate(filtered_projects[i:i+3]):
            with cols[idx]:
                status_badge = f'<span class="tag" style="background: rgba(251, 191, 36, 0.2); border-color: rgba(251, 191, 36, 0.4); color: #fbbf24;">{project["status"]}</span>' if project.get("status") else ""
                
                st.markdown(
                    f'''
                    <div class="project-card">
                        <img src="{project["img"]}" class="project-image" alt="{project["title"]}">
                        <div class="project-content">
                            <h3 class="project-title">{project["title"]}</h3>
                            {status_badge}
                            <p class="project-desc">{project["desc"]}</p>
                            <div class="tags">
                                {"".join([f'<span class="tag">{tag}</span>' for tag in project["tags"]])}
                            </div>
                            <div style="display: flex; gap: 0.75rem; margin-top: auto;">
                                {f'<a href="{project["repo"]}" target="_blank" class="btn btn-secondary" style="text-decoration: none; flex: 1;">GitHub</a>' if project["repo"] else '<span style="flex: 1;"></span>'}
                                {f'<a href="{project["demo"]}" target="_blank" class="btn btn-primary" style="text-decoration: none; flex: 1;">Live Demo</a>' if project["demo"] else ''}
                            </div>
                        </div>
                    </div>
                    ''',
                    unsafe_allow_html=True
                )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# =========================
# Experience Section
# =========================
st.markdown('<h2 class="section-title">Experience & Education</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: var(--text-secondary); font-size: 1.1rem; margin-bottom: 2.5rem;">My professional journey and academic background</p>', unsafe_allow_html=True)

timeline_col1, timeline_col2 = st.columns([1.4, 1], gap="large")

with timeline_col1:
    tab1, tab2, tab3 = st.tabs(["🎓 Education", "💼 Internships", "📜 Certifications"])
    
    def render_timeline_items(items):
        """Render timeline items with logos"""
        st.markdown('<div class="timeline">', unsafe_allow_html=True)
        for item in items:
            logo_html = ""
            if os.path.exists(item["logo"]):
                try:
                    with open(item["logo"], "rb") as f:
                        logo_b64 = base64.b64encode(f.read()).decode()
                        logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="width: 48px; height: 48px; object-fit: contain; border-radius: 8px; border: 1px solid var(--card-border);">'
                except:
                    logo_html = '<div style="width: 48px; height: 48px; border-radius: 8px; background: var(--card-bg); display: flex; align-items: center; justify-content: center; font-weight: bold; color: var(--text-muted);">🎓</div>'
            else:
                logo_html = '<div style="width: 48px; height: 48px; border-radius: 8px; background: var(--card-bg); display: flex; align-items: center; justify-content: center; font-weight: bold; color: var(--text-muted);">🎓</div>'
            
            st.markdown(
                f'''
                <div class="timeline-item">
                    <div style="display: flex; gap: 1rem; align-items: flex-start;">
                        {logo_html}
                        <div style="flex: 1;">
                            <div class="timeline-period">{item["period"]}</div>
                            <div class="timeline-title">{item["title"]}</div>
                            <div class="timeline-org">{item["organization"]}</div>
                            <div class="timeline-detail">{item["detail"]}</div>
                        </div>
                    </div>
                </div>
                ''',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab1:
        render_timeline_items(EXPERIENCES["education"])
    
    with tab2:
        render_timeline_items(EXPERIENCES["internships"])
    
    with tab3:
        render_timeline_items(EXPERIENCES["certifications"])

with timeline_col2:
    # Resume download card
    st.markdown(
        '''
        <div class="card" style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📄</div>
            <h3 style="margin-bottom: 1rem;">Download Resume</h3>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">
                Get a comprehensive overview of my skills, experience, and achievements in a single page.
            </p>
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    try:
        with open("Resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="⬇️ Download PDF Resume",
                data=pdf_file.read(),
                file_name="Ansh_Kedia_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except FileNotFoundError:
        st.warning("⚠️ Resume file not found. Please add Resume.pdf to the project directory.")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# =========================
# Contact Section
# =========================
st.markdown('<h2 class="section-title" style="text-align: center;">Let\'s Connect</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: var(--text-secondary); font-size: 1.1rem; text-align: center; margin-bottom: 3rem;">Have a project in mind or want to discuss AI/ML? Let\'s talk!</p>', unsafe_allow_html=True)

_, contact_col, _ = st.columns([1, 2, 1])

with contact_col:
    st.markdown(
        '''
        <div class="contact-card">
            <div style="font-size: 4rem; margin-bottom: 1rem;">📬</div>
            <h3 style="margin-bottom: 1rem;">Get In Touch</h3>
            <p style="color: var(--text-secondary); margin-bottom: 1.5rem;">
                I'm actively seeking opportunities in <strong>AI/ML, Data Science, and Software Development</strong>.
                <br>Whether it's a job, internship, or collaboration – I'd love to hear from you!
            </p>
            <div class="contact-email">
                anshkedia.04@gmail.com
            </div>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-top: 2rem;">
                <a href="mailto:anshkedia.04@gmail.com" class="btn btn-primary" style="text-decoration: none;">
                    📧 Send Email
                </a>
                <a href="https://www.linkedin.com/in/ansh-kedia-249843266/" target="_blank" class="btn btn-secondary" style="text-decoration: none;">
                    💼 LinkedIn
                </a>
                <a href="https://github.com/anshkedia-04" target="_blank" class="btn btn-secondary" style="text-decoration: none;">
                    💻 GitHub
                </a>
            </div>
            <div style="margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--card-border);">
                <p style="color: var(--text-muted); font-size: 0.9rem;">
                    📍 Based in Vadodara, Gujarat, India 🇮🇳
                </p>
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

# =========================
# Footer
# =========================
st.markdown(
    f'''
    <div class="footer">
        <p>© {datetime.now().year} Ansh Kedia • Built with ❤️ using Streamlit</p>
        <p style="margin-top: 0.5rem; font-size: 0.85rem;">
            Designed for innovation • Crafted for impact
        </p>
    </div>
    ''',
    unsafe_allow_html=True
)
