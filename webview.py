# pip install streamlit

import streamlit as st
import pandas as pd
import requests
import json

st.title("Prediction APP")
st.write("this is a test")

df = pd.read_csv('video games sales prediction.csv')

CONSOLE = st.selectbox("CONSOLE", pd.unique(df['CONSOLE']))
YEAR = st.number_input("YEAR", step=1, value=df['YEAR'].min())
CATEGORY = st.selectbox("CATEGORY", pd.unique(df['CATEGORY']))
PUBLISHER = st.selectbox("PUBLISHER", pd.unique(df['PUBLISHER']))
RATING = st.selectbox("RATING", pd.unique(df['RATING']))
CRITICS_POINTS = st.number_input("CRITICS_POINTS", step=0.1)
USER_POINTS = st.number_input("USER_POINTS", step=0.1)

inputs = {
"CONSOLE" : CONSOLE,
"YEAR" : YEAR,
"CATEGORY" : CATEGORY,
"PUBLISHER" : PUBLISHER,
"RATING" :  RATING,
"CRITICS_POINTS" : CRITICS_POINTS,
"USER_POINTS" : USER_POINTS
}

if st.button('Predict'):
    res = requests.post(url = "http://127.0.0.1:8000/predict", data = json.dumps(inputs))

    st.json(res.text)

# Run this command in the command prompt "streamlit run webview.py"
# This will open up "http://localhost:8501/" - Streamlit home page