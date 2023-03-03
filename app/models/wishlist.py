from .db import db, environment, SCHEMA

class Wishlist(db.Model):
    __tablename__ = "Wishlists"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    # columns
    id = db.Column(db.Integer, primary_key=True)

    # foreign keys
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    drink_id = db.Column(db.Integer, db.ForeignKey("drinks.id"), nullable=False)

    # relationships
    owner = db.relationship("User", back_populates="wishlist")
    drinks = db.relationship("Drink", back_populates="wishlist")

    def to_dict(self):
        return {
            "owner_id": self.owner_id,
            "drinks": [drink.to_dict() for drink in self.drinks]
        }
