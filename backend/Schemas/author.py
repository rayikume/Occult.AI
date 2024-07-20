from pydantic import BaseModel
from typing import Optional

class AuthorSchema(BaseModel):
    author_id: Optional[int] = None
    name: str
    biography: Optional[str] = None