import streamlit as st
from dotenv import load_dotenv
load_dotenv() #Loading all envirment variables

import streamlit as st
import os
import google.generativeai as genai

def run_chatbot():
    # Your chatbot code here
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    #Function to load Gemini Pro model and get reponses

    model = genai.GenerativeModel("gemini-pro")
    @st.cache_resource
    def get_response(question):
        response = model.generate_content(question)
        return response.text

    #Initialize our streamlit

    # st.set_page_config(page_title="Q&A Demo")
    st.header("LLM Chatbot")

    input_text = st.text_input("Ask the question :",key = "input")
    submit = st.button("Enter")

    #When submit is clicked
    if submit:
        if input_text:
            response = get_response(input_text)
            st.write(response)
        else:
            st.write("Please enter a question.")