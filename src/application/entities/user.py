from pydantic import EmailStr, Field, BaseModel
from datetime import datetime
from uuid import UUID


class User(BaseModel):
    id: str = None
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(...)
    telephone: str = Field(..., min_length=8)
    created_at: datetime = None

    class Config:
        orm_mode = True


class UserCreate(User):
    password: str = Field(..., min_length=8)
