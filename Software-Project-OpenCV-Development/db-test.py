# import the necessary packages

import pymysql

# Connect to the database

db = pymysql.connect("192.168.1.7","root","","puzluk_db" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT name, surname FROM users")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()

for firstname, lastname in data:
        print "User names from PuzNLuk : %s %s" % (firstname, lastname)

# disconnect from server
db.close()
