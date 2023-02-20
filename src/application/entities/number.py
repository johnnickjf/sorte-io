from pydantic import BaseModel, Field
from datetime import datetime


class Number(BaseModel):
    id: str = None
    user: str = Field(...)
    lottery: str = Field(...)
    number: int = Field(..., gt=0)
    sorted: bool = Field(False)
    status: int = Field(0, ge=0, le=2)
    created_at: datetime = None

    class Config:
        orm_mode = True
