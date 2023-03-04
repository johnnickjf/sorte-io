from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.application.entities.user import User
from src.infra.repositories.lottery_repository import LotteryRepository
from src.application.entities.lottery import Lottery, CreateLottery, UpdateLottery
from src.application.service.user_service import UserService


class LotteryService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = LotteryRepository(db)

    def create_lottery(self, lottery: CreateLottery, user: User) -> Lottery:
        lottery.user = user.id
        return self.repository.insert(lottery)

    def select_lottery(self, lottery_id: str) -> Lottery:
        lottery = self.repository.select_by_id(lottery_id)
        if not lottery:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lottery not found")
        return lottery

    def select_lottery_with_user(self, lottery_id: str) -> Lottery:
        lottery = self.select_lottery(lottery_id)
        lottery.user = UserService(self.db).select_user(lottery.user)
        if lottery.winner:
            winner = UserService(self.db).select_user(lottery.winner)
            lottery.winner = winner
        return lottery

    def verify_existing_lottery(self, lottery_id: str) -> bool:
        lottery = self.repository.select_by_id(lottery_id)
        if not lottery:
            return False
        return True

    def select_user_lotteries(self, user: User) -> list[Lottery]:
        lotteries = self.repository.select_by_user(user.id)
        if not lotteries:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lotteries not found")
        return lotteries

    def select_all_lotteries(self) -> list[Lottery]:
        lotteries = self.repository.select_all()
        if not lotteries:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lotteries not found")
        return lotteries

    def update_lottery(self, lottery_updated: UpdateLottery, user: User) -> Lottery:
        existing_lottery = self.repository.select_by_id(lottery_updated.id)
        if not existing_lottery or existing_lottery.user != user.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Lottery not found")
        return self.repository.update(lottery_updated)

    def delete_lottery(self, lottery_id: str) -> None:
        self.select_lottery(lottery_id)
        return self.repository.delete_by_id(lottery_id)
