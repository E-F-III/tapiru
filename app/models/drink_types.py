from .db import db

class Drink_Types(db.Model):
    __tablename__ = "drink_types"

    id = db.column(db.integer, primary_key=True)
    type = db.column(db.String(), nullable=False)

    drinks = db.relationship("Drink", back_populates="drink_types")

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type
        }
