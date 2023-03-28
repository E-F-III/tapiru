from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wttform.validators import DataRequired, ValidationError, URL, NumberRange, Optional

def validate_level(form, field):
    if not [0, 20, 40, 60, 80, 100].index(field.data):
        raise ValidationError("Levels must be in increments of 20")

class CheckInForm(FlaskForm):
    item_id = IntegerField("ItemId", validators=[DataRequired()])
    ice_level = SelectField("Ice Level", validators=[DataRequired(), validate_level])
    sugar_level = SelectField("Sugar Level", validators=[DataRequired(), validate_level])
