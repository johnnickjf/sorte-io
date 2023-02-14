from pydantic import EmailStr, Field, BaseModel
from datetime import datetime


class User(BaseModel):
    id: int = None
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(...)
    telephone: str = Field(..., min_length=8)
    created_at: datetime = None

    class Config:
        orm_mode = True


class UserCreate(User):
    password: str = Field(..., min_length=8)
