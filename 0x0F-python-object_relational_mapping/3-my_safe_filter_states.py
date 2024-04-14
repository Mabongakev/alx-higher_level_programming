#!/usr/bin/python3
"""list all the states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], password=sys.argv[2], db=sys.argv[3], port=3306)
    curs = db.cursor()
    match_arg = sys.argv[4]
    curs.execute("SELECT * FROM states WHERE name LIKE %s", (match_arg, ))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
