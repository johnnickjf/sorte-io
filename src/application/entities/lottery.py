from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal


class Lottery(BaseModel):
    id: str = None
    user: str = None
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=500)
    max_number: int = Field(10, gt=9, error_msg='O valor mínimo permitido para o campo de numeros é 10')
    price: Decimal = Field(Decimal(0.0), gt=-1)
    status: int = Field(0, ge=0, le=2)
    winner: str = None
    start_date: datetime = None
    end_date: datetime = None
    created_at: datetime = None

    class Config:
        orm_mode = True
