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
            This chart displays the emotions extracted from the analyzed data:
    """
        )

        stopwords = STOPWORDS
        text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'


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

        import pandas as pd
        import altair as alt

        train = pd.read_csv("emotion.csv")

        sentiments = train['description']
        sentiments = pd.DataFrame(sentiments)
        s = sentiments.rename(columns={'index': 'description', 'description': 'rate'})

        st.area_chart(s)


    page_names_to_funcs = {
        "—": intro,
        "Plotting the sentiments of your text": plotting_sentiment,
        "Mapping the words": mapping_emotions,
        # "DataFrame Demo": data_frame_demo
    }

    demo_name = st.sidebar.selectbox("Go somewhere", page_names_to_funcs.keys())
    page_names_to_funcs[demo_name]()
