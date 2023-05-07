import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1020sigmaligaya0230.09'
    
    )

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE HCPSMSHS_Alumni_DB")
print('All Done')
