import streamlit as st
import time
import requests


st.header('Mi analysis')


with st.spinner(text="In progress..."):
    user_input = st.text_area('Text to analyze')

    st.success(f'Sentiment: {user_input}')













# user_input = st.text_input('Text to analyze', value='')

# params = dict(
#     user_input=user_input)

# mi_person_api_url = ''
# response = requests.get(mi_person_api_url, params=params)

# prediction = response.json()

# pred = prediction['fare']

# st.header(f'Sentiment: {pred}')
