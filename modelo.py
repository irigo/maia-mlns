import streamlit as st
import joblib
import os
import funcionalidades


# =============================
# CONFIGURACIONES Y FUNCIONES
# =============================

@st.cache_resource
def cargar_modelo():
    return joblib.load("modelo_clasificacion_definitivo.pkl")


def separador():
    st.markdown("""
        <div style="
        height:3px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        border-radius:50px;
        margin-top:3rem;
        margin-bottom:1rem;">
        </div>
    """, unsafe_allow_html=True)


# =============================
# FUNCIÓN PRINCIPAL
# =============================

def show():

    model = cargar_modelo()
    carpeta = "objetivos"
    # -------------------------
    # RESET CONTROLADO
    # -------------------------

    if "resetear" in st.session_state and st.session_state.resetear:
        st.session_state.texto_usuario = ""
        st.session_state.resultado = None
        st.session_state.resetear = False

    # Estado inicial
    if "texto_usuario" not in st.session_state:
        st.session_state.texto_usuario = ""

    if "resultado" not in st.session_state:
        st.session_state.resultado = None

    # -------------------------
    # BOTITO INICIAL
    # -------------------------

    col1, col2 = st.columns([1, 3])

    with col1:
        funcionalidades.abrir_lottie_local(
            "botito.json",
            clave="botito_intro",
            tamanio=180
        )

    with col2:
        st.markdown(
            """
            <div style='
                background: rgba(200,200,200,0.15);
                padding:20px;
                border-radius:18px;
                font-size:22px;
                backdrop-filter: blur(6px);
                border: 1px solid rgba(150,150,150,0.3);
                color: inherit;'>
                Hola 👋 ¡Soy Botito! Escribe tu texto a continuación 
                y te diré a qué objetivo ODS se aproxima más.
            </div>
            """,
            unsafe_allow_html=True
        )

    separador()

    # -------------------------
    # INPUT TEXTO
    # -------------------------

    st.markdown(
        "<p style='font-size:26px; font-weight:600;'>Ingresa el texto que deseas analizar:</p>",
        unsafe_allow_html=True
    )

    text_input = st.text_area(
        "",
        height=200,
        placeholder="Aquí agregar un proyecto, idea o problemática...",
        key="texto_usuario"
    )

    col_btn1, col_btn2 = st.columns([3, 1])

    with col_btn1:
        analizar = st.button("Analizar", use_container_width=True)

    with col_btn2:
        if st.button("Reiniciar", use_container_width=True):
            st.session_state.resetear = True
            st.rerun()

    # -------------------------
    # EJECUCIÓN
    # -------------------------

    if analizar:

        if not text_input.strip():
            st.warning("⚠️ Por favor ingresa un texto antes de analizar.")
            return

        with st.spinner("Analizando..."):
            prediction = model.predict([text_input])[0]
            probabilities = model.predict_proba([text_input])[0]
            classes = model.classes_

        ranking = sorted(zip(classes, probabilities), key=lambda x: -x[1])
        st.session_state.resultado = ranking

    # -------------------------
    # MOSTRAR RESULTADOS
    # -------------------------

    if st.session_state.resultado:
        feeling = ""

        ranking = st.session_state.resultado
        objetivo_principal, prob_principal = ranking[0]

        # Determinar mensaje según confianza
        if prob_principal > 0.75:
            emoji = "🤩"
            feeling = "happy"
            mensaje_conf = f"¡Estoy {prob_principal*100:.1f}% seguro!"
        elif prob_principal > 0.50:
            emoji = "🤔"
            feeling = "neutral"
            mensaje_conf = f"Estoy levemente seguro... ({prob_principal*100:.1f}%)"
        elif prob_principal > 0.25:
            emoji = "😅"
            feeling = "unsure"
            mensaje_conf = f"No estoy muy seguro ({prob_principal*100:.1f}%)"
        else:
            emoji = "😭"
            feeling = "sad"
            mensaje_conf = "Lo siento... No tengo suficiente seguridad con este texto."

        separador()

        # -------------------------
        # BOTITO RESPUESTA
        # -------------------------
        feeling = feeling+"2"
        col1, col2 = st.columns([1, 3])

        with col1:
            st.markdown(
            f'<img src="app/static/{feeling}.png" style="width:100%;">',
            unsafe_allow_html=True
        )

        with col2:
            st.markdown(
                f"""
                <div style='
                    background: rgba(200,200,200,0.15);
                    padding:20px;
                    border-radius:18px;
                    font-size:22px;
                    backdrop-filter: blur(6px);
                    border: 1px solid rgba(150,150,150,0.3);
                    color: inherit;'>
                    El objetivo que más se relaciona es 
                    <b>ODS {int(objetivo_principal)}</b>. <br><br>
                    {mensaje_conf}
                </div>
                """,
                unsafe_allow_html=True
            )

        separador()

        # -------------------------
        # TOP 3
        # -------------------------

        st.subheader("Estos son los objetivos más relacionados")

        cols = st.columns(3)

        for i, (obj, prob) in enumerate(ranking[:3]):

            numero = int(obj)
            ruta_imagen = os.path.join(carpeta, f"objetivos_{numero:02}.png")

            with cols[i]:
                st.image(ruta_imagen, width=180)
                st.markdown(
                    f"<div style='text-align:center; font-weight:bold;'>ODS {numero}</div>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    f"<div style='text-align:center;'>{prob*100:.2f}%</div>",
                    unsafe_allow_html=True
                )

        separador()

        # -------------------------
        # DISTRIBUCIÓN COMPLETA
        # -------------------------

        st.subheader("Estadísticas completas")

        for cls, prob in ranking:
            st.progress(float(prob), text=f"ODS {int(cls)}: {prob * 100:.2f}%")