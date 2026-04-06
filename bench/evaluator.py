"""Avalia automaticamente os resultados de cada cenário."""

import json
from dataclasses import dataclass

from bench.runner import ModelResult, ScenarioResult

# Palavras PT-BR comuns que indicam resposta no idioma correto
_PT_BR_MARKERS = (
    "banco", "abre", "horas", "geralmente", "costuma", "normalmente",
    "segunda", "horário", "atendimento", "das", "às", "até",
)


@dataclass
class EvalResult:
    model_id: str
    chat_ok: bool
    instruction_ok: bool
    tool_call_ok: bool
    avg_latency_ms: float

    @property
    def total_score(self) -> int:
        return sum([self.chat_ok, self.instruction_ok, self.tool_call_ok])


def _eval_chat(s: ScenarioResult) -> bool:
    if s.error or not s.raw_response:
        return False
    text = s.raw_response.lower()
    return any(marker in text for marker in _PT_BR_MARKERS)


def _eval_instruction(s: ScenarioResult) -> bool:
    if s.error or not s.raw_response:
        return False
    text = s.raw_response.strip()
    # Remove blocos markdown se o modelo desobedeceu mas tentou JSON
    if text.startswith("```"):
        lines = text.splitlines()
        text = "\n".join(lines[1:-1]) if len(lines) > 2 else text
    try:
        json.loads(text)
        return True
    except (json.JSONDecodeError, ValueError):
        return False


def _eval_tool_call(s: ScenarioResult) -> bool:
    if s.error or not s.tool_calls:
        return False
    for tc in s.tool_calls:
        if tc.function.name == "get_current_weather":
            return True
    return False


def evaluate_all(model_results: list[ModelResult]) -> list[EvalResult]:
    evals = []
    for mr in model_results:
        scenarios_by_name = {s.name: s for s in mr.scenarios}
        latencies = [s.latency_ms for s in mr.scenarios if not s.error]
        avg_latency = sum(latencies) / len(latencies) if latencies else 0.0

        evals.append(EvalResult(
            model_id=mr.model_id,
            chat_ok=_eval_chat(scenarios_by_name.get("chat", ScenarioResult("chat", None, None, 0, "missing"))),
            instruction_ok=_eval_instruction(scenarios_by_name.get("instruction", ScenarioResult("instruction", None, None, 0, "missing"))),
            tool_call_ok=_eval_tool_call(scenarios_by_name.get("tool_call", ScenarioResult("tool_call", None, None, 0, "missing"))),
            avg_latency_ms=avg_latency,
        ))

    return sorted(evals, key=lambda e: (-e.total_score, e.avg_latency_ms))
