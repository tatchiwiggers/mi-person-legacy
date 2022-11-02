from select import select
from streamlit_option_menu import option_menu
import streamlit as st
import time
import pandas as pd
import csv
from PIL import Image
import numpy as np
from st_aggrid import AgGrid


# PAGE_CONFIGURATION

st.set_page_config(
    page_title="mi-person", # => Quick reference - Streamlit
    page_icon="",
    layout="centered", # wide
    initial_sidebar_state="auto") # auto - prefixed bar

with st.sidebar:
    selected = option_menu(
        menu_title= None,
        options=['mi-person', 'mi-project','mi-analysis', 'mi-crew'],
        icons = ['house', 'megaphone', 'magic', 'people'],
        styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "rgba(255, 0, 0, 0.858)", "font-size": "15px"},
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "rgba(89, 179, 103, 0.571)"}}
    )

# HOME_PAGE

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    if selected == 'mi-person':

        st.markdown("""# mi-person
### **say the right thing at the right time** """)
        st.write(""" """)
        st.write(""" """)
        st.markdown("""Welcome to **mi-person**! Our application is designed to indentifies
        the emotion of your client throught his review, tweet or a simple interectation with chat bots.
        """)
        st.markdown("For analysis it's only necessary to input the chosen text and click at the button below")

        st.write(""" """)

        st.markdown(" ### Let's try our application")
        with st.spinner(text="In progress..."):
                user_input = st.text_area('')

        if st.button("Do the magic"):
            time.sleep(2)
            if user_input == 'sim':
                st.success(f'Sentiment: {user_input}')
            elif user_input == 'não':
                st.error(f'Sentiment: {user_input}')
            else:
                st.warning(f'Sentiment: {user_input}')


            st.markdown('To know more about our produt:')
            st.markdown('[**about mi-person**](http://172.24.246.242:8501/about-us)',False)
            # st.write("check our github repository [mi-person repository](https://github.com/tatchiwiggers/mi-person)")

### ABOUT THE PROJECT

    if selected == 'mi-project':

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


# PRODUCTS

    if selected == 'mi-analysis':

        st.title('mi-analysis')
        st.write('')
        st.write('')
        st.write('')
        analysis1, analysis2 = st.tabs(['Single text analysis', 'Dataset analysis'])
# one single text analysis
        with analysis1:
            st.markdown(" ### Insert yout text")
            st.write('Insert the text you wish to be analyse in the box below and click to view the magic.')
            user_input = st.text_area('')

            # params = dict(
            # user_input=user_input)

            # mi_person_api_url = ''
            # response = requests.get(mi_person_api_url, params=params)

            # prediction = response.json()

            # pred = prediction['emotion']
            # if st.button("Do the magic"):
            #     if pred == 'positive':
            #         st.success(f'Sentiment: {pred}')
            #     elif pred == 'negative':
            #         st.error(f'Sentiment: {pred}')
            #     else:
            #         st.warning(f'Sentiment: {pred}')

            if st.button("Do the magic"):
                time.sleep(2)
                if user_input == 'sim':
                    st.success(f'Sentiment: {user_input}')
                elif user_input == 'não':
                    st.error(f'Sentiment: {user_input}')
                else:
                    st.warning(f'Sentiment: {user_input}')
# Dataset text analysis
        with analysis2:
            st.markdown("### **Import a dataset** ")
            st.write('If you want to analyse more than one single text at once, import a csv extansion file, displaying all texts in column A, one for wich line. Below the model csv file to download.')

            with open("csv_model.csv", "r") as file:
                st.download_button(
                    label="Download the CSV model",
                    data=file,
                    file_name="mi-model.csv",
                    mime="text/csv"
                )
            st.write('')
            st.write('')
            st.write("Upload your csv file and wait to the 'download the predictions' button appears to view the magic.")
            uploaded_file = st.file_uploader("")
            if uploaded_file is not None:
                df = pd.read_csv(uploaded_file)
                AgGrid(df)

                @st.cache
                def convert_df(data):
                    return data.to_csv().encode('utf-8')


                csv = convert_df(df)

                st.download_button(
                    label="Download the predictions",
                    data=csv,
                    file_name='mi-person_df.csv',
                    mime='text/csv',
                )




### THE CREW

    if selected == 'mi-crew':

        st.markdown('# mi - crew')
        st.write('')
        st.write('')


    ## IMAGE COLUMN
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.image('https://avatars.githubusercontent.com/u/106851222?v=4')
        with col2:
            st.image('https://avatars.githubusercontent.com/u/32474883?v=4')

        with col3:
            st.image('https://avatars.githubusercontent.com/u/50644696?v=4')

        with col4:
            st.image('https://avatars.githubusercontent.com/u/69222394?v=4')

    ## NAME COLUMN
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            col1.header('Carlos Lima')

        with col2:
            col2.header('Luiza Rosalba')

        with col3:
            col3.header('Tabatha Wiggers')

        with col4:
            col4.header('Thaís Carreira')


    ### ICON COLUMN

        def make_grid(cols,rows):
            grid = [0]*cols
            for i in range(cols):
                with st.container():
                    grid[i] = st.columns(rows)
            return grid
        mygrid = make_grid(2,24)

        mygrid[0][2].markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/carlos-campos-46b06434/)")
        mygrid[0][3].markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/Carlos-Lima-Campos)")

        mygrid[0][8].markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/luizarosalba/)")
        mygrid[0][9].markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/luizarosalba)")

        mygrid[0][14].markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/tabatha-wiggers-b17372190/)")
        mygrid[0][15].markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/tatchiwiggers)")

        mygrid[0][20].markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/thais-carreira/)")
        mygrid[0][21].markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/thaisccarreira)")
