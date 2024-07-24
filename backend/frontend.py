import re
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
from Common.Database.database import book_collection
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from Routes.query import handle_query

model = OllamaLLM(model="llama3")
textlist = []

# Chatbox
st.title("Nerd AI ☝️🤓")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message["role"] == "assistant":
        with st.chat_message(message["role"], avatar="🤓"):
            st.markdown(message["content"])
            textlist.append(message["content"])
    else:
        with st.chat_message(message["role"], avatar="🐤"):
            st.markdown(message["content"])
            textlist.append(message["content"])

promptlit = st.chat_input("Enter your prompt here")

if promptlit:
    with st.chat_message("user", avatar="🐤"):
        st.markdown(promptlit)
    st.session_state.messages.append({"role": "user", "content": promptlit})

    longtext = " ".join(textlist)
    response = handle_query(promptlit)

    with st.chat_message("assistant", avatar="🤓"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})