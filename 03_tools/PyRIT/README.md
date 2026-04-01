# Penetration Testing for AI (PAI) — Field Guide

> KISS methodology · Reusable by any tester · PyRIT 0.11.0 · Python 3.13+

---

## What Is This?

A structured, concise guide for running AI red-team engagements against LLM-based applications.
It covers environment setup, core concepts, and hands-on attack labs using PyRIT.

---

## Quick Start (3 steps)

```
Step 1 → ENV_SETUP.md       configure your API key / local model
Step 2 → CONCEPTS.md        understand the 3 roles and attack ladder
Step 3 → labs/              run the labs in order (0 → 5)
```

---

## Lab Overview

| Lab | Level | What it tests | Run when |
|-----|-------|---------------|----------|
| `0.test_conection.py` | 0 | Connection OK? | First thing, every session |
| `1.simple_attack.py`  | 1 | One prompt → manual review | Learn the flow |
| `2.batch_attack.py`   | 2 | Many prompts + encodings → manual review | Explore target behavior |
| `3.scored_attack.py`  | 3 | Batch + auto pass/fail scorer | Filter interesting responses |
| `4_red_team_attack.py`| 4 | LLM-generated attacks + scorer | Automated red-team loop |
| `5_crescendo_attack.py`| 5 | Multi-turn escalation with backtracking | Find context-dependent vulns |

---

## Lakera Challenges

> `Lakera_Challenges.md` — standalone challenge file, not modified, kept as-is.

Use the Gandalf challenges at [gandalf.lakera.ai](https://gandalf.lakera.ai) to practice
prompt injection in a safe sandboxed environment before testing real targets.
PyRIT has a built-in `GandalfTarget` for levels 1–8.

---

*PyRIT 0.11.0 · Python 3.11+ · [github.com/Azure/PyRIT](https://github.com/Azure/PyRIT)*
