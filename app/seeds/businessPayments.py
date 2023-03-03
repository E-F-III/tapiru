from app.models import db, BusinessPayment

def seed_business_payments():
  business_payments=[
    BusinessPayment(
      business_id=1, type_id=1
    ),
    BusinessPayment(
      business_id=2, type_id=2
    ),
    BusinessPayment(
      business_id=3, type_id=3
    ),
    BusinessPayment(
      business_id=4, type_id=4
    ),
    BusinessPayment(
      business_id=5, type_id=5
    ),
  ]
  for payment in business_payments:
    db.session.add(payment)
  db.session.commit()

def undo_business_payments():
  db.session.execute('TRUNCATE payments RESTART IDENTITY CASCADE;')
  db.session.commit()
