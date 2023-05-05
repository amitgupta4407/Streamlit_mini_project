import streamlit as st

st.title("WIDGITS")

if st.button("Code | Eat | Repeat"):
    st.write("Good2Know")

name = st.text_input("Name")
if name: st.write("Have a nice day " + name)

st.text_area("Enter ur address")
st.write(st.date_input("Enter date"))
st.time_input("Enter time")

if st.checkbox("you ac T&C", value = True):
    st.write("Thank You")

v1 = st.radio("Colours",["r","g","b"], index= 1)
v2 = st.selectbox("Colours",["r","g","b"], index= 1)
v3 = st.multiselect("Colours",["r","g","b"])

st.write(v1, v2, v3)

st.slider("age", min_value = 0 , max_value = 65, value = 30, step = 2)
st.number_input("age", min_value = 0 , max_value = 65, value = 30, step = 2)

img = st.file_uploader("Upload a img file")
if img: st.image(img)