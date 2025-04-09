import streamlit as st
import requests
import json
import pandas as pd

st.title('Metadata Search')

# Affichage d'un exemple simple
st.write('Example of metadata from GitHub:')

# URL de l'API GitHub pour acc?der aux m?tadonn?es
url = 'https://raw.githubusercontent.com/ThibautNguyen/DOCS/main/SGBD/Metadata/README.md'

try:
    # R?cup?ration des donn?es
    response = requests.get(url)
    
    if response.status_code == 200:
        # Affichage des m?tadonn?es
        st.code(response.text, language='markdown')
        st.success('Successfully connected to GitHub repository!')
    else:
        st.error(f'Failed to retrieve data: {response.status_code}')
except Exception as e:
    st.error(f'Error: {str(e)}')

