from fastapi import APIRouter, Depends, status
from src.infra.config.database import get_db
from sqlalchemy.orm import Session
from src.application.entities.payment import Payment, CreatePayment, UpdatePayment
from src.application.service.payment_service import PaymentService

route = APIRouter()


@route.post('/payment', status_code=status.HTTP_201_CREATED)
async def create_payment(payment: CreatePayment, db: Session = Depends(get_db)):
    return PaymentService(db).create_payment(payment)


@route.get('/payment', status_code=status.HTTP_200_OK)
async def select_payment(payment_id: str, db: Session = Depends(get_db)):
    return PaymentService(db).select_payment(payment_id)


@route.get('/payments', status_code=status.HTTP_200_OK)
async def select_all_payments(db: Session = Depends(get_db)):
    return PaymentService(db).select_all_payments()


@route.get('/lottery_payments', status_code=status.HTTP_200_OK)
async def select_payments(lottery_id: str, db: Session = Depends(get_db)):
    return PaymentService(db).select_lottery_payments(lottery_id)


@route.get('/user_payment', status_code=status.HTTP_200_OK)
async def select_user_payments(user_id: str, db: Session = Depends(get_db)):
    return PaymentService(db).select_user_payments(user_id)


@route.put('/payment', status_code=status.HTTP_200_OK)
async def update_payment(updated_payment: UpdatePayment, db: Session = Depends(get_db)):
    return PaymentService(db).update_payment_status(updated_payment)




