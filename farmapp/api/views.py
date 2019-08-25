from flask import Blueprint, flash, render_template, current_app
from flask_restplus import Api, Namespace, Resource


from farmapp.frontend.forms import PlantTypeInputForm
from farmapp.models import PlantType


backend = Blueprint('backend', __name__, url_prefix='/backend', template_folder='templates')
api = Api(backend)
ns_api = api.namespace('plants', description='Plants related operations')


class PlantTypeResource(Resource):

    def get(self):
        return render_template('addplant.html')

    def post(self):
        return self.add_plant_type()

    def add_plant_type(self):

        form = PlantTypeInputForm()

        if form.validate_on_submit():
            plant_type = PlantType(
                name=form.name.data,
                species=form.species.data,
                subspecies=form.subscpecies.data,
                suggested_sun_reqs=form.suggested_sun_reqs.data,
                grow_before=form.have_grown_before.data,
                native_to=form.native_to.data,
                notes=form.notes
            )
            current_app.db.session.add(plant_type)
            current_app.db.session.commit()
            flash('Created new plant type')
        return render_template('addplant.html')


        #Else return back to empty form


ns_api.add_resource(PlantTypeResource, '/species/add', endpoint='/plants/species/add')


