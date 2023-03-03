from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA
from sqlalchemy.orm import relationship

class Menus(db.Model):
    __tablename__ = 'menus'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    ## columns
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(), nullable=False)
    description = db.column(db.string(), nullable=False)
    
    ## foreign keys
    business_id = db.column(db.integer, db.ForeignKey('businesses.id') ,nullable=False)
    
    ## relationships
    business = db.relationship("Businesses", back_populates="menu")
    toppings_relationship = db.relationship("Toppings", back_populates="menu")
    
    def to_dict(self):
        response = {
            "id": self.id,
            "business_id": self.business_id,
            "name": self.name,
            "description": self.description,
            ## waiting for business table to add relationships stuff
            "toppings": [toppings.to_dict() for toppings in self.toppings_relationship]
        }
        return response