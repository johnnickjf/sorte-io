from sqlalchemy.orm import Session
from src.application.entities.lottery import Lottery
from src.infra.models import models


class LotteryRepository:

    def __init__(self, db: Session):
        self.db = db

    def insert(self, lottery: Lottery):
        lottery_model = models.Lottery(name=lottery.name, description=lottery.description, user=lottery.user.id,
                                       max_number=lottery.max_number, price=lottery.price)
        self.db.add(lottery_model)
        self.db.commit()
        self.db.refresh(lottery_model)
        return lottery_model

    def select(self, user_id: int):
        pass

    def select_all(self):
        pass

    def update(self):
        pass

    def delete(self, user_id: int):
        pass
