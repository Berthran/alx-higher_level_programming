#!/usr/bin/python3
"""
Module Name: 2-my_filter_states.py

Description:
This module interacts with a MySQL database to retrieve a list of states that
macthes a given name.

Functions:
- get_my_states(host, user, password, name):
    Retrieves a list of states that macthes a given name.

Usage:
This module requires the MySQLdb package and provides a function to
fetch all states from a MySQL database.

Example:
import MySQLdb

"""

import sys
import MySQLdb


def get_my_states():
    """Retrieves a list of states that macthes a given name.

    Args:
        host (str): The hostname or IP address of the MySQL server.
        user (str): The username to connect to the MySQL server.
        password (str): The password for the specified user.
        name (str): The name of the state to search for

    Returns:
        list: A list of strings representing states matching name.
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
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC;"
    try:
        cur.execute(query.format(state_name))
        states = cur.fetchall()
        for state in states:
            print(state)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    get_my_states()
