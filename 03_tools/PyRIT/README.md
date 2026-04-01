# Penetration Testing for AI (PAI) — Field Guide

> KISS methodology · Reusable by any tester · PyRIT 0.11.0 · Python 3.13+

---

## What Is This?

A structured, concise guide for running AI red-team engagements against LLM-based applications.
It covers environment setup, core concepts, and hands-on attack labs using PyRIT.

---

## Folder Structure

```
PAI/
├── README.md                        ← you are here
│
├── 01_setup/
│   └── ENV_SETUP.md                 ← configure credentials for all AI backends
│
├── 02_concepts/
│   └── CONCEPTS.md                  ← mental model, 3 roles, attack levels
│
└── 03_tools/
    └── PyRIT/
        ├── PYRIT_GUIDE.md           ← full PyRIT reference (targets, methods, converters)
        └── labs/
            ├── 0.test_conection.py  ← verify your setup
            ├── 1.simple_attack.py   ← L1: one prompt, manual review
            ├── 2.batch_attack.py    ← L2: batch + converters, manual review
            ├── 3.scored_attack.py   ← L3: batch + auto scorer (pass/fail)
            ├── 4_red_team_attack.py ← L4: LLM generates prompts automatically
            └── 5_crescendo_attack.py← L5: multi-turn escalation + backtrack
```

---

## Quick Start (3 steps)

```
Step 1 → 01_setup/ENV_SETUP.md       configure your API key / local model
Step 2 → 02_concepts/CONCEPTS.md     understand the 3 roles and attack ladder
Step 3 → 03_tools/PyRIT/labs/        run the labs in order (0 → 5)
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
