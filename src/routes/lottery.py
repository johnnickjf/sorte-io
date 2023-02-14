from fastapi import APIRouter, Depends, HTTPException, status
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.infra.repositories.lottery_repository import LotteryRepository
from src.application.entities.lottery import Lottery

route = APIRouter()


@route.post('/lottery/{user_id}', status_code=201)
async def create_lottery(lottery: Lottery, user_id: int, db: Session = Depends(get_db)):
    lottery.user = user_id
    lottery = LotteryRepository(db).insert(lottery)
    return lottery


@route.get('/lottery/{user_id}')
async def return_user_lotteries(user_id: int, db: Session = Depends(get_db)):
    lotteries = LotteryRepository(db).select_by_user(user_id)
    if not lotteries:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lotteries not found")
    return lotteries
