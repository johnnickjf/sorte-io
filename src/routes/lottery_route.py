from fastapi import APIRouter, Depends, HTTPException, status
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.infra.repositories.lottery_repository import LotteryRepository
from src.application.entities.lottery import Lottery

route = APIRouter()


@route.post('/create/lottery/{user_id}', status_code=status.HTTP_201_CREATED)
async def create_lottery(lottery: Lottery, user_id: int, db: Session = Depends(get_db)):
    lottery.user = user_id
    lottery = LotteryRepository(db).insert(lottery)
    if not lottery:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Lottery already exists")
    return lottery


@route.get('/lottery/{lottery_id}')
async def return_user_lottery(lottery_id: int, db: Session = Depends(get_db)):
    lottery = LotteryRepository(db).select(lottery_id)
    if not lottery:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lottery not found")
    return lottery


@route.get('/user/lotteries/{user_id}')
async def return_user_lotteries(user_id: int, db: Session = Depends(get_db)):
    lotteries = LotteryRepository(db).select_by_user(user_id)
    if not lotteries:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lotteries not found")
    return lotteries


@route.get('/all/lottery')
async def return_all_lotteries(db: Session = Depends(get_db)):
    lotteries = LotteryRepository(db).select_all()
    if not lotteries:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lotteries not found")
    return lotteries


@route.put('/update/lottery')
async def update_lottery(lottery_updated: Lottery, db: Session = Depends(get_db)):
    lottery_updated = LotteryRepository(db).update(lottery_updated)
    if not lottery_updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lottery not found")
    return lottery_updated


@route.delete('/delete/lottery/{lottery_id}')
async def delete_lottery(lottery_id: int, db: Session = Depends(get_db)):
    lottery = LotteryRepository(db).delete(lottery_id)
    if not lottery:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lottery not found")
    return lottery
