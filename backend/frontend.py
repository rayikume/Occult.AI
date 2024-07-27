import logging
import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_ollama import ChatOllama
from Routes.query import handle_greet
from typing import Annotated, List, Dict, Any, Optional
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

os.environ["LANGSMITH_API_KEY"] = "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"
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "LangGraph Tutorial"

if "messages" not in st.session_state:
    st.session_state.messages = []

class State(TypedDict):
    messages: Annotated[List[Dict[str, Any]], add_messages]
    intent: Optional[str]

graph_builder = StateGraph(State)

llmG = ChatOllama(model="llama3", temperature=0)
model = OllamaLLM(model="llama3", temperature=0)

def classify_intent(state: State):
    template = """
    input: {prompt}
    assess the following input and choose which one of the 4 categories that fit the input provided:
    categories:
    1. user want to greet or talk,
    2. user wants book recommendation,
    3. user want to add a book,
    4. user want to get a summery of a book.
    DON'T SAY ANYTHING JUST PRINT A CATEGORY EXACTLY LIKE PROVIDED [DON'T INCLUDE THE NUMBER].
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        'prompt': state["messages"][-1].content,
    })

    state["intent"] = response
    print(response)

    return state

def chatbot(state: State):
    state["messages"].append({"role": "assistant", "content": "OK"})
    return state

def greet(state: State):
    prompt = state["messages"][-1]
    print(f"Greet prompt: {prompt}")
    response = handle_greet(prompt)
    print(f"Greet response: {response}")
    state["messages"].append({"role": "assistant", "content": response})
    return state

# def add_new_book(state: State):
#     response = "Sure!"
#     state["messages"].append({"role": "assistant", "content": response})
#     return {"messages": state["messages"]}

# def recommend_book(state: State):
#     response = "Can you tell me what genre you're interested in?"
#     state["messages"].append({"role": "assistant", "content": response})
#     return {"messages": state["messages"]}

# def small_talk(state: State):
#     response = "Sure, let's chat! How's your day going?"
#     state["messages"].append({"role": "assistant", "content": response})
#     return {"messages": state["messages"]}

# Add nodes to the graph
graph_builder.add_node("classify_intent", classify_intent)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("greet", greet)

def decide_next_node(state: State):
    if state["intent"] == "user want to greet" or state["intent"] == "user want to greet or talk":
        return "handle_greeting"
    else:
        return "handle_talk"

graph_builder.add_conditional_edges(
    "classify_intent",
    decide_next_node,
    {
        "handle_greeting": "greet",
        "handle_talk": "chatbot"
    }
)


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

    graph_builder.set_entry_point("classify_intent")
    graph_builder.add_edge("greet", END)
    graph_builder.add_edge("chatbot", END)
    graph = graph_builder.compile()

    # /query
    # response = handle_query(promptlit)

    for event in graph.stream({"messages": [{"role": "user", "content": promptlit}]}):
        for value in event.values():
            with st.chat_message("assistant", avatar="🤓"):
                # Assuming `value` is a list of HumanMessage
                for msg in value["messages"]:
                    print(msg)  # This will display the HumanMessage object
                    st.markdown(msg)  # Access the content attribute of the HumanMessage object
            
            # Append the content of the latest message
            if value["messages"]:
                st.session_state.messages.append({"role": "assistant", "content": value["messages"][-1]})
