import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide')

st.markdown("<h1 style='text-align: center;font-size: 76px;'>Welcome to Digital Meet (Manufacturing) 2024</h1>", unsafe_allow_html=True)

def ChangeWidgetFontSize(wgt_txt, wch_font_size = '12px'):

    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('*'), i;

                    for (i = 0; i < elements.length; ++i) { if (elements[i].innerText == |wgt_txt|)

                        { elements[i].style.fontSize='""" + wch_font_size + """';} } </script>  """

 

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")

    components.html(f"{htmlstr}", height=0, width=0)

a = st.columns(3)
st.write(" ")
st.write(" ")
a[1].markdown("[Digital Meet Session Summary](https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZWVjYWI4ZGUtMjY3My00OTYxLWFhOTQtZmZmNzY3ZjRkNzdk%40thread.v2/0?context=%7b%22Tid%22%3a%22b5ff47a6-f7b4-4abf-a484-a75057bd8139%22%2c%22Oid%22%3a%22e6de7ade-191f-4b03-96a0-63290e12461e%22%7d)",
            unsafe_allow_html=True)

ChangeWidgetFontSize('Digital Meet Session Summary','43px')