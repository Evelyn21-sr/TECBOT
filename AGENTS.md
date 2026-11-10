# AGENTS.md

## Project

TECBOT is an informational platform for Instituto Tecnológico Superior de Santiago Papasquiaro, with a FastAPI + SQLite backend and a React + Vite frontend. UI text and code comments are in Spanish.

## Structure

- `backend/app/` — FastAPI app. `main.py` is the entrypoint; `models.py` holds SQLAlchemy models; `schemas.py` holds Pydantic schemas; `security.py` handles JWT and passwords; `routers/` has one router per content category.
- `frontend/src/` — React app. `pages/` has one route per section; `components/` has shared UI; `context/AuthContext.jsx` manages the session.
- Content categories (`noticia`, `convocatoria`, `evento`, `beca`, `servicio`, `recurso`) share the `Publicacion` model and the `ListaPublicaciones` component. Follow `routers/noticias.py` and `pages/Noticias.jsx` when adding one.

## Commands

Backend, from `backend/`:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m app.seed
uvicorn app.main:app --reload
```

Frontend, from `frontend/`:

```bash
npm install
npm run dev
npm run build
```

## Gotchas

- On Windows/PowerShell, if `npm` is blocked by the execution policy, use `npm.cmd`.
- The root `package.json` and `package-lock.json` are empty and unused; the frontend has its own manifest in `frontend/`.
- Backend runs on port 8000 and frontend on 5173. Vite proxies `/api` to the backend and strips the `/api` prefix.
- The SQLite database is `backend/tecbot.db`. There are no migrations: after changing models, delete the database and rerun `python -m app.seed`.
- Do not commit `.env` or `tecbot.db`; copy `.env.example` to `.env`.
