"""Cenário 2: Seguir instrução estrita (resposta em JSON puro)."""

SYSTEM = (
    "Responda APENAS com JSON válido, sem markdown, sem texto adicional, sem blocos de código. "
    "Exemplo de formato esperado: {\"chave\": \"valor\"}"
)

USER = "Qual a capital do Brasil e sua população estimada? Retorne os campos: capital, populacao_milhoes."
