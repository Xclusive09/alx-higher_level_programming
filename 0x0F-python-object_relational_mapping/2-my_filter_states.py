#!/usr/bin/python3

"""
Write a script that takes in an argument
 and displays all values in the states table 
 of hbtn_0e_0_usa where name matches the argument.

 Your script should take 4 arguments: 
 mysql username,
  mysql password,
 database name and state name searched 
"""

import sys
import MySQLdb

if __name__ == "__main__":
   db = sys.argv[3] = MySQLdb.connect(
        user = sys.argv[0],
        port = 3306,
        host = "localhost",
        passwd = sys.argv[2]
    )
def test():
    return db


c = test().cursor()
c.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(sys.argv[4]))
states = c.fetchall()
for state in states:
    if state[1] == sys.argv[4]:
        print(state)
c.close()
db.close()

