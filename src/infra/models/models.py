import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from src.infra.config.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    telephone = Column(String)
    created_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class Lottery(Base):
    __tablename__ = 'lotteries'
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    user = Column(String, ForeignKey('users.id', name='fk_lottery_user'), nullable=False)
    name = Column(String)
    description = Column(String)
    price = Column(Numeric(precision=10, scale=2))
    status = Column(Integer, default=0)
    qtd = Column(Integer)
    winner = Column(String, ForeignKey('user_numbers.id', name='fk_lottery_numbers'))
    start_date = Column(String)
    end_date = Column(String)
    created_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class Number(Base):
    __tablename__ = 'user_numbers'
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    user = Column(String, ForeignKey('users.id', name='fk_number_user'), nullable=False)
    lottery = Column(String, ForeignKey('lotteries.id', name='fk_number_lottery'), nullable=False)
    number = Column(Integer)
    created_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
