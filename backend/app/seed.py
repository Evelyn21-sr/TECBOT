from .database import Base, SessionLocal, engine
from .models import Carrera, Publicacion, Usuario
from .security import hash_password


def sembrar_datos():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        if db.query(Usuario).count() == 0:
            db.add(
                Usuario(
                    nombre="Administrador TECBOT",
                    correo="admin@tecbot.edu.mx",
                    hashed_password=hash_password("admin123"),
                    rol="admin",
                )
            )

        if db.query(Carrera).count() == 0:
            db.add(
                Carrera(
                    nombre="Ingeniería en Sistemas Computacionales",
                    descripcion="Carrera de ejemplo para el scaffold.",
                    duracion="9 semestres",
                    perfil_egreso="Perfil de egreso de ejemplo.",
                )
            )

        if db.query(Publicacion).count() == 0:
            db.add(
                Publicacion(
                    titulo="Bienvenidos a TECBOT",
                    contenido="Plataforma informativa del ITSSP.",
                    categoria="noticia",
                    publico="todos",
                )
            )

        db.commit()
        print("Datos de ejemplo insertados correctamente.")
    finally:
        db.close()


if __name__ == "__main__":
    sembrar_datos()
