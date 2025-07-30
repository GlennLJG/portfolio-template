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
st.markdown("""<h1 class="text-brown-encart" style="text-align: center;">📁 Mes Projets</h1>""", unsafe_allow_html=True)
st.markdown("""<p class="text-brown-text" style="text-align: center; font-size: 1.2rem;">Consultez mes projets récents pour avoir une idée de mon expérience.</p>""", unsafe_allow_html=True)

# Espacement
st.markdown("<br>", unsafe_allow_html=True)

# ================ PREMIÈRE LIGNE - 2 PROJETS ================
col1, col2, col3, col4, col5 = st.columns([1, 3, 0.5, 3, 1])

with col2:
    st.markdown("""<h3 class="text-brown-encart">ML Maintenance Prédictive</h3>""", unsafe_allow_html=True)
    st.image("images/ML_maintenance_predictive.jpg")
    st.markdown("""<p class="text-brown-text">Développement d'un modèle de machine learning pour prédire les pannes d'équipements industriels.</p>""", unsafe_allow_html=True)
    if st.button("🔍 Voir le projet", key="project_ml_maintenance"):
        st.switch_page("pages/Project_ML_Maintenance_Predictive.py")

with col4:
    st.markdown("""<h3 class="text-brown-encart">NLP BM25</h3>""", unsafe_allow_html=True)
    st.image("images/NLP_BM25.jpg")
    st.markdown("""<p class="text-brown-text">Système de recherche et d'analyse de texte utilisant l'algorithme BM25.</p>""", unsafe_allow_html=True)
    if st.button("🔍 Voir le projet", key="project_nlp_bm25"):
        st.switch_page("pages/7_Project_NLP_BM25.py")

# Espacement entre les lignes
st.markdown("<br>", unsafe_allow_html=True)

# ================ DEUXIÈME LIGNE - 2 PROJETS ================
col1, col2, col3, col4, col5 = st.columns([1, 3, 0.5, 3, 1])

with col2:
    st.markdown("""<h3 class="text-brown-encart">Computer Vision Welding</h3>""", unsafe_allow_html=True)
    try:
        st.image("images/CV_welding.jpg")
    except:
        st.markdown("""<div style="height: 200px; background: var(--brown-encart); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem;">🔧</div>""", unsafe_allow_html=True)
    st.markdown("""<p class="text-brown-text">Détection automatique de défauts de soudure par vision par ordinateur.</p>""", unsafe_allow_html=True)
    if st.button("🔍 Voir le projet", key="project_cv_welding"):
        st.switch_page("pages/4_Project_CV_Welding.py")

with col4:
    st.markdown("""<h3 class="text-brown-encart">Analyse de Données RTE</h3>""", unsafe_allow_html=True)
    try:
        st.image("images/outil_simu.jpg")
    except:
        st.markdown("""<div style="height: 200px; background: var(--brown-encart); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem;">⚡</div>""", unsafe_allow_html=True)
    st.markdown("""<p class="text-brown-text">Analyse et visualisation de données du réseau électrique français.</p>""", unsafe_allow_html=True)
    if st.button("🔍 Voir le projet", key="project_rte_analysis"):
        # st.switch_page("pages/Project_RTE_Analysis.py")
        st.info("🚧 Projet en cours de documentation")

# Espacement entre les lignes
st.markdown("<br>", unsafe_allow_html=True)

# ================ TROISIÈME LIGNE - 1 PROJET CENTRÉ ================
col1, col2, col3 = st.columns([2.75, 3, 2.75])

with col2:
    st.markdown("""<h3 class="text-brown-encart" >Portfolio Web Streamlit</h3>""", unsafe_allow_html=True)
    try:
        st.image("images/comparative_study.jpg")
    except:
        st.markdown("""<div style="height: 200px; background: var(--brown-encart); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-size: 3rem; margin: 0 auto;">🌐</div>""", unsafe_allow_html=True)
    st.markdown("""<p class="text-brown-text" style="text-align: center;">Développement de ce portfolio interactif avec Streamlit et déploiement cloud.</p>""", unsafe_allow_html=True)

    if st.button("🔍 Voir le code", key="project_portfolio"):
            st.info("📌 Vous consultez actuellement ce projet !")

render_footer()