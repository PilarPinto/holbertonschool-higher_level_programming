#!/usr/bin/python3
'''
 Adds the State object “Louisiana” to the database
'''
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    newS = State(name='Louisiana')
    session.add(newS)
    session.commit()

    print(newS.id)
