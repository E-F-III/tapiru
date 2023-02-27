from .db import db

class Wishlist(db.Model):
    __tablename__ = "Wishlists"

    id = db.Column(db.integer, primary_key=True)

    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    drink_id = db.Column(db.Integer, db.ForeignKey("drinks.id"), nullable=False)

    owner = db.relationship("User", back_populates="wishlist")
    drinks = db.relationship("Drink", back_populates="wishlist")

    def to_dict(self):
        return {
            "owner_id": self.owner_id,
            "drinks": [drink.to_dict() for drink in self.drinks]
        }
