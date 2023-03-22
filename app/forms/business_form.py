from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Business

def validate_name(form, field):
    name = field.data
    if len(name) <= 1:
        raise ValidationError('Please provide a valid business name')



class BusinessForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    street_address = StringField("street_address", validators=[DataRequired()])
    city = StringField("city", validators=[DataRequired()])
    region = StringField("region", validators=[DataRequired()])
    postal_code = IntegerField("postal_code", validators=[DataRequired()])
    country = StringField("country", validators=[DataRequired()])
    website = StringField("website", validators=[DataRequired()])
    telephone = IntegerField("telephone", validators=[DataRequired()])
    timezone = StringField("timezone")
    currency = IntegerField("currency", validators=[DataRequired()])
    about_location = StringField("about_location", validators=[DataRequired()])
