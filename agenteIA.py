import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

mensajes = [
    {
        "role": "system",
        "content": "Eres un bot que habla español y respondes a mis órdenes."
    }
]

while True:
    usuario_input = input("Tú: ").strip()

    if not usuario_input:
        continue
    
    if usuario_input.lower() in ["salir", "bye", "adiós", "adios"]:
        print("Nos vemos pronto :D")
        break

    #Agregar al historial de mensajes:
    mensajes.append({
        "role": "user",
        "content": usuario_input
    })

    
    # First API call with reasoning
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer "+os.getenv("API_KEY"),
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "arcee-ai/trinity-large-preview:free",
        "messages": mensajes,
        "reasoning": {"enabled": True}
    })
    )

    # Extract the assistant message with reasoning_details
    response = response.json()
    
    try:
        assistant_reply = response['choices'][0]['message']['content']
        mensajes.append({
            "role": "assistant",
            "content": assistant_reply
        })
    except:
        assistant_reply = response

    print(f"Asistente: {assistant_reply}")