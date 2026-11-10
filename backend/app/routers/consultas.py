import re
import unicodedata
from pathlib import Path

from fastapi import APIRouter

from ..schemas import ConsultaPregunta, ConsultaRespuesta, FuenteDocumento

router = APIRouter(prefix="/consultas", tags=["Consultas"])

DOC_PATH = Path(__file__).resolve().parent.parent / "docs" / "servicio_social.md"
FUENTE = FuenteDocumento(
    titulo="Servicio Social (Documento de demostración)",
    documento="backend/app/docs/servicio_social.md",
    seccion="Requisitos generales",
)

PALABRAS_SERVICIO_SOCIAL = {
    "servicio",
    "social",
    "requisito",
    "requisitos",
    "liberacion",
    "liberar",
    "registro",
    "horas",
    "reporte",
    "reportes",
    "carta",
    "presentacion",
    "solicitud",
    "dependencia",
}

PALABRAS_REQUISITOS = {
    "requisito",
    "requisitos",
    "necesito",
    "necesita",
    "pedir",
    "piden",
    "solicitar",
    "documento",
    "documentos",
    "tramite",
    "tramitar",
}


def _normalizar(texto: str) -> str:
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(ch for ch in texto if unicodedata.category(ch) != "Mn")
    return texto


def _tokens(texto: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", _normalizar(texto)))


def _es_tema_servicio_social(tokens: set[str]) -> bool:
    if "servicio" in tokens and "social" in tokens:
        return True
    if "servicio" in tokens and tokens & PALABRAS_SERVICIO_SOCIAL:
        return True
    return False


def _es_pregunta_requisitos(tokens: set[str]) -> bool:
    return bool(tokens & PALABRAS_REQUISITOS)


@router.post("/servicio-social", response_model=ConsultaRespuesta)
def consultar_servicio_social(consulta: ConsultaPregunta):
    tokens = _tokens(consulta.pregunta)

    if _es_tema_servicio_social(tokens) and _es_pregunta_requisitos(tokens):
        respuesta = (
            "Según la documentación de demostración, los requisitos generales para el servicio social incluyen: "
            "contar con el avance académico establecido por la normativa vigente; "
            "presentar carta de presentación o solicitud correspondiente; "
            "registrarse en el periodo indicado por la institución; "
            "realizarlo en un programa o dependencia autorizada; "
            "cumplir el número de horas establecido; "
            "y entregar los reportes y documentación final para la liberación. "
            "Los periodos, formatos y criterios específicos deben consultarse en los lineamientos oficiales vigentes."
        )
        return ConsultaRespuesta(respuesta=respuesta, fuentes=[FUENTE])

    if _es_tema_servicio_social(tokens):
        respuesta = (
            "Puedo orientar sobre servicio social con base en la documentación de demostración disponible. "
            "Especifica si deseas conocer requisitos, registro, horas, reportes o liberación."
        )
        return ConsultaRespuesta(respuesta=respuesta, fuentes=[FUENTE])

    respuesta = (
        "No encontré información sobre esa consulta en la documentación de servicio social disponible. "
        "Puedo ayudarte con dudas relacionadas con el servicio social, como requisitos, registro o liberación."
    )
    return ConsultaRespuesta(respuesta=respuesta, fuentes=[FUENTE])
