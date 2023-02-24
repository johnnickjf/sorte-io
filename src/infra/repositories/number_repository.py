from sqlalchemy.orm import Session
from src.infra.models.models import Number


class NumberRepository:

    def __init__(self, db: Session):
        self.db = db

    def insert(self, number: Number) -> Number:
        number_model = Number(user=number.user, number=number.number, lottery=number.lottery)
        self.db.add(number_model)
        self.db.commit()
        self.db.refresh(number_model)
        return number_model

    def select(self, number_id: str) -> Number:
        number_model = self.db.query(Number).filter(Number.id == number_id).first()
        return number_model

    def select_by_lottery(self, lottery_id: str) -> list[Number]:
        numbers_models = self.db.query(Number).filter(Number.lottery == lottery_id).all()
        return numbers_models

    def select_by_user(self, user_id: str) -> list[Number]:
        numbers_models = self.db.query(Number).filter(Number.user == user_id).all()
        return numbers_models

    def select_number_lottery(self, number: int, lottery_id: str) -> Number:
        number_model = self.db.query(Number).filter(Number.number == number, Number.lottery == lottery_id).first()
        return number_model

    def select_all(self) -> list[Number]:
        numbers_models = self.db.query(Number).all()
        return numbers_models

    def update(self, number: Number) -> Number:
        number_model = self.db.query(Number).filter(Number.id == number.id).first()
        if number_model and number:
            number_model.number = number.number
            self.db.commit()
            self.db.refresh(number_model)
        return number_model

    def delete(self, number_id: str) -> None:
        number_model = self.db.query(Number).filter(Number.id == number_id).first()
        if number_model:
            self.db.delete(number_model)
            self.db.commit()
        return number_model
