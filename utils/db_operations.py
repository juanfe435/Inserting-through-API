import mysql.connector
import csv
import os

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="kiwi2223",
        database="prueba",
        charset="utf8mb4"
    )

def initialize_database():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS prueba")
    cursor.execute("USE prueba")
    cursor.close()
    connection.close()

def process_csv_and_insert(file_path):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Abre el archivo CSV con codificación UTF-8
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)

            # Crear nombre de la tabla basado en el archivo
            table_name = os.path.splitext(os.path.basename(file_path))[0].replace(" ", "_").replace("-", "_")

            # Crear columnas dinámicamente basadas en los encabezados del CSV
            columns = ", ".join([
                f"`{col}` TEXT" if col.lower() == 'description' else f"`{col}` VARCHAR(255)"
                for col in header
            ])
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")

            # Inserta los datos
            placeholders = ', '.join(['%s'] * len(header))
            sql_insert = f"INSERT INTO {table_name} VALUES ({placeholders})"
            for row in reader:
                # Limpia y procesa cada fila
                cleaned_row = [
                    None if value.strip() in ("", "NULL") else value.strip() for value in row
                ]
                cursor.execute(sql_insert, cleaned_row)

            connection.commit()
            print(f"Datos insertados correctamente en la tabla '{table_name}'.")
    except Exception as e:
        connection.rollback()
        print(f"Error al insertar los datos: {e}")
    finally:
        cursor.close()
        connection.close()
