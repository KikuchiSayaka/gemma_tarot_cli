# gemma_tarot_cli (Local + Stateful)

A fully local, stateful CLI chatbot powered by `gemma3:1b` running on [Ollama](https://ollama.com/).  
This script maintains conversation history, supports persona control via system prompt, and is optionally extensible with RAG (retrieval-augmented generation) using FAISS and `sentence-transformers`.

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed with the `gemma3:1b` model
- (Optional) `faiss-cpu` and `sentence-transformers` for RAG-based retrieval

## Installation

```bash
pip install faiss-cpu sentence-transformers
```

## Usage

### 1. Start the Gemma model via Ollama:

```bash
ollama run gemma3:1b
```

### 2. In a separate terminal window, run the chat script:

```bash
python3 chat_gemma.py
```

### 3. The script will:

Load or initialize a conversation history (history.json)

Maintain state between inputs

Use a fixed system prompt to define the AI's personality (e.g. Tarot reader, strategist, etc.)

Save the entire conversation after each turn

### 4. To reset the conversation, delete history.json.

## Customization

The current system prompt assumes Japanese-language input and is tailored for a tarot reading assistant.
If you are a non-Japanese speaker or wish to use this tool for other purposes (e.g. productivity assistant, coding tutor, strategist),
you should customize the SYSTEM_PROMPT in chat_gemma.py accordingly.

Additionally, for context-aware functionality, you can implement retrieval-augmented generation (RAG) by indexing past conversation logs with faiss and injecting relevant results into the prompt dynamically.

## Notes

The script uses Ollama’s OpenAI-compatible API (http://localhost:11434/api/chat) with stream: false for easier integration.

This project is designed for fully offline use — no internet or external APIs are required.

## License

This project is licensed under the MIT License.
