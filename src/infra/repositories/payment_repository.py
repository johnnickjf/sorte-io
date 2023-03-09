from datetime import datetime
from sqlalchemy.orm import Session
from src.infra.models.models import PaymentORM


class PaymentRepository:

    def __init__(self, db: Session):
        self.db = db

    def insert(self, payment: PaymentORM) -> PaymentORM:
        payment_model = PaymentORM(user=payment.user, lottery=payment.lottery, price=payment.price, qtd=payment.qtd,
                                   status=payment.status, payment_date=payment.payment_date)
        self.db.add(payment_model)
        self.db.commit()
        self.db.refresh(payment_model)
        return payment_model

    def select(self, payment_id: str) -> PaymentORM:
        payment_model = self.db.query(PaymentORM).filter(PaymentORM.id == payment_id).first()
        return payment_model

    def select_by_lottery(self, lottery_id: str) -> list[PaymentORM]:
        payments_models = self.db.query(PaymentORM).filter(PaymentORM.lottery == lottery_id).all()
        return payments_models

    def select_by_user(self, user_id: str) -> list[PaymentORM]:
        payments_models = self.db.query(PaymentORM).filter(PaymentORM.user == user_id).all()
        return payments_models

    def select_all(self) -> list[PaymentORM]:
        payments_models = self.db.query(PaymentORM).all()
        return payments_models

    def update_status(self, payment: PaymentORM) -> PaymentORM:
        payment_model = self.db.query(PaymentORM).filter(PaymentORM.id == payment.id).first()
        if payment_model and payment:
            payment_model.status = payment.status
            payment_model.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.commit()
            self.db.refresh(payment_model)
        return payment_model

    def delete(self, payment_id: str) -> None:
        payment_model = self.db.query(PaymentORM).filter(PaymentORM.id == payment_id).first()
        if payment_model:
            self.db.delete(payment_model)
            self.db.commit()
        return payment_model
