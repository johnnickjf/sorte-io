from fastapi import APIRouter, Depends, status
from src.application.service.login_service import get_current_user
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.application.entities.user import User, UserAdmin, SimpleUser, UpdateUser
from src.application.service.user_service import UserService

route = APIRouter()


@route.post('/user_register', status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user: UserAdmin, db: Session = Depends(get_db)):
    return UserService(db).create_user_admin(user)


@route.post('/user', status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user: SimpleUser, db: Session = Depends(get_db)):
    return UserService(db).create_user(user)


@route.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=User)
async def select_user(user_id: str, db: Session = Depends(get_db)):
    return UserService(db).select_user(user_id)


@route.put('/user/', status_code=status.HTTP_200_OK, response_model=User)
async def update_user(user_updated: UpdateUser, current_user: User = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    return UserService(db).update_user(current_user, user_updated)


@route.get('/users', status_code=status.HTTP_200_OK, response_model=list[User])
async def select_all_users(db: Session = Depends(get_db)):
    return UserService(db).select_all_users()


# @route.delete('/user/', status_code=status.HTTP_200_OK)
# async def delete_user(user_id: str, db: Session = Depends(get_db)):
#     return UserService(db).delete_user(user_id)
