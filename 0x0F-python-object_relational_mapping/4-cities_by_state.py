#!/usr/bin/python3
"""Lists cities with their corresponding states"""

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

        # Define the SQL query to retrieve cities with their corresponding states
        query = """
            SELECT cities.id, cities.name, states.name FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """
        
        # Execute the SQL query
        cur.execute(query)

        # Fetch all rows and print the results
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close cursor and database connection
        cur.close()
        conn.close()
