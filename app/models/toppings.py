from flask_sqlalchemy import SQLAlchemy
from .db import db
from sqlalchemy.orm import relationship

class Toppings(db.Model):
    __tablename__ = 'toppings'
    
    id = db.column(db.integer, primary_key=True)
    menu_id = db.column(db.integer(), nullable=False)
    name = db.column(db.string(), nullable=False)
    price = db.column(db.integer(), nullable=False) ## price will be in cents and converted to dollars in front-end 
    ## price example 420 = $4.20 in frontend
    
    menu = db.relationship("Menus", back_populates="toppings_relationship")
    
    
    def to_dict(self):
        response = {
            "id": self.id,
            "menu_id": self.menu_id,
            "name": self.name,
            "price": self.price
        }
        return response