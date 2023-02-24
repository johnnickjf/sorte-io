from fastapi import APIRouter, Depends, HTTPException, status
from src.application.entities.user import User
from src.application.service.login_service import get_current_user
from src.application.service.user_service import UserService
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.application.entities.lottery import Lottery, CreateLottery
from src.application.service.lottery_service import LotteryService

route = APIRouter()


@route.post('/lottery/', status_code=status.HTTP_201_CREATED)
async def create_lottery(lottery: CreateLottery, current_user: User = Depends(get_current_user),
                         db: Session = Depends(get_db)):
    return LotteryService(db).create_lottery(lottery, current_user)


@route.get('/lottery/', status_code=status.HTTP_200_OK)
async def select_lottery(lottery_id: str, db: Session = Depends(get_db)):
    return LotteryService(db).select_lottery(lottery_id)


@route.get('/lotteries/', status_code=status.HTTP_200_OK)
async def select_user_lotteries(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return LotteryService(db).select_user_lotteries(current_user)


@route.get('/lotteries', status_code=status.HTTP_200_OK)
async def select_all_lotteries(db: Session = Depends(get_db)):
    return LotteryService(db).select_all_lotteries()


@route.put('/lottery', status_code=status.HTTP_200_OK)
async def update_lottery(lottery_updated: Lottery, current_user: User = Depends(get_current_user),
                         db: Session = Depends(get_db)):
    return LotteryService(db).update_lottery(lottery_updated, current_user)


@route.delete('/lottery/', status_code=status.HTTP_200_OK)  # incorrect
async def delete_lottery(lottery_id: str, db: Session = Depends(get_db)):
    return LotteryService(db).delete_lottery(lottery_id)
