from app.models import db, PaymentType

def seed_payment_types():
  types=[
    PaymentType(
      type="credit card"
    ),
    PaymentType(
      type="apple pay"
    ),
    PaymentType(
      type="cash"
    ),
    PaymentType(
      type="credit card"
    ),
    PaymentType(
      type="apple pay"
    ),
  ]
  for paymentType in types:
    db.session.add(paymentType)
  db.session.commit()

def undo_payment_types():
  db.session.execute('TRUNCATE types RESTART IDENTITY CASCADE;')
  db.session.commit()
