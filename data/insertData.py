import sqlite3
from db import DB_PATH

conn = sqlite3.connect(DB_PATH) #what to connect to, memory just put a fresh one in ram so it won't need to worry about duplications
cursor = conn.cursor() #used to query

def insert_students():
    with conn: #with is a context manager where you do not need to do conn commit after every execution
        cursor.execute(
        """INSERT INTO students (first_name,last_name,street,city,state,zip_code,phone_number,email,major) VALUES
        ("Rigel","Morales","308-3017 Justo Rd.","Morwell","CT","415018","(712) 592-7514","dis.parturient@protonmail.edu","fermentum"),
        ("Ann","Bolton","6166 Felis St.","Wolfsberg","AK","352627","(606) 582-8587","ut.tincidunt@icloud.edu","mollis"),
        ("Merritt","Foreman","P.O. Box 437, 7411 Etiam St.","Linköping","MD","43281-322","1-453-968-3344","luctus.et@aol.couk","a"),
        ("Basia","Levine","P.O. Box 833, 3593 Mauris St.","Jeju","WY","594586","(372) 355-2365","scelerisque@outlook.com","risus."),
        ("Richard","Leon","Ap #602-8550 Suscipit, Road","La Dorada","UT","9260","1-357-550-4043","sagittis.duis@icloud.edu","posuere,")"""
        )


def insert_instructors():
    with conn:
        cursor.execute(
            """INSERT INTO instructors (first_name,last_name,street,city,state,zip_code,phone_number,email,major) VALUES
            ("Lavinia","Haney","1354 Vitae Ave","HŽron","WA","71836","1-785-724-4184","lacinia@icloud.net","Engineering,"),
            ("Noah","Suarez","569-7471 Sed Street","San Juan del Río","LA","36049","1-396-743-1972","placerat@google.org","Liberal Arts"),
            ("Asher","Perry","5034 Scelerisque, Rd.","Sclayn","MD","121185","1-682-786-5048","sagittis.semper@yahoo.org","Science"),
            ("Rama","Kramer","Ap #263-4014 Dignissim Street","Łomża","WY","50628","1-651-228-8212","curabitur.sed@protonmail.org","Math,"),
            ("Rebecca","Cantu","5277 Placerat St.","Woodstock","LA","1085","1-311-158-3438","vulputate.ullamcorper@hotmail.com","Technology")"""
        )


conn.close()