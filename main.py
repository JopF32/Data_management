import os
import pandas as pd
from sqlalchemy import create_engine
from models import Base, Asignatura, Estudiante, Inscripcion
from database_setup import session, engine
from ejercicios import ejercicio_1, ejercicio_2

Base.metadata.create_all(engine)


def cargar_datos_csv():
    data_path = os.path.join(os.path.dirname(__file__), "data")

    if session.query(Inscripcion).count() > 0:
        respuesta = input(
            "La tabla Inscripcion ya tiene datos. ¿Desea borrarlos? (s/n): "
        )
        if respuesta.lower() == "s":
            session.query(Inscripcion).delete()
            session.commit()
            print("Datos de Inscripcion eliminados.")
        else:
            print("No se eliminaron los datos de Inscripcion.")
            return

    if session.query(Asignatura).count() > 0:
        respuesta = input(
            "La tabla Asignaturas ya tiene datos. ¿Desea borrarlos? (s/n): "
        )
        if respuesta.lower() == "s":
            session.query(Asignatura).delete()
            session.commit()
            print("Datos de Asignaturas eliminados.")
        else:
            print("No se eliminaron los datos de Asignaturas.")
            return

    if session.query(Estudiante).count() > 0:
        respuesta = input(
            "La tabla Estudiantes ya tiene datos. ¿Desea borrarlos? (s/n): "
        )
        if respuesta.lower() == "s":
            session.query(Estudiante).delete()
            session.commit()
            print("Datos de Estudiantes eliminados.")
        else:
            print("No se eliminaron los datos de Estudiantes.")
            return

    asignaturas_csv = os.path.join(data_path, "Asignaturas.csv")
    df_asignaturas = pd.read_csv(asignaturas_csv)
    for _, row in df_asignaturas.iterrows():
        asignatura = Asignatura(
            asignatura_id=int(row["asignatura_id"]),
            nombre=row["nombre"],
            semestre=row["Semestre"],
        )
        session.add(asignatura)

    estudiantes_csv = os.path.join(data_path, "Estudiantes.csv")
    df_estudiantes = pd.read_csv(estudiantes_csv)
    for _, row in df_estudiantes.iterrows():
        estudiante = Estudiante(
            numero_cuenta=int(row["numero_cuenta"]), nombre=row["nombre"]
        )
        session.add(estudiante)

    inscripcion_csv = os.path.join(data_path, "Inscripcion.csv")
    df_inscripcion = pd.read_csv(inscripcion_csv)

    for _, row in df_inscripcion.iterrows():
        inscripcion = Inscripcion(
            curso_id=int(row["curso_id"]),
            calificacion=int(row["calificacion"]),
            num_cuenta=int(row["num_cuenta"]),
            asignatura_id=int(row["asignatura_id"]),
        )
        session.add(inscripcion)

    try:
        session.commit()
        print("Datos cargados exitosamente desde los archivos CSV.")
    except Exception as e:
        session.rollback()
        print(f"Ocurrió un error al cargar los datos: {e}")


def mostrar_menu():
    print("\n--- Menú de Actividades ---")
    print("1. Cargar datos de archivos")
    print("2. Ejecutar ejercicio 1")
    print("3. Ejecutar ejercicio 2")
    print("4. Salir")
    print("---------------------------")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_datos_csv()
        elif opcion == "2":
            ejercicio_1()
        elif opcion == "3":
            ejercicio_2()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
