
from select import select
import streamlit as st
import webbrowser
from streamlit_option_menu import option_menu


# page configuration and sidebar setup

st.set_page_config(
    page_title="Mi-person", # => Quick reference - Streamlit
    page_icon="",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed - prefixed bar

with st.sidebar:
    selected = option_menu(
        menu_title= None,
        options=['mi-person', 'about-project','mi-analysis', 'mi-crew'],
        icons = ['house', 'megaphone', 'magic', 'people'],
        styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "rgba(255, 0, 0, 0.858)", "font-size": "15px"},
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "rgba(89, 179, 103, 0.571)"}}
    )


#FIRST_PAGE HOME PAGE
if selected == 'mi-person':

    st.markdown("""# Mi Person
### say the right thing at the right time




Com o objetivo de auxiliar na comunicação

Através da analise de sentimento o Mi-person identifica e avalia a mensagem recebida para classifica-lá

Termometro que diagnostica o tipo de sentimento por trás da mensagem.

Como saber o que a pessoa quer dizer?mi-person, seu novo melhor amigoAjuda na interpretação das mensagens…ajuda as pessoas a se comunicarem melhor por mensagens, evitando mal entendidos…

""")

    # create buttons to conect pages
    col1, col2 = st.columns(2)
    with col1:
        link = 'http://github.com'
        if st.button('Mi-emotion'):
            webbrowser.open_new(link)

        # st.markdown(link, unsafe_allow_html=True)

    with col2:
        link2 = 'http://globo.com.br'
        if st.button('Mi-analysis'):
            webbrowser.open_new(link2)

### ABOUT THE PROJECT
if selected == 'about-project':
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


### MODEL
if selected == 'mi-analysis':
    st.header('Mi analysis')
    st.write('----------')

    with st.spinner(text="In progress..."):
        user_input = st.text_area('Text to analyze')

        st.success(f'Sentiment: {user_input}')


### THE CREW

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    if selected == 'mi-crew':

        st.markdown('# Mi - CREW')
        st.write('----------')

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.title('Carlos Lima')
            st.image('https://avatars.githubusercontent.com/u/106851222?v=4')
            st.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/carlos-campos-46b06434/)")

            st.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/Carlos-Lima-Campos)")

        with col2:
            st.title('Luiza Rosalba')
            st.image('https://avatars.githubusercontent.com/u/32474883?v=4')

            st.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/luizarosalba/)")

            st.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/luizarosalba)")
        with col3:
            st.title('Tabatha Wiggers')
            st.image('https://avatars.githubusercontent.com/u/50644696?v=4')
            st.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/luizarosalba/)")
            st.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/tatchiwiggers)")

        with col4:
            st.title('Thais Carreira')
            st.image('https://avatars.githubusercontent.com/u/69222394?v=4'#, caption="I'm a financial planning analyst. \
                # I'm working now in a startup, but I've already worked at big brazilian companies.\
                    # I'm willing to learn new tecnologies and wanna change my career."
                    )
            st.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/thais-carreira/)")

            st.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/thaisccarreira)")









###### linkar streamilit api
# user_input = st.text_input('Text to analyze', value='')

# params = dict(
#     user_input=user_input)

# mi_person_api_url = ''
# response = requests.get(mi_person_api_url, params=params)

# prediction = response.json()

# pred = prediction['fare']

# st.header(f'Sentiment: {pred}')
