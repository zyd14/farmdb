"""

Project: farmdb

File Name: tables

Author: Zachary Romer, zach@scharp.org

Creation Date: 8/24/19

Version: 1.0

Purpose:

Special Notes:

"""
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Boolean, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DateTime
from sqlalchemy.dialects.postgresql import JSONB
from marshmallow_sqlalchemy import ModelSchema

metadata = MetaData()
Base = declarative_base(metadata=metadata)

def get_engine():
    engine = create_engine('postgresql://zach:buttmudd14@localhost:5432/fastq_registrar_dev', echo=True)

class PlantType(Base):

    __tablename__ = 'something.planted'

    id = Column(Integer, Sequence('plant_type_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    subspecies = Column(String, nullable=True)
    suggested_sun_reqs = Column(JSONB, nullable=True)
    suggested_harvest_reqs = Column(JSONB, nullable=True)
    grown_before = Column(Boolean, nullable=True)
    native_to = Column(String, nullable=True)
    notes = Column(String, nullable=True)

    def __repr__(self):
        return f"<PlantType>(id='%s', name='%s', species='%s', subspecies='%s', suggested_sun_reqs='%s', suggested_harvest_reqs='%s'," \
               " grown_before='%s', native_to='%s', notes='%s'" % (self.id, self.name, self.species, self.subspecies,
                                                                   self.suggested_sun_reqs, self.suggested_harvest_reqs,
                                                                   self.grown_before, self.native_to, self.notes)

class PlantTypeSchema(ModelSchema):
    class Meta:
        mode = PlantType


if __name__ == '__main__':
    get_engine()