"""Executa os 3 cenários de teste em cada modelo."""

import time
from dataclasses import dataclass, field

from openai import OpenAI
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn

from prompts import chat, instruction, tool_call


@dataclass
class ScenarioResult:
    name: str
    raw_response: str | None
    tool_calls: list | None
    latency_ms: float
    error: str | None = None


@dataclass
class ModelResult:
    model_id: str
    scenarios: list[ScenarioResult] = field(default_factory=list)


def _run_chat(client: OpenAI, model_id: str) -> ScenarioResult:
    time.sleep(1.5)
    start = time.perf_counter()
    try:
        resp = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": chat.SYSTEM},
                {"role": "user", "content": chat.USER},
            ],
            max_tokens=200,
            timeout=30,
        )
        latency_ms = (time.perf_counter() - start) * 1000
        content = resp.choices[0].message.content or ""
        return ScenarioResult("chat", content, None, latency_ms)
    except Exception as e:
        latency_ms = (time.perf_counter() - start) * 1000
        return ScenarioResult("chat", None, None, latency_ms, error=str(e))


def _run_instruction(client: OpenAI, model_id: str) -> ScenarioResult:
    time.sleep(1.5)
    start = time.perf_counter()
    try:
        resp = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": instruction.SYSTEM},
                {"role": "user", "content": instruction.USER},
            ],
            max_tokens=200,
            timeout=30,
        )
        latency_ms = (time.perf_counter() - start) * 1000
        content = resp.choices[0].message.content or ""
        return ScenarioResult("instruction", content, None, latency_ms)
    except Exception as e:
        latency_ms = (time.perf_counter() - start) * 1000
        return ScenarioResult("instruction", None, None, latency_ms, error=str(e))


def _run_tool_call(client: OpenAI, model_id: str) -> ScenarioResult:
    time.sleep(1.5)
    start = time.perf_counter()
    try:
        resp = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": tool_call.USER}],
            tools=tool_call.TOOLS,
            tool_choice="auto",
            max_tokens=200,
            timeout=30,
        )
        latency_ms = (time.perf_counter() - start) * 1000
        msg = resp.choices[0].message
        raw = msg.content or ""
        calls = msg.tool_calls
        return ScenarioResult("tool_call", raw, calls, latency_ms)
    except Exception as e:
        latency_ms = (time.perf_counter() - start) * 1000
        return ScenarioResult("tool_call", None, None, latency_ms, error=str(e))


def run_all(client: OpenAI, model_ids: list[str]) -> list[ModelResult]:
    results = []
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task("Testando modelos...", total=len(model_ids))
        for model_id in model_ids:
            progress.update(task, description=f"[bold blue]{model_id[:40]}")
            result = ModelResult(model_id=model_id)
            result.scenarios.append(_run_chat(client, model_id))
            result.scenarios.append(_run_instruction(client, model_id))
            result.scenarios.append(_run_tool_call(client, model_id))
            results.append(result)
            progress.advance(task)
    return results
