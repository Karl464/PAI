# PyRIT Red Teaming Lab

**Hands-on lab for AI red teaming with Microsoft PyRIT framework**

⏱️ Time: 2-3 hours  
🎯 Goal: Learn to use PyRIT for automated AI security testing

---

## 🎓 What You'll Learn

By completing this lab:
- ✅ Setup PyRIT framework from scratch
- ✅ Run single-turn attacks (jailbreaks)
- ✅ Execute multi-turn conversations
- ✅ Use converters (encoders/obfuscators)
- ✅ Score attack results automatically
- ✅ Test against real targets (Gandalf)
- ✅ Analyze and document findings

---

## 📋 Prerequisites

**Must have completed:**
- [✓] [Preparation](../preparation/README.md) - LLM configured
- [✓] [Lakera Challenges](../labs/Lakera_Challenges.md) - Understanding of attacks

**Required:**
- Python 3.11.x
- OpenAI/Azure/Local LLM access
- 2GB free disk space
- Terminal/command line access

**Recommended:**
- Completed Lakera Levels 1-5 (understand manual techniques)
- Basic Python knowledge (helpful but not required)

---

## 🗂️ Lab Structure

This lab has 5 exercises:

```
Lab 1: Setup PyRIT           (30 min)
  → Install framework
  → Configure credentials
  → Test connection

Lab 2: Single-Turn Attacks   (30 min)
  → Run jailbreak prompts
  → Use converters
  → Score results

Lab 3: Multi-Turn Red Team   (45 min)
  → Conversational attacks
  → Strategy orchestration
  → Advanced techniques

Lab 4: Real Target Testing   (45 min)
  → Attack Gandalf Level 5+
  → Document findings
  → Analyze success patterns

Lab 5: Custom Workflows      (30 min)
  → Create your own attacks
  → Custom converters
  → Build datasets
```

---

## 🚀 Getting Started

### Choose Your Path:

**Path A: Complete Lab (3 hours)**
- Do all 5 labs in order
- Best for learning
- Full understanding of PyRIT

**Path B: Quick Essentials (1.5 hours)**
- Lab 1 + Lab 2 + Lab 4
- Core skills only
- Practical focus

**Path C: Advanced Only (1 hour)**
- Lab 3 + Lab 5
- Assumes you know basics
- Custom workflows

---

## 📚 Lab Files

### [Lab 1: Setup PyRIT](Lab1_Setup_PyRIT.md)
**What you'll do:**
- Install PyRIT framework
- Configure environment
- Test first attack
- Verify scoring works

**Key concepts:**
- Memory initialization
- Target configuration
- Prompt sending
- Basic scoring

### [Lab 2: Single-Turn Attacks](Lab2_Single_Turn_Attacks.md)
**What you'll do:**
- Run jailbreak prompts
- Apply Base64 encoding
- Use ROT13 converter
- Compare success rates

**Key concepts:**
- Converters
- Jailbreak datasets
- Success scoring
- Attack analysis

### [Lab 3: Multi-Turn Red Teaming](Lab3_Multi_Turn_RedTeam.md)
**What you'll do:**
- Orchestrate conversations
- Use strategies (crescendo, etc.)
- Chain multiple attacks
- Advanced scoring

**Key concepts:**
- Red Team Orchestrator
- Multi-turn strategies
- Objective-based attacks
- Complex workflows

### [Lab 4: Real Target Testing](Lab4_Real_Target_Testing.md)
**What you'll do:**
- Attack Gandalf Level 5+
- Test custom endpoints
- Document vulnerabilities
- Report findings

**Key concepts:**
- HTTP targets
- Custom prompts
- Result analysis
- Responsible disclosure

### [Lab 5: Custom Workflows](Lab5_Custom_Workflows.md)
**What you'll do:**
- Create custom converters
- Build attack datasets
- Write scoring logic
- Share your findings

**Key concepts:**
- Converter development
- Dataset creation
- Custom scorers
- Community contribution

---

## 💡 Lab Tips

### **Save Money:**
- Use `gpt-3.5-turbo` for practice (10x cheaper)
- Switch to `gpt-4o` only for final tests
- Local LLM (Dolphin) is free for attacker role

### **Best Setup:**
```
Attacker:  Local Dolphin (uncensored, free)
Target:    GPT-4o / Gandalf (what you're testing)
Scorer:    gpt-3.5-turbo (cheap, fast)
```

### **Track Progress:**
- Complete checkboxes in each lab
- Save code snippets you write
- Document successful attacks
- Note what doesn't work (learn from failures)

### **Get Help:**
- Check PyRIT docs: https://azure.github.io/PyRIT/
- Watch video series: https://www.youtube.com/playlist?list=PLlrxD0HtieHhXnVUQM42aKRPrirbUIDdh
- GitHub issues: https://github.com/Azure/PyRIT/issues
- Community discussions

---

## 🎯 Learning Objectives

By completing all labs, you will be able to:

