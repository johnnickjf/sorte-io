import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Index
from src.infra.config.database import Base
from sqlalchemy.orm import relationship


class UserORM(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    telephone = Column(String)
    created_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class LotteryORM(Base):
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


class NumberORM(Base):
    __tablename__ = 'user_numbers'
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    user = Column(String, ForeignKey('users.id', name='fk_number_user'), nullable=False)
    lottery = Column(String, ForeignKey('lotteries.id', name='fk_number_lottery'), nullable=False)
    payment = Column(String, ForeignKey('payments.id', name='fk_number_payment'), nullable=False)
    number = Column(Integer)
    created_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    __table_args__ = (
        Index('ix_number_lottery', 'number', 'lottery', unique=True),
    )


class PaymentORM(Base):
    __tablename__ = 'payments'
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    user = Column(String, ForeignKey('users.id', name='fk_payment_user'), nullable=False)
    lottery = Column(String, ForeignKey('lotteries.id', name='fk_payment_lottery'), nullable=False)
    price = Column(Numeric(precision=10, scale=2))
    qtd = Column(Integer)
    status = Column(Integer, default=0)
    updated_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    payment_date = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class LastNumberORM(Base):
    __tablename__ = 'last_numbers'
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    lottery = Column(String, ForeignKey('lotteries.id', name='fk_payment_lottery'), nullable=False)
    last_number = Column(Integer, default=0)
    old_last_number = Column(Integer, default=0)
    updated_at = Column(String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
