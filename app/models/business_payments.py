from .db import db, environment, SCHEMA

class Business_Payment(db.Model):
  __tablename__ = "business_payments"

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

  id = db.Column("id", db.Integer, primary_key=True)

# FOREIGN KEY
  business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
  type_id = db.Column(db.Integer, db.ForeignKey('payment_types.id'), nullable=False)

# RELATIONSHIP
  payment_types = db.relationship("Payment_Type", back_populates="business_payments", cascade="all, delete")
  business = db.relationship("Business", back_populates="business_payments", cascade="all, delete")

  def to_dict(self):
    return {
      "id": self.id,
      "business_id": self.business_id,
      "type_id": self.type_id
    }
