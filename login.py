import mysql.connector


db = mysql.connector.connect(
    host='127.0.0.1',
    user='juan',
    password='123456',
    database='parcial1_lenguaje4',
    port=3308

)
cursor = db.cursor()
cursor.execute('select * from login')
   
print(cursor.fetchall())