from select import select
import streamlit as st
import pandas as pd
import csv
from PIL import Image
import numpy as np
import json
import requests
# from pre import sentiment_scores
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


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

    def sentiment_scores(sentence):
        # Create a SentimentIntensityAnalyzer object.
        sid_obj = SentimentIntensityAnalyzer()

        # polarity_scores method of SentimentIntensityAnalyzer
        # object gives a sentiment dictionary.
        # which contains pos, neg, neu, and compound scores.
        sentiment_dict = sid_obj.polarity_scores(sentence)
        
        print("Overall sentiment: ", sentiment_dict)
        print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
        print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
        print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

        print("\nSentence overall rated as", end = " ",)

        # decide sentiment as positive, negative and neutral
        # sentence = input("Enter a sentence to be analyzed: ")

        # sentiment_scores(sentence)
        return sentiment_dict
    

    if st.button("Do the magic"):
        # res = requests.post(url ='http://127.0.0.1:8504/mi-person', data=json.dumps(user_input))
        
        sentiment_dict = sentiment_scores(sentence)
        
        if sentiment_dict['compound'] >= 0.05 :
            res = "Positive, say something nice back :)"

        elif sentiment_dict['compound'] <= - 0.05 :
            res = "Negative, try to chill a bit before answering..."

        else :
            res = "Neutral, so no problem here ;)"
            
        
        if res.split(',')[0] == 'Positive':
            st.subheader('Sucesso')
            st.success(f'sentiment: {res}')
        elif res.split(',')[0] == 'Neutral':
            st.subheader('Sucesso')
            st.warning(f'sentiment: {res}')
        elif res.split(',')[0] == 'Negative':
            st.subheader('Sucesso')
            st.error(f'sentiment: {res}')
        else:
            st.subheader('Analysis failed.')
            st.error('The model could not evaluate any emotion in the text')

        st.subheader('Individual percentages per emotion')
        
        s = pd.DataFrame([sentiment_dict])
        s = s[['neg', 'pos', 'neu']]
        s = s.rename(columns={'neg': 'negative', 'pos': 'positive', 'neu': 'neutral'}).reset_index(drop=True)
        s = s.style.format("{:.2%}")

        # CSS to inject contained in a string
        hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """

        # Inject CSS with Markdown
        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        # Display a static table
        st.table(s)
    
    
        st.markdown('To know more about our product:')
        # st.markdown('[**about mi-person**](http://192.168.0.8:8501/about-us)',False)
        st.write("check out our github repository @ [mi-person repository](https://github.com/tatchiwiggers/mi-person)")
