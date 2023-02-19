from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.application.entities.user import User, Token
from src.application.service.login_service import LoginService, get_current_user

from src.infra.config.database import get_db

router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK, response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return LoginService(db).authenticate_user(form_data.username, form_data.password)


@router.get("/users/me", status_code=status.HTTP_200_OK, response_model=User)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
