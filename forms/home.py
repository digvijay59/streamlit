import streamlit as st
from supabase import create_client
import page1
import page2
import form

if "page" not in st.session_state:
    st.session_state.page = "home"


def go_home():
    st.session_state.page = "home"

def go_signup():
    st.session_state.page = "signup"

def go_signin():
    st.session_state.page = "signin"

if st.session_state.page == "home":
    st.title("Welcome!")

    col1, col2 = st.columns(2)
    with col1:
        st.button("Signup", on_click=go_signup)
    with col2:
        st.button("Signin", on_click=go_signin)

elif st.session_state.page == "signup":
    page1.render(go_home)

elif st.session_state.page == "signin":
    page2.render(go_home)
elif st.session_state.page == "form":
    form.render()
