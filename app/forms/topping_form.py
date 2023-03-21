from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, url, NumberRange

def validate_name(form, field):
    if len(field.data) > 35:
        raise ValidationError("Name must be less than 35 characters")
    elif len(field.data) <= 0:
        raise ValidationError("Name must not be empty")

class ToppingForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), validate_name])
    price = IntegerField("Price", validators=[NumberRange(min=0, max=8)])
    submit = SubmitField("Submit")
