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

    # st.markdown('esboço 1 do about rs')

    # st.markdown(""" O projeto mi-person surgiu com o objetivo de ajudar às empresas no relacionamento com
    #             seus clientes, frente aos reviews, reclamações ou até mesmo chat-bots.
    #             """)
    # st.markdown(""" Atualmente com a difusão da tecnologia ... """)

    # st.markdown("""Nosso modelo categoriza os textos em diferentes sentimentos que são agrupados
    #             em três diferentes categorias, a fim de auxiliar no relacionamento com os clientes,
    #             marketing pós-venda, assistência etc etc amanhã escrevo melhor""")

    # st.markdown('As categorias agrupadas estão abaixo.')

    # st.markdown('esboço 2 do about rs')

    st.markdown("""
                It's hard to communicate.
                
                How do you know what the other person is means to say? Do you fully understand
                what they mean? Can you get you message accross based on somone's response?
                
                Mi-person was created with the intent of helping people to identify the
                feelings behind any text, where understanding the real meaning can be troublesome, 
                dus to the lack of context of voice intonation. Mi-person can help you understand 
                sentences from casual text messages , tweets, emails or a simple interaction with chatbots. 
                
                As an open source web application, mi-person, can also be used to translate datasets making
                it possible to classify large-scale texts in one go. 
                
                Based on the words and context of each text, mi-person translates in a simplified way the
                sentiments presented in text format in three main categories: Negative, Neutral and Positive.
                These three categories are composed, at the moment, of 27 different emotions, which can be analyzed as below:
                """)

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

    # st.footer("""
    #          Check out our github repository - 
    #          [mi-person repository](https://github.com/tatchiwiggers/mi-person)
    #          """
    #          )
    