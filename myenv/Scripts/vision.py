# import streamlit as st
# import os
# import google.generativeai as genai
# from PIL import Image
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ##Function to load Gemini Pro model and get reponses

# model = genai.GenerativeModel("gemini-pro-vision")
# @st.cache_resource
# def get_gemini_response(input,image):
#     if input != "":
#         response = model.generate_content([input,image])
#     else:
#         response = model.generate_content(image)
#     return response.text

# #Initialize our streamlit

# st.set_page_config(page_title="Image Demo")
# st.header("Gemini Application")

# input_text = st.text_input("Input Prompt :",key = "input")

# uploaded_file =st.file_uploader("Choose an Image...", type=["jpg","jpge","png"])
# image = ""

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image.", use_column_width=True)

# submit = st.button("Enter")

# #if submit is clicked
# if submit:
#     response = get_gemini_response(input,image)
#     st.header("The Response is")
#     st.write(response)

# #When submit is clicked
# if submit:
#     if input_text:
#         response = get_gemini_response(input,image)
#         st.header("The Response is")
#         st.write(response)
#     else:
#         st.write("Please enter a question.")

from dotenv import load_dotenv
load_dotenv() #Loading all envirment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the generative AI with API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro-vision")

#@st.cache_resource
def get_gemini_response(input_text, image):
    if input_text:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content([image])
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Image Demo")
st.header("Gemini Application")

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
