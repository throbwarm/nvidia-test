"""Auto-descobre modelos LLM disponíveis na NVIDIA API."""

from openai import OpenAI

# Prefixos/sufixos que indicam modelos não-LLM (embeddings, visão, etc.)
_NON_LLM_KEYWORDS = (
    "embed",
    "rerank",
    "vision",
    "ocr",
    "clip",
    "vlm",
    "imagen",
    "stable-diffusion",
    "segmentation",
    "detection",
    "whisper",
    "tts",
    "retrieval",
)


def list_models(client: OpenAI) -> list[str]:
    """Retorna lista de model IDs de LLMs disponíveis na NVIDIA API."""
    response = client.models.list()
    models = []
    for model in response.data:
        model_id = model.id.lower()
        if any(kw in model_id for kw in _NON_LLM_KEYWORDS):
            continue
        models.append(model.id)
    return sorted(models)
