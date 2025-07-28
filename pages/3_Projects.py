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
st.title("Mes Projets")
st.write("Voici quelques-uns de mes projets récents.")

# Exemple de projet
col1,col2,col3,col4,col5= st.columns([1, 3,0.5, 3, 1])

with col2:
    st.subheader("ML_maintenance_predictive")
    st.write("Description du projet 1.")
    st.image("images/ML_maintenance_predictive.jpg")
    if st.button("🔍 Voir le projet", key="cv_welding_btn"):
        st.switch_page("pages/Project_ML_Maintenance_Predictive.py")

with col4:
    st.subheader("NLP_BM25")
    st.write("Description du projet 2.")
    st.image("images/NLP_BM25.jpg")
    if st.button("🔍 Voir le projet", key="project2"):
        st.switch_page("pages/7_Project_NLP_BM25.py")

render_footer()