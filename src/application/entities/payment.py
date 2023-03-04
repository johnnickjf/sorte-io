from pydantic import BaseModel, Field
from datetime import datetime


class Payment(BaseModel):
    id: str = None
    user: str
    lottery: str
    price: float = Field(gt=-1)
    qtd: int = Field(gt=0)
    status: int = 0
    payment_date: datetime = None

    class Config:
        orm_mode = True


class UpdatePayment(BaseModel):
    id: str = None
    status: int = Field(0, ge=0, le=2)

    class Config:
        orm_mode = True


class CreatePayment(BaseModel):
    user: str
    lottery: str
    qtd: int = Field(gt=0)

    class Config:
        orm_mode = True
