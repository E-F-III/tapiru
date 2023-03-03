from .db import db, environment, SCHEMA

class Drink_Prices(db.Model):
    __tablename__ = "drink_prices"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    # columns
    id = db.column(db.integer, primary_key=True)
    size = db.column(db.String(), nullable=False)
    price = db.column(db.Integer(), nullable=False)

    # foreign keys
    drink_id = db.column(db.String(), db.ForeignKey('drinks.id'), nullable=False)

    # relationships
    drinks = db.relationship("Drink", back_populates="drink_types")

    def to_dict(self):
        return {
            "id": self.id,
            "size": self.size,
            "price": self.price,
            "drink_id": self.drink_id
        }
