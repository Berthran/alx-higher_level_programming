#!/usr/bin/python3
"""
Module Name: 0-select_states.py

Description:
This module interacts with a MySQL database to retrieve a list of all states.

Functions:
- get_all_states(host, user, password):
    Retrieves a list of all states from a MySQL database.

    Args:
        host (str): The hostname or IP address of the MySQL server.
        user (str): The username to connect to the MySQL server.
        password (str): The password for the specified user.

    Returns:
        list: A list of strings representing all states.

Usage:
This module requires the MySQLdb package and provides a function to fetch all states from a MySQL database.

Example:
import MySQLdb

# Fetch all states from the database
states = MySQLdb.get_all_states('localhost', 'user', 'password')

# Print the list of states
print(states)
"""

import sqlalchemy
import MySQLdb
import sys

def get_all_states():
    username = sys.argv[0]
    password = sys.argv[0]
    db_name = sys.argv[0]

    print(dir())
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
    query = "SELECT * FROM states ORDER BY id ASC";
    cur.execute(query)
    query_table = cur.fetchall()
    for row in query_table:
        print(row)

if __name__ == "__main__":
    get_all_states()
