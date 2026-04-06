"""Cenário 3: Tool calling — modelo deve acionar uma ferramenta."""

USER = "Como está o tempo em São Paulo agora?"

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Obtém a previsão do tempo atual para uma cidade.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Nome da cidade, ex: São Paulo, BR",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Unidade de temperatura",
                    },
                },
                "required": ["location"],
            },
        },
    }
]
