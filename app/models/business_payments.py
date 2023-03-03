from .db import db, environment, SCHEMA

class Business_Payment(db.Model):
  __tablename__ = "business_payments"

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

  id = db.Column("id", db.Integer, primary_key=True)
  business_id = db.Column("business_id", db.Integer, nullable=False)
  type_id = db.Column("type_id", db.Integer, nullable=False)

# FOREIGN KEY
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

# RELATIONSHIP
  paymentTypes = db.relationship("paymentTypes", back_populates="businessPayment", cascade="all, delete")
  business = db.relationship("business", back_populates="businessPayment", cascade="all, delete")

  def to_dict(self):
    return {
      "id": self.id,
      "business_id": self.business_id,
      "type_id": self.type_id
    }
