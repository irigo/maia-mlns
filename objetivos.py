import streamlit as st
import os

def show():

    carpeta = "objetivos"

    # -------------------------------
    # TÍTULO PRINCIPAL
    # -------------------------------
    st.markdown(
        "<h1 style='text-align: center;font-family: \"Sora\", sans-serif;font-weight: 800;'>"
        "Objetivos de Desarrollo Sostenible (ODS)"
        "</h1>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <p style='text-align: justify; font-size:24px;'>
        Los 17 Objetivos de Desarrollo Sostenible (ODS) conforman una hoja de ruta global 
        adoptada para enfrentar los principales desafíos sociales, económicos y ambientales 
        de nuestro tiempo. Cada objetivo aborda una dimensión específica del desarrollo, 
        pero todos están interconectados y requieren un enfoque integral para generar 
        transformaciones reales y sostenibles.
        <br><br>
        A continuación, podrás explorar cada uno de los objetivos junto con una breve 
        descripción de su propósito y alcance.
        </p>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------
    # LISTADO DE OBJETIVOS
    # -------------------------------
    ods_info = [
        ("ODS 1 – Fin de la pobreza",
         "Busca erradicar la pobreza en todas sus formas y dimensiones, garantizando "
         "que todas las personas tengan acceso a recursos básicos, protección social "
         "y oportunidades económicas."),

        ("ODS 2 – Hambre cero",
         "Promueve el acceso universal a una alimentación segura y nutritiva, "
         "impulsando sistemas agrícolas sostenibles y resilientes."),

        ("ODS 3 – Salud y bienestar",
         "Garantiza una vida sana y promueve el bienestar en todas las edades, "
         "fortaleciendo los sistemas de salud y el acceso equitativo a servicios médicos."),

        ("ODS 4 – Educación de calidad",
         "Asegura una educación inclusiva, equitativa y de calidad, "
         "fomentando oportunidades de aprendizaje durante toda la vida."),

        ("ODS 5 – Igualdad de género",
         "Busca eliminar todas las formas de discriminación y violencia contra mujeres "
         "y niñas, promoviendo su participación plena en la sociedad."),

        ("ODS 6 – Agua limpia y saneamiento",
         "Garantiza la disponibilidad de agua potable y sistemas de saneamiento "
         "seguros y sostenibles para toda la población."),

        ("ODS 7 – Energía asequible y no contaminante",
         "Promueve el acceso a energía moderna, sostenible y asequible, "
         "impulsando fuentes renovables y eficiencia energética."),

        ("ODS 8 – Trabajo decente y crecimiento económico",
         "Fomenta el crecimiento económico sostenido, el empleo productivo "
         "y condiciones laborales dignas para todos."),

        ("ODS 9 – Industria, innovación e infraestructura",
         "Impulsa infraestructuras resilientes, industrialización sostenible "
         "e innovación tecnológica."),

        ("ODS 10 – Reducción de las desigualdades",
         "Busca disminuir las desigualdades dentro y entre los países, "
         "promoviendo inclusión social, económica y política."),

        ("ODS 11 – Ciudades y comunidades sostenibles",
         "Promueve asentamientos humanos inclusivos, seguros, resilientes "
         "y sostenibles."),

        ("ODS 12 – Producción y consumo responsables",
         "Impulsa modelos de consumo y producción sostenibles "
         "que reduzcan el impacto ambiental."),

        ("ODS 13 – Acción por el clima",
         "Adopta medidas urgentes para combatir el cambio climático "
         "y sus efectos."),

        ("ODS 14 – Vida submarina",
         "Conserva y utiliza de forma sostenible los océanos, mares "
         "y recursos marinos."),

        ("ODS 15 – Vida de ecosistemas terrestres",
         "Protege, restaura y promueve el uso sostenible de los ecosistemas "
         "terrestres y la biodiversidad."),

        ("ODS 16 – Paz, justicia e instituciones sólidas",
         "Promueve sociedades pacíficas e inclusivas, el acceso a la justicia "
         "y la construcción de instituciones eficaces."),

        ("ODS 17 – Alianzas para lograr los objetivos",
         "Fortalece los medios de implementación y revitaliza la alianza "
         "mundial para el desarrollo sostenible.")
    ]

    # -------------------------------
    # RENDER DE CADA ODS
    # -------------------------------
    for indice, (titulo, descripcion) in enumerate(ods_info, start=1):
        # Línea divisora
        st.markdown("""
    <div style="
        height: 3px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        border-radius: 50px;
        margin-top: 3rem;
        margin-bottom: 1rem;
    "></div>
    """, unsafe_allow_html=True)

        ruta_imagen = os.path.join(carpeta, f"objetivos_{indice:02}.png")

        st.markdown("<br><br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([2,1,2])

        with col2:
            st.image(ruta_imagen, width=150)

        st.markdown("<br>", unsafe_allow_html=True)

        # Título
        st.markdown(
            f"<h1 style='text-align: center;font-family: \"Sora\", sans-serif;font-weight: 800;'>"
            f"{titulo}"
            f"</h1>",
            unsafe_allow_html=True
        )

        # Descripción
        st.markdown(
            f"<p style='text-align: center; font-size:24px;'>"
            f"{descripcion}"
            f"</p>",
            unsafe_allow_html=True
        )

