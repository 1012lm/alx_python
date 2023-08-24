#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument (case-sensitive).
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute the query to fetch states matching sorted by id
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch all rows from the result set
    rows = cur.fetchall()

    # Print the states in the desired format
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
