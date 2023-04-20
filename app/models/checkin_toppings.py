from .db import db, environment, SCHEMA

class Checkin_Topping(db.Model):
    __tablename__ = 'checkin_toppings'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    # foreign keys
    checkin_id = db.Column(db.Integer, db.ForeignKey('checkins.id'), nullable=False)
    topping_id = db.Column(db.Integer, db.ForeignKey('toppings.id'), nullable=False)

    # relationships
    checkins = db.relationship('Checkin', back_populates='toppings')
    toppings = db.relationship('Topping', back_populates='checkin_toppings')

    def to_dict(self):
        return {
            'id': self.id,
            'checkin_id': self.checkin_id,
            'topping_id': self.topping_id
        }
