from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales de las variables de entorno
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
db = os.getenv('POSTGRES_DB')
host = os.getenv('POSTGRES_HOST', 'localhost')

# Crear la cadena de conexión utilizando las variables de entorno
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{db}')

# Ejemplo de uso: Ejecutar una consulta simple
def test_connection():
    query = text("SELECT 1")
    with engine.connect() as connection:
        result = connection.execute(query)
        print(result.fetchall())

# Llamada de prueba
if __name__ == "__main__":
    test_connection()
