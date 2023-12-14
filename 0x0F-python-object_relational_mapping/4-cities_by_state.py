#!/usr/bin/python3
"""  Scritp to list all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    """  Scritp to list all states from the database hbtn_0e_0_usa """
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    # defie db cursor
    cursor = db.cursor()
    cursor.execute(
            """
            SELECT cities.id, cities.name, states.name
            FROM cities INNER JOIN states ON states.id = cities.id
            """
            )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()