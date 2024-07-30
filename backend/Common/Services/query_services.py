import os
from nanoid import generate
import ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_ollama import ChatOllama
from typing import Annotated, List, Dict, Any, Optional
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END, START
from langgraph.graph.message import add_messages, AnyMessage
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from Common.Database.database import book_collection
from chromadb.utils import embedding_functions

from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig

os.environ["LANGCHAIN_API_KEY"] = "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"
# os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"

model = OllamaLLM(model="llama3.1", temperature=0)

intent_mapping = {
    "1": "user want to greet",
    "2": "user want to talk about something outside of books topics",
    "3": "user wants book recommendation",
    "4": "user want to add a book",
    "5": "user want to get a summary of a book"
}

class State(TypedDict):
    messages: Annotated[List[Dict[str, Any]], add_messages]
    intent: Optional[str]

workflow = StateGraph(State)
    
def classify_intent(state: State):
    print(state["messages"][-1])
    template = """
    assess the following input and choose which one of the 5 intents that fit the input provided:
    1. user want to greet,
    2. user want to talk about something outside of books topics,
    3. user wants book recommendation,
    4. user want to add a book,
    5. user want to get a summery of a book.
    DON'T SAY ANYTHING JUST PRINT A INTENT NUMBER in the given format.
    user's input: {prompt}
    """
    prompt = PromptTemplate(
        template=template,
        input_variables=["prompt"],
    )
    chain = prompt | model
    print(state["messages"][-1])
    response = chain.invoke({
        'prompt': state["messages"][-1].content,
    })
    print(response)
    print(intent_mapping.get(response))
    state["intent"] = intent_mapping.get(response)
    return state

def chatbot(state: State):
    promptlit = state["messages"][-1].content
    template = """You are an AI assistant called Nerd AI that provide summary of a book the user want.
    always begin your reply with 'erm... Actually' and always have the tone of a nerdy guy that sees himself as highly intellectual person.
    if the user say somwthing outside of books always steer the conversation back to books.
    make your response short and to the point
    user's input/question: {prompt}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        'prompt': promptlit,
    })
    state["messages"].append({"role": "assistant", "content": response})
    return state

def greet(state: State):
    promptlit = state["messages"][-1].content
    template = """You are an AI assistant called Nerd AI that greet bookworms and ask if they want any book suggestions.
    always begin your reply with 'erm... Actually' and always have the tone of a nerdy guy that sees himself as highly intellectual person.
    bookworms input: {prompt}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        'prompt': promptlit,
    })
    state["messages"].append({"role": "assistant", "content": response})
    return state

def summerize_book(state: State):
    promptlit = state["messages"][-1].content
    template = """You are an AI assistant called Nerd AI that provide summary of a book the user want.
    always begin your reply with 'erm... Actually' and always have the tone of a nerdy guy that sees himself as highly intellectual person.
    make it concise and comprahensive.
    user's input: {prompt}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        'prompt': promptlit,
    })
    state["messages"].append({"role": "assistant", "content": response})
    return state

def add_new_book(state: State):
    promptlit = state["messages"][-1].content
    template = """You are an AI That format user's input so it can be entered into the database.
    analyze the user input and organize it in a unified format. [DON'T REPLY TO THE USER JUST PRINT THE FORMAT]
    I want you to follow the format STRICTLY.
    the format is as follows:
    book title: str, catagories: str, subtitle: 'unknown', description: str
    user's input: {prompt}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        'prompt': promptlit,
    })

    print(response)

    default_ef = embedding_functions.DefaultEmbeddingFunction()
    embedding = default_ef([response])

    print(embedding)
    book_collection.add(
        ids=[generate()],
        embeddings=embedding
    )

    # Embedding dimension 384 does not match collection dimensionality 1024

    state["messages"].append({"role": "assistant", "content": "Erm... the book is submitted successfully."})
    return state

def recommend_book(state: State):
    promptlit = state["messages"][-1].content
    template = """You are an AI assistant that generate a list of 10 keywords of a book, 
    based on what genre of books the user wants. [DON'T SAY ANYTHING JUST PRINT THE LIST]
    dont't say: Here is a list of 10 keywords for etc...
    user's input: {prompt}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        'prompt': promptlit,
    })

    table = book_collection.query(
        query_texts=response,
        n_results=5
    )

    templatev2 = """You are an AI assistant called Nerd AI that list 5 books and provide a quick summary of each on of them.
    always begin your reply with 'erm... Actually' and always have the tone of a nerdy guy that sees himself as highly intellectual person.
    make it concise and comprahensive.
    Top 5 list: {list}
    """
    promptv2 = ChatPromptTemplate.from_template(templatev2)
    chain = promptv2 | model
    responsev2 = chain.invoke({
        'list': table,
    })

    state["messages"].append({"role": "assistant", "content": responsev2})
    return state

def decide_next_node(state: State):
    if state["intent"] == "user want to greet":
        return "handle_greeting"
    elif state["intent"] == "user want to add a book":
        return "handle_adding_new_book"
    elif state["intent"] == "user wants book recommendation":
        return "handle_book_recommendation"
    elif state["intent"] == "user want to get a summary of a book":
        return "handle_book_summery"
    else:
        return "handle_talk"

workflow.add_node("classify_intent", classify_intent)
workflow.add_node("chatbot", chatbot)
workflow.add_node("greet", greet)
workflow.add_node("add_new_book", add_new_book)
workflow.add_node("recommend_book", recommend_book)
workflow.add_node("summerize_book", summerize_book)

workflow.add_conditional_edges(
    "classify_intent",
    decide_next_node,
    {
        "handle_greeting": "greet",
        "handle_talk": "chatbot",
        "handle_adding_new_book": "add_new_book",
        "handle_book_recommendation": "recommend_book",
        "handle_book_summery": "summerize_book"
    }
)

workflow.set_entry_point("classify_intent")
workflow.add_edge("greet", END)
workflow.add_edge("add_new_book", END)
workflow.add_edge("recommend_book", END)
workflow.add_edge("summerize_book", END)
workflow.add_edge("chatbot", END)
graph = workflow.compile()

def getResponse(prompt):
    for event in graph.stream({"messages": [{"role": "user", "content": prompt}]}):
        for value in event.values():
            print(value)
            if isinstance(value["messages"][-1], Dict):
                print(value["messages"][-1]["content"])
                return value["messages"][-1]["content"]