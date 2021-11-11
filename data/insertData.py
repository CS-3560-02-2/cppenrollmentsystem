import sqlite3

conn = sqlite3.connect(":memory") #what to connect to
cursor = conn.cursor() #used to query
#""" doc string

# cursor.execute("INSERT INTO courses VALUES (1, 'Database', 'learningDatabases', 3, 'CS', 2000 )")
cursor.execute(
    """INSERT INTO students (first_name,last_name,street,city,state,zip_code,phone_number,email,major) VALUES
    ("Rigel","Morales","308-3017 Justo Rd.","Morwell","CT","415018","(712) 592-7514","dis.parturient@protonmail.edu","fermentum"),
    ("Ann","Bolton","6166 Felis St.","Wolfsberg","AK","352627","(606) 582-8587","ut.tincidunt@icloud.edu","mollis"),
    ("Merritt","Foreman","P.O. Box 437, 7411 Etiam St.","Linköping","MD","43281-322","1-453-968-3344","luctus.et@aol.couk","a"),
    ("Basia","Levine","P.O. Box 833, 3593 Mauris St.","Jeju","WY","594586","(372) 355-2365","scelerisque@outlook.com","risus."),
    ("Richard","Leon","Ap #602-8550 Suscipit, Road","La Dorada","UT","9260","1-357-550-4043","sagittis.duis@icloud.edu","posuere,")"""
)
conn.commit()

cursor.execute("INSERT INTO courses VALUES ('Database', 'learningDatabases', 3, 'CS', 2000 )")
        # cursor.execute("SELECT * FROM students WHERE last_name='Morales'")
        # print(cursor.fetchone())
        # cursor.execute("SELECT * FROM courses WHERE course_title='Database'")
        # print(cursor.fetchone())
conn.commit()



conn.close()