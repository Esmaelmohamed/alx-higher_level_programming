#!/usr/bin/python3
"""List all cities with their corresponding states"""
from sys import argv
from model_state import Base, State  # Assuming model_state contains the definition of State class
from model_city import City  # Assuming model_city contains the definition of City class
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    # Create all tables defined in the Base class (including State and City) in the database
    Base.metadata.create_all(engine)

    # Create a session class bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Query cities with their corresponding states
    results = session.query(City, State).filter(City.state_id == State.id).all()

    # Print the results (city name, city ID, state name)
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Commit the session (unnecessary in this case since no changes were made)
    session.commit()

    # Close the session
    session.close()
