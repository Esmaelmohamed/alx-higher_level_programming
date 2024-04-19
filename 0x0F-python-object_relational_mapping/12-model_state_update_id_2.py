#!/usr/bin/python3
"""Update the name of a state in the database"""
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

    # Query the state with ID 2
    states = session.query(State).filter(State.id == 2).all()

    # If the state with ID 2 exists, update its name to "New Mexico"
    if states:
        states[0].name = "New Mexico"
    
    # Commit the session to save the changes to the database
    session.commit()

    # Close the session
    session.close()
