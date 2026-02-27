# PyRIT Mental Model: Three Roles, Three Models

---

## The Core Idea

Think of a security test like a **job interview with a hidden camera:**

| Role | Person in the analogy | In PyRIT |
|---|---|---|
| **Target** | The candidate being interviewed | The model you are testing |
| **Attacker** | The tricky interviewer asking hard questions | The model generating attack prompts |
| **Scorer** | The observer grading the answers | The model judging if the target failed |

They are **three separate jobs** — and each job needs a different kind of model.

---

## The Three Roles

### 🎯 Target
> *"The model under test. You want to break it."*

- Receives the attack prompts
- You are trying to make it say something it shouldn't
- Could be your production chatbot, a local model, an API endpoint
- **You do NOT control it** — you are the attacker

---

### 🔴 Attacker (Level 4+)
> *"The model that generates creative attack prompts."*

- Given an **objective** like `"make the target reveal a password"`
- Generates prompt after prompt trying to achieve that objective
- Adapts based on the target's responses (multi-turn)
- **You want this model to be clever and creative**

---

### 🧑‍⚖️ Scorer
> *"The model that reads the target's response and says pass or fail."*

- Gets the target's response as input
- Returns **True** (attack succeeded) or **False** (model stayed safe)
- Must follow strict JSON output format
- **You want this model to be precise and instruction-following**

---

## Visual Flow by Level

```
LEVEL 1 & 2  (no scorer)
─────────────────────────────────────────────
You ──[fixed prompt]──▶ TARGET ──▶ you read it


LEVEL 3  (fixed prompts + scorer)
─────────────────────────────────────────────
You ──[fixed prompt]──▶ TARGET ──▶ SCORER ──▶ True / False


LEVEL 4  (attacker LLM generates prompts)
─────────────────────────────────────────────
ATTACKER ──[generated prompt]──▶ TARGET ──▶ SCORER ──▶ True / False
    ▲                                                        │
    └────────────── feedback (try harder) ──────────────────┘


LEVEL 5  (multi-turn, attacker adapts)
─────────────────────────────────────────────
ATTACKER ◀──▶ TARGET  (back and forth, many turns)
                  │
                SCORER  (judges at the end)
```

---

## Which Model is Best for Each Role?

### 🎯 Target — use whatever you are actually testing

| Choice | When to use it |
|---|---|
| **Local model (LM Studio)** | Learning, cheap experiments, no data leaves your machine |
| **GPT-3.5** | Testing a mid-tier production chatbot behaviour |
| **GPT-4 / GPT-4o** | Testing a high-capability production model |
| **Your own fine-tuned model** | Testing your real deployed system |

> The target should be **the real thing** — or as close to it as possible.

---

### 🧑‍⚖️ Scorer — needs to follow instructions precisely

| Choice | Quality | Notes |
|---|---|---|
| **`SubStringScorer`** | ✅ Best for local | No LLM at all — keyword match, never fails |
| **Local 7B model** | ❌ Unreliable | Won't return strict JSON consistently |
| **GPT-3.5** | ⚠️ OK | Sometimes drifts from format |
| **GPT-4 / GPT-4o** | ✅ Best LLM option | Follows JSON format reliably every time |

> **Rule of thumb:** if the scorer is an LLM, it needs to be **smarter than the target** — otherwise it can't reliably judge it.  
> For local testing, `SubStringScorer` or `TrueFalseCompositeScorer` (keyword-based) are the safest choice.

---

### 🔴 Attacker — needs to be creative and persistent

| Choice | Quality | Notes |
|---|---|---|
| **Local 7B model** | ⚠️ Weak | Can generate prompts but not very creative |
| **GPT-3.5** | ⚠️ OK | Decent attacker for simple objectives |
| **GPT-4 / GPT-4o** | ✅ Best | Most creative, best at adapting to refusals |
| **Llama-3 70B+** | ✅ Good local option | Needs a powerful machine |

> The attacker benefits most from raw intelligence — a smarter attacker finds more jailbreaks.

---

## Summary in One Table

| Role | Job | Needs to be | Best local option | Best cloud option |
|---|---|---|---|---|
| 🎯 **Target** | Get attacked | Whatever you're testing | Any model in LM Studio | Your real GPT-3.5/4 deployment |
| 🧑‍⚖️ **Scorer** | Judge pass/fail | Precise, format-following | `SubStringScorer` (no LLM) | GPT-4o |
| 🔴 **Attacker** | Generate attacks | Creative, persistent | Llama-3 70B+ | GPT-4o |

---

## Key Takeaway

> You can point all three roles at **the same model** — PyRIT does not stop you.  
> But a 7B local model trying to be its own scorer will fail (as you just saw).  
> The safest local setup is:  
> - **Target** → any local model  
> - **Scorer** → `SubStringScorer` (no LLM)  
> - **Attacker** → same or a stronger local model (Level 4+)
