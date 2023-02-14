from fastapi import APIRouter, HTTPException, Depends, status
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.application.entities.user import User, UserCreate
from src.infra.repositories.user_repository import UserRepository

route = APIRouter()


@route.post('/register', status_code=201, response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = UserRepository(db).insert(user)
    return user


@route.get('/user/{user_id}', status_code=200, response_model=User)
async def return_user(user_id: int, db: Session = Depends(get_db)):
    user = UserRepository(db).select(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@route.get('/users')
async def return_all_users(db: Session = Depends(get_db)):
    users = UserRepository(db).select_all()
    return users


@route.get('/delete/{user_id}')
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = UserRepository(db).delete(user_id)
    return user
