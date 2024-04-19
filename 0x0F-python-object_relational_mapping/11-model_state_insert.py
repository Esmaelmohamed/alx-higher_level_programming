#!/usr/bin/python3
"""Add a new state to the database and print its ID"""
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

    # Create a new State object and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)

    # Commit the session to save the changes to the database
    session.commit()

    # Print the ID of the newly added state
    print(new_state.id)

    # Close the session
    session.close()
