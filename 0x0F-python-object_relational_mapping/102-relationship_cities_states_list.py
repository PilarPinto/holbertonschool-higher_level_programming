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

    qtwo = session.query(State, City).join(City).order_by(City.id)

    for state, city  in qtwo.all():
        print('{}: {} -> {}'.format(city.id, city.name, state.name))
