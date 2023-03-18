#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Set up connection to the database
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(db_username, db_password, db_name),
                           pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session to communicate with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to retrieve all City objects and print them out
    for state, city in session.query(State, City)\
            .filter(State.id == City.state_id)\
            .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
