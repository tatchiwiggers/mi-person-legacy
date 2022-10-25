import streamlit as st
import webbrowser

st.set_page_config(
    page_title="Mi-person", # => Quick reference - Streamlit
    page_icon="",
    layout="centered", # wide
    initial_sidebar_state="collapsed") # auto - prefixed bar


# primaryColor="#F63366"
# backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#F0F2F6"
# textColor="#262730"
# font="sans serif"

st.markdown("""# Mi Person
### say the right thing at the right time




Com o objetivo de auxiliar na comunicação

Através da analise de sentimento o Mi-person identifica e avalia a mensagem recebida para classifica-lá

Termometro que diagnostica o tipo de sentimento por trás da mensagem.

Como saber o que a pessoa quer dizer?mi-person, seu novo melhor amigoAjuda na interpretação das mensagens…ajuda as pessoas a se comunicarem melhor por mensagens, evitando mal entendidos…

""")
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
