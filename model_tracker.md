# NVIDIA Models Tracker

Nesta tabela iterativa, acompanharemos a performance dos endpoints na conversação, aderência a json e tool calling.

## Code (Programação)
| Model ID | Testado | Score (0-3) | Latência | Suporta Tools? | Notas |
|---|---|---|---|---|---|
| `bigcode/starcoder2-15b` | ✅ | 0/3 | - | ❌ | |
| `bigcode/starcoder2-7b` | ❌ | - | - | - | |
| `deepseek-ai/deepseek-coder-6.7b-instruct` | ✅ | 0/3 | - | ❌ | |
| `google/codegemma-1.1-7b` | ✅ | 0/3 | - | ❌ | |
| `google/codegemma-7b` | ❌ | - | - | - | |
| `ibm/granite-34b-code-instruct` | ✅ | 0/3 | - | ❌ | |
| `ibm/granite-8b-code-instruct` | ❌ | - | - | - | |
| `meta/codellama-70b` | ✅ | 0/3 | - | ❌ | |
| `mistralai/codestral-22b-instruct-v0.1` | ✅ | 0/3 | - | ❌ | |
| `mistralai/mamba-codestral-7b-v0.1` | ❌ | - | - | - | |
| `nvidia/nv-embedcode-7b-v1` | ❌ | - | - | - | |
| `qwen/qwen2.5-coder-32b-instruct` | ✅ | 2/3 | 740ms | ❌ | |
| `qwen/qwen2.5-coder-7b-instruct` | ✅ | 2/3 | - | ❌ | |
| `qwen/qwen3-coder-480b-a35b-instruct` | ❌ | - | - | - | |


## Vision / Multimodal
| Model ID | Testado | Score (0-3) | Latência | Suporta Tools? | Notas |
|---|---|---|---|---|---|
| `adept/fuyu-8b` | ❌ | - | - | - | |
| `google/paligemma` | ❌ | - | - | - | |
| `meta/llama-3.2-11b-vision-instruct` | ❌ | - | - | - | |
| `meta/llama-3.2-90b-vision-instruct` | ❌ | - | - | - | |
| `microsoft/kosmos-2` | ❌ | - | - | - | |
| `microsoft/phi-3-vision-128k-instruct` | ❌ | - | - | - | |
| `microsoft/phi-3.5-vision-instruct` | ❌ | - | - | - | |
| `nvidia/llama-3.1-nemotron-nano-vl-8b-v1` | ❌ | - | - | - | |
| `nvidia/llama-3.2-nemoretriever-1b-vlm-embed-v1` | ❌ | - | - | - | |
| `nvidia/llama-nemotron-embed-vl-1b-v2` | ❌ | - | - | - | |
| `nvidia/nemotron-nano-12b-v2-vl` | ❌ | - | - | - | |
| `nvidia/neva-22b` | ❌ | - | - | - | |
| `nvidia/streampetr` | ❌ | - | - | - | |


## Embeddings / Parse / Rerank / RAG
| Model ID | Testado | Score (0-3) | Latência | Suporta Tools? | Notas |
|---|---|---|---|---|---|
| `baai/bge-m3` | ❌ | - | - | - | |
| `nvidia/embed-qa-4` | ❌ | - | - | - | |
| `nvidia/llama-3.2-nemoretriever-300m-embed-v1` | ❌ | - | - | - | |
| `nvidia/llama-3.2-nv-embedqa-1b-v1` | ❌ | - | - | - | |
| `nvidia/llama-3.2-nv-embedqa-1b-v2` | ❌ | - | - | - | |
| `nvidia/llama-nemotron-embed-1b-v2` | ❌ | - | - | - | |
| `nvidia/llama3-chatqa-1.5-70b` | ❌ | - | - | - | |
| `nvidia/llama3-chatqa-1.5-8b` | ❌ | - | - | - | |
| `nvidia/nemoretriever-parse` | ❌ | - | - | - | |
| `nvidia/nemotron-parse` | ❌ | - | - | - | |
| `nvidia/nv-embed-v1` | ❌ | - | - | - | |
| `nvidia/nv-embedqa-e5-v5` | ❌ | - | - | - | |
| `nvidia/nv-embedqa-mistral-7b-v2` | ❌ | - | - | - | |
| `nvidia/nvclip` | ❌ | - | - | - | |
| `snowflake/arctic-embed-l` | ❌ | - | - | - | |


