"""

Project: farmdb

File Name: backends

Author: Zachary Romer, zach@scharp.org

Creation Date: 8/24/19

Version: 1.0

Purpose:

Special Notes:

"""
from flask import Blueprint

backend = Blueprint('backend', __name__, url_prefix='/backend/', template_folder='templates')