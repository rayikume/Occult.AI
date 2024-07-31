from fastapi import FastAPI
from Routes import query, users, authors, books

app = FastAPI()

app.include_router(query.router, prefix="/query")
app.include_router(users.router, prefix="/users")
app.include_router(authors.router, prefix="/authors")
app.include_router(books.router, prefix="/books")

@app.get("/")
def root():
    return {"Message": "Welcome to Occult.AI"}