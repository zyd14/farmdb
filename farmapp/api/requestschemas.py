from flask_marshmallow.sqla import ModelSchema
from marshmallow import fields, post_load
from farmapp.models import PlantType

class InsertNewPlantType(ModelSchema):

    class Meta:
        model = PlantType
    # name = fields.String(required=True)
    # species = fields.String(required=True)
    # subspecies = fields.Sting(required=False)
    # suggested_sun_reqst = fields.Dict(required=False)
    # suggested_harvest_reqs = fields.Dict(required=False)
    # have_grown_before = fields.Boolean(default=False)
    # native_to = fields.String(required=False)
    # notes = fields.String(required=False)

    @post_load
    def clean(self, item: dict):
        for key, value in item.keys():
            if isinstance(value, str):
                item[key] = value.strip()

        return item

c = InsertNewPlantType()