import os
import pandas as pd
from sqlalchemy import func, text
from models import Inscripcion, Estudiante
from database_setup import session
from queries import query_1, query_2


def ejercicio_1():
    sql_query = query_1

    resultados = session.execute(text(sql_query)).fetchall()

    df_alumnos = pd.DataFrame(
        resultados,
        columns=[
            "nombre_alumno",
            "nombre_materia",
            "calificacion",
            "calificacion_promedio",
            "bandera1",
        ],
    )

    alumnos_mayor_promedio = df_alumnos[df_alumnos["bandera1"] == 1]

    ruta_respuesta = os.path.join(os.path.dirname(__file__), "respuesta")
    os.makedirs(ruta_respuesta, exist_ok=True)

    alumnos_mayor_promedio.to_csv(
        os.path.join(ruta_respuesta, "alumnos_mayor_promedio.csv"), index=False
    )

    print(
        "Ejercicio 1 ejecutado y resultados guardados en 'respuesta/alumnos_mayor_promedio.csv'."
    )


def ejercicio_2():

    sql_query = query_2
    resultados = session.execute(text(sql_query)).fetchall()

    df_avance = pd.DataFrame(
        resultados,
        columns=[
            "nombre_alumno",
            "total_materias_cursadas",
            "total_materias",
            "porcentaje_avance",
            "bandera_calificacion",
        ],
    )

    df_avance["porcentaje_avance"] = pd.to_numeric(
        df_avance["porcentaje_avance"], errors="coerce"
    )

    top_10 = df_avance.nlargest(10, "porcentaje_avance")
    bottom_10 = df_avance.nsmallest(10, "porcentaje_avance")

    ruta_respuesta = os.path.join(os.path.dirname(__file__), "respuesta")
    os.makedirs(ruta_respuesta, exist_ok=True)

    top_10.to_csv(os.path.join(ruta_respuesta, "top_10_alumnos.csv"), index=False)
    bottom_10.to_csv(os.path.join(ruta_respuesta, "bottom_10_alumnos.csv"), index=False)

    print("CSV generados con éxito en la carpeta 'respuesta'.")
