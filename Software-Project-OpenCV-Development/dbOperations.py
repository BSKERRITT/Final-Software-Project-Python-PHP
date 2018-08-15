import pymysql.cursors

def updateDB():
    
    # Connect to the database
    db = pymysql.connect("192.168.1.6","root","","puzluk_db" )
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Prepare SQL query to UPDATE required records
    sql = "UPDATE users SET object_identified = 2 WHERE name = '%s'" % ('Morty') # Need to set this to the logged in user.

    try: 
        # Execute the SQL command
        cursor.execute(sql)
        
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
     
        # disconnect from server
        db.close()


def readDB():
    # Connect to the database
    db = pymysql.connect("192.168.1.6","root","","puzluk_db" )
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Prepare SQL query to UPDATE required records
    sql = "SELECT fruit_selection FROM users WHERE name = '%s'" % ('Morty')  # Need to set this to the logged in user.
        
    
    # Execute the SQL command
    cursor.execute(sql)
   
    result = cursor.fetchall()
    for row in result:
        fruitNum = row[0]
        print fruitNum
        return fruitNum;
    
        # disconnect from server
        db.close()

#Invoke the functions
updateDB()
readDB()
   


