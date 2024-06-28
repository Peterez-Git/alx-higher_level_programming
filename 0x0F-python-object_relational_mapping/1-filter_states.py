#!/usr/bin/python3
"""  a script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa:  """
import MySQLdb
import sys


if __name__ == "main":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
