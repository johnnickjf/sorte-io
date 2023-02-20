from sqlalchemy.orm import Session
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

    def select(self, user_id: str):
        user_model = self.db.query(User).filter(User.id == user_id).first()
        return user_model

    def select_user_by_email(self, email: str):
        user_model = self.db.query(User).filter(User.email == email).first()
        return user_model

    def select_all(self):
        users_models = self.db.query(User).all()
        return users_models

    def update(self, user: User):
        user_model = self.db.query(User).filter(User.id == user.id).first()
        if user_model and user:
            user_model.name = user.name
            user_model.email = user.email
            user_model.telephone = user.telephone
            user_model.password = user.password
            self.db.commit()
            self.db.refresh(user_model)
        return user_model

    def delete(self, user_id: str):
        user_model = self.db.query(User).filter(User.id == user_id).first()
        if user_model:
            self.db.delete(user_model)
            self.db.commit()
        return user_model
