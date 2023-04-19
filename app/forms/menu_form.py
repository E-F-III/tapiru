from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, url

def validate_name(form, field):
    if len(field.data) > 50:
        raise ValidationError("Name must be less than 50 characters")
    elif len(field.data) <= 0:
        raise ValidationError("Name must not be empty")

def validate_description(form, field):
    if len(field.data) > 350:
        raise ValidationError("Description must be less than 350 characters")
    elif len(field.data) <= 0:
        raise ValidationError("Description must not be empty")

class MenuForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), validate_name])
    description = StringField("Description", validators=[DataRequired(), validate_description])
    toppings = SelectField("Toppings", validators=[DataRequired()])
    submit = SubmitField("Submit")
