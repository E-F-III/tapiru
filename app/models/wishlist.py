from .db import db, environment, SCHEMA

class Wishlist(db.Model):
    __tablename__ = "Wishlists"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    # columns
    id = db.Column(db.Integer, primary_key=True)

    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    drink_id = db.Column(db.Integer, db.ForeignKey("drinks.id"), nullable=False)

    # relationships
    user = db.relationship("User", back_populates="wishlist")
    drinks = db.relationship("Drink", back_populates="wishlist")

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "drinks": [drink.to_dict() for drink in self.drinks]
        }
