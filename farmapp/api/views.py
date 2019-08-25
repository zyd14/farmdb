from flask import Blueprint, flash, render_template, current_app, request


from farmapp.frontend.forms import PlantTypeInputForm
from farmapp.models import PlantType


backend = Blueprint('backend', __name__, url_prefix='/backend', template_folder='templates')


@backend.route('/species/add', methods=['GET', 'POST'])
def add_plant_type():

    form = PlantTypeInputForm()

    if request.method == 'POST':
        if form.validate():
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
    return render_template('addplant.html', form=form)


        #Else return back to empty form
def unpack_to_html(form: PlantTypeInputForm):

    for fields in form._fields:
        pass
