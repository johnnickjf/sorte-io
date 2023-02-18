from sqlalchemy.orm import Session
from typing import List
from src.infra.repositories.user_repository import UserRepository
from src.application.entities.user import User, UserCreate
from fastapi import HTTPException, status


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, user: UserCreate) -> User:
        existing_user = self.repository.select_user_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
        return self.repository.insert(user)

    def get_user(self, user_id: str) -> User:
        user = self.repository.select(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    def update_user(self, user_id: str, user: UserCreate) -> User:
        existing_user = self.repository.select(user_id)
        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return self.repository.update(user_id, user)

    def get_all_users(self) -> List[User]:
        users = self.repository.select_all()
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found")
        return users

    def delete_user(self, user_id: str) -> None:
        existing_user = self.repository.select(user_id)
        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        self.repository.delete(user_id)
