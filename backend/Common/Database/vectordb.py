import pandas as pd
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_text_splitters import CharacterTextSplitter
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
import chromadb
import time

# VECTOR DATABASE
# start = time.time()

chroma_client = chromadb.PersistentClient(path="/Users/aalbusayla001/Desktop/July2024 Projects/Occult_AI/backend/Chroma_db")
book_collection = chroma_client.get_or_create_collection(name="Book_Collection")
# dataset = []

# df = pd.read_csv('books.csv')
# df = df.loc[6001:6800]
# books_df_cleaned = df.copy()
# print(df)
# categorical = ['authors', 'subtitle', 'categories', 'thumbnail', 'description']
# numerical = ['published_year', 'average_rating', 'num_pages', 'ratings_count']

# for column in categorical:
#     books_df_cleaned.fillna({f'{column}': 'unknown'}, inplace=True)

# for column in numerical:
#     books_df_cleaned.fillna({f'{column}': -1}, inplace=True)

# def getBooks(row):
#     text = f"title: {row['title']}, subtitle: {row['subtitle']}, authors: {row['authors']}, catagories: {row['categories']}, thumbnail: {row['thumbnail']}, description: {row['description']}, published_year: {row['published_year']}, average_rating: {row['average_rating']}"
#     dataset.append(text)

# books_df_cleaned.apply(getBooks, axis=1)

# ids1 = books_df_cleaned["isbn10"].to_list()

# book_collection.upsert(
#     documents=dataset,
#     ids=ids1
# )

# print(time.time() - start)