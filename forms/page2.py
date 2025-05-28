import streamlit as st
from supabase import create_client
import json

with open("SUPABASE_API.json") as f:
    config = json.load(f)

SUPABASE_URL = config["SUPABASE_URL"]
SUPABASE_KEY = config["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def go_home():
    st.session_state.page = "home"

def render(go_home_callback):
    st.title("Sign In")
    st.write("Enter your email and password.")

    email = st.text_input("Email address", key="signin_email")
    password = st.text_input("Password", type="password", key="signin_password")

    if st.button("Sign In", key="signin_button"):
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if response.user:
            st.session_state.user = response.user
            st.session_state.page = "form"
            st.success(f"Welcome back, {response.user.email}!")
            # st.write("Access Token:", response.session.access_token)
            # st.write("Refresh Token:", response.session.refresh_token)
            st.rerun()
        else:
            st.error("Login failed. Please check your credentials.")

    st.button("Back to Home", on_click=go_home_callback, key="back_home")
