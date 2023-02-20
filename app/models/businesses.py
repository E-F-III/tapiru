from .db import db


class Business(db.Model):
    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    name = db.Column(db.String(255), nullable=False)
    logo_url = db.Column(db.String(255), nullable=False)
    street_address = db.Column(db.Varchar(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    region = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255), nullable=False)
    telephone = db.Column(db.Integer, nullable=False)
    timezone = db.Column(db.String(255), nullable=False)
    currency = db.Column(db.String(255), nullable=False)
    about_location = db.Column(db.String(255), nullable=False)

    #Relationships for Businesses:
    owner = db.relationship("User", back_populates="businesses")

    # Businesses --> Menu Relationship:
    # menus = db.relationship("Menu", back_populates="")


    def to_dict(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "name": self.name,
            "logo_url": self.logo,
            "street_address": self.street_address,
            "city": self.city,
            "region": self.region,
            "postal_code": self.postal_code,
            "country": self.country,
            "website": self.website,
            "telephone": self.telephone,
            "timezone": self.timezone,
            "currency": self.currency,
            "about_us": self.about_location
        }
