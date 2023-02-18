from fastapi import APIRouter, Depends, HTTPException, status
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.application.entities.lottery import Lottery
from src.application.service.lottery_service import LotteryService

route = APIRouter()


@route.post('/lottery/{user_id}', status_code=status.HTTP_201_CREATED)
async def create_lottery(lottery: Lottery, user_id: str, db: Session = Depends(get_db)):
    return LotteryService(db).create_lottery(lottery, user_id)


@route.get('/lottery/{lottery_id}', status_code=status.HTTP_200_OK)
async def select_lottery(lottery_id: str, db: Session = Depends(get_db)):
    return LotteryService(db).select_lottery(lottery_id)


@route.get('/lotteries/{user_id}', status_code=status.HTTP_200_OK)
async def select_user_lotteries(user_id: str, db: Session = Depends(get_db)):
    return LotteryService(db).select_user_lotteries(user_id)


@route.get('/lotteries', status_code=status.HTTP_200_OK)
async def select_all_lotteries(db: Session = Depends(get_db)):
    return LotteryService(db).select_all_lotteries()


@route.put('/lottery', status_code=status.HTTP_200_OK)
async def update_lottery(lottery_updated: Lottery, db: Session = Depends(get_db)):
    return LotteryService(db).update_lottery(lottery_updated)


@route.delete('/lottery/{lottery_id}', status_code=status.HTTP_200_OK)
async def delete_lottery(lottery_id: str, db: Session = Depends(get_db)):
    return LotteryService(db).delete_lottery(lottery_id)
