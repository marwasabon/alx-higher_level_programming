#!/usr/bin/python3
"""ORM class to connect to table in database
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String,MetaData
from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()
# Create a base class for declarative models
Base = declarative_base(metadata=metadata)
# Define a model for the states table

class State(Base):
    """ORM class to connect to table in database"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
