from fastapi import FastAPI, Depends
from src.application.entities.lottery import Lottery
from src.infra.config.database import get_db, create_db, drop_db
from sqlalchemy.orm import Session
from src.application.entities.user import User
from src.infra.repositories.user_repository import UserRepository
from src.infra.repositories.lottery_repository import LotteryRepository

app = FastAPI()

create_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/user/{user_id}')
async def return_user(user_id: int, db: Session = Depends(get_db)):
    user = UserRepository(db).select(user_id)
    if user is None:
        return {'message': 'User not found'}
    return user


@app.get('/users')
async def return_all_users(db: Session = Depends(get_db)):
    users = UserRepository(db).select_all()
    return users


@app.post('/user')
async def create_user(user: User, db: Session = Depends(get_db)):
    user = UserRepository(db).insert(user)
    return user


@app.get('/delete/{user_id}')
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = UserRepository(db).delete(user_id)
    return user


@app.post('/lottery/{user_id}')
async def create_lottery(lottery: Lottery, user_id: int, db: Session = Depends(get_db)):
    lottery.user = UserRepository(db).select(user_id)
    if lottery.user is None:
        return {'message': 'User not found'}
    lottery = LotteryRepository(db).insert(lottery)
    return lottery
