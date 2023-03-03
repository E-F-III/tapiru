from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA
from sqlalchemy.orm import relationship

class Drinks(db.Model):
    __tablename__ = 'drinks'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    
    ## columns
    id = db.column(db.integer, primary_key=True)
    drink_type = db.column(db.integer, nullable=False)
    name = db.column(db.string, nullable=False)
    description = db.column(db.string, nullable=False)
    image = db.column(db.string)
    
    ## foreign keys
    menu_id = db.column(db.integer, db.ForeignKey('menus.id'), nullable=False)
    
    
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