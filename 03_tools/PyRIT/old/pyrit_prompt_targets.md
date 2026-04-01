# PyRIT 0.11 — PromptTarget Types

> Reference for all ways to define a target in PyRIT.  
> Source: [PyRIT Docs](https://azure.github.io/PyRIT/code/targets/0_prompt_targets.html) + confirmed from working codebase.

---

## The Two Base Classes

Everything in PyRIT that receives a prompt inherits from one of two classes:

```
PromptTarget                  ← base: only needs send_prompt_async()
└── PromptChatTarget          ← extends base: adds system prompt + conversation history
```

| | `PromptTarget` | `PromptChatTarget` |
|---|---|---|
| `send_prompt_async()` | ✅ | ✅ |
| System prompt support | ❌ | ✅ |
| Conversation history | ❌ | ✅ |
| Required by multi-turn attacks (PAIR, TAP, Flip) | ❌ | ✅ |
| Works with `PromptSendingAttack` | ✅ | ✅ |
| Works with `RedTeamingAttack` / `CrescendoAttack` | ✅ | ✅ (preferred) |

---

## Approach 1 — Built-in `PromptChatTarget` subclasses

**When to use:** talking to a known LLM API.  
**What you get:** conversation history, system prompts, multi-turn support.

| Class | Backend | Import |
|---|---|---|
| `OpenAIChatTarget` | GPT-4, LM Studio, Ollama, any OpenAI-compatible endpoint | `from pyrit.prompt_target import OpenAIChatTarget` |
| `AzureMLChatTarget` | Azure Machine Learning hosted models | `from pyrit.prompt_target import AzureMLChatTarget` |
| `HuggingFaceChatTarget` | Local HuggingFace models | `from pyrit.prompt_target import HuggingFaceChatTarget` |
| `OllamaChatTarget` | Local Ollama server | `from pyrit.prompt_target import OllamaChatTarget` |

```python
# Reads OPENAI_* env vars automatically
target = OpenAIChatTarget()

# Point to a local LM Studio or Ollama endpoint
target = OpenAIChatTarget(
    model_name=os.getenv("OLLAMA_MODEL"),
    endpoint=os.getenv("OLLAMA_CHAT_ENDPOINT")
)
```

> **Used in your codebase as:** the attacker LLM in red-team attacks, the scorer LLM, and the target in all labs.

---

## Approach 2 — Built-in `PromptTarget` subclasses (non-chat)

**When to use:** the target is not a conversational LLM — it's an HTTP endpoint, storage, image gen, CTF challenge, etc.  
**What you get:** `send_prompt_async()` only — no history management.

### 2a. `HTTPTarget` — generic HTTP endpoint

The closest built-in to a fully custom target. Paste a raw HTTP request (from Burp, browser DevTools, or Wireshark) with `{PROMPT}` as the placeholder.

```python
from pyrit.prompt_target import HTTPTarget, get_http_target_json_response_callback_function

raw_http = """POST /api/chat HTTP/1.1
Host: my-app.com
Content-Type: application/json

{"message": "{PROMPT}"}"""

def parse_response(response):
    return response.json()["reply"]

target = HTTPTarget(
    http_request=raw_http,
    callback_function=parse_response,
    use_tls=True     # set False for HTTP-only endpoints
)
```

**Limitation for Gandalf adventure-6:** `HTTPTarget` does not handle multipart/form-data or rotating session cookies — that is why a custom class was needed.

---

### 2b. CTF / Challenge targets (built-in)

| Class | Platform | Import |
|---|---|---|
| `GandalfTarget` | [gandalf.lakera.ai](https://gandalf.lakera.ai) levels 1–8 | `from pyrit.prompt_target import GandalfTarget, GandalfLevel` |
| `CrucibleTarget` | DEF CON AI CTF ([crucible.dreadnode.io](https://crucible.dreadnode.io)) | `from pyrit.prompt_target import CrucibleTarget` |

```python
# Standard Gandalf levels (1-8) — built-in
from pyrit.prompt_target import GandalfTarget, GandalfLevel
target = GandalfTarget(level=GandalfLevel.LEVEL_1)

# DEF CON CTF challenge
from pyrit.prompt_target import CrucibleTarget
target = CrucibleTarget(endpoint="https://puppeteer1.crucible.dreadnode.io")
```

> **Note:** `GandalfTarget` built-in only covers levels 1–8.  
> Adventure-6 (Truthteller) has a different evaluation mechanism → requires a custom target.

---

### 2c. Multi-modal targets (built-in)

| Class | Modality | Backend |
|---|---|---|
| `OpenAIImageTarget` | text → image | DALL-E |
| `OpenAITTSTarget` | text → audio | OpenAI TTS |
| `OpenAIVideoTarget` | text → video | OpenAI Sora |
| `OpenAIResponsesTarget` | text → text (responses API) | OpenAI Responses |

---

### 2d. Storage / infrastructure targets (built-in)

| Class | Use case |
|---|---|
| `AzureBlobStorageTarget` | Azure Blob Storage — used in XPIA (cross-prompt injection) attacks |
| `PromptShieldTarget` | Azure Content Safety API — used as a scorer target |

---

### 2e. Browser / WebSocket targets (built-in)

| Class | Use case |
|---|---|
| `PlaywrightTarget` | Browser automation — interact with web UIs that have no API |
| `WebSocketTarget` | WebSocket-based AI applications |

---

## Approach 3 — Custom `PromptTarget` subclass

**When to use:** the target has special auth, session cookie rotation, non-standard request format (multipart, XML, GraphQL), or any logic `HTTPTarget` cannot express.  
**Examples in this project:** `GandalfTarget` (adventure-6), `PromptAirlinesTarget`.

### Minimum required implementation

```python
import httpx
from typing import Optional
from pyrit.prompt_target import PromptTarget
from pyrit.models.message import Message, MessagePiece

class MyCustomTarget(PromptTarget):

    _model_name = "my-app"          # mirrors OpenAIChatTarget attribute name
    _endpoint   = "https://..."     # mirrors OpenAIChatTarget attribute name

    def __init__(self, verbose=False, max_requests_per_minute=20):
        super().__init__(
            verbose=verbose,
            max_requests_per_minute=max_requests_per_minute,
        )

    def _validate_request(self, *, prompt_request_piece) -> None:
        # optional: raise ValueError for unsupported data types
        pass

    async def send_prompt_async(
        self,
        *,
        message: Message,
        target_identifier: Optional[dict] = None,
    ) -> list[Message]:

        user_text = next(
            (p.converted_value or p.original_value
             for p in message.message_pieces if p.role == "user"),
            "",
        )

        async with httpx.AsyncClient(http2=True, timeout=30) as client:
            resp = await client.post(
                "https://my-app.com/api",
                json={"prompt": user_text},
            )
            resp.raise_for_status()

        answer = resp.json().get("answer", "")

        return [Message(message_pieces=[
            MessagePiece(
                role="assistant",
                original_value=answer,
                converted_value=answer,
                original_value_data_type="text",
                converted_value_data_type="text",
            )
        ])]
```

Once implemented, it works **identically** to any built-in target:

```python
# Direct call (Level 1)
responses = await target.send_prompt_async(message=msg)

# With PromptSendingAttack (Level 1 / 2)
attack = PromptSendingAttack(objective_target=target)

# With AttackExecutor batch (Level 2)
executor = AttackExecutor(max_concurrency=1)
await executor.execute_attack_async(attack=attack, objectives=prompts)

# As the objective target in red-team / crescendo (Level 4 / 5)
attack = RedTeamingAttack(objective_target=target, ...)
```

---

## Full Hierarchy

```
PromptTarget                        ← base class
│   send_prompt_async()             ← only required method
│
├── PromptChatTarget                ← + system prompt + conversation history
│   ├── OpenAIChatTarget            ← GPT-4 / LM Studio / Ollama / any OpenAI-compat  ★ most used
│   ├── AzureMLChatTarget           ← Azure ML endpoints
│   ├── HuggingFaceChatTarget       ← local HuggingFace
│   └── OllamaChatTarget            ← local Ollama
│
├── HTTPTarget                      ← generic HTTP via raw request + {PROMPT} placeholder
│
├── GandalfTarget                   ← built-in for gandalf.lakera.ai levels 1–8
├── CrucibleTarget                  ← built-in for DEF CON CTF
│
├── OpenAIImageTarget               ← text → image (DALL-E)
├── OpenAITTSTarget                 ← text → audio
├── OpenAIVideoTarget               ← text → video
├── OpenAIResponsesTarget           ← OpenAI Responses API
│
├── AzureBlobStorageTarget          ← Azure storage (XPIA attacks)
├── PromptShieldTarget              ← Azure Content Safety
├── PlaywrightTarget                ← browser automation
├── WebSocketTarget                 ← WebSocket endpoints
│
└── <YourCustomTarget>              ← extend PromptTarget, implement send_prompt_async()
        gandalf_target.py           ← adventure-6 (Truthteller) — this project
        promptairlines_target.py    ← PromptAirlines CTF — this project
```

---

## Decision Guide

```
Do you need multi-turn conversation history? (PAIR, TAP, Crescendo)
  YES → PromptChatTarget subclass (OpenAIChatTarget)
  NO  ↓

Is it a known CTF platform?
  Gandalf levels 1-8  → GandalfTarget (built-in)
  DEF CON Crucible    → CrucibleTarget (built-in)
  Other / custom level → Custom PromptTarget ↓

Is the request format simple JSON / form with no session management?
  YES → HTTPTarget (paste raw HTTP, add {PROMPT})
  NO  ↓

Does it need: multipart/form-data, cookie rotation, custom auth, XML, GraphQL?
  YES → Custom PromptTarget subclass
        inherit PromptTarget, implement send_prompt_async()
```

---

*PyRIT v0.11.0 — [github.com/Azure/PyRIT](https://github.com/Azure/PyRIT)*
