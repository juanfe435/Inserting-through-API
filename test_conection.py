import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kiwi2223",
        database="prueba"
    )
    if connection.is_connected():
        print("Conexión exitosa a la base de datos MySQL")
except mysql.connector.Error as e:
    print(f"Error al conectar a MySQL: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Conexión cerrada")
