from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text

from .database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    rol = Column(String(30), nullable=False, default="aspirante")
    # Roles: aspirante, estudiante, docente, egresado, admin


class Publicacion(Base):
    __tablename__ = "publicaciones"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    contenido = Column(Text, nullable=False)
    categoria = Column(String(50), nullable=False, index=True)
    # Categorías: noticia, aviso, convocatoria, evento, beca, recurso, servicio
    publico = Column(String(100), nullable=False, default="todos")
    # "todos" o roles separados por coma: "estudiante,docente"
    fecha_publicacion = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    activo = Column(Boolean, default=True)


class Carrera(Base):
    __tablename__ = "carreras"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), unique=True, nullable=False)
    descripcion = Column(Text)
    duracion = Column(String(50))
    perfil_egreso = Column(Text)
