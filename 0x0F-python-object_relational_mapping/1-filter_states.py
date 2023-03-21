#!/usr/bin/python3

"""
Write a script that lists all states with a name
 starting with N (upper N) from the database 
 hbtn_0e_0_usa:

 Your script should take 3 arguments: 
 mysql username,
  mysql password and 
  database name

"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[0],
        passwd=sys.argv[1],
        db=sys.argv[2]
    )
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")

    sts = c.fetchall()

   
    [print(state) for state in sts if state[1] [0] == "N"]