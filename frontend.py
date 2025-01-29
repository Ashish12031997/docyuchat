import streamlit as st
import pandas as pd
import numpy as np
import random
import time
import requests
import json
st.title('Ashish Chatbot')

st.write('This is a chatbot that can answer questions about Ashish. Ask a question and the chatbot will respond with an answer related to Ashish.')
# Streamed response emulator
def response_generator(prompt):
    stream_url = 'http://localhost:8000/embeddings/ask'
    body = {"question": prompt}
    with requests.post(stream_url,json=body,stream=True) as response:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                yield chunk
                time.sleep(1)
        
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
