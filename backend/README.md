# TECBOT Backend

API REST con FastAPI y SQLite para la plataforma informativa TECBOT.

## Ejecución

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m app.seed
uvicorn app.main:app --reload
```

Documentación interactiva: http://localhost:8000/docs
