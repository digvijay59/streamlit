import streamlit as st
import json
from supabase import *
import streamlit

with open("SUPABASE_API.json") as f:
    config = json.load(f)

SUPABASE_URL = config["SUPABASE_URL"]
SUPABASE_KEY = config["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def render():
    st.title("Your form")
    name = st.text_input("Name",key ="name")
    city = st.text_input("City",key ="city")
    state = st.text_input("State",key ="state")
    if st.button("submit"):
        response = supabase.table("user_info").insert({
            "name": name,
            "city": city,
            "state": state
        }).execute()

        if response.data:
            st.success("Data inserted successfully!")
        else:
            st.warning("Insert attempted but returned no data.")
