import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Ajustar parametros de acuerdo a su conexión
server = "LAPTOP-27U46USM\\SQLEXPRESS"
database = "RADIUS"


connection_string = f"mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"


engine = create_engine(connection_string)


Session = sessionmaker(bind=engine)
session = Session()


try:
    with engine.connect() as conn:
        print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
