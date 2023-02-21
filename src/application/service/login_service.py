from sqlalchemy.orm import Session
from src.application.entities.user import Token, verify_password
from src.infra.config.database import get_db
from src.infra.repositories.user_repository import UserRepository
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class LoginService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def authenticate_user(self, email: str, password: str):
        user = self.repository.select_user_by_email(email)
        if not user:
            raise HTTPException(status_code=401, detail="Credenciais inválidas")
        if not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Password incorreto")
        access_token = create_access_token(data={"id": user.id, "email": user.email})
        return Token(access_token=access_token)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=[os.getenv('ALGORITHM')])
        username: str = payload.get("email")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = UserRepository(db).select_user_by_email(username)
    if user is None:
        raise credentials_exception
    return user
