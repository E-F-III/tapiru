from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA
from sqlalchemy.orm import relationship

class Topping(db.Model):
    __tablename__ = 'toppings'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    ## columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer, nullable=False) ## price will be in cents and converted to dollars in front-end
    ## price example 420 = $4.20 in frontend

    ## foreign keys
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'),nullable=False)

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
