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

metadata = MetaData()
Base = declarative_base(metadata=metadata)

def get_engine():
    engine = create_engine('postgresql://zach:buttmudd14@localhost:5432/fastq_registrar_dev', echo=True)

class PlantType(Base):

    __tablename__ = 'something.planted'

    id = Column(Integer, Sequence('plant_type_id_seq'), primary_key=True)
    name = Column(String)
    species = Column(String)
    subspecies = Column(String)
    suggested_sun_reqs = Column(JSONB)
    suggested_harvest_reqs = Column(JSONB)
    grown_before = Column(Boolean)
    native_to = Column(String)
    notes = Column(String)

    def __repr__(self):
        return f"<PlantType>(id='%s', name='%s', species='%s', subspecies='%s', suggested_sun_reqs='%s', suggested_harvest_reqs='%s'," \
               " grown_before='%s', native_to='%s', notes='%s'" % (self.id, self.name, self.species, self.subspecies,
                                                                   self.suggested_sun_reqs, self.suggested_harvest_reqs,
                                                                   self.grown_before, self.native_to, self.notes)

if __name__ == '__main__':
    get_engine()