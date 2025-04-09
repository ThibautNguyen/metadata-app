import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title='Metadata Manager',
    page_icon='??',
    layout='wide'
)

# Titre et introduction
st.title('Metadata Management System')
st.write('This application allows you to manage metadata for your datasets.')

# Creation des cartes pour les fonctionnalites
col1, col2 = st.columns(2)

with col1:
    st.info('### ?? Metadata Entry')
    st.write('''
    Create and edit metadata records easily.
    
    Features:
    - Structured form
    - Automatic validation
    - JSON and TXT storage
    ''')
    st.page_link('pages/02_Saisie.py', label='Go to Entry Form', icon='??')

with col2:
    st.info('### ?? Search')
    st.write('''
    Search quickly through existing metadata.
    
    Features:
    - Keyword search
    - Category filtering
    - Direct access to records
    ''')
    st.page_link('pages/03_Recherche.py', label='Go to Search', icon='??')

# Footer
st.markdown('---')
st.write('? 2025 - Metadata Management System v1.0')

