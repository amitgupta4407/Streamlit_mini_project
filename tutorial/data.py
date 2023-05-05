import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1,2,3,4,5,6,7,8,9,10]
n = np.array(a)
nd = n.reshape((2,5))
dic = {
    "name" : "Amit",
    "age" :  21,
    "city" : "noida"
}

# data = pd.read_csv("data//salary_data")
st.dataframe(dic)
st.table(dic)
st.json(dic)
st.write(a)

@st.cache_data
def ret_time():
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time())

if st.checkbox("2"):
    st.write(ret_time())