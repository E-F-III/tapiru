from .db import db, environment, SCHEMA

class Drink_Types(db.Model):
    __tablename__ = "drink_types"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    # columns
    id = db.column(db.integer, primary_key=True)
    type = db.column(db.String(), nullable=False)

    # relationships
    drinks = db.relationship("Drink", back_populates="drink_types")

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type
        }
