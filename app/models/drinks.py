from .db import db, environment, SCHEMA

class Drink(db.Model):
    __tablename__ = 'drinks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    ## columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    image = db.Column(db.String())

    ## foreign keys
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('drink_types.id'), nullable=False)

    ##relationships
    wishlists = db.relationship("Wishlist", back_populates="drinks")
    checkins = db.relationship("Checkin", back_populates="drinks")
    drink_prices = db.relationship("Drink_Price", back_populates="drinks")
    drink_type = db.relationship("Drink_Type", back_populates="drinks")

    def to_dict(self):
        return {
            "id": self.id,
            "menu_id": self.menu_id,
            "type_id": self.type_id,
            "name": self.name,
            "description": self.description,
            "image": self.image
        }
