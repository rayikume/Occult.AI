from fastapi import APIRouter
import ollama
from nanoid import generate
from Common.Database.database import book_collection
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import numpy as np
import chromadb
from chromadb.config import Settings
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

router = APIRouter()
model = OllamaLLM(model="llama3")

@router.get("/greet")
def handle_greet(promptlit):

    template = """You are an AI assistant called Nerd AI that greet bookworms and ask if they want any book suggestions.
    always begin your reply with 'erm... Actually' and always have the tone of a nerdy guy that sees himself as highly intellectual person.
    bookworms input: {prompt}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        'prompt': promptlit,
    })

    return response

@router.get("/addbook")
def handle_adding_new_book(promptlit):
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

    prompt_db = ollama.embeddings(model="mxbai-embed-large", prompt=response)
    embedding = prompt_db["embedding"]
    book_collection.add(
        ids=[generate()],
        embeddings=[embedding]
    )

    return "Erm... the book is submitted successfully."

@router.get("/recommendation")
def handle_book_recommendation(promptlit):
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

    # Embedding dimension 384 does not match collection dimensionality 1024

    return table

@router.get("/summerization")
def handle_book_summerization(promptlit):
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

    return response