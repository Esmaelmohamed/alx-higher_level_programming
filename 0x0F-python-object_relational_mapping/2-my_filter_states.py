#!/usr/bin/python3
"""
Lists states whose names match a given pattern from the database.
The pattern is passed as an argument to the script.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Define the SQL query to retrieve states matching the pattern
    query = """
            SELECT * FROM states 
            WHERE name LIKE BINARY '{}' 
            ORDER BY states.id ASC
            """.format(argv[4])

    # Execute the SQL query
    cur.execute(query)

    # Fetch all rows that match the query
    query_rows = cur.fetchall()
    
    # Iterate over the query results and print the matching states
    for row in query_rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    conn.close()
