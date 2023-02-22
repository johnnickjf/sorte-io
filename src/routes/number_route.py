from fastapi import APIRouter, Depends, HTTPException, status
from src.application.entities.user import User
from src.application.service.login_service import get_current_user
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.application.entities.number import Number
from src.application.service.number_service import NumberService

route = APIRouter()


@route.post('/number', status_code=status.HTTP_201_CREATED, response_model=Number)
async def create_number(number: Number, db: Session = Depends(get_db)):
    return NumberService(db).create_number(number)


@route.get('/number', status_code=status.HTTP_200_OK, response_model=Number)
async def select_number(number_id: str, db: Session = Depends(get_db)):
    return NumberService(db).select_number(number_id)


@route.get('/numbers', status_code=status.HTTP_200_OK, response_model=Number)
async def select_all_numbers(db: Session = Depends(get_db)):
    return NumberService(db).select_all_numbers()


@route.get('/lottery/numbers', status_code=status.HTTP_200_OK, response_model=Number)
async def select_numbers(lottery_id: str, db: Session = Depends(get_db)):
    return NumberService(db).select_lottery_numbers(lottery_id)


@route.put('/user/numbers', status_code=status.HTTP_200_OK, response_model=Number)
async def select_user_numbers(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return NumberService(db).select_user_numbers(user.id)


