from sqlalchemy.orm import Session
from src.infra.repositories.user_repository import UserRepository
from src.application.providers.hash_provider import *
from src.application.entities.user import *
from fastapi import HTTPException, status


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, user: SimpleUser) -> User:
        if self.verify_existing_user(user.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
        return self.repository.insert_simple(user)

    def create_user_admin(self, user: UserAdmin) -> User:
        if self.verify_existing_user(user.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
        user.password = get_password_hash(user.password)
        return self.repository.insert(user)

    def select_user(self, user_id: str) -> User:
        user = self.repository.select(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    def select_user_by_email(self, email: str) -> User:
        user = self.repository.select_user_by_email(email)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    def verify_existing_user(self, email: str) -> bool:
        user = self.repository.select_user_by_email(email)
        if not user:
            return False
        return True

    def select_all_users(self) -> list[User]:
        users = self.repository.select_all()
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found")
        return users

    def update_user(self, current_user: User, updated_user: UserAdmin) -> User:
        existing_user = self.repository.select_user_by_email(updated_user.email)
        if existing_user and existing_user.id != current_user.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        current_user.name = updated_user.name
        current_user.email = updated_user.email
        current_user.telephone = updated_user.telephone
        if updated_user.password:
            current_user.password = get_password_hash(updated_user.password)
        return self.repository.update(current_user)

    def delete_user(self, user_id: str) -> None:
        self.select_user(user_id)
        return self.repository.delete(user_id)
