
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

        
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
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
            # res = requests.post(url ='http://127.0.0.1:8504/mi-person', data=json.dumps(user_input)) for later
            
            sentiment_dict = sentiment_scores(user_input)
            
            if sentiment_dict['compound'] >= 0.05 :
                res = "Positive, say something nice back :)"

            elif sentiment_dict['compound'] <= - 0.05 :
                res = "Negative, try to chill a bit before answering..."

            else :
                res = "Neutral, so no problem here ;)"
                
            
            if res.split(',')[0] == 'Positive':
                # st.subheader('Sucesso')
                st.success(f'sentiment: {res}')
            elif res.split(',')[0] == 'Neutral':
                # st.subheader('Sucesso')
                st.warning(f'sentiment: {res}')
            elif res.split(',')[0] == 'Negative':
                # st.subheader('Sucesso')
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


    # Dataset text analysis
    with analysis2:
        st.markdown("### **Import a dataset** ")
        st.write('''If you want to analyze more than one single text at once, 
                 import a csv extansion file, displaying all texts in column A,
                 one for wich line. Below the model csv file to download.''')

        with open("csv_model.csv", "r") as file:
            st.download_button(
                label="Download CSV File",
                data=file,
                file_name="mi-model.csv",
                mime="text/csv"
            )
            st.write('')
            st.write('')
            st.write("Upload your csv file with your input text then download the predictions to 'view the magic'.")
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
