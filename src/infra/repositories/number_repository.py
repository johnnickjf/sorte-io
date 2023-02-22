from sqlalchemy.orm import Session
from src.infra.models.models import Number


class NumberRepository:

    def __init__(self, db: Session):
        self.db = db

    def insert(self, number: Number):
        number_model = Number(number)
        self.db.add(number_model)
        self.db.commit()
        self.db.refresh(number_model)
        return number_model

    def select(self, number_id: str):
        number_model = self.db.query(Number).filter(Number.id == number_id).first()
        return number_model

    def select_by_lottery(self, lottery_id: str):
        numbers_models = self.db.query(Number).filter(Number.lottery == lottery_id).all()
        return numbers_models

    def select_by_user(self, user_id: str):
        numbers_models = self.db.query(Number).filter(Number.user == user_id).all()
        return numbers_models

    def select_all(self):
        numbers_models = self.db.query(Number).all()
        return numbers_models

    def update(self, number: Number):
        number_model = self.db.query(Number).filter(Number.id == number.id).first()
        if number_model and number:
            number_model.number = number.number
            self.db.commit()
            self.db.refresh(number_model)
        return number_model

    def delete(self, number_id: str):
        number_model = self.db.query(Number).filter(Number.id == number_id).first()
        if number_model:
            self.db.delete(number_model)
            self.db.commit()
        return number_model
