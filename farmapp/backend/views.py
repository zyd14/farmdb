"""

Project: farmdb

File Name: backends

Author: Zachary Romer, zach@scharp.org

Creation Date: 8/24/19

Version: 1.0

Purpose:

Special Notes:

"""
from flask import Blueprint, flash
from flask_restplus import Api, Namespace, Resource

from farmapp.app import db, app
from farmapp.models import PlantType
from farmapp.frontend.forms import PlantTypeInputForm

backend = Blueprint('backend', __name__, url_prefix='/backend/', template_folder='templates')
backend_api = Api(backend)

ns_api = Namespace('plants', description='Plants related operations')




        #Else return back to empty form




