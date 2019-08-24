from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    BooleanField
)

standard_validators = [DataRequired(), Length(0, 255)]


class PlantTypeInputForm(FlaskForm):

    name = StringField('Name', validators=standard_validators)
    species = StringField('Species', validators=standard_validators)
    subscpecies = StringField('Subspecies', validators=standard_validators, description='Any subspecies information to differentiate this plant from others of the same species')
    suggested_sun_reqs = TextAreaField('Suggested Sun Requirements', validators=standard_validators)
    have_grown_before = BooleanField('Have you grown this before?')
    native_to = StringField('This plant is native to', validators=standard_validators)
    notes = TextAreaField('Any other notes')
    submit = SubmitField('Submit')
