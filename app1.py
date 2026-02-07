import streamlit as st
import google.generativeai as genai

st.title("Welcome to gemini models viewer")

user_input = st.text_input("Enter your google api key: ")
genai.configure(api_key = "AIzaSyBuZxJBXZj2jqdw3Hx6tKUipgq54Yfb2uc")

genai.GenerativeModel("models/gemini-2.5-flash")
if user_input:
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(user_input)
    st.write("Generated content")

    st.write(response.text)
