import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
)
db_cursor = db.cursor()
db_cursor.execute("create database face_re")
print('connected')