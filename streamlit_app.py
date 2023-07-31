import streamlit as st
import websocket
import json

# Set up the Dify AI API endpoint and secret key
dify_endpoint = "https://api.dify.ai/v1/chat-messages"
secret_key = "app-OZw6qix4wsjQl4MUTmlpEukZ"


# Global variables
conversation_id = ""
response_received = False

def on_message(ws, message):
    global response_received
    response_data = json.loads(message)
    if "output" in response_data:
        output_text = response_data["output"]["text"]
        st.write("Response:")
        st.write(output_text)
        response_received = True

def send_message(text):
    global conversation_id, response_received
    response_received = False

    # Create a JSON payload with the input text and other metadata
    payload = {
        "inputs": {"text": text},
        "query": "eh",
        "response_mode": "streaming",
        "conversation_id": conversation_id,
        "user": ""
    }

    # Set up the WebSocket connection
    ws = websocket.WebSocketApp(
        dify_endpoint,
        on_message=on_message,
        header={"Authorization": f"Bearer {secret_key}"}
    )

    # Send the payload as a message
    ws.send(json.dumps(payload))

    # Wait for response
    while not response_received:
        ws.run_forever()

    # Close the WebSocket connection
    ws.close()

# Streamlit interface
st.title("Dify AI Chat")

# Get user input
user_input = st.text_input("Enter a message")

# Send user input as a message
if st.button("Send"):
    send_message(user_input)
