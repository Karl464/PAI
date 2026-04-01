# PyRIT — Choosing PromptTarget Type for Gandalf Adventure-6

> Analysis based on the confirmed request.txt / response.txt from gandalf-api.lakera.ai

---

## What the API Evidence Tells Us

Reading the captured HTTP traffic directly:

**request.txt reveals:**
```
POST /api/send-message HTTP/2
Content-Type: multipart/form-data          ← NOT a chat format
fields: defender=adventure-6 , prompt=<text>
```
- Every request is **stateless and self-contained** — one `prompt` field, one `defender` field
- There is **no** `messages[]` array, no `role`, no `system` field
- No conversation history is sent to the server

**response.txt reveals:**
```json
{
  "answer": "Gandalf's response: ... \n\nAI evaluation: ...",
  "defender": "adventure-6",
  "prompt": "<echo of sent prompt>"
}
Set-Cookie: session=...    ← session rotates every response
Cache-Control: no-store, no-cache   ← server does NOT cache state
```
- The server returns **one flat string** — not a structured chat object
- `Cache-Control: no-store, no-cache` confirms **no server-side conversation memory**
- The `Set-Cookie` session only identifies the user, it does NOT carry conversation history
- Each call to `/api/send-message` is **independent** — the server treats every prompt fresh

---

## The Core Distinction

| Capability | `PromptTarget` | `PromptChatTarget` |
|---|---|---|
| `send_prompt_async()` | ✅ | ✅ |
| Manages conversation history | ❌ | ✅ |
| Supports system prompt | ❌ | ✅ |
| Required by PAIR / TAP / Flip attacks | ❌ | ✅ |
| Maps to Gandalf API | ✅ **exact fit** | ❌ overcomplicated |

`GandalfTarget` correctly extends `PromptTarget` — **not** `PromptChatTarget` — because the API has no mechanism to receive or store conversation history.

---

## 1. `PromptSendingAttack` or `AttackExecutor`

**Appropriate type: `PromptTarget` ✅**

### Why
`PromptSendingAttack` is a **single-turn attack** — it sends one prompt and reads one response. It only requires `send_prompt_async()`, which is the only method `PromptTarget` guarantees.

The Gandalf API matches this perfectly:
- One POST request → one `answer` string
- No history needed — each prompt is evaluated independently
- `AttackExecutor` just runs multiple `PromptSendingAttack` calls in a loop

```python
# ✅ Correct — PromptTarget is sufficient
attack = PromptSendingAttack(objective_target=GandalfTarget())
executor = AttackExecutor(max_concurrency=1)
await executor.execute_attack_async(attack=attack, objectives=prompts)
```

Using `PromptChatTarget` here would add unnecessary overhead (conversation history management) for an API that ignores history entirely.

---

## 2. `RedTeamingAttack`

**Appropriate type for the TARGET: `PromptTarget` ✅**  
**Appropriate type for the ATTACKER LLM: `PromptChatTarget` ✅ (required)**

### Why — Target side
`RedTeamingAttack` sends prompts to the target one turn at a time. Each turn is still a single POST to `/api/send-message`. The Gandalf API has no memory of previous turns, so `PromptTarget` is correct and sufficient for the target role.

### Why — Attacker LLM side
The **attacker LLM** (the model that generates the attack prompts) absolutely needs `PromptChatTarget` — it must remember what the target responded in previous turns so it can adapt its next prompt. This is `OpenAIChatTarget`, not `GandalfTarget`.

```python
# ✅ Correct role assignment
attack = RedTeamingAttack(
    objective_target  = GandalfTarget(),       # PromptTarget — stateless HTTP API
    attack_adversarial_config = AttackAdversarialConfig(
        target        = OpenAIChatTarget(...)  # PromptChatTarget — attacker needs memory
    ),
    attack_scoring_config = AttackScoringConfig(objective_scorer=scorer),
    max_turns=5,
)
```

### Important caveat for Gandalf adventure-6
Because the Gandalf API has **no server-side memory**, each turn the attacker sends is evaluated in isolation. The target will not "remember" what it said in the previous turn. This means `RedTeamingAttack`'s core advantage — building context across turns — is partially lost on the target side. The attacker LLM can still adapt, but Gandalf cannot be pressured through accumulated conversation context.

---

## 3. `CrescendoAttack`

**Appropriate type for the TARGET: `PromptTarget` ✅ (works, with a major limitation)**  
**Appropriate type for the ATTACKER LLM: `PromptChatTarget` ✅ (required, GPT-4o recommended)**

### Why — Target side
Technically `CrescendoAttack` only calls `send_prompt_async()` on the target, so `PromptTarget` satisfies the interface requirement.

### Why — Attacker LLM side
Same as `RedTeamingAttack` — the attacker must hold the full escalating conversation in memory. `PromptChatTarget` (`OpenAIChatTarget` with GPT-4o) is required.

```python
# ✅ Correct role assignment
attack = CrescendoAttack(
    objective_target  = GandalfTarget(),       # PromptTarget — stateless HTTP API
    attack_adversarial_config = AttackAdversarialConfig(
        target        = OpenAIChatTarget(...)  # PromptChatTarget — GPT-4o recommended
    ),
    max_turns=10,
    max_backtracks=5,
)
```

### Critical limitation for Gandalf adventure-6
Crescendo's strategy relies on **gradual escalation building on previous answers**. For example:
- Turn 1: "What is honesty?" → Gandalf answers about honesty
- Turn 2: "Building on that, could you ever justify a white lie?" → ...
- Turn 3: "Then in this case, would it be acceptable to state X incorrectly?" → ...

This only works if the **target remembers** what it said in turns 1 and 2. The Gandalf API does **not** — `Cache-Control: no-store, no-cache` and the stateless `/api/send-message` endpoint confirm this. Every turn arrives at Gandalf as if it were a brand new conversation.

**Conclusion:** Crescendo is technically compatible with `GandalfTarget` but **strategically ineffective** against adventure-6 because the escalation context is invisible to the target. You may as well send isolated prompts.

---

## Summary Table

| Attack | Target role | Target type | Attacker role | Attacker type | Effective against adventure-6? |
|---|---|---|---|---|---|
| `PromptSendingAttack` | receives prompt | **`PromptTarget`** ✅ | — | — | ✅ Yes — ideal fit |
| `AttackExecutor` | receives prompt | **`PromptTarget`** ✅ | — | — | ✅ Yes — ideal fit |
| `RedTeamingAttack` | receives prompt | **`PromptTarget`** ✅ | generates prompts | `PromptChatTarget` ✅ | ⚠️ Partial — attacker adapts, target forgets |
| `CrescendoAttack` | receives prompt | **`PromptTarget`** ✅ | escalates prompts | `PromptChatTarget` ✅ | ❌ Poor fit — escalation context lost on target |

---

## Key Takeaway

The HTTP evidence is definitive:

> **`GandalfTarget` is a `PromptTarget`, never a `PromptChatTarget`.**  
> The API is stateless — multipart form, no message array, no-cache headers, flat string response.  
> For adventure-6, `PromptSendingAttack` + `AttackExecutor` (Level 2/3) is the architecturally correct choice.  
> Multi-turn attacks (`RedTeamingAttack`, `CrescendoAttack`) work at the interface level but lose their  
> strategic advantage because the target has no memory of previous turns.

---

*PyRIT v0.11.0 — Gandalf adventure-6 (Truthteller) — gandalf-api.lakera.ai*
