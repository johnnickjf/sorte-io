from fastapi import APIRouter, HTTPException, Depends, status
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.application.entities.user import User, UserCreate
from src.infra.repositories.user_repository import UserRepository

route = APIRouter()


@route.post('/register', status_code=201, response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = UserRepository(db).insert(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    return user


@route.get('/select/user/{user_id}', status_code=200, response_model=User)
async def select_user(user_id: int, db: Session = Depends(get_db)):
    user = UserRepository(db).select(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@route.put('/update/user/{user_id}', status_code=200, response_model=User)
async def update_user(user_id: int, user_updated: UserCreate, db: Session = Depends(get_db)):
    user_updated = UserRepository(db).update(user_id, user_updated)
    if not user_updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_updated


@route.get('/all/users', status_code=200, response_model=list[User])
async def select_all_users(db: Session = Depends(get_db)):
    users = UserRepository(db).select_all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return users


@route.delete('/delete/user/{user_id}')
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = UserRepository(db).delete(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
