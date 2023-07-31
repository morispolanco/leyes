import streamlit as st
import socketio

# Set up the Dify AI API endpoint and secret key
dify_endpoint = "https://api.dify.ai/v1/chat-messages"
secret_key = "app-OZw6qix4wsjQl4MUTmlpEukZ"


# Global variables
conversation_id = ""
response_received = False

def on_message(data):
    global response_received
    if "output" in data:
        output_text = data["output"]["text"]
        st.write("Response:")
        st.write(output_text)
        response_received = True

def send_message(text):
    global conversation_id, response_received
    response_received = False

    # Set up the SocketIO connection
    sio = socketio.Client()

    @sio.on("message")
    def handle_message(data):
        on_message(data)

    # Connect to the SocketIO server
    sio.connect(dify_endpoint, headers={"Authorization": f"Bearer {secret_key}"})

    # Send the message payload
    payload = {
        "inputs": {"text": text},
        "query": "eh",
        "response_mode": "streaming",
        "conversation_id": conversation_id,
        "user": ""
    }
    sio.emit("message", payload)

    # Wait for response
    while not response_received:
        sio.sleep(0.1)

    # Disconnect from the SocketIO server
    sio.disconnect()

# Streamlit interface
st.title("Dify AI Chat")

# Get user input
user_input = st.text_input("Enter a message")

# Send user input as a message
if st.button("Send"):
    send_message(user_input)
