"""
python con funcionalidades de la página
(apertura, carga de elementos etc)

"""
import streamlit as st
from streamlit_lottie import st_lottie
import json
import joblib
import numpy as np
import requests
import time
import json


def cargar_estilos(filepath: str):
    """Carga un archivo txt desde disco con los estilos."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            css = f.read()
            st.markdown(css, unsafe_allow_html=True)
        return True
    except Exception as e:
        print(f"Error al cargar Lottie desde archivo: {e}")

        return False

@st.cache_data(show_spinner=False)
def request_lottie(url: str, clave: str, tamanio : int = 140):
    """Descarga JSON de Lottiefiles."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            lottie_json = response.json()  # convertir a dict
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                st_lottie(lottie_json, height=tamanio, key=clave, speed=0.8)
        else:
            st.markdown('<div class="bot-avatar">🤖</div>', unsafe_allow_html=True)

    except Exception as e:
        print(f"Error al cargar Lottie desde archivo: {e}")
        st.markdown('<div class="bot-avatar">🤖</div>', unsafe_allow_html=True)

    return None





def abrir_lottie_local(filepath: str, clave: str, tamanio : int = 140):
    """Carga un archivo Lottie JSON desde disco."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lottie_data =  json.load(f)
            if lottie_data:
                col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                st_lottie(lottie_data, height=tamanio, key=clave, speed=0.8)
    except Exception as e:
        print(f"Error al cargar Lottie desde archivo: {e}")
        st.markdown('<div class="bot-avatar">🤖</div>', unsafe_allow_html=True)
        return None
