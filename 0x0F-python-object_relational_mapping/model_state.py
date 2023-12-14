#!/usr/bin/python3
"""ORM class to connect to table in database
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.
            format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create a base class for declarative models
    Base = declarative_base()
    # Define a model for the states table

    class State(Base):
    """ORM class to connect to table in database"""
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
    print(engine)
