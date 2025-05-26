import streamlit as st

st.title("WIDGETS")

if st.button("button click"):
    st.success("button clicked")

checkbox = st.checkbox("first-page done")

if checkbox:
    st.success("first page done")

to_do_next = st.radio("pick your next task",["django","flask","react"])

if to_do_next :
    st.write(f"you have picked {to_do_next}")

requirements = st.selectbox("requirements",["python","html","css"])
if requirements :
    st.write(f"requirements are {requirements}")

satisfaction = st.slider("satisfaction",0,100)
if satisfaction <20:
    st.write(f"you are not satisfied")
elif satisfaction <= 60 and satisfaction>=20:
    st.write(f"you are moderately satisfied")
else:
    st.write(f"you are fully satisfied")

days = st.number_input("how many days",min_value=1,max_value=3)
if days :
    st.write(f"you have {days} days")

name = st.text_input("enter your name")
if name :
    st.write(f"your name {name}")

dob = st.date_input("enter your date of birth")
if dob :
    st.write(f"your date of birth is {dob}")