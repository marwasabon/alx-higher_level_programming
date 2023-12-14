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
    val = sys.argv[4]
    cursor.execute(
            """
            SELECT cities.name FROM
            cities INNER JOIN states ON states.id = cities.state_id
            WHERE states.name=%s""", (val,))
    rows = cursor.fetchall()
    mylist_val = list(row[0] for row in rows)
    print(*mylist_val, sep=", ")
    cursor.close()
    db.close()
