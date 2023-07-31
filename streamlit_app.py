import streamlit as st
import requests

# Set up the Dify AI API endpoint and secret key
dify_endpoint = "https://api.dify.ai/v1/chat-messages"
secret_key = "app-OZw6qix4wsjQl4MUTmlpEukZ"



# Global variables
conversation_id = ""

def send_message(text):
    global conversation_id

    # Create the payload with the input text and other metadata
    payload = {
        "inputs": {"text": text},
        "query": "eh",
        "response_mode": "streaming",
        "conversation_id": "",
        "user": ""
    }

    # Set the headers with the secret key
    headers = {
        "Authorization": f"Bearer {secret_key}",
        "Content-Type": "application/json"
    }

    # Send the POST request to the Dify AI API
    response = requests.post(dify_endpoint, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        if "output" in response_data:
            output_text = response_data["output"]["text"]
            st.write("Response:")
            st.write(output_text)

        # Update the conversation ID for maintaining context
        conversation_id = response_data.get("conversation_id", "")
    else:
        st.write("Error occurred while sending the message")

# Streamlit interface
st.title("Dify AI Chat")

# Get user input
user_input = st.text_input("Enter a message")

# Send user input as a message
if st.button("Send"):
    send_message(user_input)
