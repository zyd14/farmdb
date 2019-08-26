from flask import Blueprint, flash, render_template, current_app, request, jsonify
from flask_restplus import Api

from farmapp.frontend.forms import PlantTypeInputForm
from farmapp.models import PlantType, PlantTypeSchema
from farmapp.setup_app import get_db_session

plants = Blueprint('plants', __name__, url_prefix='/plants', template_folder='templates')
api = Api(plants)

@plants.route('/species/add', methods=['GET', 'POST'])
def add_plant_type():
    db = get_db_session()
    form = PlantTypeInputForm(request.form)


    if request.method == 'POST':
        if form.validate():
            plant_type = PlantType(
                name=form.name.data,
                species=form.species.data,
            )
            db.session.add(plant_type)
            db.session.commit()
            flash('Created new plant type')
        else:
            flash('you dun fucked up')


    return render_template('addplant.html', form=form)


@plants.route('/view', methods=['GET'])
def get_plant_types():
    db = get_db_session()
    plants = db.session.query(PlantType).all()
    data = PlantTypeSchema().dump(plants)

    return jsonify(data), 201
