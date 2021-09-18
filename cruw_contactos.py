import mysql.connector
import hashlib

db = mysql.connector.connect(
    host='127.0.0.1',
    user='juan',
    password='123456',
    database='parcial1_lenguaje4',
    port=3308

)
def crearUser(nombre, email, password):
    cursor = db.cursor()

    cursor.execute('''insert into
    usuarios(nombre, email, password)
    values(%s, %s, %s)''',(
        nombre,
        email, 
        password
    ))
    
    db.commit()
    cursor.close() 
h = hashlib.new("sha1", b"4123")
crearUser('juanpiz','jupa24609@gmail.com','42131')
cursor = db.cursor()
cursor.execute('select * from usuarios')
usuarios = cursor.fetchall()
print(usuarios)