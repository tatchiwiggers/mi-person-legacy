import streamlit as st
st.set_page_config(
    page_title="mi-person", # => Quick reference - Streamlit
    page_icon="",
    layout="centered", # wide
    initial_sidebar_state="auto") # auto - prefixed bar

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.markdown('# mi-teachers')
    st.write('')
    st.write('')
    st.write('')

    ## IMAGE COLUMN
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image('https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1644940036/rjngbhyeskblbjvmnu58.jpg')
        
    with col2:
        st.image('https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1655413318/qichgsj7ulwov8c5mvjp.jpg')

    with col3:
        st.image('https://avatars.githubusercontent.com/u/26282955?v=4')


    ## NAME COLUMN
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        col3.header('Lucas Hisroshi')

    with col2:
        col2.header('Luis Trindade')

    with col3:
        col1.header('Marcio Garcia')


    ### ICON COLUMN

    def make_grid(cols,rows):
        grid = [0]*cols
        for i in range(cols):
            with st.container():
                grid[i] = st.columns(rows)
        return grid
    mygrid = make_grid(3,24)
