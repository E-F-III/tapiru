from flask_sqlalchemy import SQLAlchemy
from .db import db
from sqlalchemy.orm import relationship

class Drinks(db.Model):
    __tablename__ = 'drinks'
    
    id = db.column(db.integer, primary_key=True)
    menu_id = db.column(db.integer, nullable=False)
    drink_type = db.column(db.integer, nullable=False)
    name = db.column(db.string, nullable=False)
    description = db.column(db.string, nullable=False)
    image = db.column(db.string)
    
    ##relationships
    # wishlist = db.relationship("Wishlists", back_populates="drinks")
    # checkin = db.relationship("Checkins", back_populates="drinks")
    # drink_prices = db.relationship("Drink_Prices", back_populates="drinks")
    
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