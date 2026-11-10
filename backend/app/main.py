from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import (
    auth,
    becas,
    carreras,
    convocatorias,
    eventos,
    noticias,
    recursos,
    servicios,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TECBOT API",
    description="API informativa del Instituto Tecnológico Superior de Santiago Papasquiaro",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(noticias.router)
app.include_router(carreras.router)
app.include_router(convocatorias.router)
app.include_router(eventos.router)
app.include_router(becas.router)
app.include_router(servicios.router)
app.include_router(recursos.router)


@app.get("/")
def inicio():
    return {"mensaje": "API de TECBOT funcionando"}
