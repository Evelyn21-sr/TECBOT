from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UsuarioCreate(BaseModel):
    nombre: str
    correo: EmailStr
    password: str
    rol: str = "aspirante"


class UsuarioOut(BaseModel):
    id: int
    nombre: str
    correo: EmailStr
    rol: str

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class PublicacionCreate(BaseModel):
    titulo: str
    contenido: str
    publico: str = "todos"


class PublicacionOut(BaseModel):
    id: int
    titulo: str
    contenido: str
    categoria: str
    publico: str
    fecha_publicacion: datetime
    activo: bool

    model_config = ConfigDict(from_attributes=True)


class CarreraCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    duracion: Optional[str] = None
    perfil_egreso: Optional[str] = None


class CarreraOut(CarreraCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ConsultaPregunta(BaseModel):
    pregunta: str


class FuenteDocumento(BaseModel):
    titulo: str
    documento: str
    seccion: Optional[str] = None


class ConsultaRespuesta(BaseModel):
    respuesta: str
    fuentes: list[FuenteDocumento]
