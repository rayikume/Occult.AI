from pydantic import BaseModel
from pydantic import Field
from datetime import datetime

class UserSchema(BaseModel):
    username: str
    password: str
    role: str = Field("user", pattern="^(user|admin)$")

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class UserActivitySchema(BaseModel):
    username: str
    activity: str
    timestamp: datetime