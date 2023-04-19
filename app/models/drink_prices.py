from .db import db, environment, SCHEMA

class Drink_Price(db.Model):
    __tablename__ = "drink_prices"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    # columns
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

    # foreign keys
    drink_id = db.Column(db.String(), db.ForeignKey('drinks.id'), nullable=False)

    # relationships
    drinks = db.relationship("Drink", back_populates="drink_types")

    def to_dict(self):
        return {
            "id": self.id,
            "size": self.size,
            "price": self.price,
            "drink_id": self.drink_id
        }
