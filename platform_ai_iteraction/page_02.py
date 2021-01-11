import streamlit as st
import streamlit_embedcode
import project_regression as pReg
from streamlit_embedcode import github_gist

def app():
    st.markdown("<h2 style='text-align: center; color: black;'>Regressão Linear</h2>", unsafe_allow_html=True)

    #st.markdown("<p style='text-align: justify;'>Introdução à Regressão Linear.</p>", unsafe_allow_html=True)
    #st.markdown("<p style='text-align: justify;'>Explicação do primeiro passo</p>", unsafe_allow_html=True)

    st.markdown("""<ul><li>Introdução à regressão Linear</li>
                <p style='text-align: justify;'>[...]</p>
                <li>Explicação do primeiro passo</li>
                <p style='text-align: justify;'>[...]</p>
                </ul>  """,unsafe_allow_html=True)

    values = st.text_area('code')
    if st.button("run"):
        lines = values.split('\n')
        IsCorrect = pReg.expected_step_one(lines)
        if IsCorrect == True:
            status = pReg.import_libraries(lines)
            if status == True:
                st.write("Parabéns! Primeiro passo executado com sucesso!")
            else:
                st.write("Oh não! Algo deu errado, verifique a solução proposta abaixo.")
        else:
            st.write("Oh não! Algo deu errado, verifique a solução proposta abaixo.")
        #st.write(lines)
            github_gist("https://gist.github.com/iagovargas/5ad1238afe39077a5441224148baa4d8",width=710)


    
    


    
