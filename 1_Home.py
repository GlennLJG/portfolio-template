import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from constant import *
from PIL import Image
from components import load_css, render_header, render_footer

# Configuration de la page
st.set_page_config(
    page_title='Glenn - Ingénieur Data/IA',
    layout="wide",
    page_icon='🏠',
    initial_sidebar_state="collapsed"
)

# CSS personnalisé pour un design moderne
st.markdown("""
<style>
    /* Styles spécifiques à la page d'accueil */
    .profile-section h2 {
        font-size: 3rem;
        margin: 0 0 1rem 0;
    }
    
    .profile-section h3 {
        font-size: 2.2rem;
        margin-bottom: 1.5rem;
    }
    
    .profile-section p {
        font-size: 1.5rem;
        line-height: 1.6;
        text-align: left;
    }
    
    .competency-card h4 {
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .competency-card p {
        font-size: 1.3rem;
        line-height: 1.6;
    }
    
    .expertise-title {
        color: var(--brown-text);
        margin-bottom: 1rem;
    }
    
    .skills-section {
        text-align: center;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

load_css()

render_header()

# ================ SECTION PRÉSENTATION ================
col1, col2, col3, col4 = st.columns([1.2, 1, 2, 1])


with col2:
    # Section image
    try:
        profile_image = Image.open("images/portrait.jpg")
        st.image(profile_image, width=400, use_container_width=False)
    except:
        st.markdown("""
        <div style="width: 300px; height: 300px; border-radius: 20px; background: var(--brown-encart); 
                    display: flex; align-items: center; justify-content: center; color: var(--white-text); font-size: 6rem; margin: 0 auto;">
            👨‍💻
        </div>
        """, unsafe_allow_html=True)

with col3:
    # Section texte
    st.markdown("""
        <div class="profile-section">
            <h2 class="text-brown-encart">👋 Hello, Je m'appelle Glenn</h2>
            <h3 class="text-brown-text">Je suis un ingénieur Data/IA basé à Paris.</h3>
            <p class="text-brown-text">
                Passionné par l'intelligence artificielle et l'analyse de données, je transforme les données 
                en insights actionnables. Mon expertise couvre le machine learning, la data science et le 
                développement d'applications IA innovantes.
            </p>
        </div>
    """, unsafe_allow_html=True)

# ================ TAGS COMPÉTENCES ================
st.markdown("""
<div class="skills-section">
    <h3 class="expertise-title">🎯 Mes Domaines d'Expertise</h3>
    <div>
        <span class="skill-tag">🐍 Python</span>
        <span class="skill-tag">📊 Data Science</span>
        <span class="skill-tag">🤖 Machine Learning</span>
        <span class="skill-tag">🧠 Deep Learning</span>
        <span class="skill-tag">☁️ Cloud Computing</span>
        <span class="skill-tag">📈 Data Visualization</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ================ 3 ENCARTS COMPÉTENCES ================
st.markdown("<h3 class='text-center text-brown-text mb-2'>💼 Mes Compétences Clés</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="competency-card">
        <h4 class="text-brown-encart">🤖 Machine Learning & IA</h4>
        <p class="text-brown-text">
            Expérience projet en NLP, Computer Vision, Machine Learning, Deep Learning, Data visualisation.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="competency-card">
        <h4 class="text-brown-encart">🤖 Expérience professionnelle</h4>
        <p class="text-brown-text">
            Alternance de 2 ans comme datascientist junior chez RTE (Réseau de transport d'électricité).
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="competency-card">
        <h4 class="text-brown-encart">⚙️ Soft skills développés</h4>
        <p class="text-brown-text">
            Gestion de Projet, Travail d'équipe, Design Thinking, Optimisation, Inventivité.
        </p>
    </div>
    """, unsafe_allow_html=True)

render_footer()