## Safety / Guardrails / Reward
| Model ID | Testado | Score (0-3) | Latência | Suporta Tools? | Notas |
|---|---|---|---|---|---|
| `ibm/granite-guardian-3.0-8b` | ❌ | - | - | - | |
| `meta/llama-guard-4-12b` | ❌ | - | - | - | |
| `nvidia/gliner-pii` | ❌ | - | - | - | |
| `nvidia/llama-3.1-nemoguard-8b-content-safety` | ❌ | - | - | - | |
| `nvidia/llama-3.1-nemoguard-8b-topic-control` | ❌ | - | - | - | |
| `nvidia/llama-3.1-nemotron-70b-reward` | ❌ | - | - | - | |
| `nvidia/llama-3.1-nemotron-safety-guard-8b-v3` | ❌ | - | - | - | |
| `nvidia/nemotron-4-340b-reward` | ❌ | - | - | - | |
| `nvidia/nemotron-content-safety-reasoning-4b` | ❌ | - | - | - | |


## General Purpose (LLaMA/Mistral/Gemma/Qwen/Phi/etc)
| Model ID | Testado | Score (0-3) | Latência | Suporta Tools? | Notas |
|---|---|---|---|---|---|
| `01-ai/yi-large` | ❌ | - | - | - | |
| `abacusai/dracarys-llama-3.1-70b-instruct` | ❌ | - | - | - | |
| `ai21labs/jamba-1.5-large-instruct` | ❌ | - | - | - | |
| `ai21labs/jamba-1.5-mini-instruct` | ❌ | - | - | - | |
| `baichuan-inc/baichuan2-13b-chat` | ❌ | - | - | - | |
| `bytedance/seed-oss-36b-instruct` | ✅ | 2/3 | 435s | ❌ | |
| `databricks/dbrx-instruct` | ❌ | - | - | - | |
| `deepseek-ai/deepseek-r1-distill-llama-8b` | ✅ | 0/3 | Error/Timeout | ❌ | |
| `deepseek-ai/deepseek-r1-distill-qwen-14b` | ❌ | - | - | - | |
| `deepseek-ai/deepseek-r1-distill-qwen-32b` | ❌ | - | - | - | |
| `deepseek-ai/deepseek-r1-distill-qwen-7b` | ❌ | - | - | - | |
| `deepseek-ai/deepseek-v3.1` | ✅ | 3/3 | 8429ms | ✅ | |
| `deepseek-ai/deepseek-v3.1-terminus` | ❌ | - | - | - | |
| `deepseek-ai/deepseek-v3.2` | ✅ | 2/3 | 35s+ | ✅ | Falhou PT-BR |
| `google/gemma-2-27b-it` | ✅ | 0/3 | Error/Timeout | ❌ | |
| `google/gemma-2-2b-it` | ❌ | - | - | - | |
| `google/gemma-2-9b-it` | ❌ | - | - | - | |
| `google/gemma-2b` | ❌ | - | - | - | |
| `google/gemma-3-12b-it` | ❌ | - | - | - | |
| `google/gemma-3-1b-it` | ❌ | - | - | - | |
| `google/gemma-3-27b-it` | ✅ | 2/3 | 836ms | ❌ | |
| `google/gemma-3-4b-it` | ❌ | - | - | - | |
| `google/gemma-3n-e2b-it` | ❌ | - | - | - | |
| `google/gemma-3n-e4b-it` | ❌ | - | - | - | |
| `google/gemma-4-31b-it` | ✅ | 0/3 | Timeout | ❌ | |
| `google/gemma-7b` | ❌ | - | - | - | |
| `google/recurrentgemma-2b` | ❌ | - | - | - | |
| `google/shieldgemma-9b` | ❌ | - | - | - | |
| `gotocompany/gemma-2-9b-cpt-sahabatai-instruct` | ❌ | - | - | - | |
| `ibm/granite-3.0-3b-a800m-instruct` | ❌ | - | - | - | |
| `ibm/granite-3.0-8b-instruct` | ❌ | - | - | - | |
| `ibm/granite-3.3-8b-instruct` | ❌ | - | - | - | |
| `institute-of-science-tokyo/llama-3.1-swallow-70b-instruct-v0.1` | ❌ | - | - | - | |
| `institute-of-science-tokyo/llama-3.1-swallow-8b-instruct-v0.1` | ❌ | - | - | - | |
| `mediatek/breeze-7b-instruct` | ❌ | - | - | - | |
| `meta/llama-3.1-405b-instruct` | ✅ | 2/3 | (Falhou em JSON) | ✅ | |
| `meta/llama-3.1-70b-instruct` | ✅ | 3/3 | ~4s | ✅ | |
| `meta/llama-3.1-8b-instruct` | ✅ | 3/3 | 746ms | ✅ | |
| `meta/llama-3.2-1b-instruct` | ✅ | 2/3 | - | ❌ | |
| `meta/llama-3.2-3b-instruct` | ✅ | 1/3 | - | ❌ | |
| `meta/llama-3.3-70b-instruct` | ✅ | 3/3 | 11s+ | ✅ | |
| `meta/llama-4-maverick-17b-128e-instruct` | ✅ | 2/3 | 696ms | ❌ | |
| `meta/llama-4-scout-17b-16e-instruct` | ✅ | 0/3 | - | ❌ | |
| `meta/llama2-70b` | ❌ | - | - | - | |
| `meta/llama3-70b-instruct` | ❌ | - | - | - | |
| `meta/llama3-8b-instruct` | ❌ | - | - | - | |
| `microsoft/phi-3-medium-128k-instruct` | ❌ | - | - | - | |
| `microsoft/phi-3-medium-4k-instruct` | ❌ | - | - | - | |
| `microsoft/phi-3-mini-128k-instruct` | ❌ | - | - | - | |
| `microsoft/phi-3-mini-4k-instruct` | ❌ | - | - | - | |
| `microsoft/phi-3-small-128k-instruct` | ❌ | - | - | - | |
| `microsoft/phi-3-small-8k-instruct` | ❌ | - | - | - | |
| `microsoft/phi-3.5-mini-instruct` | ❌ | - | - | - | |
| `microsoft/phi-3.5-moe-instruct` | ✅ | 0/3 | - | ❌ | |
| `microsoft/phi-4-mini-flash-reasoning` | ❌ | - | - | - | |
| `microsoft/phi-4-mini-instruct` | ✅ | 1/3 | - | ❌ | |
| `microsoft/phi-4-multimodal-instruct` | ❌ | - | - | - | |
| `mistralai/devstral-2-123b-instruct-2512` | ❌ | - | - | - | |
| `mistralai/magistral-small-2506` | ❌ | - | - | - | |
| `mistralai/mathstral-7b-v0.1` | ❌ | - | - | - | |
| `mistralai/ministral-14b-instruct-2512` | ❌ | - | - | - | |
| `mistralai/mistral-7b-instruct-v0.2` | ❌ | - | - | - | |
| `mistralai/mistral-7b-instruct-v0.3` | ❌ | - | - | - | |
| `mistralai/mistral-large` | ❌ | - | - | - | |
| `mistralai/mistral-large-2-instruct` | ✅ | 0/3 | Timeout | ❌ | Continua caindo |
| `mistralai/mistral-large-3-675b-instruct-2512` | ❌ | - | - | - | |
| `mistralai/mistral-medium-3-instruct` | ✅ | 0/3 | Timeout | ❌ | |
| `mistralai/mistral-nemotron` | ✅ | 2/3 | 2000ms+ | ❌ | |
| `mistralai/mistral-small-24b-instruct` | ✅ | 2/3 | - | ❌ | |
| `mistralai/mistral-small-3.1-24b-instruct-2503` | ✅ | 3/3 | Rápido | ✅ | |
| `mistralai/mistral-small-4-119b-2603` | ✅ | 3/3 | 622ms | ✅ | 🚀 Incrível! |
| `mistralai/mixtral-8x22b-instruct-v0.1` | ✅ | 2/3 | 743ms | ❌ | |
| `mistralai/mixtral-8x22b-v0.1` | ❌ | - | - | - | |
| `mistralai/mixtral-8x7b-instruct-v0.1` | ✅ | 1/3 | - | ❌ | |
| `nv-mistralai/mistral-nemo-12b-instruct` | ✅ | 0/3 | - | ❌ | |
| `nvidia/llama-3.1-nemotron-51b-instruct` | ✅ | 0/3 | Timeout | ❌ | |
| `nvidia/llama-3.1-nemotron-70b-instruct` | ✅ | 0/3 | - | ❌ | |
| `nvidia/llama-3.1-nemotron-nano-4b-v1.1` | ❌ | - | - | - | |
| `nvidia/llama-3.1-nemotron-nano-8b-v1` | ✅ | 2/3 | - | ❌ | |
| `nvidia/llama-3.1-nemotron-ultra-253b-v1` | ❌ | - | - | - | |
| `nvidia/llama-3.3-nemotron-super-49b-v1` | ✅ | 3/3 | 1703ms | ✅ | |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ | 0/3 | Timeout | ❌ | |
| `nvidia/mistral-nemo-minitron-8b-8k-instruct` | ❌ | - | - | - | |
| `nvidia/mistral-nemo-minitron-8b-base` | ❌ | - | - | - | |
| `nvidia/nemotron-3-nano-30b-a3b` | ❌ | - | - | - | |
| `nvidia/nemotron-3-super-120b-a12b` | ❌ | - | - | - | |
| `nvidia/nemotron-3-super-120b-a12b` | ❌ | - | - | - | |
| `nvidia/nemotron-4-340b-instruct` | ❌ | - | - | - | |
| `nvidia/nemotron-4-mini-hindi-4b-instruct` | ❌ | - | - | - | |
| `nvidia/nemotron-mini-4b-instruct` | ❌ | - | - | - | |
| `nvidia/nemotron-nano-3-30b-a3b` | ❌ | - | - | - | |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ✅ | 1/3 | - | ✅ | |
| `qwen/qwen2-7b-instruct` | ❌ | - | - | - | |
| `qwen/qwen2.5-7b-instruct` | ✅ | 2/3 | - | ❌ | |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ | 3/3 | 1888ms | ✅ | |
| `qwen/qwen3-next-80b-a3b-thinking` | ❌ | - | - | - | |
| `qwen/qwen3.5-122b-a10b` | ❌ | - | - | - | |
| `qwen/qwen3.5-397b-a17b` | ❌ | - | - | - | |
| `qwen/qwq-32b` | ✅ | 0/3 | - | ❌ | |
| `tokyotech-llm/llama-3-swallow-70b-instruct-v0.1` | ❌ | - | - | - | |
| `yentinglin/llama-3-taiwan-70b-instruct` | ❌ | - | - | - | |


