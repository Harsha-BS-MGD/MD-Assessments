# 🚀 LangChain Prompt Template Demo

## 📌 Project Overview

This project demonstrates how to use **LangChain Prompt Templates** to generate dynamic responses based on different roles and audiences.

The goal is to show how the same topic can be explained differently depending on the **context and audience**.

---

## 🎯 Task

Create a prompt template:

```text
"You are a {role}. Explain {topic} for {audience}"
```

---

## 🧪 Test Inputs

### Case 1

* role = "teacher"
* audience = "5-year-old"

### Case 2

* role = "software architect"
* audience = "developer"

👉 Goal: **See adaptability of LLM responses**

---

## 🛠️ Tech Stack

* Python
* LangChain
* OpenAI / OpenRouter
* dotenv

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langchain-prompt-template.git
cd langchain-prompt-template
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Setup Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

(or use OpenRouter if configured)

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

---

## 💡 Example Outputs

### Input 1

```text
role = teacher  
audience = 5-year-old  
topic = "What is Kubernetes?"
```

### Output 1

```text
Kubernetes is like a helper that makes sure your apps run smoothly.
It keeps everything organized like your toy box.
It fixes problems automatically when something breaks.
```

---

### Input 2

```text
role = software architect  
audience = developer  
topic = "What is Kubernetes?"
```

### Output 2

```text
Kubernetes is a container orchestration platform.
It automates deployment, scaling, and management of microservices.
It is essential for building resilient cloud-native systems.
```

---

## 🧩 Project Structure

```text
langchain-prompt-template/
│── main.py  
│── requirements.txt  
│── README.md  
│── .env  
```

---

## 🔗 Core Concept

### Prompt Template

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "You are a {role}. Explain {topic} for {audience}"
)
```

---

## 📚 Learnings

* Dynamic prompt creation
* Context-aware responses
* Role-based explanation generation
* Prompt engineering basics

---

## 🤝 Contributing

Feel free to fork and improve this project!

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Harsha

