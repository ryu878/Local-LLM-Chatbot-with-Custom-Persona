import requests

OLLAMA_API_URL = "http://localhost:11434/api/chat"

def send_to_ollama(messages, model="llama3"):
    """
    Send chat messages to the local Ollama instance using REST API.
    messages: list of dicts: [{"role": "system"/"user"/"assistant", "content": "..."}]
    """
    payload = {
        "model": model,
        "messages": messages,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    return response.json()["message"]["content"]
