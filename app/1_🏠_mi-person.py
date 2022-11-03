from select import select
import streamlit as st
import pandas as pd
import csv
from PIL import Image
import numpy as np



# PAGE_CONFIGURATION

st.set_page_config(
    page_title="mi-person", # => Quick reference - Streamlit
    page_icon="",
    layout="centered", # wide
    initial_sidebar_state="auto") # auto - prefixed bar


# HOME_PAGE

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



    st.markdown("""# mi-person""")
    st.markdown("""### **say the right thing at the right time**
    """)
    st.write(""" """)
    st.write(""" """)
    st.markdown("""Welcome to **mi-person**! Our application is designed to indentifies
    the emotion of your client throught his review, tweet or a simple interectation with chat bots.
    """)
    st.markdown("For analysis it's only necessary to input the chosen text and click at the button below")

    st.write(""" """)

    st.markdown(" ### Let's try our application")

    user_input = st.text_area('')

    if st.button("Do the magic"):

        if user_input == 'sim':
            st.success(f'Sentiment: {user_input}')
        elif user_input == 'não':
            st.error(f'Sentiment: {user_input}')
        else:
            st.warning(f'Sentiment: {user_input}')


        st.markdown('To know more about our produt:')
        # st.markdown('[**about mi-person**](http://192.168.0.8:8501/about-us)',False)
        st.write("check our github repository [mi-person repository](https://github.com/tatchiwiggers/mi-person)")
