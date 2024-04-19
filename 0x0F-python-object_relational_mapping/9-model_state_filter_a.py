#!/usr/bin/python3
"""List all states whose names contain the letter 'a'"""
from sys import argv
from model_state import Base, State  # Assuming model_state contains the definition of State class
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    # Create all tables defined in the Base class (including State) in the database
    Base.metadata.create_all(engine)

    # Create a session class bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Query all states whose names contain the letter 'a' and print their id and name
    for state in session.query(State).filter(State.name.like('%a%')).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
