
# 🚀 PyRIT Ship –  Guide

## 🧭 What is PyRIT Ship?
PyRIT Ship is a framework to **simulate and evaluate prompt-based attacks** against Large Language Models (LLMs).  
It integrates with **Burp Suite**, **OpenAI API**, and PyRIT’s **scoring engine** to automate adversarial testing and measure model robustness.

![image](imgs/PyRIT-Ship_Attack.png)

---

## 📌 References

* [Microsoft AI Red Teaming 101](https://www.youtube.com/watch?v=DabrWAKNQZc&list=PLlrxD0HtieHhXnVUQM42aKRPrirbUIDdh&index=1)
* [PyRIT](https://azure.github.io/PyRIT/)
* [PyRIT-Ship](https://github.com/microsoft/PyRIT-Ship/)

---

## ✅ Prerequisite
Before starting, make sure you have:

- **Burp Suite** → [Download](https://portswigger.net/burp)  
- **Java JDK 21** → [Download](https://jdk.java.net/java-se-ri/21)  
- **Python 3.11.x** → Download [(python.org)](https://www.python.org/downloads/release/python-3119/)  
- **OpenAI API Key** → [Get Key](https://platform.openai.com/account/api-keys)  
- **OpenAI Credits ($5+)** → [Check Usage](https://platform.openai.com/usage)  

---

## 🚀 Workflow Overview
Here’s the **big picture** of how PyRIT Ship works:

- **PyRIT Agent** → Your chosen OpenAI model (e.g., `gpt-4o`)  
- **Converters** → Encode/obfuscate prompts to bypass filters  
- **Target App** → Example: Gandalf (Lakera AI challenge)  
- **Scoring Engine** → Evaluates if the attack succeeded  

👉 More details: [Architecture Details.md](Architecture%20Details.md)

---
## 🛠️ Step-by-Step Process

Follow these high-level steps to get PyRIT Ship running. Each step links to its dedicated guide for details:

1. **Configure OpenAI Access**  
   - Create your API key and set up environment variables  
   👉 See: [OpenAI API.md](1.%20OpenAI%20API.md)

2. **Setup Burp Suite Extension**  
   - Compile/Deploy the PyRIT-Ship extension with Java + Gradle  
   👉 See: 
      
      [Build PyRIT-Ship](2.1.%20Build%20PyRIT-Ship%20Burp%20Extension.md)

      [Deploy PyRIT-Ship.md](2.2.%20Deploy%20PyRIT-Ship%20Burp%20Extension.md)

3. **Deploy PyRIT Server**  
   - Set up Python environment, install dependencies, and launch the server  
   👉 See: [PyRIT Ship Server.md](3.%20PyRIT%20Ship%20Server.md)

4. **Run an Attack Demo**  
   - Capture requests in Burp, configure Intruder, and analyze results  
   👉 See: Burp Gandalf Demo [Attack Example.md](4.%20Attack%20Example.md)

5. **Understand the Architecture**  
   - Learn how datasets, converters, agents, and scoring engine fit together  
   👉 See: [Architecture Details.md](Architecture%20Details.md)

---

## 🧠 Tips for Junior Pentesters
- Start with **Gandalf level 3+** for meaningful tests  
- Track **token usage** to manage API costs  
- Experiment with **converters** to improve evasion  
- Use results to **learn how LLM defenses work**  

