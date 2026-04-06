# nvidia-bench

Benchmark automatizado de providers LLM gratuitos da NVIDIA API (build.nvidia.com).

Roda um único comando, auto-descobre os modelos disponíveis, testa cada um em 3 cenários e imprime um ranking no terminal.

## Resultado do Benchmark (2026-04-06)

Testados ~40 modelos. Ranking final dos viáveis para o Sonny (score 3/3 + tools + latência < 2s):

| # | Modelo | Score | Latência | Tools |
|---|--------|-------|----------|-------|
| 🥇 | `mistralai/mistral-small-4-119b-2603` | 3/3 | **622ms** | ✅ |
| 🥈 | `meta/llama-3.1-8b-instruct` | 3/3 | **746ms** | ✅ |
| 🥉 | `openai/gpt-oss-120b` | 3/3 | **982ms** | ✅ |
| 4 | `mistralai/mistral-small-3.1-24b-instruct-2503` | 3/3 | Rápido | ✅ |
| 5 | `nvidia/llama-3.3-nemotron-super-49b-v1` | 3/3 | 1703ms | ✅ |
| 6 | `qwen/qwen3-next-80b-a3b-instruct` | 3/3 | 1888ms | ✅ |

**Recomendação:** `mistralai/mistral-small-4-119b-2603` como primário. `meta/llama-3.1-8b-instruct` como backup se houver rate limit.

## Contexto

Criado para ajudar o projeto **OpenClaw / Sonny** (assistente WhatsApp) a escolher qual modelo LLM usar. Os critérios de avaliação refletem esse caso de uso: chat em PT-BR, seguir instruções estritas e suporte a tool calling.

## Uso

```bash
cp .env.example .env
# editar .env e preencher NVIDIA_API_KEY
pip install -r requirements.txt
python run.py
```

## O que é testado

| Cenário | Prompt | Avaliação automática |
|---------|--------|---------------------|
| Chat PT-BR | "Que horas abre o banco amanhã?" | Detecta resposta em PT-BR |
| Instrução JSON | "Retorne capital e população em JSON puro" | `json.loads()` sem erro |
| Tool calling | "Como está o tempo em SP?" | Verifica se acionou `get_current_weather` |

Cada modelo recebe score 0–3. O ranking final ordena por `score DESC`, `latência ASC`.

## Estrutura

```
run.py                  # entrypoint — python run.py roda tudo
bench/
  discovery.py          # lista modelos LLM da NVIDIA API (filtra embeddings, visão, etc.)
  runner.py             # executa os 3 cenários por modelo, com progress bar
  evaluator.py          # avalia respostas automaticamente e calcula scores
  reporter.py           # imprime tabela rich com ranking e destaques
prompts/
  chat.py               # cenário 1: chat conversacional PT-BR
  instruction.py        # cenário 2: instrução estrita (responder em JSON)
  tool_call.py          # cenário 3: tool calling (get_current_weather)
```

## Stack

- Python 3.11+
- `openai` SDK (NVIDIA API é compatível com OpenAI)
- `rich` para output no terminal
- `python-dotenv` para carregar a API key

## Para estender

- **Adicionar cenário:** crie `prompts/novo.py` com `SYSTEM`, `USER` (e `TOOLS` se necessário), adicione chamada em `runner.py` e lógica de avaliação em `evaluator.py`.
- **Mudar prompts:** edite os arquivos em `prompts/` — os prompts refletem o contexto do Sonny, ajuste para seu caso de uso.
- **Exportar resultados:** `reporter.py` recebe `list[EvalResult]` — fácil adicionar dump JSON antes de `print_report()`.
