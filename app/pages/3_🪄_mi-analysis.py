
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import csv

st.set_page_config(
    page_title="mi-person", # => Quick reference - Streamlit
    page_icon="",
    layout="centered", # wide
    initial_sidebar_state="auto") # auto - prefixed bar

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

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
