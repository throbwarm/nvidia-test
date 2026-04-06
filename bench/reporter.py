"""Imprime tabela rankeada dos resultados no terminal."""

from datetime import date

from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text

from bench.evaluator import EvalResult

console = Console()


def _check(ok: bool) -> Text:
    return Text("✅", style="green") if ok else Text("❌", style="red")


def _score_style(score: int) -> str:
    if score == 3:
        return "bold green"
    if score == 2:
        return "yellow"
    if score == 1:
        return "orange3"
    return "red"


def print_report(evals: list[EvalResult]) -> None:
    console.print()
    console.rule(f"[bold cyan]NVIDIA Provider Benchmark — {date.today()}")
    console.print()

    table = Table(
        box=box.ROUNDED,
        show_header=True,
        header_style="bold white on dark_blue",
        row_styles=["", "dim"],
    )

    table.add_column("Modelo", style="cyan", no_wrap=True, min_width=30)
    table.add_column("Score", justify="center", min_width=7)
    table.add_column("Chat PT-BR", justify="center")
    table.add_column("Instrução JSON", justify="center")
    table.add_column("Tool Call", justify="center")
    table.add_column("Lat. média (ms)", justify="right")

    best_score = evals[0].total_score if evals else 0
    fastest = min((e for e in evals if e.total_score > 0), key=lambda e: e.avg_latency_ms, default=None)
    best_tools = [e for e in evals if e.tool_call_ok]

    for e in evals:
        score_text = Text(f"{e.total_score}/3", style=_score_style(e.total_score))
        lat_text = f"{e.avg_latency_ms:.0f}"
        table.add_row(
            e.model_id,
            score_text,
            _check(e.chat_ok),
            _check(e.instruction_ok),
            _check(e.tool_call_ok),
            lat_text,
        )

    console.print(table)
    console.print()

    # Destaques
    top = next((e for e in evals if e.total_score == best_score), None)
    if top:
        console.print(f"[bold yellow]🏆 Melhor geral:[/]     [cyan]{top.model_id}[/]  (score {top.total_score}/3, {top.avg_latency_ms:.0f}ms)")

    if fastest:
        console.print(f"[bold yellow]⚡ Mais rápido:[/]      [cyan]{fastest.model_id}[/]  ({fastest.avg_latency_ms:.0f}ms, score {fastest.total_score}/3)")

    if best_tools:
        names = ", ".join(e.model_id for e in best_tools[:3])
        console.print(f"[bold yellow]🔧 Suporta tools:[/]    [cyan]{names}[/]")

    console.print()
    console.print(f"[dim]Total de modelos testados: {len(evals)}[/]")
    console.print()
