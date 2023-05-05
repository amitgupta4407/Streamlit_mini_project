import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import time

hide_st_style = """
            <style>
            #mainMenue {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

plt.style.use("ggplot")

data = {
    "num":[x for x in range(11)],
    "square":[x**2 for x in range(11)],
    "twice":[x*2 for x in range(11)],
    "thrice":[x*3 for x in range(11)]
}
rad = st.sidebar.radio("Navigation", ["Home","About Us"])
if rad == "Home":
    df = pd.DataFrame(data = data)

    col = st.sidebar.multiselect("Select a number ",df.columns)

    plt.plot(df["num"], df[col])
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

if rad =="About Us":
    # st.write("you are on About Us page")

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
    st.balloons()
    st.error("Error")
    st.success("Show Success")
    st.info("Information")
    st.exception(RuntimeError("This is the error"))
    st.warning("This is the warning")