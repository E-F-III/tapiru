from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, URL, NumberRange, Optional

def validate_name(form, field):
    if len(field.data) > 50:
        raise ValidationError("Name must be less than 50 characters")
    elif len(field.data) <= 0:
        raise ValidationError("Name must not be empty")

class DrinkForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), validate_name])
    type = SelectField("Type", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    image = StringField("Image", validators=[URL(), Optional()])
    submit = SubmitField("Submit")
