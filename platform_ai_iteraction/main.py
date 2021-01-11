import page_01
import page_02
import page_03
import page_04
import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def local_css_side(file_name):
    with open(file_name) as f:
        st.sidebar.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

#local_css("./style.css")
#local_css_side("./style_side.css")

st.markdown(
    """
<style>

.st-bb {
    background-color: transparent;
}
.st-at {
    background-color: transparent;
}
</style>
""",
    unsafe_allow_html=True,
)



PAGES = {
    "Inicio": page_01,
    "Regressão Linear": page_02,
    "Aprendizado Supervisionado": page_03,
    "Sobre":page_04
}
logo = './AI_Logo.png'

st.sidebar.image(logo,width=224,use_column_width=True)
selection = st.sidebar.selectbox("Ir para", list(PAGES.keys()))
page = PAGES[selection]
page.app()