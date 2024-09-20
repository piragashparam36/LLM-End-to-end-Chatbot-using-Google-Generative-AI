# import streamlit as st
# from app import run_chatbot  # Assuming you have a function to run the chatbot
# from vision import run_chatbot_with_image  # Assuming you have a function for the image chatbot

# def main():
#     st.sidebar.title("Menu")
#     option = st.sidebar.selectbox("Select a section", ["Chatbot", "Chatbot with Image"])

#     if option == "Chatbot":
#         run_chatbot()  # Function to run your chatbot app
#     elif option == "Chatbot with Image":
#         run_chatbot_with_image()  # Function to run your image chatbot app

# if __name__ == "__main__":
#     main()


import streamlit as st
from app import run_chatbot  # Import chatbot logic from app.py
from vision import run_chatbot_with_image  # Import chatbot with image logic from vision.py

# Set the page configuration (make sure this is at the very top of the file)
st.set_page_config(page_title="Main App", layout="wide")

def main():
    # Sidebar with menu options
    st.sidebar.title("Menu")
    option = st.sidebar.radio("Select a section", ["Chatbot", "Chatbot with Image"])

    # Show the selected section based on the user input
    if option == "Chatbot":
        st.title("Chatbot")
        run_chatbot()  # Call your chatbot logic from app.py

    elif option == "Chatbot with Image":
        st.title("Chatbot with Image")
        run_chatbot_with_image()  # Call the image chatbot logic from vision.py

if __name__ == "__main__":
    main()
