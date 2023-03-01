from sqlalchemy.orm import Session
from src.infra.models.models import UserORM


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def insert(self, user: UserORM) -> UserORM:
        user_model = UserORM(name=user.name, password=user.password,
                             email=user.email, telephone=user.telephone)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model

    def insert_simple(self, user: UserORM) -> UserORM:
        user_model = UserORM(name=user.name, email=user.email, telephone=user.telephone)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model

    def select(self, user_id: str) -> UserORM:
        user_model = self.db.query(UserORM).filter(UserORM.id == user_id).first()
        return user_model

    def select_user_by_email(self, email: str) -> UserORM:
        user_model = self.db.query(UserORM).filter(UserORM.email == email).first()
        return user_model

    def select_all(self) -> list[UserORM]:
        users_models = self.db.query(UserORM).all()
        return users_models

    def update(self, user: UserORM) -> UserORM:
        user_model = self.db.query(UserORM).filter(UserORM.id == user.id).first()
        if user_model and user:
            user_model.name = user.name
            user_model.email = user.email
            user_model.telephone = user.telephone
            user_model.password = user.password
            self.db.commit()
            self.db.refresh(user_model)
        return user_model

    def delete(self, user_id: str) -> None:
        user_model = self.db.query(UserORM).filter(UserORM.id == user_id).first()
        if user_model:
            self.db.delete(user_model)
            self.db.commit()
        return user_model
