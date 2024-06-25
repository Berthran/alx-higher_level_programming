#!/usr/bin/python3
"""
Module Name: 0-select_states.py

Description:
This module interacts with a MySQL database to retrieve a list of all states.

Functions:
- get_all_states(host, user, password):
    Retrieves a list of all states from a MySQL database.

Usage:
This module requires the MySQLdb package and provides a function to
fetch all states from a MySQL database.

Example:
import MySQLdb

"""

import sys
import MySQLdb


def get_all_states():
    """Retrieves a list of all states from a MySQL database.

    Args:
        host (str): The hostname or IP address of the MySQL server.
        user (str): The username to connect to the MySQL server.
        password (str): The password for the specified user.

    Returns:
        list: A list of strings representing all states.
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
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    get_all_states()
