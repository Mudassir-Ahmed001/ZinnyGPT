import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

#loading environment variables
load_dotenv()

#configuring streamlit page settings
st.set_page_config(
    page_title="Zinny - Gemini Pro Chatbot",
    layout="centered",
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#setting up google gemini-pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

#function to translate roles btw Gemini-pro and steamlit terminology
def translation_role_for_stramlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

#initializing chat session in streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

#displaying the chatbot's title on the page
st.title("🤖Zinny - Gemini Pro Chatbot")

#displaying the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translation_role_for_stramlit(message.role)):
        st.markdown(message.parts[0].text)

#input field for user's message
user_prompt = st.chat_input("Ask Zinny...")
if user_prompt:
    #add user's message to chat and display it
    st.chat_message('user').markdown(user_prompt)

    #sending user's message to gemini pro and displaying it
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    #displaying gemini-pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)