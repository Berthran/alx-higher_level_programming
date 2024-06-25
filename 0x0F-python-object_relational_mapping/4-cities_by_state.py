#!/usr/bin/python3
"""
Module Name: 4-cities_by_state.py

Description:
This module interacts with a MySQL database to retrieve a list of all cities.

Functions:
- get_all_cities(host, user, password):
    Retrieves a list of all cities from a MySQL database.

Usage:
This module requires the MySQLdb package and provides a function to
fetch all states from a MySQL database.

Example:
import MySQLdb

"""

import sys
import MySQLdb


def get_all_cities():
    """Retrieves a list of all cities from a MySQL database.

    Args:
        host (str): The hostname or IP address of the MySQL server.
        user (str): The username to connect to the MySQL server.
        password (str): The password for the specified user.

    Returns:
        list: A list of strings representing all cities.
    """
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
    except Exception:
        pass

    # Establish connection to a MySQL database
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=db_name,
                           charset="utf8")

    # Set cursor position
    cur = conn.cursor()
    query1 = "SELECT cities.id, cities.name, states.name FROM cities "
    query2 = "JOIN states on cities.state_id = states.id "
    query3 = "order by cities.state_id, states.id;"
    query = query1 + query2 + query3
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    get_all_cities()
