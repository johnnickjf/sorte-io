from sqlalchemy.orm import Session
from src.application.entities.user import User
from src.infra.models import models


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def insert(self, user: User):
        user_model = models.User(name=user.name, password=user.password, email=user.email, telephone=user.telephone)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model

    def select(self, user_id: int):
        user = self.db.query(models.User).filter(models.User.id == user_id).first()
        return user

    def select_all(self):
        users = self.db.query(models.User).all()
        return users

    def update(self):
        pass

    def delete(self, user_id: int):
        user = self.db.query(models.User).filter(models.User.id == user_id).first()
        self.db.delete(user)
        self.db.commit()
        return user
