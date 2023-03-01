from pydantic import BaseModel, Field
from datetime import datetime


class Number(BaseModel):
    id: str = None
    user: str
    lottery: str
    number: int = Field(gt=0)
    created_at: datetime = None

    class Config:
        orm_mode = True


class CreateNumber(BaseModel):
    user: str
    lottery: str

    class Config:
        orm_mode = True
