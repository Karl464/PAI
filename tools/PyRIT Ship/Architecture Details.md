## 🧱 Architecture Summary

![PyRIT_Security_Testing_Workflow](imgs/PyRIT_Security_Testing_Workflow.png)

```
[PyRIT Dataset] → [Converters] → [PyRIT Agent (LLM)] → [Target App (Gandalf)] → [Scoring Engine]
```

- **PyRIT Agent**: Your selected OpenAI model (e.g., `gpt-4o)
- **Converters**: Encode/obfuscate prompts to evade filters
- **Scoring Engine**: Evaluates if the attack bypassed defenses

### 🧠 PyRIT Agent Behavior and Dataset Strategy

In this setup, the **PyRIT Agent** refers to the **OpenAI model** selected in step 3 (e.g., `gpt-3.5-turbo` or `gpt-4o`). PyRIT dynamically **parameterizes the model to act as an attack agent**, systematically executing a wide range of adversarial prompts derived from curated datasets.

These prompts are often **encoded or obfuscated using converters** to bypass content filters and moderation systems. The goal is to simulate real-world adversarial behavior and evaluate the model’s robustness against various attack vectors.

### 📚 Attack Datasets

|Dataset|# Prompts|Category|Purpose|
|---|---|---|---|
|**jailbreaks**|150+|Filter Evasion|Test the model’s ability to resist prompt-based moderation bypasses|
|**illegal_harm**|200+|Harmful Content|Detect generation of illegal or dangerous outputs|
|**prompt_injection**|100+|Injection Attacks|Evaluate susceptibility to prompt injection vulnerabilities|
|**bias_testing**|300+|Fairness & Bias|Assess model bias and fairness across sensitive topics|
|**misinformation**|250+|Hallucinations|Test the model’s tendency to generate false or misleading information|
### 🧪 Converters

|**Converters**|Techniques used to transform prompts and evade detection (e.g., encoding, obfuscation, symbol substitution, spacing tricks)|
|---|---|
### 🎯 Scoring Engine

After each prompt is executed, the **Scoring Engine** analyzes the model’s response to determine whether the attack was successful. It uses predefined criteria to classify outputs as compliant, borderline, or violating — enabling automated evaluation of model vulnerabilities.