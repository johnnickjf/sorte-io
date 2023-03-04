from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.application.entities.number import Number
from src.application.entities.payment import Payment
from src.infra.models.models import NumberORM, LastNumberORM
from src.infra.repositories.number_repository import NumberRepository


class NumberService:
    def __init__(self, db: Session):
        self.repository = NumberRepository(db)

    def create_number(self, pay: Payment) -> list[Number]:
        if pay.status != 1:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payment not confirmed")
        last_num = self.select_last_number_for_lottery(pay)
        numbers = []
        for i in range(pay.qtd):
            next_num = last_num + i + 1
            number = NumberORM(user=pay.user, lottery=pay.lottery, number=next_num)
            numbers.append(number)
        return self.repository.insert(numbers)

    def select_last_number_for_lottery(self, pay: Payment) -> int:
        last_num = self.repository.select_last_number_for_lottery(pay.lottery)
        if not last_num:
            last_num = self.repository.create_last_number_for_lottery(pay.lottery)
        number = last_num.last_number
        self.repository.update_last_number_for_lottery(last_num.id, pay.qtd + number)
        return number

    def select_number(self, number_id: str) -> Number:
        number = self.repository.select_by_id(number_id)
        if not number:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Number not found")
        return self.repository.select_by_id(number_id)

    def select_last_numbers(self) -> list[Number]:
        numbers = self.repository.select_last_numbers()
        if not numbers:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Numbers not found")
        return numbers

    def select_lottery_numbers(self, lottery_id: str) -> list[Number]:
        numbers = self.repository.select_by_lottery(lottery_id)
        if not numbers:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Numbers not found")
        return numbers

    def select_user_numbers(self, user_id: str) -> list[Number]:
        numbers = self.repository.select_by_user(user_id)
        if not numbers:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Numbers not found")
        return numbers
