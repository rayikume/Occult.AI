from fastapi import FastAPI
from Routes import query

app = FastAPI()

app.include_router(query.router, prefix="/query")

@app.get("/")
def root():
    return {"Message": "Welcome to Nerd AI"}