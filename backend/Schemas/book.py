from pydantic import BaseModel
from typing import Optional

class BookSchema(BaseModel):
    book_id: Optional[int] = None
    title: str
    subtitle: Optional[str]
    author: str
    author_id: Optional[int] = None
    genre: Optional[str]
    thumbnail: Optional[str]
    description: Optional[str]
    published_year: Optional[str]
    average_rating: Optional[str]