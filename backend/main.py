from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
import csv
import nanoid
from Routes import users, books, authors, query
from sqlalchemy.orm import Session
from Common.Database.models import Author, Base, Book
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

app.include_router(query.router, prefix="/query")
app.include_router(users.router, prefix="/users")
app.include_router(authors.router, prefix="/authors")
app.include_router(books.router, prefix="/books")

@app.get("/")
def root():
    return {"Message": "Welcome to Occult.AI"}

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db_connection)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")

    # Read and parse the CSV file
    content = await file.read()
    reader = csv.DictReader(content.decode('utf-8').splitlines())

    # authors = []
    # for row in reader:
    #     author = Author(
    #         name = row['authors'],
    #         biography = "unknown",
    #     )
    #     authors.append(author)

    # db.add_all(authors)
    # db.commit()

    books = []
    for row in reader:
        book = Book(
            title = row['title'],
            subtitle = row['subtitle'],
            author = row['authors'],
            genre = row["categories"],
            thumbnail = row['thumbnail'],
            description = row["description"],
            published_year = row["published_year"],
            average_rating = row["average_rating"]
        )
        books.append(book)

    # Insert the books into the database
    db.add_all(books)
    db.commit()


    return {"status": "success", "message": f"{len(books)} books and authors have been added to the database"}