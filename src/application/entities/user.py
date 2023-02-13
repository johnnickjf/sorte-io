from pydantic import BaseModel, EmailStr, Field
from pydantic.dataclasses import dataclass
from datetime import datetime


class User(BaseModel):
    id: int = None
    name: str
    email: EmailStr
    password: str
    telephone: str
    created_at: datetime = None

    class Config:
        orm_mode = True
