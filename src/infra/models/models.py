from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric
from src.infra.config.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    telephone = Column(String)
    created_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class Lottery(Base):
    __tablename__ = 'lotteries'
    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer)
    name = Column(String)
    description = Column(String)
    max_number = Column(Integer)
    price = Column(Numeric(precision=10, scale=2))
    winner = Column(Integer)
    start_date = Column(String)
    end_date = Column(String)
    created_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
