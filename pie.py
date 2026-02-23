import streamlit as st
from streamlit_lottie import st_lottie
import funcionalidades

# -------------------------
# CARGA LOTTIES
# -------------------------
MOLINOS = 'molinos.json'
def generar_pie():
    st.markdown("""
    <div style="
        height: 3px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        border-radius: 50px;
        margin-top: 3rem;
        margin-bottom: 1rem;
    "></div>
    """, unsafe_allow_html=True)


    col1, col2 = st.columns([2,1])  # proporción ancho texto vs animación

    with col1:
        st.markdown("""<div style="
    display: flex;
    justify-content: center;   
    align-items: center;       
    height: 80px;              
    color: gray;
    font-size: 18px;">
     <h4 style="
                font-family: 'Sora', sans-serif;
                font-weight: 800;
                color: white;
                margin: 20;
                text-align:center;"> © 2026 Proyecto Ai-ODS 2030 - Autores: IER - NSC </h4></div>""", unsafe_allow_html=True)

    with col2:
        lottie_json = funcionalidades.abrir_lottie_local(MOLINOS, clave = 'molinos', tamanio = 100)
