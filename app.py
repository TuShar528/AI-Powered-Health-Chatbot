import streamlit as st
import requests
from bs4 import BeautifulSoup
import pytz, os, sys
import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Endpoints
API_BASE_URL = os.getenv("API_BASE_URL")
API_AUTH_URL = f"{API_BASE_URL}/auth"
API_CHAT_URL = f"{API_BASE_URL}/healthbot"
API_CHAT_HISTORY_URL = f"{API_BASE_URL}/chat_history"

# Page Configuration
st.set_page_config(page_title="SvasthBot - AI Health Assistant", page_icon="🩺", layout="wide")

# Custom CSS for enhanced UI
st.markdown(
    """
    <style>
    body {
        font-family: sans-serif; /* Modern font */
        background-color: #f4f4f4; /* Light background */
        color: #333; /* Dark text color for contrast */
    }
    .main .block-container {
        max-width: 900px; /* Center the content */
        padding-top: 2rem;
    }
    .stButton>button {
        background-color: #007bff; /* Blue buttons */
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        margin: 0.5rem 0;
    }
    .stButton>button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }
    .chat-container {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        background-color: white;
    }
    .message {
        padding: 0.5rem;
        margin-bottom: 0.5rem;
        border-radius: 5px;
        max-width: 80%; /* Prevent messages from taking full width */
        clear: both; /* Ensure messages are displayed correctly */
    }
    .user-message {
        background-color: #e9ecef; /* Light gray for user messages */
        float: right; /* Align user messages to the right */
    }
    .bot-message {
        background-color: #d1ecf1; /* Light blue for bot messages */
        float: left; /* Align bot messages to the left */
    }
    .message-content {
        white-space: pre-wrap; /* Allow line breaks in messages */
    }
    .sidebar .block-container {
        padding: 2rem;
    }
    .sidebar-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .chat-history-item {
        cursor: pointer;
        padding: 0.5rem 0;
    }
    .chat-history-item:hover {
        background-color: #eee;
    }
    .disclaimer {
        color: gray;
        font-size: small;
        margin-top: 1rem;
        text-align: center; /* Center disclaimer text */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Initialize Session State
# ... (rest of your session state initialization code)

# Helper Functions (convert_utc_to_ist, api_request)
# ... (your existing helper functions)

# Load Chat Sessions
# ... (your load_chat_sessions function)

# Load Selected Chat
# ... (your load_selected_chat function)

# Sidebar - Authentication & Chat History
with st.sidebar:
    st.markdown("<div class='sidebar-title'>Authentication</div>", unsafe_allow_html=True)  # Styled title
    # ... (rest of your authentication code)

    if not st.session_state.is_guest:
        st.markdown("<div class='sidebar-title'>Chat History</div>", unsafe_allow_html=True)  # Styled title
        # ... (rest of your chat history display code)


# Main App - Chat Interface
if st.session_state.auth_token:
    st.markdown("<h1 style='text-align: center;'>SvasthBot - AI Health Assistant</h1>", unsafe_allow_html=True)  # Centered title
    st.markdown("<p style='text-align: center;'>Ask me about medical symptoms, treatments, and general health advice!</p>", unsafe_allow_html=True)  # Centered subtitle
    st.markdown("<hr>")  # Horizontal line

    # Chat Messages Display
    with st.container():  # Use a container for better layout
        for message in st.session_state.messages:
            role = message["role"]
            content = message["content"]
            st.markdown(f"<div class='message {role}-message'><div class='message-content'>{content}</div></div>", unsafe_allow_html=True)

    # Chat Input
    query = st.text_area("Type your message here...", height=75) # Use text_area for multi-line input

    if st.button("Send"):  # Send button
        if query:
            # ... (rest of your query processing and response code)

    # Clear Chat/History Buttons
    st.markdown("<hr>")  # Horizontal line before buttons

    col1, col2 = st.columns(2)  # Use columns for better button placement

    with col1:
        if st.button("Clear Chat"):
            # ... (your clear chat logic)
    with col2:
        if not st.session_state.is_guest:
            if st.button("Delete Chat History"):
                # ... (your delete history logic)

    st.markdown("<div class='disclaimer'>Disclaimer: This information is for educational purposes only and should not be considered medical advice. Consult a healthcare professional for diagnosis and treatment.</div>", unsafe_allow_html=True)

else:
    # ... (your login message)