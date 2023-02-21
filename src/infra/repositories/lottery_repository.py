from sqlalchemy.orm import Session
from src.infra.models.models import Lottery


class LotteryRepository:

    def __init__(self, db: Session):
        self.db = db

    def insert(self, lottery: Lottery):
        lottery_model = Lottery(name=lottery.name, description=lottery.description, user=lottery.user,
                                qtd=lottery.qtd, price=lottery.price)
        self.db.add(lottery_model)
        self.db.commit()
        self.db.refresh(lottery_model)
        return lottery_model

    def select(self, lottery_id: str):
        lottery_model = self.db.query(Lottery).filter(Lottery.id == lottery_id).first()
        return lottery_model

    def select_by_user(self, user_id: str):
        lottery_model = self.db.query(Lottery).filter(Lottery.user == user_id).all()
        return lottery_model

    def select_all(self):
        lotteries_models = self.db.query(Lottery).all()
        return lotteries_models

    def update(self, lottery: Lottery):
        lottery_model = self.db.query(Lottery).filter(Lottery.id == lottery.id).first()
        if lottery_model and lottery:
            lottery_model.name = lottery.name
            lottery_model.description = lottery.description
            lottery_model.qtd = lottery.qtd
            lottery_model.price = lottery.price
            lottery_model.status = lottery.status
            self.db.commit()
            self.db.refresh(lottery_model)
        return lottery_model

    def delete(self, lottery_id: str):
        lottery_model = self.db.query(Lottery).filter(Lottery.id == lottery_id).first()
        if lottery_model:
            self.db.delete(lottery_model)
            self.db.commit()
        return lottery_model
