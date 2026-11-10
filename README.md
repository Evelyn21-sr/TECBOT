# TECBOT

Plataforma informativa del Instituto Tecnológico Superior de Santiago Papasquiaro,
dirigida a aspirantes, estudiantes, docentes y egresados.

## Contenido

- Noticias y avisos
- Carreras
- Convocatorias
- Eventos
- Becas
- Servicios escolares
- Recursos

## Tecnologías

- Backend: FastAPI + SQLAlchemy + SQLite
- Frontend: React + Vite + React Router

## Estructura

- `backend/`: API REST
- `frontend/`: aplicación web

## Ejecución rápida

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m app.seed
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

- API: http://localhost:8000
- Documentación Swagger: http://localhost:8000/docs
- Frontend: http://localhost:5173
