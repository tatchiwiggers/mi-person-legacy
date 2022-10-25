import streamlit as st

import numpy as np
import pandas as pd



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
