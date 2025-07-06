from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai


# funciton to load gemini Pro Model and get responses
model = genai.GenerativeModel('gemini-2.5-pro')

def get_gemini_response(quesiton):
    response = model.generate_content(quesiton)
    return response.text

## initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input = st.text_input("input: ", key = "input")
submit = st.button("Ask the question!")

## when submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is: ")
    st.write(response) 