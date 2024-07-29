from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
import csv
import nanoid
from Routes import users, books, authors
from sqlalchemy.orm import Session
from Common.Database.models import Base, Book
from Common.Database.database import engine, get_db_connection
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5173",
    "http://localhost:5173"
    # add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(books.router)
app.include_router(authors.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Simple User API"}

@app.get("/healthcheck")
def health_check():
        return {"message": "API is running"}

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db_connection)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")

    # Read and parse the CSV file
    content = await file.read()
    reader = csv.DictReader(content.decode('utf-8').splitlines())

    books = []
    for row in reader:
        book = Book(
            title=row['title'],
            genre=row["categories"],
            description=["description"],
            thumbnail=row['thumbnail'],
        )
        books.append(book)

    # Insert the books into the database
    db.add_all(books)
    db.commit()

    return {"status": "success", "message": f"{len(books)} books have been added to the database"}