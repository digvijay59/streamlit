import streamlit as st
import pandas as pd

st.title("Data Representation")
file = st.file_uploader("upload your csv ",type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df)
if file:
    st.subheader("summary stats")
    st.write(df.describe())
if file:
    num = df["Game Number"].unique()
    selected_number = st.selectbox("filter by number", num)
    filtered_data = df[df["Game Number"] == selected_number]
    st.dataframe(filtered_data)

