import streamlit as st

st.set_page_config(
    page_title="mi-person", # => Quick reference - Streamlit
    page_icon="🏠",
    layout="centered", # wide
    initial_sidebar_state="auto") # auto - prefixed bar




with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    def intro():
        import streamlit as st

        st.write("# Welcome to mi-person! 👋")
        st.sidebar.success("What would you like to do?")

        st.markdown(
        """
            mi-person is an open-source web application built specifically to help
            people understand each other!
            **👈 Select an action from the dropdown on the left** to see some examples
            of what mi person can do!
        """
        )

    def mapping_emotions():
        from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
        import matplotlib.pyplot as plt



        st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
        st.write(
            """
                    The wordcloud below displays the emotions extracted from the analyzed data
                    based on the lexical disposition of the words:
            """
        )

        stopwords = STOPWORDS
        # text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'
        text = "I, hate, hate, fun, fun, awesome, awesome, awesome, believe, can't, amazing, amazing, amazing"


        # Create and generate a word cloud image:
        wordcloud = WordCloud(stopwords=stopwords, background_color= "white", width=440, height=280, colormap='Set3').generate(text)

        # Display the generated image:

        fig, ax = plt.subplots(figsize = (12, 8))
        ax.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(fig)

    def plotting_sentiment():
        import streamlit as st
        import seaborn as sns

        st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
        st.write(
            """
            This plot illustrates the combination of sentiments found in the text.
            Though the analysis is based on 3 classes only: positive, negative and neutral -
            sentiments in a sentence are not limited to that ;)

            Enjoy!
            
            
            """
        )

    
        import streamlit as st
        import pandas as pd
        import numpy as np
        import plotly.express as px
        from plotly.subplots import make_subplots
        import plotly.graph_objects as go
        import matplotlib.pyplot as plt
        train = pd.read_csv("emotion.csv")


        sentiments = train['description']
        sentiments = pd.DataFrame(sentiments)
        # s = sentiments.rename(columns={'description': 'description', 'description': 'rate'})

        chart_data = pd.DataFrame(
            [[7.0], [18.26], [9.5], [11.42], [18.02], [35.80]],
            columns=['rate'],
            index=['dispapproval', 'excitement', 'joy',
                   'optimism', 'surprise', 'neutral']
        )

        st.bar_chart(chart_data)
    
        
    page_names_to_funcs = {
        "—": intro,
        "Plotting the sentiments of your text": plotting_sentiment,
        "Mapping the words": mapping_emotions,
        # "DataFrame Demo": data_frame_demo
    }

    demo_name = st.sidebar.selectbox("Go somewhere", page_names_to_funcs.keys())
    page_names_to_funcs[demo_name]()
