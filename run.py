"""
nvidia-bench — NVIDIA Provider Benchmark
Uso: python run.py

Requer NVIDIA_API_KEY no .env (ou variável de ambiente).
"""

import os
import sys

from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console

from bench import discovery, runner, evaluator, reporter

console = Console()


def main() -> None:
    load_dotenv()

    api_key = os.getenv("NVIDIA_API_KEY")
    if not api_key:
        console.print("[bold red]Erro:[/] NVIDIA_API_KEY não encontrada.")
        console.print("Copie [cyan].env.example[/] para [cyan].env[/] e preencha sua chave.")
        sys.exit(1)

    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=api_key,
    )

    console.print("[bold]Buscando modelos disponíveis na NVIDIA API...[/]")
    models = discovery.list_models(client)

    batch_final = [
        "mistralai/mistral-small-4-119b-2603",
        "qwen/qwen3-next-80b-a3b-instruct",
        "stepfun-ai/step-3.5-flash",
        "minimaxai/minimax-m2.5",
        "bytedance/seed-oss-36b-instruct",
    ]
    models = [m for m in models if m in batch_final]

    if not models:
        console.print("[yellow]Nenhum modelo LLM encontrado. Verifique sua API key.[/]")
        sys.exit(1)

    console.print(f"[green]{len(models)} modelos encontrados.[/] Iniciando testes...\n")

    results = runner.run_all(client, models)
    evals = evaluator.evaluate_all(results)
    reporter.print_report(evals)


if __name__ == "__main__":
    main()
