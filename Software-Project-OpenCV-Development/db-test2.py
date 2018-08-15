import pymysql

# Connect to the database
db = pymysql.connect("192.168.1.11","root","","puzluk_db" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

def read_db():
    # Prepare SQL query to UPDATE required records
    sql = "SELECT fruit_selection FROM users WHERE name = '%s'" % ('Rick')  # Need to set this to the logged in user.
    
    # Execute the SQL command
    cursor.execute(sql)
   
    result = cursor.fetchall()
    for row in result:
        fruitNum = row[0]
        print fruitNum
    
    return fruitNum;

read_db()
# disconnect from server
db.close()
