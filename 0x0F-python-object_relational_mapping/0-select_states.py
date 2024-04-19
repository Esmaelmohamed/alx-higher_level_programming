import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost",
                             user=username,
                             passwd=password,
                             db=database,
                             port=3306)
        cursor = db.cursor()

        # Execute SQL query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        
        # Fetch all rows and print results
        states = cursor.fetchall()
        for state in states:
            print(state)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)
    
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call function to list states
    list_states(username, password, database)
