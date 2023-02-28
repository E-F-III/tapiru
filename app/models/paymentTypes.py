# from sqlalchemy import func
from .db import db

class PaymentType(db.Model):
  __tablename__ = "paymentTypes"

  id = db.Column("id", db.Integer, primary_key=True)
  type = db.Column("type", db.String, nullable=False)

  businessPayments = db.relationship("BusinessPayments", back_populates="paymentType", cascade="all, delete")

  def to_dict(self):
    return {
      "id": self.id,
      "type": self.type,
    }
