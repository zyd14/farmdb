from wtforms.validators import DataRequired, Length
from wtforms import Form, StringField, BooleanField, TextAreaField, SubmitField

standard_validators = [DataRequired(), Length(0, 255)]


class PlantTypeInputForm(Form):

    name = StringField('Name')
    species = StringField('Species')
    subscpecies = StringField('Subspecies', description='Any subspecies information to differentiate this plant from others of the same species')
    suggested_sun_reqs = TextAreaField('Suggested Sun Requirements')
    have_grown_before = BooleanField('Have you grown this before?')
    native_to = StringField('This plant is native to')
    notes = TextAreaField('Any other notes')
    submit = SubmitField('Submit', )
