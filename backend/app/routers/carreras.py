from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Carrera
from ..schemas import CarreraCreate, CarreraOut
from ..security import get_current_user

router = APIRouter(prefix="/carreras", tags=["Carreras"])


@router.get("/", response_model=list[CarreraOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Carrera).all()


@router.post("/", response_model=CarreraOut)
def crear(
    datos: CarreraCreate,
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user),
):
    if usuario.rol not in ("admin", "docente"):
        raise HTTPException(status_code=403, detail="No autorizado")

    carrera = Carrera(**datos.model_dump())
    db.add(carrera)
    db.commit()
    db.refresh(carrera)
    return carrera
