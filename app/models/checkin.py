from .db import db, environment, SCHEMA

class Checkin(db.Model):
    __tablename__ = 'checkins'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    # columns
    id = db.Column(db.Integer, primary_key=True)
    sugar_level = db.Column(db.Integer, nullable=False)
    ice_level = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    drink_id = db.Column(db.Integer, db.ForeignKey('drinks.id'), nullable=False)

    # relationships
    user = db.relationship('User', back_populates='checkins')
    drink = db.relationship('Drink', back_populates='checkins')
    toppings = db.relationship('Topping', secondary='checkin_toppings', back_populates='checkins')

    def to_dict(self):
        return {
            'id': self.id,
            'sugar_level': self.sugar_level,
            'ice_level': self.ice_level,
            'user_id': self.user_id,
            'drink_id': self.drink_id,
            'toppings': [topping.to_dict() for topping in self.toppings],
            'datetime': self.datetime
        }
