import streamlit as st

st.title('STREAMLIT')
st.subheader('MY FIRST STREAMLIT PAGE')
st.text("This is my first page using streamlit(text)")
st.write("you are?")
profession = st.selectbox("you are?",["student","intern","engineer","doctor"])
st.write(f"you choose {profession}")
st.success("your profession has been noted")