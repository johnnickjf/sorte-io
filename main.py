from fastapi import FastAPI, Depends
from src.infra.config.database import get_db, create_db
from sqlalchemy.orm import Session
from src.application.entities.user import User
from src.infra.repositories.user_repository import UserRepository

app = FastAPI()

create_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/user/{user_id}')
def return_user(user_id: int, db: Session = Depends(get_db)):
    users = UserRepository(db).select(user_id)
    return users


@app.get('/users')
def return_user(db: Session = Depends(get_db)):
    users = UserRepository(db).select_all()
    return users


@app.post('/user')
def create_user(user: User, db: Session = Depends(get_db)):
    user = UserRepository(db).insert(user)
    return user


@app.get('/delete/{user_id}')
def create_user(user_id: int, db: Session = Depends(get_db)):
    user = UserRepository(db).delete(user_id)
    return user
