#!/usr/bin/python3
"""Lists states from the database"""

import MySQLdb
from sys import argv

def list_states(username, password, database):
    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=database, charset="utf8")
        cur = conn.cursor()

        # Execute SQL query to retrieve states
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        
        # Fetch all rows and print results
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        # Close cursor and database connection
        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        return None

if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        exit(1)
    
    # Extract arguments
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # Call function to list states
    list_states(username, password, database)
