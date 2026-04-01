# Environment Setup

Configure credentials once. PyRIT reads everything from `~/.pyrit/.env`.

---

## 1 · Install PyRIT

```bash
pip install pyrit==0.11.0
```

Verify:
```bash
python -c "import pyrit; print(pyrit.__version__)"
# Expected: 0.11.0
```

---

## 2 · Create the `.env` File

```bash
# Windows
mkdir %USERPROFILE%\.pyrit
notepad %USERPROFILE%\.pyrit\.env

# Linux / Mac
mkdir -p ~/.pyrit
nano ~/.pyrit/.env
```

---

## 3 · Pick Your Backend — Copy the Matching Block

### Option A — OpenAI (ChatGPT)
```env
OPENAI_CHAT_ENDPOINT=https://api.openai.com/v1
OPENAI_CHAT_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx
OPENAI_CHAT_MODEL=gpt-4o
```

### Option B — Azure OpenAI
```env
AZURE_OPENAI_CHAT_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_CHAT_KEY=your_azure_key
AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4
AZURE_OPENAI_API_VERSION=2024-02-01
```

### Option C — Local model (LM Studio)
```env
OPENAI_CHAT_ENDPOINT=http://localhost:1234/v1
OPENAI_CHAT_KEY=not-needed
OPENAI_CHAT_MODEL=llama3-8b
```
> LM Studio: open app → **Local Server** tab → load model → **Start Server**

### Option D — Local model (Ollama)
```env
OLLAMA_CHAT_ENDPOINT=http://localhost:11434/v1
OLLAMA_MODEL=llama3
```

---

## 4 · Multi-Role Setup (Levels 4–5)

Red-team and Crescendo attacks use **three separate models**:
target, attacker LLM, and scorer LLM.
Use different env var prefixes to configure each independently.

```env
# Target — the system under test
OPENAI_CHAT_ENDPOINT=http://localhost:1234/v1
OPENAI_CHAT_KEY=not-needed
OPENAI_CHAT_MODEL=llama3-8b

# Attacker LLM — generates attack prompts (needs to be capable)
OPENAI_ATTACKER_ENDPOINT=https://api.openai.com/v1
OPENAI_ATTACKER_KEY=sk-proj-xxxx
OPENAI_ATTACKER_MODEL=gpt-4o

# Scorer LLM — judges responses (must follow JSON format reliably)
OPENAI_SCORER_ENDPOINT=https://api.openai.com/v1
OPENAI_SCORER_KEY=sk-proj-xxxx
OPENAI_SCORER_MODEL=gpt-4o
```

---

## 5 · Verify Connection

```bash
python PAI/03_tools/PyRIT/labs/0.test_conection.py
```

Expected output:
```
✓ Target  : gpt-4o
✓ EndPoint: https://api.openai.com/v1
[response from model]
```

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `Central memory instance not initialized` | Add `await initialize_pyrit_async(...)` at top |
| `Could not load environment variables` | Check `~/.pyrit/.env` exists with correct keys |
| `APIConnectionError` | LM Studio / Ollama not running, or wrong port |
| `send_prompt_async() got unexpected keyword 'prompt'` | Use `Message` + `MessagePiece` objects, not plain strings |
