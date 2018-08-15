import pymysql.cursors

def readDB():
    # Connect to the database
    db = pymysql.connect("192.168.1.14","root","","puzluk_db" )
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Prepare SQL query to UPDATE required records
    sql = "SELECT game1_fruit_selected FROM users WHERE avatar = '%s'" % ('Bats')  # Need to set this to the logged in user.       
    
    # Execute the SQL command
    cursor.execute(sql)
   
    result = cursor.fetchall()
    for row in result:
        fruitNum = row[0]
        return fruitNum;
    
        # disconnect from server
        db.close()

#Invoke the functions
readDB()
   


