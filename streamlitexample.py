import streamlit as st

# Title
st.title("My First Streamlit App")

# Text input
name = st.text_input("Enter your name:")

# Button
if st.button("Say Hello"):
    st.write(f"Hello, {name}!")

# Slider
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")