**Technical Skills:**
- [ ] Install and configure PyRIT
- [ ] Run automated jailbreak attacks
- [ ] Use converters for obfuscation
- [ ] Score attack results
- [ ] Execute multi-turn strategies
- [ ] Test real-world targets
- [ ] Create custom workflows

**Security Analysis:**
- [ ] Identify LLM vulnerabilities
- [ ] Understand attack patterns
- [ ] Measure attack success rates
- [ ] Document findings professionally
- [ ] Recommend mitigations

**Ethical Practice:**
- [ ] Test only authorized systems
- [ ] Follow responsible disclosure
- [ ] Understand legal boundaries
- [ ] Respect API terms of service

---

## 📊 Expected Results

### **Lab 1 Success:**
```python
✅ PyRIT installed
✅ First attack executed
✅ Response received and scored
```

### **Lab 2 Success:**
```python
✅ 10+ jailbreak attempts
✅ 2+ different converters tested
✅ Success rate calculated
```

### **Lab 3 Success:**
```python
✅ Multi-turn conversation executed
✅ Orchestrator strategy working
✅ Objective achieved
```

### **Lab 4 Success:**
```python
✅ Gandalf Level 5+ password extracted
✅ Custom target tested
✅ Findings documented
```

### **Lab 5 Success:**
```python
✅ Custom converter created
✅ Custom dataset built
✅ Workflow automated
```

---

## 🔧 Common Issues

**Before Starting Labs:**

❌ **"PyRIT install fails"**
- Use Python 3.11.x (not 3.12+)
- Create virtual environment first
- Install dependencies separately if needed

❌ **"Memory initialization error"**
- Always call `initialize_pyrit()` first
- Use `IN_MEMORY` for learning
- Don't create targets before init

❌ **"OpenAI authentication failed"**
- Check .env file formatting
- Verify API key is valid
- Ensure sufficient credits

❌ **"Slow responses"**
- Normal for complex attacks
- Multi-turn takes 2-5 min
- Consider using gpt-3.5-turbo

---

## 📚 Reference Materials

### **Official PyRIT Resources:**
- Documentation: https://azure.github.io/PyRIT/
- GitHub: https://github.com/Azure/PyRIT
- Examples: https://github.com/Azure/PyRIT/tree/main/doc/code_examples

### **Video Tutorials:**
- PyRIT Overview: https://youtu.be/DwFVhFdD2fs
- Full Playlist: https://youtube.com/playlist?list=PLlrxD0HtieHhXnVUQM42aKRPrirbUIDdh

### **Related Labs:**
- Lakera Gandalf: https://gandalf.lakera.ai
- Manual Techniques: [../labs/Lakera_Challenges.md](../labs/Lakera_Challenges.md)

---

## 🎓 Certification Path (Optional)

After completing all labs:

1. **Self-Assessment Quiz**
   - 20 questions on PyRIT concepts
   - Hands-on challenge
   - Pass: 80%+

2. **Capstone Project**
   - Test authorized target
   - Document findings
   - Propose mitigations
   - Present results

3. **Community Contribution**
   - Share successful converter
   - Contribute to PyRIT dataset
   - Write blog post
   - Help others in discussions

---

## ⚠️ Legal & Ethical Notice

**CRITICAL - READ BEFORE STARTING:**

✅ **Authorized Testing Only:**
- Only test systems you own
- Or have written permission to test
- Gandalf is intentionally vulnerable (safe to test)

❌ **Never:**
- Attack production APIs without permission
- Test systems you don't own
- Violate API terms of service
- Use for malicious purposes

✅ **Responsible Disclosure:**
- Report vulnerabilities privately
- Give vendors time to fix
- Follow coordinated disclosure
- Document your process

✅ **Cost Management:**
- Set OpenAI spending limits
- Monitor token usage
- Use cheaper models for practice
- Local LLMs are free

---

## 🚀 Ready to Start?

### **Quick Start Checklist:**

- [ ] Prerequisites completed
- [ ] LLM configured and tested
- [ ] 2-3 hours available
- [ ] Understood legal notice
- [ ] Chose learning path

### **Next Step:**

**Begin with:** [Lab 1: Setup PyRIT](Lab1_Setup_PyRIT.md)

Or jump to specific lab if you're experienced.

---

## 💬 Feedback

After completing labs:
- What worked well?
- What was confusing?
- What would you add?
- Any errors to fix?

**Share your feedback:**
- GitHub Issues
- Discussions
- Pull Requests
- Community channels

---

## 📈 Track Your Progress

```
[ ] Lab 1: Setup PyRIT
[ ] Lab 2: Single-Turn Attacks
[ ] Lab 3: Multi-Turn Red Teaming
[ ] Lab 4: Real Target Testing
[ ] Lab 5: Custom Workflows

Completion: 0/5 labs
```

---

**Let's start red teaming! 🛡️**

*Estimated total time: 2-3 hours*  
*Difficulty: Intermediate*  
*Prerequisites: Manual attacks understanding*
