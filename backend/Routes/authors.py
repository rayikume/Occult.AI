from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from Common.Database.database import get_db_connection as get_db
from Schemas.author import AuthorSchema
from Middleware.security import get_current_user, admin_required
from Common.Services.author_services import get_authors, get_author_by_id, create_author, update_author, delete_author

router = APIRouter()

@router.get("/", response_model=List[AuthorSchema], tags=["Authors"], operation_id="get_authors_list")
def get_authors_route(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return get_authors(db)

@router.get("/{author_id}", response_model=AuthorSchema, tags=["Authors"], operation_id="get_author_by_id")
def get_author_route(author_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    author = get_author_by_id(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.post("/", response_model=AuthorSchema, tags=["Authors"], operation_id="create_author_record")
def create_author_route(author: AuthorSchema, db: Session = Depends(get_db), current_user: dict = Depends(admin_required)):
    return create_author(db, author)

@router.put("/{author_id}", response_model=AuthorSchema, tags=["Authors"], operation_id="update_author_record")
def update_author_route(author_id: int, author: AuthorSchema, db: Session = Depends(get_db), current_user: dict = Depends(admin_required)):
    try:
        return update_author(db, author_id, author)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{author_id}", tags=["Authors"], operation_id="delete_author_record")
def delete_author_route(author_id: int, db: Session = Depends(get_db), current_user: dict = Depends(admin_required)):
    try:
        delete_author(db, author_id)
        return {"message": "Author deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))