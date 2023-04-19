from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA
from sqlalchemy.orm import relationship

class Drink(db.Model):
    __tablename__ = 'drinks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    ## columns
    id = db.Column(db.Integer, primary_key=True)
    drink_type = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    image = db.Column(db.String())

    ## foreign keys
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)


    ##relationships
    wishlist = db.relationship("Wishlists", back_populates="drinks")
    checkin = db.relationship("Checkins", back_populates="drinks")
    drink_prices = db.relationship("Drink_Prices", back_populates="drinks")

    def to_dict(self):
        response = {
            "id": self.id,
            "menu_id": self.menu_id,
            "type": self.drink_type,
            "name": self.name,
            "description": self.description,
            "image": self.image
        }
        return response
