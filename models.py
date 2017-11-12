import os
import sys
import config

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine

Base = declarative_base()

class Guest(Base):
  __tablename__ = 'guests'

  id = Column(Integer, primary_key=True)
  first_name = Column(String(250), nullable=False)
  last_name = Column(String(250), nullable=False)
  additional_guest = Column(Boolean, default=False)
  ag_first_name = Column(String(250))
  ag_last_name = Column(String(250))

  def __repr__(self):
    return "<User(first_name={0}, last_name={1}, additional_guest={2}".format(
      self.first_name, self.last_name, self.additional_guest)

  @property
  def serialize(self):
    #Returns object data in easily serializable format
    return {
      'id': self.id,
      'first_name': self.first_name,
      'last_name': self.last_name,
      'additional_guest': self.additional_guest,
      'ag_first_name': self.ag_first_name,
      'ag_last_name': self.ag_last_name,
    }

#This is required to create the table itself
dbURI = os.environ['DATABASE_URL']
engine = create_engine(dbURI)

Base.metadata.create_all(engine)