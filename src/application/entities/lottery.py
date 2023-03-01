from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from src.application.entities.number import Number
from src.application.entities.user import User


class Lottery(BaseModel):
    id: str = None
    user: User = None
    name: str = Field(max_length=100)
    description: str = Field(min_length=30, max_length=500)
    price: Decimal = Field(Decimal(0.0), gt=-1)
    status: int = Field(0, ge=0, le=2)
    qtd: int = None
    winner: Number = None
    start_date: datetime = None
    end_date: datetime = None
    created_at: datetime = None

    class Config:
        orm_mode = True


class CreateLottery(BaseModel):
    id: str = None
    user: User = None
    name: str = Field(max_length=100)
    description: str = Field(min_length=30, max_length=500)
    price: Decimal = Field(Decimal(0.0), gt=-1)
    qtd: int = None
    start_date: datetime = None
    end_date: datetime = None

    class Config:
        orm_mode = True


class UpdateLottery(BaseModel):
    id: str = None
    name: str = Field(max_length=100)
    description: str = Field(min_length=30, max_length=500)
    price: Decimal = Field(Decimal(0.0), gt=-1)
    status: int = Field(0, ge=0, le=2)
    qtd: int = None
    start_date: datetime = None
    end_date: datetime = None
    winner: str = None

    class Config:
        orm_mode = True
