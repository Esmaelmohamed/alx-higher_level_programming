#!/usr/bin/python3
"""Lists states whose names match a given name from the database"""

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

        # Define the SQL query to retrieve states with the given name
        query = """
            SELECT * FROM states 
            WHERE name = %s 
            ORDER BY states.id ASC
            """
        
        # Execute the SQL query with the provided name as a parameter
        cur.execute(query, (argv[4],))

        # Fetch all rows that match the query
        query_rows = cur.fetchall()

        # Iterate over the query results and print the matching states
        for row in query_rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close cursor and database connection
        cur.close()
        conn.close()
