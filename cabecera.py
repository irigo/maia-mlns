import streamlit as st

def generar_cabecera():
    st.markdown("""
    <div style="
        padding: 3px;
        border-radius: 24px;
        background: linear-gradient(135deg, var(--accent), var(--accent2));
        margin-bottom: 2rem;
    ">
        <div style="
            background: #0b1120;
            border-radius: 18px;
            padding: 1.2rem;
            text-align: center;
        ">
            <h1 style="
                font-family: 'Sora', sans-serif;
                font-weight: 800;
                color: white;
                margin: 0;
            ">
                🤖 PROYECTO Ai-ODS-2030 🌱
            </h1>
        </div>
    </div>
    """, unsafe_allow_html=True)