import streamlit as st
import cabecera, pie, funcionalidades
import introduccion, objetivos, modelo, recursos


st.set_page_config(
    page_title="Proyecto Ai-ODS 2030",
    page_icon="🌱",
    layout="wide"
)


# -------------------------
# CARGA MODELO Y LOTTIES
# -------------------------
LOTTIE_1 = 'https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json'
LOTTIE_2 = 'https://assets9.lottiefiles.com/packages/lf20_kxsd2ytq.json'

# -------------------------
# CARGA ESTILOS Y HEADER
# -------------------------
funcionalidades.cargar_estilos("estilos.css")
cabecera.generar_cabecera()

# -------------------------
# DICCIONARIO DE PÁGINAS
# -------------------------
PAGES = {
    "Botito": modelo.show,
    "Guía": introduccion.show,
    "Los 17 Objetivos": objetivos.show,
    "Recursos": recursos.show
}

# -------------------------
# ESTADO DE NAVEGACIÓN
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "Botito"

# -------------------------
# SIDEBAR NAV
# -------------------------
with st.sidebar:
    st.markdown(
        """
        <div style='margin-top:80px; text-align:center;'>
            <p style='font-size:24px; font-weight:bold; color:#e8f0fe;'>
                Navegación
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    for page_name in PAGES.keys():
        if st.button(page_name, use_container_width=True):
            st.session_state.page = page_name

    funcionalidades.request_lottie(LOTTIE_1, clave = 'computadora',)



# -------------------------
# RENDER PRINCIPAL
# -------------------------
with st.spinner("Cargando..."):
    PAGES[st.session_state.page]()

# -------------------------
# FOOTER
# -------------------------
pie.generar_pie()