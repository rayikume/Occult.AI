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

model = OllamaLLM(model="mistral")
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

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

if promptlit:
    with st.chat_message("user", avatar="🐤"):
        st.markdown(promptlit)
        filtered_text = preprocess_text(promptlit)
    st.session_state.messages.append({"role": "user", "content": promptlit})

    db = book_collection.query(
        query_texts=filtered_text,
        n_results=5
    )
    longtext = " ".join(textlist)
    template = """You're an AI assistance named Nerd AI that suggust books for users, 
    you can also conversate with the user but always steer the conversation back to book recommendation,
    the question of the user: {question}
    Suggust only the books in this database: {database}
    to remember the conversation with the user, here's all the interaction you've had with the user: {history}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        'database': db.get("documents"),
        'question': promptlit,
        'history': longtext
    })

    with st.chat_message("assistant", avatar="🤓"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})