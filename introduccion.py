import streamlit as st
import os

def show():
    # -------------------------------
    # HERO SECTION
    # -------------------------------
    st.markdown("<h1 style='text-align: center;font-family: 'Sora', sans-serif;font-weight: 800;'> Objetivos de Desarrollo Sostenible (ODS) </h1>", unsafe_allow_html=True)

    st.markdown("""
    <p style='text-align: justify; font-size:24px;'>
    <br><br>
    Los 17 Objetivos de Desarrollo Sostenible constituyen una agenda global diseñada para 
    construir un futuro más justo, inclusivo y sostenible. Estos objetivos están profundamente 
    conectados entre sí y abordan desafíos fundamentales como la pobreza, la desigualdad, 
    el cambio climático, la degradación ambiental, la prosperidad económica, la paz y la justicia.
    <br><br>
    Para garantizar que nadie quede atrás, es fundamental avanzar de manera integral 
    en cada uno de ellos antes del año 2030.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        height: 3px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        border-radius: 50px;
        margin-top: 3rem;
        margin-bottom: 1rem;
    "></div>
    """, unsafe_allow_html=True)

    # -------------------------------
    # GRID DE IMÁGENES (6x3)
    # -------------------------------
    st.subheader("Los 17 Objetivos")

    carpeta = "objetivos"
    total_objetivos = 17
    columnas_por_fila = 6

    for i in range(0, total_objetivos, columnas_por_fila):
        cols = st.columns(columnas_por_fila)
        for j in range(columnas_por_fila):
            indice = i + j + 1
            if indice <= total_objetivos:
                ruta_imagen = os.path.join(carpeta, f"objetivos_{indice:02}.png")
                with cols[j]:
                    st.image(ruta_imagen, use_container_width=True)

    st.markdown("""
    <div style="
        height: 3px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        border-radius: 50px;
        margin-top: 3rem;
        margin-bottom: 1rem;
    "></div>
    """, unsafe_allow_html=True)

    # -------------------------------
    # EXPLICACIÓN DE LA APP
    # -------------------------------
    st.markdown("<h1 h1 style='text-align: center;font-family: 'Sora', sans-serif;font-weight: 800;'> ¿Qué propone esta página?</h1>", unsafe_allow_html=True)

    st.markdown("""
    <p style='text-align: justify; font-size:24px;'>
    <br><br>
    Esta plataforma no solo presenta los Objetivos de Desarrollo Sostenible, 
    sino que te invita a interactuar con un asistente inteligente.
    <br><br>
    Podrás ingresar un texto, una idea, un proyecto o una problemática, 
    y el sistema analizará su contenido para sugerirte cuál de los 
    17 Objetivos está más relacionado con tu consulta.
    <br><br>
    De esta manera, transformamos la información en una herramienta dinámica, 
    facilitando la comprensión y conexión entre iniciativas concretas 
    y los desafíos globales que buscan resolverse.
    </p>
    """, unsafe_allow_html=True)