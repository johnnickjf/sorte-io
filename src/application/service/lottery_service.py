from src.application.entities.lottery import Lottery
from src.infra.repositories.lottery_repository import LotteryRepository
from sqlalchemy.orm import Session


def create(lottery: Lottery, user_id: int, db: Session):
    lottery.user = user_id
    lottery = LotteryRepository(db).insert(lottery)
    return lottery


def user_lotteries(user_id: int, db: Session):
    lotteries = LotteryRepository(db).select_by_user(user_id)
    if lotteries:
        return lotteries
    raise "Lotteries not found"
