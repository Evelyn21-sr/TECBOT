from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Publicacion
from ..schemas import PublicacionCreate, PublicacionOut
from ..security import get_current_user

router = APIRouter(prefix="/servicios", tags=["Servicios"])
CATEGORIA = "servicio"


@router.get("/", response_model=list[PublicacionOut])
def listar(db: Session = Depends(get_db)):
    return (
        db.query(Publicacion)
        .filter(Publicacion.categoria == CATEGORIA, Publicacion.activo.is_(True))
        .order_by(Publicacion.fecha_publicacion.desc())
        .all()
    )


@router.post("/", response_model=PublicacionOut)
def crear(
    datos: PublicacionCreate,
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user),
):
    if usuario.rol not in ("admin", "docente"):
        raise HTTPException(status_code=403, detail="No autorizado")

    valores = datos.model_dump()
    valores["categoria"] = CATEGORIA
    publicacion = Publicacion(**valores)

    db.add(publicacion)
    db.commit()
    db.refresh(publicacion)
    return publicacion
