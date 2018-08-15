import pymysql.cursors

def updateDB():
    
    # Connect to the database
    db = pymysql.connect("192.168.1.14","root","","puzluk_db" )
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Prepare SQL query to UPDATE required records
    sql = "UPDATE users SET game1_object_identified = 1 WHERE avatar = '%s'" % ('Bats') # Need to set this to the logged in user.

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


#Invoke the functions
updateDB()
   


