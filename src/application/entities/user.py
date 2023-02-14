from pydantic import EmailStr, Field, BaseModel
from datetime import datetime


class User(BaseModel):
    id: int = None
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(None, min_length=8)
    telephone: str = Field(..., min_length=8)
    created_at: datetime = None

    class Config:
        orm_mode = True

