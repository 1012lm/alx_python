#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Get MySQL credentials, database name, and state name from command-line
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

    # Execute the query to fetch cities of the given state sorted by cities.id
    query = """
    SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Fetch the result
    result = cur.fetchone()[0]

    # Print the cities of the given state
    if result:
        print(result)
    else:
        print("No cities found for the given state.")

    # Close the cursor and database connection
    cur.close()
    db.close()
