import streamlit as st
from supabase import create_client
import json

with open("SUPABASE_API.json") as f:
    config = json.load(f)

SUPABASE_URL = config["SUPABASE_URL"]
SUPABASE_KEY = config["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def render(go_home_callback):
    st.title("Signup Page")
    st.write("Enter your email and password.")
    email = st.text_input("Email address:",key="signup_email")
    password = st.text_input("password:",key="signup_password")
    if st.button("Sign Up"):
        response = supabase.auth.sign_up({"email": email, "password": password})
        if response.user:
            st.success("Signup successful! Check your email for a confirmation link.Confirm and signin")
        else:
            st.error("something went wrong")
    st.button("Back to Home", on_click=go_home_callback)

