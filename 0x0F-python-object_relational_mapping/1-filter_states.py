#!/usr/bin/python3
'''
Create a conection and list states with
capital N
'''
import MySQLdb
import sys


def mysqlconnect():
    db_connection = None
    db_connection = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name REGEXP '^N'")
    states = cursor.fetchall()

    for state in states:
        print(state)

if __name__ == '__main__':
    mysqlconnect()
