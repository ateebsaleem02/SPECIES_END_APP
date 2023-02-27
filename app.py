import streamlit as st

st.title("WELCOME!!! to save the Endangered species")
st.snow()
st.text_area("Hi, This is Ateeb an Activist to save the endangered species, and i will be sharing with you the details for the ENDANGERED Specie, SAVE OUR ANIMALS SAVE OUR EARTH")

btn_click = st.button("Let's take you on animals tour!")

if btn_click == True:
    st.subheader("You clicked me :smile:")
    st.balloons()