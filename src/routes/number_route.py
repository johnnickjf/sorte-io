from fastapi import APIRouter, Depends, status
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.application.entities.number import Number
from src.application.service.number_service import NumberService

route = APIRouter()


# @route.post('/number', status_code=status.HTTP_201_CREATED, response_model=Number)
# async def create_number(number: CreateNumber, db: Session = Depends(get_db)):
#     return NumberService(db).create_number(number)


@route.get('/number', status_code=status.HTTP_200_OK, response_model=Number)
async def select_number(number_id: str, db: Session = Depends(get_db)):
    return NumberService(db).select_number(number_id)


@route.get('/numbers', status_code=status.HTTP_200_OK, response_model=list[Number])
async def select_last_numbers(db: Session = Depends(get_db)):
    return NumberService(db).select_last_numbers()


@route.get('/lottery_numbers', status_code=status.HTTP_200_OK, response_model=list[Number])
async def select_numbers(lottery_id: str, db: Session = Depends(get_db)):
    return NumberService(db).select_lottery_numbers(lottery_id)


@route.get('/user_numbers', status_code=status.HTTP_200_OK, response_model=list[Number])
async def select_user_numbers(user_id: str, db: Session = Depends(get_db)):
    return NumberService(db).select_user_numbers(user_id)
