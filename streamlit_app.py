import streamlit as st
import requests

# Set up the Dify AI API endpoint and secret key
dify_endpoint = "https://api.dify.ai/v1/chat-messages"
secret_key = "app-OZw6qix4wsjQl4MUTmlpEukZ"



def send_message(text):
    # Create a JSON payload with the input text and other metadata
    payload = {
        "inputs": {"text": text},
        "query": "eh",
        "response_mode": "streaming",
        "conversation_id": "",
        "user": ""
    }

    # Set up the HTTP headers with the Authorization token
    headers = {
        "Authorization": f"Bearer {secret_key}",
        "Content-Type": "application/json"
    }

    try:
        # Send the request to the Dify AI API
        response = requests.post(dify_endpoint, json=payload, headers=headers)

        # Print the response from the Dify AI API (if there is one)
        print(response.json())
    except Exception as e:
        # Print an error message if there was an issue sending the request
        print(f"Error sending message: {e}")

# Streamlit interface
st.title("Dify AI Chat")

# Get user input
user_input = st.text_input("Enter a message")

# Send user input as a message
if st.button("Send"):
    send_message(user_input)
