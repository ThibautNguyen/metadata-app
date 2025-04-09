import streamlit as st
import os
import sys

# Configuration de la page
st.set_page_config(
    page_title="Gestion des Métadonnées",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ajout du chemin pour les modules personnalisés
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Titre et introduction
st.title("Système de Gestion des Métadonnées")
st.markdown("""
Cette application permet de gérer les métadonnées de vos jeux de données statistiques.
Elle offre les fonctionnalités suivantes :
""")

# Création des cartes pour les fonctionnalités
col1, col2 = st.columns(2)

with col1:
    st.info("### 📝 Saisie des métadonnées")
    st.markdown("""
    Créez et modifiez facilement des fiches de métadonnées pour vos données.
    
    Fonctionnalités:
    - Formulaire structuré
    - Validation automatique
    - Enregistrement en JSON et TXT
    """)
    st.page_link("pages/02_Saisie.py", label="Accéder à la saisie", icon="✏️")

with col2:
    st.info("### 🔍 Recherche")
    st.markdown("""
    Recherchez rapidement parmi les métadonnées existantes.
    
    Fonctionnalités:
    - Recherche par mot-clé
    - Filtrage par catégorie
    - Accès direct aux fiches
    """)
    st.page_link("pages/03_Recherche.py", label="Accéder à la recherche", icon="🔎")

# Pied de page
st.markdown("---")
st.markdown("© 2025 - Système de Gestion des Métadonnées v1.0") 