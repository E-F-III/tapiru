# from sqlalchemy import func
from .db import db, environment, SCHEMA

class PaymentType(db.Model):
  __tablename__ = "paymentTypes"

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

  id = db.Column("id", db.Integer, primary_key=True)
  type = db.Column("type", db.String, nullable=False)

# FOREIGN KEY
  user_id = db.Column(db.integer, db.ForeignKey("users.id"), nullable=False)

# RELATIONSHIP
  businessPayments = db.relationship("BusinessPayments", back_populates="paymentType", cascade="all, delete")

  def to_dict(self):
    return {
      "id": self.id,
      "type": self.type,
    }
