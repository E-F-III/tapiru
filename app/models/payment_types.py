# from sqlalchemy import func
from .db import db, environment, SCHEMA

class Payment_Type(db.Model):
  __tablename__ = "payment_types"

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

  id = db.Column("id", db.Integer, primary_key=True)
  type = db.Column("type", db.String, nullable=False)

# RELATIONSHIP
  business_payments = db.relationship("Business_Payment", back_populates="payment_types", cascade="all, delete")

  def to_dict(self):
    return {
      "id": self.id,
      "type": self.type,
    }
