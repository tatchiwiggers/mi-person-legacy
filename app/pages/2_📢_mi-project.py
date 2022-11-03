import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(
    page_title="mi-person", # => Quick reference - Streamlit
    page_icon="",
    layout="centered", # wide
    initial_sidebar_state="auto") # auto - prefixed bar

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.title('mi-project')

    st.markdown('esboço 1 do about rs')

    st.markdown(""" O projeto mi-person surgiu com o objetivo de ajudar às empresas no relacionamento com
                seus clientes, frente aos reviews, reclamações ou até mesmo chat-bots.
                """)
    st.markdown(""" Atualmente com a difusão da tecnologia ... """)

    st.markdown("""Nosso modelo categoriza os textos em diferentes sentimentos que são agrupados
                em três diferentes categorias, a fim de auxiliar no relacionamento com os clientes,
                marketing pós-venda, assistência etc etc amanhã escrevo melhor""")

    st.markdown('As categorias agrupadas estão abaixo.')

    st.markdown('esboço 2 do about rs')

    st.markdown("""O mi-person é uma aplicação de NLP que surgiu com o objetivo de auxiliar os usuários a identificar os sentimentos de seus clientes, seguidores entre outros a respeito de seus posts, reviews de produtos ou serviços de forma mais eficaz.
    Nosso modelo tem como principal característica ajudar na rápida identificação da interação do 'cliente' para que o usuário possa concentrar esforços em suas estratégias de forma eficiente e planejada.
    Os sentimentos são divididos em 27 categorias que agrupamos em 3 tipos de estados para facilitar na abordagem. Os estados sendo: Neutro, Negativo e Positivo.
    As 27 categorias pertencentes a cada estado estão exemplificadas abaixo.

            """)
    st.write("check our github repository [mi-person repository](https://github.com/tatchiwiggers/mi-person)")

    selected2 = option_menu(
            menu_title= None,
            options=['POSITIVE', 'NEUTRAL','NEGATIVE'],
            icons = ['emoji-smile', 'emoji-neutral', 'emoji-frown'],
            orientation= 'horizontal',
            styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "rgba(255, 0, 0, 0.858)", "font-size": "15px"},
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "rgba(89, 179, 103, 0.571)"}}
    )
    if selected2 == 'POSITIVE':
        image = Image.open('tab_positive.jpeg')
        st.image(image, width=730)

    if selected2 == 'NEGATIVE':
        image = Image.open('tab_negative.jpeg')
        st.image(image, width=730)

    if selected2 == 'NEUTRAL':
        image = Image.open('tab_neutral.jpeg')
        st.image(image, width=730)
