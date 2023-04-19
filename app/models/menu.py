from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA
from sqlalchemy.orm import relationship

class Menu(db.Model):
    __tablename__ = 'menus'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    ## columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)

    ## foreign keys
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id') ,nullable=False)

    ## relationships
    business = db.relationship("Business", back_populates="menu")
    drinks = db.relationship("Drink", back_populates="menu")
    toppings = db.relationship("Topping", back_populates="menu")

    def to_dict(self):
        return {
            "id": self.id,
            "business_id": self.business_id,
            "name": self.name,
            "description": self.description,
            ## waiting for business table to add relationships stuff
            "toppings": [toppings.to_dict() for toppings in self.toppings_relationship]
        }
