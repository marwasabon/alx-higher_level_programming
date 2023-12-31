#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # create session maker
    Session = sessionmaker(bind=engine)
    newObj = State(name='Louisiana')
    session = Session()
    session.add(newObj)
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)
    session.commit()
