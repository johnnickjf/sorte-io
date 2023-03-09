from datetime import datetime
from sqlalchemy.orm import Session
from src.infra.models.models import NumberORM, LastNumberORM


class NumberRepository:

    def __init__(self, db: Session):
        self.db = db

    def insert(self, numbers: list[NumberORM]) -> True:
        try:
            for n in numbers:
                number_model = NumberORM(user=n.user, lottery=n.lottery, payment=n.payment, number=n.number)
                self.db.add(number_model)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select_by_id(self, number_id: str) -> NumberORM:
        number_model = self.db.query(NumberORM).filter(NumberORM.id == number_id).first()
        return number_model

    def select_by_lottery(self, lottery_id: str) -> list[NumberORM]:
        numbers_models = self.db.query(NumberORM).filter(NumberORM.lottery == lottery_id).all()
        return numbers_models

    def select_by_user(self, user_id: str) -> list[NumberORM]:
        numbers_models = self.db.query(NumberORM).filter(NumberORM.user == user_id).all()
        return numbers_models

    def create_last_number_for_lottery(self, lottery_id: str) -> LastNumberORM:
        last = LastNumberORM(lottery=lottery_id)
        self.db.add(last)
        self.db.commit()
        return last

    def select_last_number_for_lottery(self, lottery_id: str) -> LastNumberORM:
        last = self.db.query(LastNumberORM).filter(LastNumberORM.lottery == lottery_id).first()
        return last

    def update_last_number_for_lottery(self, last_id: str, new_total: int) -> LastNumberORM:
        search = self.db.query(LastNumberORM).filter(LastNumberORM.id == last_id).first()
        if search:
            print(search.last_number)
            search.old_last_number = search.last_number
            search.last_number = new_total
            search.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.commit()
            self.db.refresh(search)
        return search

    def select_number_lottery(self, number: int, lottery_id: str) -> NumberORM:
        number_model = self.db.query(NumberORM).filter(NumberORM.number == number,
                                                       NumberORM.lottery == lottery_id).first()
        return number_model

    def select_all(self) -> list[NumberORM]:
        numbers_models = self.db.query(NumberORM).all()
        return numbers_models

    def select_last_numbers(self) -> list[NumberORM]:
        numbers_models = self.db.query(NumberORM).order_by(NumberORM.created_at.desc()).limit(1000).all()
        return numbers_models

    def update(self, number: NumberORM) -> NumberORM:
        number_model = self.db.query(NumberORM).filter(NumberORM.id == number.id).first()
        if number_model and number:
            number_model.last_number = number.number
            self.db.commit()
            self.db.refresh(number_model)
        return number_model

    def delete(self, number_id: str) -> None:
        number_model = self.db.query(NumberORM).filter(NumberORM.id == number_id).first()
        if number_model:
            self.db.delete(number_model)
            self.db.commit()
        return number_model
