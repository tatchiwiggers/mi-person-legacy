from select import select
from streamlit_option_menu import option_menu
import streamlit as st
import webbrowser
import time
import pandas as pd

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

# HOME_PAGE (app)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    if selected == 'mi-person':
        st.markdown("""# mi-person
### **say the right thing at the right time** """)

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


            st.markdown('For undertand more about our produt')
            st.markdown('[**about mi-person**](http://172.24.246.242:8501/about-us)',False)


### ABOUT THE PROJECT

if selected == 'mi-project':

    st.title('mi-project')

    st.markdown('esboço 1')

    st.markdown(""" O projeto mi-person surgiu com o objetivo de ajudar às empresas no relacionamento com
                seus clientes, frente aos reviews, reclamações ou até mesmo chat-bots.
                """)
    st.markdown(""" Atualmente com a difusão da tecnologia ... """)

    st.markdown("""Nosso modelo categoriza os textos em diferentes sentimentos que são agrupados
                em três diferentes categorias, a fim de auxiliar no relacionamento com os clientes,
                marketing pós-venda, assistência etc etc amanhã escrevo melhor""")

    st.markdown('As categorias agrupadas estão abaixo.')

    st.markdown('esboço 2')

    st.markdown("""O mi-person é uma aplicação de NLP que surgiu com o objetivo de auxiliar os usuários a identificar os sentimentos de seus clientes, seguidores entre outros a respeito de seus posts, reviews de produtos ou serviços de forma mais eficaz.
Nosso modelo tem como principal característica ajudar na rápida identificação da interação do 'cliente' para que o usuário possa concentrar esforços em suas estratégias de forma eficiente e planejada.
Os sentimentos são divididos em 27 categorias que agrupamos em 3 tipos de estados para facilitar na abordagem. Os estados sendo: Neutro, Negativo e Positivo.
As 27 categorias pertencentes a cada estado estão exemplificadas abaixo.

               """)

    st.markdown('esboço 3')

    st.markdown("""O mi-person nasceu com o objetivo de auxiliar as empresas identificar de forma mais otimizada o sentimento expresso por seus clientes através de seus reviews, interações via rede sociais ou até mesmo contato com os chat-bots.
O principal intuito da nossa aplicação é que não seja necessário a utilização máxima de recursos para as análises de interação dos clientes, mas que se possa focar apenas nas que sejam importantes para a manutenção/fidelização, tratamento de danos ou até mesmo suporte técnico.
Nosso modelo traduz de forma simplificada o sentimento apresentado em três principais categorias, sendo elas Negativo, Neutro e Positivo.
As três categorias englobam outras 27 categorias de sentimentos que poderão ser exploradas também pelos usuários da plataforma.
A segmentação em três principais categorias irá assessorar na seleção da melhor estratégia para cada caso, otimizando o emprego dos recursos.
""")


    tab1, tab2, tab3 = st.tabs(['Positive', 'Neutral', 'Negative'])

    with tab1:
        st.subheader('Emotions')
        with st.container():
            st.write('admiration,amusement,approval,caring,curiosity,\
                    desire,excitement,gratitude,joy,love,optimism,relief,realization')

    with tab2:
        st.subheader('Emotions')
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:

        st.subheader('Emotions')
        with st.container():
            st.write('anger,annoyance,confusion,disappointment,disapproval,disgust,embarrassment,\
        fear,grief,nervousness,pride,remorse,sadness')


# PRODUCTS

if selected == 'mi-analysis':

    st.title('mi-analysis')

    col1, col2 = st.columns(2)


    with col1:

        st.markdown('Análise através de input de texto:')
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

    with col2:

        st.markdown("""Análise através de datasets em extensão csv:
                    """)

        uploaded_file = st.file_uploader("")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write(df)


            csv = df.to_csv()

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='mi-person_df.csv',
                mime='text/csv',
            )



### THE CREW

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    if selected == 'mi-crew':

        st.markdown('# mi - CREW')
        st.write('----------')

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.image('https://avatars.githubusercontent.com/u/106851222?v=4')
            col1.header('Carlos Lima')

            st.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/carlos-campos-46b06434/)")

            st.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/Carlos-Lima-Campos)")

        with col2:
            st.image('https://avatars.githubusercontent.com/u/32474883?v=4')
            col2.header('Luiza Rosalba')

            st.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/luizarosalba/)")

            st.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/luizarosalba)")
        with col3:
            st.image('https://avatars.githubusercontent.com/u/50644696?v=4')
            col3.header('Tabatha Wiggers')
            st.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/luizarosalba/)")
            st.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/tatchiwiggers)")

        with col4:
            st.image('https://avatars.githubusercontent.com/u/69222394?v=4')
            col4.header('Thaís Carreira')
            st.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/thais-carreira/)")

            st.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/thaisccarreira)")


# col1, col2 = st.columns(2)
# with col1:
#     if st.button('Mi-emotion'):
#         link = 'http://172.24.246.242:8501/mi-emotions'
#         webbrowser.open_new(link)

#     # st.markdown(link, unsafe_allow_html=True)

# with col2:
#     link2 = 'http://172.24.246.242:8501/mi-analys'
#     if st.button('Mi-analysis'):
#         webbrowser.open_new(link2)
