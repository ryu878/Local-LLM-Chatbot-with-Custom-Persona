# Local LLM Chatbot with Custom Persona

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

***

## 📄 License
MIT License - Feel free to modify and distribute.


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.

## ⚠️ Disclaimer

> This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial, or other advice. Nothing contained here is a recommendation, endorsement, or offer by me to buy or sell any securities or other financial instruments.
>
> **If you intend to use real money, use it at your own risk.**
>
> Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs, or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

***

## 📞 Contact Me

I develop trading bots of any complexity, dashboards, and indicators for crypto exchanges, forex, and stocks. 🚀

To contact me, please send a message:

*   **Telegram:** [https://t.me/ryu8777](https://t.me/ryu8777) ✈️
*   **Discord:** [https://discord.gg/zSw58e9Uvf](https://discord.gg/zSw58e9Uvf) 🤝

***

## 🤝 Become My Crypto Partner

Start your trading journey on Bybit! Join using my referral link below:

**Join Bybit:** [https://www.bybit.com/invite?ref=P11NJW](https://www.bybit.com/invite?ref=P11NJW)

***

## 🖥️ VPS for Your Bots and Scripts

Keep your bots running 24/7! I prefer and recommend using **DigitalOcean**.

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=3d7f6e57bc04&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

**Get $200 in credit over 60 days** by using my referral link:

👉 [https://m.do.co/c/3d7f6e57bc04](https://m.do.co/c/3d7f6e57bc04)
