from sqlalchemy.orm import Session
from src.application.entities.number import Number

from src.infra.repositories.number_repository import NumberRepository


class NumberService:
    def __init__(self, db: Session):
        self.repository = NumberRepository(db)

    def create_number(self, number: Number) -> Number:
        if self.repository.select(number.id):
            raise ValueError("Number already exists")
        return self.repository.insert(number)

    def select_number(self, number_id: str) -> Number:
        number = self.repository.select(number_id)
        if not number:
            raise ValueError("Number not found")
        return self.repository.select(number_id)

    def select_all_numbers(self) -> list[Number]:
        numbers = self.repository.select_all()
        if not numbers:
            raise ValueError("Numbers not found")
        return numbers

    def select_lottery_numbers(self, lottery_id: str) -> list[Number]:
        numbers = self.repository.select_by_lottery(lottery_id)
        if not numbers:
            raise ValueError("Numbers not found")
        return numbers

    def select_user_numbers(self, user_id: str) -> list[Number]:
        numbers = self.repository.select_by_user(user_id)
        if not numbers:
            raise ValueError("Numbers not found")
        return numbers
