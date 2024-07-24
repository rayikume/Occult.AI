import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

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
    template = """You're Nerd AI, always begine your reply with 'well actuaklly'.
    Make your tone sounds nerdy and thinking highly of yourself. 
    Your job is to help the user by answering his/her questions. 
    Answer this Question: {question}.
    The conversation history between you and the user (DON'T MENTION CONVO HISTORY TO THE USER): {history}"""
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({'history': {longtext}, 'question': f"{promptlit}"})

    with st.chat_message("assistant", avatar="🤓"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})