## Outros / Específicos
| Model ID | Testado | Score (0-3) | Latência | Suporta Tools? | Notas |
|---|---|---|---|---|---|
| `aisingapore/sea-lion-7b-instruct` | ❌ | - | - | - | |
| `google/deplot` | ❌ | - | - | - | |
| `igenius/colosseum_355b_instruct_16k` | ❌ | - | - | - | |
| `igenius/italia_10b_instruct_16k` | ❌ | - | - | - | |
| `marin/marin-8b-instruct` | ❌ | - | - | - | |
| `minimaxai/minimax-m2.5` | ✅ | 3/3 | 4861ms | ✅ | |
| `moonshotai/kimi-k2-instruct` | ✅ | 3/3 | 2489ms | ✅ | |
| `moonshotai/kimi-k2-instruct-0905` | ❌ | - | - | - | |
| `moonshotai/kimi-k2-thinking` | ❌ | - | - | - | |
| `moonshotai/kimi-k2.5` | ✅ | 0/3 | 90s+ | ❌ | Timeout |
| `nvidia/cosmos-reason2-8b` | ❌ | - | - | - | |
| `nvidia/riva-translate-4b-instruct` | ❌ | - | - | - | |
| `nvidia/riva-translate-4b-instruct-v1.1` | ❌ | - | - | - | |
| `nvidia/vila` | ❌ | - | - | - | |
| `openai/gpt-oss-120b` | ✅ | 3/3 | 982ms | ✅ | Surpreendente |
| `openai/gpt-oss-120b` | ✅ | 3/3 | 982ms | ✅ | Dois endpoints? |
| `openai/gpt-oss-20b` | ✅ | 3/3 | - | ✅ | |
| `openai/gpt-oss-20b` | ✅ | 2/3 | Falhou PT | ✅ | |
| `opengpt-x/teuken-7b-instruct-commercial-v0.4` | ❌ | - | - | - | |
| `rakuten/rakutenai-7b-chat` | ❌ | - | - | - | |
| `rakuten/rakutenai-7b-instruct` | ❌ | - | - | - | |
| `sarvamai/sarvam-m` | ❌ | - | - | - | |
| `speakleash/bielik-11b-v2.3-instruct` | ❌ | - | - | - | |
| `speakleash/bielik-11b-v2.6-instruct` | ❌ | - | - | - | |
| `stepfun-ai/step-3.5-flash` | ✅ | 2/3 | 139s | ✅ | |
| `stockmark/stockmark-2-100b-instruct` | ❌ | - | - | - | |
| `thudm/chatglm3-6b` | ❌ | - | - | - | |
| `tiiuae/falcon3-7b-instruct` | ❌ | - | - | - | |
| `upstage/solar-10.7b-instruct` | ❌ | - | - | - | |
| `utter-project/eurollm-9b-instruct` | ❌ | - | - | - | |
| `writer/palmyra-creative-122b` | ❌ | - | - | - | |
| `writer/palmyra-fin-70b-32k` | ❌ | - | - | - | |
| `writer/palmyra-med-70b` | ❌ | - | - | - | |
| `writer/palmyra-med-70b-32k` | ❌ | - | - | - | |
| `z-ai/glm4.7` | ❌ | - | - | - | |
| `z-ai/glm5` | ❌ | - | - | - | |
| `zyphra/zamba2-7b-instruct` | ❌ | - | - | - | |

