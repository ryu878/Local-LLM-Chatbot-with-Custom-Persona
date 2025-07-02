import gradio as gr
from personas import PERSONAS
from llm_chat import send_to_ollama

# Session memory: store full chat per session
chat_memory = []

def respond(user_input, persona_name):
    if not user_input:
        return "", chat_memory

    # Start chat if empty
    if not chat_memory:
        system_message = {"role": "system", "content": PERSONAS[persona_name]}
        chat_memory.append(system_message)

    # Add user message
    chat_memory.append({"role": "user", "content": user_input})

    # Call local LLM
    try:
        reply = send_to_ollama(chat_memory)
    except Exception as e:
        return f"⚠️ Error: {e}", chat_memory

    chat_memory.append({"role": "assistant", "content": reply})
    return reply, chat_memory

def reset_chat():
    global chat_memory
    chat_memory = []
    return "", chat_memory

# Gradio interface
with gr.Blocks(title="Local LLM Chatbot") as demo:
    gr.Markdown("## 🧠 Local LLM Chatbot with Custom Persona")
    persona = gr.Dropdown(list(PERSONAS.keys()), label="Select Persona", value="Default Assistant")
    chatbox = gr.Chatbot()
    user_input = gr.Textbox(label="Your message")
    send_btn = gr.Button("Send")
    clear_btn = gr.Button("🧹 Clear Chat")

    send_btn.click(fn=respond, inputs=[user_input, persona], outputs=[chatbox, chatbox])
    user_input.submit(fn=respond, inputs=[user_input, persona], outputs=[chatbox, chatbox])
    clear_btn.click(fn=reset_chat, outputs=[chatbox, chatbox])

demo.launch()
