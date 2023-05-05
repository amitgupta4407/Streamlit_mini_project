import streamlit as st

st.title("Hello streamlit")

st.header("Header")

st.subheader("Sub header")

st.text("Whoo text inside")

st.markdown("""
# h1 tag
## h2 tag
:moon: <br>
:sunglasses:
refer this: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#youtube-videos
""", True)

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')

st.write("harsh", "kumar", " # st", sum,st)
# st.camera_input("input camera")
