from sqlalchemy.orm import Session
from src.application.entities.user import User
from src.infra.models.models import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def insert(self, user: User):
        user_model = User(name=user.name, password=user.password,
                          email=user.email, telephone=user.telephone)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model

    def select(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        return user

    def select_all(self):
        users = self.db.query(User).all()
        return users

    def update(self):
        pass

    def delete(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        self.db.delete(user)
        self.db.commit()
        return user
