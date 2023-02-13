from datetime import datetime
from sqlalchemy import Column, Integer, String
from src.infra.config.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    telephone = Column(String)
    created_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
