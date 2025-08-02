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

load_css()

# CSS personnalisé pour un design moderne
st.markdown("""
<style>
    /* Styles spécifiques à la page d'accueil */
    .profile-section h2 {
        font-size: 2.0rem;
        margin-bottom: 0.3rem;
    }
    
    .profile-section h3 {
        font-size: 1.6rem;
        margin-bottom: 0.5rem;
    }
    
    .profile-section p {
        font-size: 1.3rem;
        line-height: 1.6;
        text-align: left;
    }
    
    .competency-card h4 {
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .competency-card p {
        font-size: 1.2rem;
        line-height: 1.6;
    }
    
    .skills-section {
        text-align: center;
        margin-top: 0px;
        margin-bottom: 3rem;
    }
</style>
""", unsafe_allow_html=True)

render_header()

# ================ SECTION PRÉSENTATION ================
col1, col2,col_space, col3, col4 = st.columns([0.3, 1.2,0.2 ,2, 0.3])


with col2:
    # Section image
    try:
        profile_image = Image.open("images/portrait.jpg")
        st.image(profile_image, width=600, use_container_width=False)
    except:
        st.markdown("""
        <div style="width: 300px; height: 300px; border-radius: 20px; background: var(--color_encart); 
                    display: flex; align-items: center; justify-content: center; color: var(--color_text_on_encart); font-size: 6rem; margin: 0 auto;">
            👨‍💻
        </div>
        """, unsafe_allow_html=True)

with col3:
    # Section texte
    st.markdown("""
        <div class="profile-section">
            <h2 class="title_text"> Hello, Je m'appelle Glenn </h2>
            <h3 class="text_on_background">Je suis un ingénieur Data/IA basé à Paris.</h3>
            <p class="text_on_background">
            Fort de deux ans d’alternance en tant que Data Scientist Junior, je m’intéresse à l’ensemble des problématiques IA.<br>
            Je me suis particulièrement spécialisé en machine learning, que j’ai approfondi au travers de projets concrets.
            </p>
        </div>
    """, unsafe_allow_html=True)

# ================ TAGS COMPÉTENCES ================
    st.markdown("""
    <div class="skills-section">
        <div>
            <span class="skill-tag">🐍 Python</span>
            <span class="skill-tag">🧠 Machine Learning</span>
            <span class="skill-tag">📊 Data Science & Analytics</span>
            <span class="skill-tag">💻 Ingénierie Logicielle</span>
            <span class="skill-tag">📝 NLP</span>
            <span class="skill-tag">🔍 Computer Vision</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================ 3 ENCARTS COMPÉTENCES ================
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="competency-card">
        <h4 class="title_text">🧰 Stack Technique</h4>
        <p class="text_on_background">
            <strong>Python :</strong>
            Pandas, Scikit-learn, NumPy, TensorFlow, PyTorch<br>
            <strong>Languages :</strong>
            SQL, C#, C++, Bash<br>
            <strong>Outils :</strong>
            Git, Docker, Power BI
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="competency-card">
        <h4 class="title_text">💼 Expérience professionnelle</h4>
        <p class="text_on_background">
            <strong>RTE</strong> : Data Scientist Junior (<em>Alternance de 2 ans</em>)<br>
            • Développement d'un ETL<br>
            • Mise en œuvre de scénarios de simulation<br>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="competency-card">
        <h4 class="title_text">🤝 Soft Skills</h4>
        <p class="text_on_background">
            <strong>Management :</strong>
            Gestion de projet, Agile Scrum<br>
            <strong>Créativité :</strong>
            Design Thinking, Inventivité<br>
            <strong>Collaboration :</strong>
            Travail d'équipe
        </p>
    </div>
    """, unsafe_allow_html=True)

render_footer()