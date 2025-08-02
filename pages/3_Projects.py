import streamlit as st
from constant import *
from PIL import Image
from components import load_css, render_header, render_footer

# Configuration de la page
st.set_page_config(
    page_title='Mes Projets - Glenn',
    layout="wide",
    page_icon='📁',
    initial_sidebar_state="collapsed"
)

# Charger les styles CSS
load_css()

# Rendu du header avec navigation
render_header()

# Contenu principal de la page
st.markdown("""<h1 class="title_text" style="text-align: center;">📁 Mes Projets</h1>""", unsafe_allow_html=True)
st.markdown("""<p class="text_on_background" style="text-align: center; font-size: 1.2rem;">Consultez mes projets récents pour avoir une idée de mon expérience.</p>""", unsafe_allow_html=True)

# Espacement
st.markdown("<br>", unsafe_allow_html=True)

# ================ PREMIÈRE LIGNE - 2 PROJETS ================
col1, col2, col3, col4, col5 = st.columns([1, 3, 0.5, 3, 1])

with col2:
    st.markdown("""<h3 class="title_text">ML pour la maintenance prédictive</h3>""", unsafe_allow_html=True)
    st.image("images/ML_maintenance_predictive.jpg")
    st.markdown("""<p class="text_on_background">Développement d'un modèle d'ensemble learning capable de gérer le déséquilibre des classes, pour prédire les pannes de disques durs à partir de relevés temporels.</p>""", unsafe_allow_html=True)
    if st.button("🔍 Voir le projet", key="project_ml_maintenance"):
        st.switch_page("pages/Projet_ML_Maintenance_Predictive.py")

with col4:
    st.markdown("""<h3 class="title_text">NLP pour l'analyse de commentaires</h3>""", unsafe_allow_html=True)
    st.image("images/NLP_BM25.jpg")
    st.markdown("""<p class="text_on_background">Développement d'un système de recommandation d'hôtels basé sur l'analyse sémantique des avis clients, surpassant BM25.</p>""", unsafe_allow_html=True)
    if st.button("🔍 Voir le projet", key="project_nlp_bm25"):
        st.switch_page("pages/Projet_NLP_TripAdvisor.py")

# Espacement entre les lignes
st.markdown("<br>", unsafe_allow_html=True)

# ================ DEUXIÈME LIGNE - 2 PROJETS ================
col1, col2, col3, col4, col5 = st.columns([1, 3, 0.5, 3, 1])

with col2:
    st.markdown("""<h3 class="title_text">Computer Vision pour évaluer la qualité des soudures</h3>""", unsafe_allow_html=True)
    try:
        st.image("images/CV_welding.jpg")
    except:
        st.markdown("""<div style="height: 200px; background: var(--color_encart); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem;">🔧</div>""", unsafe_allow_html=True)
    st.markdown("""<p class="text_on_background">Comparaison approfondie de YOLO vs DETR pour la détection automatique de défauts de soudure.</p>""", unsafe_allow_html=True)
    if st.button("🔍 Voir le projet", key="project_cv_welding"):
        st.switch_page("pages/Projet_CV_welding.py")

with col4:
    st.markdown("""<h3 class="title_text">Développement d'un ETL selon les besoins métiers</h3>""", unsafe_allow_html=True)
    try:
        st.image("images/outil_simu.jpg")
    except:
        st.markdown("""<div style="height: 200px; background: var(--color_encart); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem;">⚡</div>""", unsafe_allow_html=True)
    st.markdown("""<p class="text_on_background">Développement d'un ETL automatisé avec interface Streamlit pour simuler des flux de données de production.</p>""", unsafe_allow_html=True)
    if st.button("🔍 Voir le projet", key="project_rte_analysis"):
        st.switch_page("pages/Projet_Outil_simulation.py")

# Espacement entre les lignes
st.markdown("<br>", unsafe_allow_html=True)

# ================ TROISIÈME LIGNE - 1 PROJET CENTRÉ ================
col1, col2, col3 = st.columns([2.75, 3, 2.75])

with col2:
    st.markdown("""<h3 class="title_text">Etude comparative des modèles de ML</h3>""", unsafe_allow_html=True)
    try:
        st.image("images/comparative_study.jpg")
    except:
        st.markdown("""<div style="height: 200px; background: var(--color_encart); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem; margin: 0 auto;">🌐</div>""", unsafe_allow_html=True)
    st.markdown("""<p class="text_on_background" ;">Analyse comparative entre méthodes d'ensemble et programmation génétique sur la détection du boson de Higgs.</p>""", unsafe_allow_html=True)

    if st.button("🔍 Voir le code", key="project_portfolio"):
        st.switch_page("pages/Projet_ML_comparative_study.py")

render_footer()