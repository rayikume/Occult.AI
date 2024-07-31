from fastapi import APIRouter
import ollama
from nanoid import generate
from Common.Database.vectordb import book_collection
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from Common.Services.query_services import getResponse
import numpy as np
import chromadb
from chromadb.config import Settings
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

router = APIRouter()
model = OllamaLLM(model="llama3.1")

@router.post("/")
def handle_query(prompt):
    response = getResponse(prompt)
    return response