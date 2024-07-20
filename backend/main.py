from fastapi import FastAPI
from Routes import users, books, authors
from Common.Database.models import Base
from Common.Database.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(books.router)
app.include_router(authors.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Simple User API"}

@app.get("/healthcheck")
def health_check():
        return {"message": "API is running"}