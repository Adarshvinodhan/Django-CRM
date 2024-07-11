import mysql.connector


dataBase = mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd ='14118198'

)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE adarsh")
print("Done")

