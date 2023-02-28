from .db import db

class Drink_Prices(db.Model):
    __tablename__ = "drink_prices"

    id = db.column(db.integer, primary_key=True)
    drink_id = db.column(db.String(), db.ForeignKey('drinks.id'), nullable=False)
    size = db.column(db.String(), nullable=False)
    price = db.column(db.Integer(), nullable=False)

    drinks = db.relationship("Drink", back_populates="drink_types")

    def to_dict(self):
        return {
            "id": self.id,
            "drink_id": self.drink_id,
            "size": self.size,
            "price": self.price
        }
