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
    else:
        with st.chat_message(message["role"], avatar="🐤"):
            st.markdown(message["content"])

promptlit = st.chat_input("Enter your prompt here")

if promptlit:
    with st.chat_message("user", avatar="🐤"):
        st.markdown(promptlit)
    st.session_state.messages.append({"role": "user", "content": promptlit})
    textlist += promptlit

    longtext = "".join(textlist)
    template = "Remember this convo: {history} Answer this Question: {question}"
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({'history': {longtext}, 'question': f"{promptlit}"})
    print(textlist)
    print(st.session_state.messages)

    with st.chat_message("assistant", avatar="🤓"):
        st.markdown(response)
        textlist += response
    st.session_state.messages.append({"role": "assistant", "content": response})