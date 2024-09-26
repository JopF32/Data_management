from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Asignatura(Base):
    __tablename__ = "asignaturas"

    asignatura_id = Column(Integer, primary_key=True)
    nombre = Column(String)
    semestre = Column(Integer)

    inscripciones = relationship("Inscripcion", back_populates="asignatura")


class Estudiante(Base):
    __tablename__ = "estudiantes"

    numero_cuenta = Column(Integer, primary_key=True)
    nombre = Column(String)

    inscripciones = relationship("Inscripcion", back_populates="estudiante")


class Inscripcion(Base):
    __tablename__ = "inscripciones"

    curso_id = Column(Integer, primary_key=True)
    calificacion = Column(Integer)
    num_cuenta = Column(Integer, ForeignKey("estudiantes.numero_cuenta"))
    asignatura_id = Column(Integer, ForeignKey("asignaturas.asignatura_id"))

    estudiante = relationship("Estudiante", back_populates="inscripciones")
    asignatura = relationship("Asignatura", back_populates="inscripciones")
