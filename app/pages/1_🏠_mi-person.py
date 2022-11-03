from select import select
import streamlit as st
import pandas as pd
import csv
from PIL import Image
import numpy as np
import json
import requests



# PAGE_CONFIGURATION

st.set_page_config(
    page_title="mi-person", # => Quick reference - Streamlit
    page_icon="🏠",
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
    st.markdown("""Welcome to **mi-person**! Our application is designed to indentify
    a person's emotion based on any text, such as reviews, tweets or a simple interaction with chatbots.
    """)
    st.markdown("To get yout text analyzed, simply input the chosen text and click at the button below")

    st.write(""" """)

    st.markdown(" ### Try it out")

    sentence = st.text_input(label='Enter a sentence to be analyzed:')

    user_input = {'sentence': sentence }

    if st.button("Do the magic"):
        res = requests.post(url ='http://127.0.0.1:8504/mi-person', data=json.dumps(user_input))
        st.subheader(f'Response from API = {res.status_code}')
        
        
        if user_input == 'sim':
            st.success(f'Sentiment: {user_input}')
        elif user_input == 'não':
            st.error(f'Sentiment: {user_input}')
        else:
            st.warning(f'Sentiment: {user_input}')


        st.markdown('To know more about our product:')
        # st.markdown('[**about mi-person**](http://192.168.0.8:8501/about-us)',False)
        st.write("check out our github repository @ [mi-person repository](https://github.com/tatchiwiggers/mi-person)")
