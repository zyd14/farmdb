"""

Project: farmdb

File Name: flask_restplus_patch

Author: Zachary Romer, zach@scharp.org

Creation Date: 8/24/19

Version: 1.0

Purpose:

Special Notes:

"""
import flask_marshmallow
class SchemaMixin(object):

    def __deepcopy__(self, memo):
        # XXX: Flask-RESTplus makes unnecessary data copying, while
        # marshmallow.Schema doesn't support deepcopyng.
        return self


class Schema(SchemaMixin, flask_marshmallow.Schema):
    pass


if flask_marshmallow.has_sqla:
    class ModelSchema(SchemaMixin, flask_marshmallow.sqla.ModelSchema):
        pass