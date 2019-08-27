from flask import Blueprint, render_template
from flask_restplus import Api

frontend = Blueprint('flaskfront', __name__, template_folder='templates')
frontend_api = Api(frontend)


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/docs/', defaults={'path': 'index'})
@frontend.route('/docs/<path:path>/', endpoint='page')
def page(path):
    # Documentation views
    return render_template('index.html')