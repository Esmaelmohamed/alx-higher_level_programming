#!/usr/bin/python3
"""Lists states whose names start with 'N' from the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Execute SQL query to retrieve states starting with 'N'
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all rows that start with 'N'
    query_rows = cur.fetchall()
    
    # Iterate over the query results and print the states starting with 'N'
    for row in query_rows:
        if row[1].startswith("N"):
            print(row)

    # Close cursor and database connection
    cur.close()
    conn.close()
