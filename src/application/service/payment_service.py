from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.application.entities.payment import Payment, CreatePayment, UpdatePayment
from src.application.service.lottery_service import LotteryService
from src.application.service.number_service import NumberService
from src.infra.repositories.payment_repository import PaymentRepository


class PaymentService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = PaymentRepository(db)

    def create_payment(self, payment: Payment) -> Payment:
        lottery = LotteryService(self.db).select_lottery(payment.lottery)
        if not lottery:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Lottery not found")
        if lottery.status != 1:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Lottery closed")
        payment = Payment(**payment.dict(), price=float(lottery.price * payment.qtd))
        return self.repository.insert(payment)

    def select_payment(self, payment_id: str) -> Payment:
        payment = self.repository.select(payment_id)
        if not payment:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payment not found")
        return payment

    def select_all_payments(self) -> list[Payment]:
        payments = self.repository.select_all()
        if not payments:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payments not found")
        return payments

    def select_lottery_payments(self, lottery_id: str) -> list[Payment]:
        payments = self.repository.select_by_lottery(lottery_id)
        if not payments:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payments not found")
        return payments

    def select_user_payments(self, user_id: str) -> list[Payment]:
        payments = self.repository.select_by_user(user_id)
        if not payments:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payments not found")
        return payments

    def update_payment_status(self, updated_payment: UpdatePayment) -> Payment:
        payment = self.select_payment(updated_payment.id)
        payment.status = updated_payment.status
        if payment.status == 1:
            NumberService(self.db).create_number(payment)
        payment = self.repository.update_status(payment)
        return payment

    def delete_payment(self, payment_id: str) -> None:
        payment = self.repository.select(payment_id)
        if not payment:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payment not found")
        return self.repository.delete(payment_id)
