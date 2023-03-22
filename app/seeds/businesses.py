from app.models import db, Business

def seed_businesses():
  businesses=[
    Business(
        owner_id=1,
        name="Boba Tea Shop",
        logo="https://www.eriereader.com/uploads/articles/164895_andorras2.jpg",
        street_address="1234 Boba Tea Lane",
        city="Boba City",
        region="Boba Region",
        postcode="12345",
        country="Boba Country",
        website="www.bobateashop.com",
        phone="123-456-7890",
        timezone="America/Los_Angeles",
        currency="USD",
        about_location="Boba Tea Shop is located in Boba City, Boba Region, Boba Country.",
        payment_types=[1,2,3,4,5],
    ),
    Business(
        owner_id=1,
        name="Tea Time Boba Shop",
        logo="https://www.eriereader.com/uploads/articles/164895_andorras2.jpg",
        street_address="5678 Boba Street",
        city="Boba City",
        region="Boba Region",
        postcode="12345",
        country="Boba Country",
        website="www.teatimebobashop.com",
        phone="123-456-7890",
        timezone="America/Los_Angeles",
        currency="USD",
        about_location="Tea Time Boba Shop is located in Boba City, Boba Region, Boba Country.",
        payment_types=[1,2,3,4,5],
    ),
    Business(
        owner_id=1,
        name="Sweet Leaf Boba",
        logo="https://www.eriereader.com/uploads/articles/164895_andorras2.jpg",
        street_address="9876 Boba Blvd",
        city="Boba City",
        region="Boba Region",
        postcode="12345",
        country="Boba Country",
        website="www.sweetleafboba.com",
        phone="123-456-7890",
        timezone="America/Los_Angeles",
        currency="USD",
        about_location="Sweet Leaf Boba is located in Boba City, Boba Region, Boba Country.",
        payment_types=[1,2,3,4,5],
    ),
    Business(
        owner_id=1,
        name="Boba Bliss",
        logo="https://www.eriereader.com/uploads/articles/164895_andorras2.jpg",
        street_address="4321 Boba Way",
        city="Boba City",
        region="Boba Region",
        postcode="12345",
        country="Boba Country",
        website="www.bobabliss.com",
        phone="123-456-7890",
        timezone="America/Los_Angeles",
        currency="USD",
        about_location="Boba Bliss is located in Boba City, Boba Region, Boba Country.",
        payment_types=[1,2,3,4,5],
    ),
    Business(
        owner_id=1,
        name="Boba Buzz",
        logo="https://www.eriereader.com/uploads/articles/164895_andorras2.jpg",
        street_address="1357 Boba Circle",
        city="Boba City",
        region="Boba Region",
        postcode="12345",
        country="Boba Country",
        website="www.bobabuzz.com",
        phone="123-456-7890",
        timezone="America/Los_Angeles",
        currency="USD",
        about_location="Boba Buzz is located in Boba City, Boba Region, Boba Country.",
        payment_types=[1,2,3,4,5],
    )
  ]
  for business in businesses:
    db.session.add(business)
  db.session.commit()

def undo_businesses():
  db.session.execute('TRUNCATE businesses RESTART IDENTITY CASCADE;')
  db.session.commit()
