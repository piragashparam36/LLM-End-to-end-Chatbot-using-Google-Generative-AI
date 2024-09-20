from dotenv import load_dotenv
load_dotenv() #Loading all envirment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

import streamlit as st

def run_chatbot_with_image():
    # st.title("Chatbot with Image")
    # Your image chatbot code here
    # Configure the generative AI with API key from environment variables
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Function to load Gemini model and get responses
    model = genai.GenerativeModel("gemini-1.5-flash")

    #@st.cache_resource
    def get_gemini_response(input_text, image):
        if input_text:
            response = model.generate_content([input_text, image])
        else:
            response = model.generate_content([image])
        return response.text

    # Initialize our Streamlit app
    # st.set_page_config(page_title="Image Demo")
    st.header("LLM Chatbot with image Application")

    input_text = st.text_input("Input Prompt:", key="input")

    uploaded_file = st.file_uploader("Choose an Image...", type=["jpg", "jpeg", "png"])
    image = None

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Enter")

    # If submit is clicked
    if submit and image is not None:
        response = get_gemini_response(input_text, image)
        st.header("The Response is")
        st.write(response)
    else:
        if submit:
            st.warning("Please upload an image before submitting.")
