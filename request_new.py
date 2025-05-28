import streamlit as st
import requests
import json

with open("rate_api.json") as f:
    config = json.load(f)
url = config["url"]
api_key = config.get("api_key")

st.title("Currency Converter")
amount_in_inr = st.number_input("Amount in INR", min_value=0.0)
with open("rates.json") as f:
    fileinfo = json.load(f)
currency = list(fileinfo["rates"].keys())
target_currency = st.selectbox("Target Currency", currency)

if st.button("Convert"):
    querystring = {
        "access_key": api_key,
        "symbols": f"INR,{target_currency}"
    }
    response = requests.get(url, params=querystring)
    if response.status_code == 200:
        data = response.json()
        inr_rate = data["rates"]["INR"]
        target_rate = data["rates"][target_currency]
        amount_in_eur = amount_in_inr / inr_rate
        converted_amount = amount_in_eur * target_rate

        st.success(f"{amount_in_inr} INR = {converted_amount} {target_currency}")
    else:
        st.error("Failed to fetch exchange rates. Please try again later.")
