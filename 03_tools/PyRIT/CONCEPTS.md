# Core Concepts

> Read this once before running any labs.

---

## The 3 Roles

Every AI red-team test involves up to 3 actors:

```
[ATTACKER MODEL]  ──prompt──►  [TARGET]  ──response──►
    (optional)                                │
                           [SCORER]  ◄────────┘
                           (optional)
```

| Role | What it does | Required? |
|------|-------------|-----------|
| 🎯 **Target** | The AI system under test — receives prompts, returns responses | Always |
| 🔴 **Attacker LLM** | Generates creative attack prompts automatically, adapts based on responses | Levels 4–5 only |
| 🧑‍⚖️ **Scorer** | Judges each response: did the attack succeed? (True/False or 0.0–1.0) | Levels 3–5 |

### Choosing Models for Each Role

| Role | Best local option | Best cloud option | Minimum quality |
|------|------------------|-------------------|-----------------|
| 🎯 Target | Any model in LM Studio | Your real deployment | Whatever you're testing |
| 🔴 Attacker | Llama-3 70B+ | GPT-4o | Must be creative & persistent |
| 🧑‍⚖️ Scorer | `SubStringScorer` (no LLM) | GPT-4o | Must follow JSON format reliably |

> **Rule:** The scorer must be smarter than the target — otherwise it can't reliably judge it.

---

## The Attack Ladder (L0 → L5)

Start at L0. Move up as you understand each level.

```
L0  Connection test         — does the target even respond?
L1  One fixed prompt        — manual review, learn the target
L2  Batch fixed prompts     — explore behavior, still manual review
L3  Batch + scorer          — automated pass/fail, no more reading every line
L4  LLM-generated prompts   — attacker writes its own attacks, scorer judges
L5  Multi-turn escalation   — attacker adapts each turn, backtracks on refusal
```

### What Each Level Needs

| Level | Target | Fixed Prompts | Attacker LLM | Scorer |
|-------|--------|---------------|--------------|--------|
| L0 | ✅ | 1 | ❌ | ❌ |
| L1 | ✅ | 1 | ❌ | ❌ |
| L2 | ✅ | many | ❌ | ❌ |
| L3 | ✅ | many | ❌ | ✅ |
| L4 | ✅ | ❌ | ✅ | ✅ |
| L5 | ✅ | ❌ | ✅ | ✅ (built-in) |

---

## PyRIT Building Blocks

### Targets — what receives prompts

```
PromptTarget (base)
├── PromptChatTarget          adds system prompt + conversation history
│   ├── OpenAIChatTarget  ★   GPT-4, LM Studio, Ollama, any OpenAI-compatible endpoint
│   ├── AzureMLChatTarget
│   └── OllamaChatTarget
├── HTTPTarget                paste a raw HTTP request with {PROMPT} placeholder
├── GandalfTarget             built-in for gandalf.lakera.ai levels 1–8
├── CrucibleTarget            built-in for DEF CON CTF
└── <YourCustomTarget>        extend PromptTarget, implement send_prompt_async()
```

**Which to use:**
- Standard LLM API → `OpenAIChatTarget`
- Simple JSON HTTP endpoint → `HTTPTarget` (paste raw request, use `{PROMPT}`)
- Custom auth / session cookies / multipart → subclass `PromptTarget`
- Multi-turn attacks → must use `PromptChatTarget` subclass

### Sending Methods — how prompts are sent

| Method | Level | Use when |
|--------|-------|----------|
| `target.send_prompt_async()` | L0 | Testing connection, manual loops |
| `PromptSendingAttack` | L1–L3 | One prompt, optional converter & scorer |
| `AttackExecutor` | L2–L5 | Batch: many prompts in one call |
| `RedTeamingAttack` | L4 | Attacker LLM generates & adapts prompts |
| `CrescendoAttack` | L5 | Gradual escalation, backtracks on refusal |

### Scorers — how results are judged

| Scorer | LLM needed? | Use when |
|--------|-------------|----------|
| `SubStringScorer` | ❌ | Check if a keyword appears in the response |
| `RegexScorer` | ❌ | Pattern match on the response |
| `SelfAskTrueFalseScorer` | ✅ | LLM judges if response violates a policy |
| `SelfAskScaleScorer` | ✅ | LLM rates harmfulness on 0.0–1.0 scale |

### Converters — prompt transformations before sending

| Converter | What it does | Use for |
|-----------|-------------|---------|
| `Base64Converter` | Encodes prompt in Base64 | Bypassing keyword filters |
| `ROT13Converter` | ROT-13 substitution | Obfuscating intent |
| `UnicodeSubstitutionConverter` | Replaces letters with Unicode lookalikes | Evading content checks |

Converters can be chained: `prompt → Base64 → ROT13 → target`

---

## Decision Trees

### Which Target Type?
```
Need multi-turn conversation history?
  YES → OpenAIChatTarget (PromptChatTarget)
  NO  ↓
Simple JSON endpoint?
  YES → HTTPTarget (paste raw request, {PROMPT})
  NO  ↓
Custom auth / cookies / multipart?
  YES → Custom PromptTarget subclass
```

### Which Attack Level?
```
Need automated prompt generation?
  YES → L4 RedTeamingAttack or L5 CrescendoAttack
  NO  ↓
Many prompts to test?
  YES → L2/L3 AttackExecutor + PromptSendingAttack
  NO  ↓
Need auto pass/fail scoring?
  YES → L3 PromptSendingAttack + scorer
  NO  ↓
Just exploring target behavior?
  YES → L1 PromptSendingAttack (read manually)
  NO  → L0 target.send_prompt_async()
```

### RedTeaming vs Crescendo (L4 vs L5)?

| | `RedTeamingAttack` (L4) | `CrescendoAttack` (L5) |
|---|---|---|
| Strategy | Adaptive, free-form | Gradual escalation from benign |
| On refusal | Continues to next turn | **Backtracks** (removes turn from memory) |
| Scorer type | True / False | Float 0.0–1.0 |
| Attacker model | GPT-4o-mini works | **GPT-4o recommended** (strict JSON required) |
| Use when | General automated red-team | Target only vulnerable after multiple turns |
