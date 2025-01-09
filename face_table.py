import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="face_re"
)
db_cursor = db.cursor()
#db_cursor.execute('ALTER TABLE attendance RENAME TO Student;')

db_cursor.execute("create table Student(Enrollment_No varchar(250) NOT NULL, "
                  "NAME varchar(250) NOT NULL, "
                  "PHOTO LONGBLOB NOT NULL)")
print("Attendace recor deleted")