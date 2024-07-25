import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_ollama import ChatOllama
from Routes.query import handle_query
from typing import Annotated, List, Dict, Any
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from IPython.display import Image, display

os.environ["LANGSMITH_API_KEY"] = "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"
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "LangGraph Tutorial"

if "messages" not in st.session_state:
    st.session_state.messages = []

class State(TypedDict):
    messages: Annotated[List[Dict[str, Any]], add_messages]
    intent: str

graph_builder = StateGraph(State)

llmG = ChatOllama(model="llama3", temperature=0)
model = OllamaLLM(model="llama3")

def recognize_intent(user_input: str) -> str:
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "greet"
    elif "book" in user_input or "recommend" in user_input:
        return "recommend_book"
    else:
        return "small_talk"

def chatbot(state: State):
    intent = recognize_intent(state["messages"][-1].content)
    state["intent"] = intent
    if intent == "greet":
        return greet(state)
    elif intent == "recommend_book":
        return recommend_book(state)
    else:
        return small_talk(state)

def greet(state: State):
    response = "AAAAAAAA"
    state["messages"] = list(state["messages"])
    state["messages"].append(response)
    return {"messages": state["messages"]}

def add_new_book(state: State):
    response = "Sure!"
    state["messages"] = list(state["messages"])
    state["messages"].append(response)
    return {"messages": state["messages"]}

def recommend_book(state: State):
    response = "Can you tell me what genre you're interested in?"
    state["messages"] = list(state["messages"])
    state["messages"].append(response)
    return {"messages": state["messages"]}

def small_talk(state: State):
    response = "Sure, let's chat! How's your day going?"
    state["messages"] = list(state["messages"])
    state["messages"].append(response)
    return {"messages": state["messages"]}

# Add nodes to the graph
graph_builder.add_node("greet", greet)
graph_builder.add_node("recommend_book", recommend_book)
graph_builder.add_node("small_talk", small_talk)
graph_builder.add_node("add_new_book", add_new_book)
graph_builder.add_node("chatbot", chatbot)

textlist = []

# Chatbox
st.title("Nerd AI ☝️🤓")

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

    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge(START, "greet")
    graph_builder.add_edge(START, "recommend_book")
    graph_builder.add_edge(START, "small_talk")
    graph_builder.add_edge(START, "add_new_book")
    graph_builder.add_edge("greet", END)
    graph_builder.add_edge("recommend_book", END)
    graph_builder.add_edge("small_talk", END)
    graph_builder.add_edge("chatbot", END)
    graph_builder.add_edge("add_new_book", END)
    graph = graph_builder.compile()

    # /query
    # response = handle_query(promptlit)

    for event in graph.stream({"messages": ("user", promptlit)}):
        for value in event.values():
            with st.chat_message("assistant", avatar="🤓"):
                st.markdown(value["messages"][-1])
            st.session_state.messages.append({"role": "assistant", "content": value["messages"][-1]})