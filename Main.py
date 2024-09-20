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
