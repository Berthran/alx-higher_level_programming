#!/usr/bin/python3
"""
Module Name: 5-filter_cities.py

Description:
This module interacts with a MySQL database to retrieve a list of cities that
are in a given state.

Functions:
- get_my_cities(host, user, password, name):
    Retrieves a list of cities that are in a given state.

Usage:
This module requires the MySQLdb package and provides a function to
fetch all states from a MySQL database.

Example:
import MySQLdb

"""

import sys
import MySQLdb


def get_my_cities():
    """Retrieves a list of cities that are in a given state.

    Args:
        host (str): The hostname or IP address of the MySQL server.
        user (str): The username to connect to the MySQL server.
        password (str): The password for the specified user.
        name (str): The name of the state to search for

    Returns:
        list: A list of strings representing cities in the state.
    """
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
    except Exception:
        exit()

    # Establish connection to a MySQL database
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=db_name,
                           charset="utf8")

    # Set cursor position
    cur = conn.cursor()
    query1 = "SELECT cities.name FROM cities "
    query2 = "JOIN states on cities.state_id = states.id "
    query3 = "WHERE states.name = '{}' ORDER BY cities.id ASC"
    query = query1 + query2 + query3
    try:
        cur.execute(query.format(state_name))
        cities = cur.fetchall()
        for city in cities:
            print(city)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    get_my_cities()
