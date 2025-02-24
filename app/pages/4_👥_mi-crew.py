import streamlit as st
st.set_page_config(
    page_title="mi-person", # => Quick reference - Streamlit
    page_icon="",
    layout="centered", # wide
    initial_sidebar_state="auto") # auto - prefixed bar

with open('app/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    st.markdown('# mi - crew')
    st.write('')
    st.write('')


    ## IMAGE COLUMN
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image('https://avatars.githubusercontent.com/u/106851222?v=4')
    with col2:
        st.image('https://avatars.githubusercontent.com/u/32474883?v=4')

    with col3:
        st.image('https://avatars.githubusercontent.com/u/50644696?v=4')

    with col4:
        st.image('https://avatars.githubusercontent.com/u/69222394?v=4')

    ## NAME COLUMN
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        col1.header('Carlos Lima')

    with col2:
        col2.header('Luiza Rosalba')

    with col3:
        col3.header('Tabatha Wiggers')

    with col4:
        col4.header('Thaís Carreira')


    ### ICON COLUMN

    def make_grid(cols,rows):
        grid = [0]*cols
        for i in range(cols):
            with st.container():
                grid[i] = st.columns(rows)
        return grid
    mygrid = make_grid(2,24)

    mygrid[0][2].markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/carlos-campos-46b06434/)")
    mygrid[0][3].markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/Carlos-Lima-Campos)")

    mygrid[0][8].markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/luizarosalba/)")
    mygrid[0][9].markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/luizarosalba)")

    mygrid[0][14].markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/tabatha-wiggers-b17372190/)")
    mygrid[0][15].markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/tatchiwiggers)")

    mygrid[0][20].markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/thais-carreira/)")
    mygrid[0][21].markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/thaisccarreira)")
