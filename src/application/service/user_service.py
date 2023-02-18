from sqlalchemy.orm import Session
from typing import List
from src.infra.repositories.user_repository import UserRepository
from src.application.entities.user import User, UserCreate


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, user: UserCreate) -> User:
        existing_user = self.repository.select_user_by_email(user.email)
        if existing_user:
            raise ValueError('User already exists')
        return self.repository.insert(user)

    def get_user(self, user_id: int) -> User:
        user = self.repository.select(user_id)
        if not user:
            raise ValueError('User not found')
        return user

    def update_user(self, user_id: int, user: UserCreate) -> User:
        existing_user = self.repository.select(user_id)
        if not existing_user:
            raise ValueError('User not found')
        return self.repository.update(user_id, user)

    def get_all_users(self) -> List[User]:
        users = self.repository.select_all()
        if not users:
            raise ValueError('No users found')
        return users

    def delete_user(self, user_id: int) -> None:
        existing_user = self.repository.select(user_id)
        if not existing_user:
            raise ValueError('User not found')
        self.repository.delete(user_id)
