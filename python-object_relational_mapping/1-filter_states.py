"""
Script that lists all states with a name starting
with N (case-insensitive) from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute the query to fetch states starting with 'N' (case-insensitive), sorted by id
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' "
        "COLLATE utf8mb4_general_ci ORDER BY id ASC"
    )

    # Fetch all rows from the result set
    rows = cur.fetchall()

    # Print the states in the desired format
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
