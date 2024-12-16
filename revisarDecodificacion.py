import chardet

# Reemplaza 'archivo.csv' con la ruta a tu archivo
file_path = r"C:\Users\ASUS\OneDrive\Documentos\Data-Analyst-Challenge\Inserting through API\data\datos.csv"

with open(file_path, 'rb') as f:
    result = chardet.detect(f.read())
    print(f"La codificación detectada es: {result['encoding']}")
