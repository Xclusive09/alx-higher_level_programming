#!/usr/bin/python3

# Write a script that lists all cities from the database hbtn_0e_4_usa:
# Your script should take 3 arguments:
#  mysql username, 
#  mysql password and
#   database name

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user = sys.argv[1],
        passwd = sys.argv[2],
        db = sys.argv[3]
    )
    
def data():
    return db


cursor = data().cursor()
cursor.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name`  \
FROM `cities` as `c` \
    INNER JOIN `states` as `s` \
        ON `c`.`state_id` = `s`.`id` \
            ORDER BY `c`.`id`")
            
base = cursor.fetchall()

for city in base :
    print(city)