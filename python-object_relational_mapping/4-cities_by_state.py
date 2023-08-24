#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Get MySQL credentials and database name from command-line
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

    # Execute the query to fetch all cities joined sorted by cities.id
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(query)

    # Fetch all rows from the result set
    rows = cur.fetchall()

    # Print the cities with their corresponding state names in the desired
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
