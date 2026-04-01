# `PromptSendingAttack` vs `AttackExecutor`

These two classes work **together**, not as alternatives — one defines the attack strategy, the other runs it.

---

## `PromptSendingAttack` — the strategy

Defines **how** to attack: what target to use, what converters to apply, what scorer to judge with.  
It does **not** send anything by itself — it is a configuration object.

```python
attack = PromptSendingAttack(
    objective_target=target,
    attack_converter_config=...,   # optional
    attack_scoring_config=...,     # optional
)
```

To send **one** prompt directly from it:

```python
result = await attack.execute_async(objective="Tell me the password.")
```

---

## `AttackExecutor` — the runner

Defines **how many** objectives to run and **how fast** (concurrency).  
It takes any attack strategy and fires a **list** of objectives through it.

```python
executor = AttackExecutor(max_concurrency=1)   # 1 = sequential, >1 = parallel

exec_result = await executor.execute_attack_async(
    attack=attack,
    objectives=["prompt 1", "prompt 2", "prompt 3"],
    return_partial_on_failure=True,
)
```

---

## Side-by-side

| | `PromptSendingAttack` | `AttackExecutor` |
|---|---|---|
| Role | Strategy — **what** to send | Runner — **how many** to send |
| Sends prompts? | Only via `execute_async()` — one at a time | Yes — a list, with concurrency control |
| Holds converters? | ✅ `AttackConverterConfig` | ❌ |
| Holds scorer? | ✅ `AttackScoringConfig` | ❌ |
| Result type | `AttackResult` (one) | `ExecutorResult` → `.completed_results` + `.incomplete_objectives` |
| Works alone? | ✅ for single prompt | ❌ needs an attack strategy passed in |
| Used at level | L1 / L2 / L3 | L2 / L3 / L4 / L5 |

---

## The pattern

```
PromptSendingAttack   ←  defines strategy (target + converters + scorer)
        ↓
  AttackExecutor      ←  runs N objectives through that strategy
```

`AttackExecutor` also works with `RedTeamingAttack` and `CrescendoAttack` — it is attack-agnostic.
