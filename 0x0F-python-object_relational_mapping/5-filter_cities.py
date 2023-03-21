#!/usr/bin/python3


# Write a script that takes in the name of a state as an argument
#  and lists all cities of that state,
#   using the database hbtn_0e_4_usa

# Your script should take 4 arguments:
#  mysql username,
#   mysql password,
#    database name and
#     state name (SQL injection free!)

import sys
import MySQLdb

if __name__ == "__main__" :
    db = MySQLdb.connect(
        user = sys.argv[1],
        db = sys.argv[2],
        passwd = sys.argv[3],
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `cities` as `c` \
        INNER JOIN `states` as `s` \
            ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print (", ".join([ct[2] for ct in cursor.fetchall() if ct[4] == sys.argv[4]]))
    
