import streamlit as st
import requests
from streamlit_lottie import st_lottie

# -------------------------------
# FUNCION PARA CARGAR LOTTIE
# -------------------------------
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def show():

    st.markdown(
        "<h1 style='text-align: center;font-family: \"Sora\", sans-serif;font-weight: 800;'>"
        "Recursos y Créditos"
        "</h1>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------------
    # INTRO
    # -------------------------------
    st.markdown(
        """
        <p style='text-align: justify; font-size:24px;'>
        Esta sección reúne las fuentes, recursos gráficos, animaciones y 
        documentación técnica utilizadas en el desarrollo de la plataforma. 
        Todos los materiales referenciados contribuyen a enriquecer la experiencia 
        visual, conceptual y tecnológica del proyecto.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
        <div style="
        height:3px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        border-radius:50px;
        margin-top:3rem;
        margin-bottom:1rem;">
        </div>
    """, unsafe_allow_html=True)

    # -------------------------------
    # LOTTIE ANIMACIONES
    # -------------------------------
    st.markdown(
        "<h1 style='text-align: center;font-family: \"Sora\", sans-serif;font-weight: 800;'>Animaciones Lottie</h1>",
        unsafe_allow_html=True
    )

    robot = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")
    molino = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_kxsd2ytq.json")

    col1, col2 = st.columns(2)

    with col1:
        if robot:
            st_lottie(robot, height=200)
        st.markdown("<p style='text-align:center;'>Computador</p>", unsafe_allow_html=True)

    with col2:
        if molino:
            st_lottie(molino, height=200)
        st.markdown("<p style='text-align:center;'>Cargando</p>", unsafe_allow_html=True)

    st.markdown("""
        <div style="
        height:3px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        border-radius:50px;
        margin-top:3rem;
        margin-bottom:1rem;">
        </div>
    """, unsafe_allow_html=True)

    # -------------------------------
    # RECURSOS GRÁFICOS
    # -------------------------------
    st.markdown(
        "<h1 style='text-align: center;font-family: \"Sora\", sans-serif;font-weight: 800;'>Recursos Gráficos</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align: justify; font-size:24px;'>
        Material visual complementario inspirado en recursos de diseño disponibles en:
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("- [Freepik – Infografía ODS](https://www.freepik.es/vector-gratis/infografia-infografia-sdg-dibujada-mano_29830257.htm)")

    st.markdown("""
        <div style="
        height:3px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        border-radius:50px;
        margin-top:3rem;
        margin-bottom:1rem;">
        </div>
    """, unsafe_allow_html=True)

    # -------------------------------
    # FUENTES OFICIALES
    # -------------------------------
    st.markdown(
        "<h1 style='text-align: center;font-family: \"Sora\", sans-serif;font-weight: 800;'>Fuentes Oficiales</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align: justify; font-size:24px;'>
        Información conceptual y contenido oficial basado en documentación publicada por Naciones Unidas:
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("- [Adopción de la Agenda 2030](https://www.un.org/sustainabledevelopment/es/2015/09/la-asamblea-general-adopta-la-agenda-2030-para-el-desarrollo-sostenible/)")
    st.markdown("- [Objetivos de Desarrollo Sostenible – ONU](https://www.un.org/sustainabledevelopment/es/sustainable-development-goals/)")

    st.markdown("""
        <div style="
        height:3px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        border-radius:50px;
        margin-top:3rem;
        margin-bottom:1rem;">
        </div>
    """, unsafe_allow_html=True)

    # -------------------------------
    # DOCUMENTACIÓN TÉCNICA
    # -------------------------------
    st.markdown(
        "<h1 style='text-align: center;font-family: \"Sora\", sans-serif;font-weight: 800;'>Documentación Técnica</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align: justify; font-size:24px;'>
        Plataforma desarrollada utilizando Streamlit. 
        Documentación oficial disponible en:
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("- [Documentación oficial de Streamlit](https://streamlit.io/)")