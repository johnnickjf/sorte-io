from fastapi import APIRouter, HTTPException, Depends, status
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.application.entities.user import User, UserCreate
from src.application.service.user_service import UserService

route = APIRouter()


@route.post('/user', status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService(db).create_user(user)


@route.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=User)
async def select_user(user_id: str, db: Session = Depends(get_db)):
    return UserService(db).get_user(user_id)


@route.put('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=User)
async def update_user(user_id: str, user_updated: UserCreate, db: Session = Depends(get_db)):
    return UserService(db).update_user(user_id, user_updated)


@route.get('/users', status_code=status.HTTP_200_OK, response_model=list[User])
async def select_all_users(db: Session = Depends(get_db)):
    return UserService(db).get_all_users()


@route.delete('/user/{user_id}', status_code=status.HTTP_200_OK)
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    return UserService(db).delete_user(user_id)
