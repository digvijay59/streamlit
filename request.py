# import streamlit as st
# import pandas as pd
# import requests
#
# st.title("Currency convertor")
# amount = st.number_input("Amount in INR",min_value=0)
#
# target_currency = st.selectbox("Target Currency",["USD","EUR","VND"])
#
# if st.button("Convert"):
#     url = "https://api.exchangerate-api.com/v4/latest/INR"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         response = response.json()
#         rate = response["rates"][target_currency]
#         converted = rate*amount
#         st.success(f"{converted} {target_currency}")
#     else:
#         st.error("Request failed")

# import streamlit as st
# import pandas as pd
# import requests
#
# st.title("Currency convertor")
# amount = st.number_input("Amount in INR",min_value=0)
#
# url = "https://api.exchangerate-api.com/v4/latest/INR"
# response = requests.get(url)
#
# if response.status_code == 200:
#     response = response.json()
#     rate = response["rates"]
# else:
#     st.error("Request failed")
#
# target_currency = st.selectbox("Target Currency",rate)
#
# if st.button("Convert"):
#         converted = rate[target_currency]*amount
#         st.success(f"{converted} {target_currency}")


import streamlit as st
import pandas as pd
import requests
import json

with open("rate_api.json") as f:
    config = json.load(f)

url = config["url"]

st.title("Currency convertor")
amount = st.number_input("Amount in INR",min_value=0)
with open("rates.json") as f:
    fileinfo= json.load(f)

currency = fileinfo["rates"]

target_currency = st.selectbox("Target Currency",currency)

if st.button("Convert"):
    querystring = {"base": "EUR", "symbols": "INR"}
    response = requests.get(url, params=querystring)
    data = response.json()
    amount_in_eur = amount / (data['rates']['INR'])

    querystring = {"base": "EUR", "symbols": target_currency}
    response = requests.get(url, params=querystring)
    data = response.json()
    st.write(data)
    converted_currency  = amount_in_eur * (data['rates'][target_currency])

    st.success(f"{converted_currency} {target_currency}")


