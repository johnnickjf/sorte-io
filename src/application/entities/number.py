from pydantic import BaseModel, Field
from datetime import datetime
from src.application.entities.user import User
from src.application.entities.lottery import Lottery


class Number(BaseModel):
    id: str = None
    user: str = Field(...)
    lottery: str = Field(...)
    number: int = Field(..., gt=0)
    created_at: datetime = None

    class Config:
        orm_mode = True
