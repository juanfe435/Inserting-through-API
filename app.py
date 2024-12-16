from flask import Flask, request, jsonify
import os
from utils.db_operations import initialize_database, process_csv_and_insert


app = Flask(__name__)

# Endpoint raíz para verificar si la API está activa
@app.route('/')
def home():
    return "API Running. Use /upload_csv to upload CSV files."

# Endpoint para subir archivos CSV
@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    # Validar si se subió un archivo
    file = request.files.get('file')
    if not file or file.filename == '':
        return jsonify({"error": "No file provided"}), 400

    # Guardar el archivo temporalmente
    file_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(file_path)

    # Procesar el archivo e insertar los datos
    try:
        initialize_database()  # Inicializa la base de datos si no existe
        process_csv_and_insert(file_path)  # Procesa e inserta los datos del CSV
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        os.remove(file_path)  # Eliminar el archivo después de procesarlo

    return jsonify({"message": f"CSV {file.filename} uploaded successfully"}), 200

# Iniciar la aplicación
if __name__ == '__main__':
    # Verificar la conexión antes de levantar el servidor
    try:
        initialize_database()  # Confirma que la base de datos existe y está accesible
        print("Conexión inicial a la base de datos exitosa.")
    except Exception as e:
        print(f"Error en la conexión inicial: {e}")
        exit(1)  # Termina el programa si la conexión falla

    app.run(debug=True)