import streamlit as st 
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("Salary Predictor")

data = pd.read_csv(r"streamlit_mini_project\data\Salary_Data.csv",on_bad_lines='skip')
x = np.array(data["YearsExperience"]).reshape(-1,1)
lr = LinearRegression()
lr.fit(x, np.array(data['Salary']))

# st.write(st.sidebar.radio)
nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])
if nav == "Home":
    st.image("https://img.freepik.com/premium-photo/stack-black-money-coin-banking-currency-business-finance-cash-dollar-treasure-earnings-financial-profit-market-investment-stock-exchange-dark-3d-background-with-success-economy-income_79161-2032.jpg?w=800")
    if st.checkbox("Show data"):
        st.table(data)

    graph = st.selectbox("What kind of graph? ", ["Non-Interactive", "Interactive"])

    val = st.slider("Filter data using years", 0, 20)
    data = data.loc[data["YearsExperience"] >= val]
    if graph == "Non-Interactive":
        plt.figure(figsize = (10,5))
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("Year of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    else:
        layout = go.Layout(
            xaxis = dict(range = [0,16]),
            yaxis = dict(range = [0,120000])
        )
        fig = go.Figure(data=go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode='markers'),layout = layout)
        st.plotly_chart(fig)
if nav == "Prediction":
    st.header("Know your Salary")
    val = st.number_input("Enter you exp", 0.00, 20.00, step = 0.25)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]

    if st.button("Predice"):
        st.success(f"Your predicted salary is {round(pred)}")
if nav == "Contribute":
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter your Experience ", 0.0,20.0)
    sal = st.number_input("Enter your Salary", 0.00, 1000000.00, step = 1000.0)
    if st.button("submit") and ex and sal:
        to_add = {"YearsExperience":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("streamlit_mini_project/data/Salary_Data.csv",mode="a",header=False,index=False)
        st.success("Submitted")
    