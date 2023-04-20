from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, URL, NumberRange, Optional

class WishlistForm(FlaskForm):
    drink_id = IntegerField("Drink_Id", validators=[DataRequired()])