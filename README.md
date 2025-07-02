# Local-LLM-Chatbot-with-Custom-Persona

Private, fast, and fully local chatbot powered by open-source LLMs like LLaMA 3, with customizable characters and memory.

### 🔧 Features
- 💻 Runs fully offline using Ollama

- 🧠 Supports character presets (e.g. sarcastic dev, stoic philosopher)

- 🗃️ Context memory within chat session

- 🖥️ Lightweight Gradio UI

### 📦 Installation

```
git clone https://github.com/ryu878/Local-LLM-Chatbot-with-Custom-Persona.git
cd Local-LLM-Chatbot-with-Custom-Persona
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```
### ▶️ Run the App
```
# Make sure Ollama is installed and running
ollama run llama3

# Then run the Python app
python app.py
```

Open http://localhost:7860 in your browser.

### 📁 Project Structure
```
📦 Local-LLM-Chatbot-with-Custom-Persona/ 
├── app.py # Main Gradio app
├── llm_chat.py # LLM interaction logic
├── personas.py # Persona definitions
├── requirements.txt # Dependencies
└── README.md # This file
``` 


### 🧠 LLM Backend
- Ollama (https://ollama.com) with any supported model (llama3, mistral, gemma, etc.)

- Uses simple prompt engineering to inject persona behavior

### ✨ Example Personas

- 👨‍💻 Sarcastic Developer: “Oh great, another null pointer. I’m thrilled.”

- 🧘‍♂️ Zen Monk: “Breathe. The answer lies not in code, but within.”

- 💼 Professional Advisor: “Here’s what I recommend based on best practices…”

### 📜 License
MIT — open for commercial and personal use.

### ✅ TODOs
- Save chat history

- Add speech input/output

- Add persona editor

- Add Ollama model switcher in UI

## Contacts
To contact me please pm:

Telegram: https://t.me/ryu8777

Discord: https://discord.gg/zSw58e9Uvf
