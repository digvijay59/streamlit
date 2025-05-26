import streamlit as st
import pandas as pd
import requests

st.title("Currency convertor")
amount = st.number_input("Amount in INR",min_value=0)

target_currency = st.selectbox("Target Currency",["USD","EUR","VND"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        response = response.json()
        rate = response["rates"][target_currency]
        converted = rate*amount
        st.success(f"{converted} {target_currency}")
    else:
        st.error("Request failed")