from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA
from sqlalchemy.orm import relationship

class Toppings(db.Model):
    __tablename__ = 'toppings'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    ## columns
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(), nullable=False)
    price = db.column(db.integer(), nullable=False) ## price will be in cents and converted to dollars in front-end 
    ## price example 420 = $4.20 in frontend
    
    ## foreign keys
    menu_id = db.column(db.integer(), db.ForeignKey('menus.id'),nullable=False)
    
    ## relationships
    menu = db.relationship("Menus", back_populates="toppings_relationship")
    
    
    def to_dict(self):
        response = {
            "id": self.id,
            "menu_id": self.menu_id,
            "name": self.name,
            "price": self.price
        }
        return response