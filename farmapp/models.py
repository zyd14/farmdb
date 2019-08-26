"""

Project: farmdb

File Name: tables

Author: Zachary Romer, zach@scharp.org

Creation Date: 8/24/19

Version: 1.0

Purpose:

Special Notes:

"""
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DateTime
from sqlalchemy.dialects.postgresql import JSONB
from marshmallow_sqlalchemy import ModelSchema
from flask_sqlalchemy import SQLAlchemy

from farmapp.setup_app import db

class PlantType(db.Model):

    __tablename__ = 'plant_types'

    id = db.Column(db.Integer, db.Sequence('plant_type_id_seq'), primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    subspecies = db.Column(db.String, nullable=True)
    suggested_sun_reqs = db.Column(db.String, nullable=True)
    suggested_harvest_reqs = db.Column(db.String, nullable=True)
    grown_before = db.Column(db.Boolean, nullable=True)
    native_to = db.Column(db.String, nullable=True)
    notes = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<PlantType>(id='{self.name}', name='{self.species}'"

class PlantTypeSchema(ModelSchema):
    class Meta:
        model = PlantType

class Planted(db.Model):

    __tablename__ = 'planted'

    #TODO set date_planted to default time
    id = db.Column(db.Integer, db.Sequence('planted_id_seq'), primary_key=True)
    plant_type_id = db.Column(db.Integer, db.ForeignKey('plant_types.id'))
    date_planted = db.Column(db.DateTime, nullable=True)
    date_harvested = db.Column(db.DateTime, nullable=True)
    harvest_yield = db.Column(db.Integer, nullable=True)
    quality = db.Column(db.String, nullable=True)
    notes = db.Column(db.String, nullable=True)

