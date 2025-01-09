import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertLONGBLOB(Enrollment_No, NAME , PHOTO):
    print("Inserting LONGBLOB into Attendance table")
    try:
        connection = mysql.connector.connect( host="localhost",
                                              user="root",
                                              passwd="12345",
                                              database="face_re")

        cursor = connection.cursor()
        sql_insert_longblob_query = """ INSERT INTO Attendance(Enrollment_No, NAME , PHOTO) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(PHOTO)

        # Convert data into tuple format
        insert_longblob_tuple = (Enrollment_No, NAME, empPicture)
        result = cursor.execute(sql_insert_longblob_query, insert_longblob_tuple)
        connection.commit()
        print("Image inserted successfully as a LOPNGBLOB into Attendance table", result)

    except mysql.connector.Error as error:
        print("Failed inserting LONGBLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertLONGBLOB("0808CS223d09", "Naman Saxena","C:\\Extra\\Python\\FaceRecognitionProject\\ImagesAttendance\\Naman.jpg")
insertLONGBLOB("0808CS223d09", "Kalash Upadhyay", "C:\Extra\Python\FaceRecognitionProject\ImagesAttendance\Kalash.jpg")
insertLONGBLOB("0808CS211077","Isha Sharma", "C:\Extra\Python\FaceRecognitionProject\ImagesAttendance\Isha.jpg")
insertLONGBLOB("0808CS223d06","Falguni Verma","C:\Extra\Python\FaceRecognitionProject\ImagesAttendance\Falguni.jpg")
