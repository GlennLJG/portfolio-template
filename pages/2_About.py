import streamlit as st
import base64
from constant import *
from PIL import Image
from components import load_css, render_header, render_footer

# Configuration de la page
st.set_page_config(
    page_title='À Propos - Glenn',
    layout="wide",
    page_icon='👨‍💼',
    initial_sidebar_state="collapsed"
)

# Charger les styles CSS
load_css()

# CSS personnalisé pour ajuster l'alignement des titres
st.markdown("""
<style>
    .title-section {
        padding-top: 0rem !important;
        margin-top: -1rem !important;
    }
    .centered-title {
        text-align: center !important;
    }
    .text_on_background {
        font-size: 1.3rem !important;
        line-height: 1.7 !important;
    }
    
</style>
""", unsafe_allow_html=True)

# Rendu du header avec navigation
render_header()

# ================ SECTION À PROPOS ================
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown("""<h1 class="title_text centered-title">À Propos de Moi</h1>""", unsafe_allow_html=True)

# Espacement
st.markdown("<br><br>", unsafe_allow_html=True)

# ================ SECTION BACKGROUND ================
col_title1, col_content1 = st.columns([1, 4])

with col_title1:
    st.markdown("""<div class="title-section"><h2 class="title_text">Background</h2></div>""", unsafe_allow_html=True)

with col_content1:
    st.markdown("""
    <div class="text_on_background">
    <div style="height: 5px;"></div>
    Diplômé d’une école d’ingénieur généraliste avec une majeure en Data et Intelligence Artificielle. 
    <br>Ce qui me motive, c’est de pouvoir relier la logique de la programmation aux nombreuses perspectives qu’ouvre l’IA dans un monde en pleine mutation technologique.
    <br><br>      
    Durant mes deux dernières années d'études, j'ai forgé ma spécialisation en machine learning en développant des projets concrets, directement applicables à des problématiques d’entreprise (voir la section Projets pour en savoir plus).
    <br>En parallèle, mon alternance chez RTE fut une immersion décisive dans le monde de la data science. J'y ai développé une expertise pratique en traitement et manipulation de données, au service de missions d'intérêt général.
    <br><br>            
    En dehors de mon parcours académique et professionnel, je cultive plusieurs passions qui façonnent ma manière de travailler et d’aborder les défis :

    - **Escalade** : cette discipline m'apprend la maîtrise de soi face à la difficulté, l'adaptabilité et la logique pour identifier la meilleure approche.

    - **Scoutisme** : dix années d'engagement m'ont permis de développer des compétences en leadership, ma débrouillardise et mon autonomie, tout en cultivant un fort esprit d'équipe.

    - **Horlogerie** : une passion qui reflète mon appétence pour la rigueur, la précision et le souci du détail.

    - **Production musicale (MAO)** : j'y cultive ma créativité et ma capacité à apprendre de manière autonome des outils complexes.

    - **Engagement associatif** : membre actif d'une association de voyage et de restauration du patrimoine, je m'investis dans des projets collectifs porteurs de sens qui nourrissent ma curiosité.
    </div>
    """, unsafe_allow_html=True)

# Espacement
st.markdown("<br><br>", unsafe_allow_html=True)

# ================ SECTION FORMATION ================
col_title2, col_content2 = st.columns([1, 4])

with col_title2:
    st.markdown("""<div class="title-section"><h2 class="title_text">Formation</h2></div>""", unsafe_allow_html=True)

with col_content2:
    st.markdown("""
    <div class="text_on_background">
    <div style="height: 5px;"></div>
                
    **2020-2025** : Cursus Ingénieur, ESILV, La Défense
    
    **2022** : Semestre d'échange en Corée du Sud, Chung-Ang University, Seoul
    
    </div>
    """, unsafe_allow_html=True)

# Espacement
st.markdown("<br><br>", unsafe_allow_html=True)

# ================ SECTION CV ================
col_title3, col_content3,_ = st.columns([1, 3, 1])

with col_title3:
    st.markdown("""<div class="title-section"><h2 class="title_text">📄 Mon CV</h2></div>""", unsafe_allow_html=True)

with col_content3:
    st.markdown("""<p class="text_on_background">Vous pouvez télécharger mon CV ou consulter l'aperçu ci-dessous.</p>""", unsafe_allow_html=True)
    
    # Bouton de téléchargement
    try:
        with open("images/Glenn_Grobli_CV.pdf","rb") as f:
            pdf_bytes = f.read()
        
        col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
        with col_btn2:
            st.download_button(
                label="📄 Télécharger mon CV (PDF)",
                data=pdf_bytes,
                file_name="Glenn_Grobli_CV.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except FileNotFoundError:
        st.markdown("""
        <div class="text_on_background">
        <p>📄 CV PDF non disponible pour le moment.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Espacement
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Affichage simple d'une image du CV
    try:
        st.image("images/Glenn_Grobli_CV.jpg", caption="Aperçu de mon CV", use_container_width=True)
    except:
        st.markdown("""
        <div class="text_on_background">
        <p>💡 <em>Ajoutez une image "CV_apercu.jpg" dans le dossier images/ pour afficher un aperçu du CV.</em></p>
        </div>
        """, unsafe_allow_html=True)

render_footer()
