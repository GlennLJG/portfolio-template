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
    .text-brown-text {
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
    st.markdown("""<h1 class="text-brown-encart centered-title">👨‍💼 À Propos de Moi</h1>""", unsafe_allow_html=True)

# Espacement
st.markdown("<br><br>", unsafe_allow_html=True)

# ================ SECTION BACKGROUND ================
col_title1, col_content1 = st.columns([1, 4])

with col_title1:
    st.markdown("""<div class="title-section"><h2 class="text-brown-encart">Background</h2></div>""", unsafe_allow_html=True)

with col_content1:
    st.markdown("""
    <div class="text-brown-text">
    <div style="height: 5px;"></div>
    Je suis diplômé d'une école d'ingénieur généraliste avec une majeure en intelligence artificielle. Passionné par la logique de la programmation et fasciné par les possibilités qu'offre l'IA, je me suis naturellement orienté vers ce domaine innovant, au cœur des mutations technologiques actuelles.
    
    Enrichie par une alternance chez RTE en tant que data scientist junior, ma spécialisation a porté sur mes deux dernières années d'études. J'y ai développé des compétences solides en machine learning, en traitement de données et en modélisation, à travers des projets concrets et à forte valeur ajoutée. (Voir la section Projets pour en savoir plus.)
    
    Côté tempérament, on me décrit comme quelqu'un de logique, rigoureux et ingénieux, capable de s'adapter à différents contextes. J'aime autant travailler en autonomie qu'en équipe, et je cherche toujours à équilibrer rigueur analytique et créativité dans ce que j'entreprends.
    
    En dehors de l'IA, je cultive plusieurs centres d'intérêt : horlogerie, escalade, trek et production musicale. J'ai aussi fait dix ans de scoutisme, une expérience marquante qui a renforcé mon goût pour l'aventure, l'adaptation et le travail en équipe. Enfin, je suis actif dans une association dédiée au voyage, à la découverte et à la restauration du patrimoine.
    
    </div>
    """, unsafe_allow_html=True)

# Espacement
st.markdown("<br><br>", unsafe_allow_html=True)

# ================ SECTION FORMATION ================
col_title2, col_content2 = st.columns([1, 4])

with col_title2:
    st.markdown("""<div class="title-section"><h2 class="text-brown-encart">Formation</h2></div>""", unsafe_allow_html=True)

with col_content2:
    st.markdown("""
    <div class="text-brown-text">
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
    st.markdown("""<div class="title-section"><h2 class="text-brown-encart">📄 Mon CV</h2></div>""", unsafe_allow_html=True)

with col_content3:
    st.markdown("""<p class="text-brown-text">Vous pouvez télécharger mon CV ou consulter l'aperçu ci-dessous.</p>""", unsafe_allow_html=True)
    
    # Solution 1 : Bouton de téléchargement
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
        <div class="text-brown-text">
        <p>📄 CV PDF non disponible pour le moment.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Espacement
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Affichage simple d'une image du CV
    try:
        st.image("images/CV_apercu.jpg", caption="Aperçu de mon CV", use_container_width=True)
    except:
        st.markdown("""
        <div class="text-brown-text">
        <p>💡 <em>Ajoutez une image "CV_apercu.jpg" dans le dossier images/ pour afficher un aperçu du CV.</em></p>
        </div>
        """, unsafe_allow_html=True)""", unsafe_allow_html=True)
    
    # Solution 1 : Bouton de téléchargement
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
        <div class="text-brown-text">
        <p>📄 CV PDF non disponible pour le moment.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Espacement
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Solution 3 : Affichage des images du CV (si disponibles)
    try:
        # Tentative d'affichage des images du CV
        cv_images = ["images/CV_page1.jpg", "images/CV_page2.jpg"]
        for i, img_path in enumerate(cv_images):
            try:
                st.image(img_path, caption=f"CV - Page {i+1}", use_container_width=True)
            except:
                # Si les images n'existent pas, on essaie encore l'iframe en dernier recours
                if i == 0:  # Seulement pour la première tentative
                    st.markdown("""
                    <div class="text-brown-text">
                    <p><em>💡 Si le PDF ne s'affiche pas, utilisez le bouton de téléchargement ci-dessus.</em></p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Iframe en fallback (peut être bloqué)
                    try:
                        with open("images/Glenn_Grobli_CV.pdf","rb") as f:
                            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>'
                            st.markdown(pdf_display, unsafe_allow_html=True)
                    except:
                        st.markdown("""
                        <div class="text-brown-text">
                        <p>� Pour convertir votre PDF en images JPG :</p>
                        <ol>
                        <li>Ouvrez votre PDF</li>
                        <li>Exportez chaque page en JPG</li>
                        <li>Renommez-les CV_page1.jpg, CV_page2.jpg, etc.</li>
                        <li>Placez-les dans le dossier images/</li>
                        </ol>
                        </div>
                        """, unsafe_allow_html=True)
                break
    except Exception as e:
        st.markdown("""
        <div class="text-brown-text">
        <p>📝 Images du CV non disponibles. Utilisez le bouton de téléchargement pour accéder au CV.</p>
        </div>
        """, unsafe_allow_html=True)

render_footer()
