from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from Common.Database.database import get_db_connection as get_db
from Schemas.book import BookSchema
from Middleware.auth import get_current_user, admin_required
from Middleware.logger import log_user_activity
from Common.Services import bookServices

router = APIRouter()

@router.get("/", response_model=List[BookSchema], tags=["Books"], operation_id="get_books_list")
def get_books(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    log_user_activity(db, current_user['username'], "Searched for all books")
    return bookServices.get_books(db)

# @router.get("/")
# def get_books(db: Session = Depends(get_db)):
#     return bookServices.get_books(db)

@router.get("/{book_id}", response_model=BookSchema, tags=["Books"], operation_id="get_book_by_title")
def get_book(book_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    book = bookServices.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    log_user_activity(db, current_user['username'], f"Searched for book with title: {book['title']}")
    return book

@router.post("/", response_model=BookSchema, tags=["Books"], operation_id="create_book_record")
def create_book(book: BookSchema, db: Session = Depends(get_db), current_user: dict = Depends(admin_required)):
    log_user_activity(db, current_user['username'], "Book creation")
    return bookServices.create_book(db, book)

@router.put("/{book_id}", response_model=BookSchema, tags=["Books"], operation_id="update_book_record")
def update_book(book_id: int, book: BookSchema, db: Session = Depends(get_db), current_user: dict = Depends(admin_required)):
    log_user_activity(db, current_user['username'], "Book update")
    return bookServices.update_book(db, book_id, book)

@router.delete("/{book_id}", tags=["Books"])
def delete_book(book_id: int, db: Session = Depends(get_db), current_user: dict = Depends(admin_required)):
    log_user_activity(db, current_user['username'], "Book deletion")
    return bookServices.delete_book(db, book_id)

@router.get("/recommendations", response_model=List[BookSchema], tags=["Recommendations"])
def get_recommended_books_route(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        return bookServices.get_recommended_books(db, current_user["username"])
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))