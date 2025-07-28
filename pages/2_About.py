import streamlit as st
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

# Rendu du header avec navigation
render_header()

render_footer()
