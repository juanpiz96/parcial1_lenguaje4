import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    user='juan',
    password='123456',
    database='parcial1_lenguaje4',
    port=3308

)
def crearUsuario(nombre, email, contrasena):
    cursor = db.cursor()

    cursor.execute('''insert into
    usuarios(nombre, email, contrasena)
    values(%s, %s, %s)''',(
        nombre,
        email, 
        contrasena
    ))
    #creacion, modificacion, eliminacion de datos para
    db.commit()
    cursor.close() 
crearUsuario('juanpa','jupa@gmail.com','1256')
cursor = db.cursor()
cursor.execute('select * from usuarios')
usuarios = cursor.fetchall()
print(usuarios)