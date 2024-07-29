from pydantic import BaseModel
from typing import Optional

class BookSchema(BaseModel):
    book_id: Optional[int] = None
    title: str
    genre: Optional[str] = None
    description: Optional[str] = None
    thumbnail: Optional[str] = None

# class BookSchemaGET(BaseModel):
#     title: str
#     genre: Optional[str] = None
#     description: Optional[str] = None
#     thumbnail: Optional[str] = None