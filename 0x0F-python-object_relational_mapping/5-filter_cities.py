#!/usr/bin/python3
"""Lists cities within a given state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
        )
        
        # Create a cursor object to interact with the database
        cur = conn.cursor()

        # Define the SQL query to retrieve cities within the given state
        query = """
            SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """

        # Execute the SQL query with the provided state name as a parameter
        cur.execute(query, (argv[4],))

        # Fetch all rows and extract city names
        cities = [row[0] for row in cur.fetchall()]

        # Print the city names as a comma-separated list
        print(", ".join(cities))

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close cursor and database connection
        cur.close()
        conn.close()
