from fastapi import APIRouter
import ollama
from nanoid import generate
from pydantic import BaseModel
from Common.Database.vectordb import book_collection
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from Common.Services.queryServices import getResponse
import numpy as np
import chromadb
from chromadb.config import Settings
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

router = APIRouter()
model = OllamaLLM(model="llama3.1")

class Query(BaseModel):
    prompt: str

@router.post("/")
def handle_query(query: Query):
    response = getResponse(query.prompt)
    return response