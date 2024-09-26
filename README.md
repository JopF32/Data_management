# Data Management Project
Este proyecto tiene como objetivo gestionar datos académicos, ejecutar consultas SQL y realizar análisis utilizando Python, SQLAlchemy y Pandas. El proyecto incluye la generación de CSV con los resultados obtenidos de una base de datos, centrados en la comparación de calificaciones de estudiantes con los promedios de las asignaturas.

```
Data_management/
│
├── queries.py              # Archivo que contiene las consultas SQL.
├── ejercicios.py           # Archivo que contiene las funciones principales que ejecutan las consultas y generan archivos CSV.
├── respuesta/              # Carpeta donde se guardan los resultados en formato CSV.
├── data/                   # Carpeta donde se guardan los archivos de datos csv que se subiran a la base.
├── database_setup.py       # Archivo de conexión a base de datos.
├── models.py               # Definición de las clases y modelos ORM para la base de datos.
├── main.py                 # Punto de entrada principal del proyecto.
├── README.md               # Instrucciones y documentación del proyecto.
└── requirements.txt        # Dependencias del proyecto.
```

# Requisitos
Python 3.8 o superior
SQLAlchemy
Pandas
Motor de base de datos (PostgreSQL, MySQL, etc.)

# Instalación de Dependencias
Para instalar las dependencias necesarias, usa el archivo requirements.txt

# Configuración
Configuración de la base de datos: Debes configurar la conexión a la base de datos en el archivo database_setup.py. Asegúrate de definir correctamente las credenciales para conectarte al motor de base de datos que estés utilizando.

# Funciones Principales
```
* Creación de tablas desde python a la base de datos
* Creación de relaciones de tablas
* Carga de datos desde CSV a base de datos
* Borrado de tablas para evitar carga repetida de datos
```
