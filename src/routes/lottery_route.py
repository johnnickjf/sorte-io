from fastapi import APIRouter, Depends, status
from src.application.entities.user import User
from src.application.service.login_service import get_current_user
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.application.entities.lottery import Lottery, CreateLottery, UpdateLottery, SimpleLottery
from src.application.service.lottery_service import LotteryService

route = APIRouter()


@route.post('/lottery/', status_code=status.HTTP_201_CREATED, response_model=SimpleLottery)
async def create_lottery(lottery: CreateLottery, current_user: User = Depends(get_current_user),
                         db: Session = Depends(get_db)):
    return LotteryService(db).create_lottery(lottery, current_user)


@route.get('/lottery/', status_code=status.HTTP_200_OK, response_model=Lottery)
async def select_lottery(lottery_id: str, db: Session = Depends(get_db)):
    return LotteryService(db).select_lottery_with_user(lottery_id)


@route.get('/lotteries/', status_code=status.HTTP_200_OK, response_model=list[SimpleLottery])
async def select_user_lotteries(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return LotteryService(db).select_user_lotteries(current_user)


@route.get('/lotteries', status_code=status.HTTP_200_OK, response_model=list[SimpleLottery])
async def select_all_lotteries(db: Session = Depends(get_db)):
    return LotteryService(db).select_all_lotteries()


@route.put('/lottery', status_code=status.HTTP_200_OK, response_model=SimpleLottery)
async def update_lottery(lottery_updated: UpdateLottery, current_user: User = Depends(get_current_user),
                         db: Session = Depends(get_db)):
    return LotteryService(db).update_lottery(lottery_updated, current_user)


# @route.delete('/lottery/', status_code=status.HTTP_200_OK)
# async def delete_lottery(lottery_id: str, db: Session = Depends(get_db)):
#     return LotteryService(db).delete_lottery(lottery_id)
