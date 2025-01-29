import streamlit as st
import pandas as pd
import numpy as np
import random
import time
import requests
import json
from streamlit.components.v1 import html

st.title('Ashish Chatbot')
st.header("Use this chatbot to know more about Ashish",divider="gray" )
st.write('This is a chatbot that can answer questions about Ashish. Ask a question and the chatbot will respond with an answer related to Ashish.')


def clear_history():
    st.session_state.clear()
# Sidebar with additional information
with st.sidebar:
    st.title("Settings ⚙️")
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    st.selectbox("Choose Model", ["GPT-4", "Gemini", "DeepSeek"])
    st.slider("Creativity Level", 0.0, 1.0, 0.7)
    st.button("Clear History", clear_history())
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
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"], unsafe_allow_html=True)

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            user_message = f'<div class="user-message">👤 {prompt}</div>'
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner('Thinking...'):
        # Display assistant response in chat message container
            with st.chat_message("assistant"):
                response = response_generator(prompt)
                text = ''.join(byte_string.decode('utf-8') for byte_string in response)
                response = st.write(text)
                bot_message = f'<div class="bot-message">🤖 {text}</div>'
            # Add assistant response to chat history
            print("--",text)
            st.session_state.messages.append({"role": "assistant", "content": text})
            
    st.markdown('</div>', unsafe_allow_html=True)
# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    Powered by Streamlit | Made with ❤️ by Ashish
</div>
""", unsafe_allow_html=True)
