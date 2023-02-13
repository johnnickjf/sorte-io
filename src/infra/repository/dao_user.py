from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.models import models


class RepositoryUser:

    def __init__(self, db: Session):
        self.db = db

    def insert(self, user: schemas.User):
        db_user = models.User(name=user.name, password=user.password, email=user.email, telephone=user.telephone)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

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
