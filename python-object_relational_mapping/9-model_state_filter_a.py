#!/usr/bin/python3
"""
objects that contain the letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine and establish the database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Query State objects that contain the letter 'a' and sort them
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Print the State objects
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
