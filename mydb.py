import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '14118198',

)


cursorobject = database.cursor()

cursorobject.execute("create database mycompany")
print("done")