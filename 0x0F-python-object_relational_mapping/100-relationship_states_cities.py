#!/usr/bin/python3
'''
Changes the name of a State object
'''
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    creState = State(name='California')
    creCity = City(name='San Francisco')

    creState.cities.append(creCity)

    session.add(creState)
    session.add(creCity)
    session.commit()
