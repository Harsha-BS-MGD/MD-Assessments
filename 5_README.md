# 🚀 Multi-Platform Content Generator (LangChain)

## 📌 Project Overview
This project demonstrates how to generate **multiple types of content from a single input topic** using LangChain (LCEL).

The application takes one topic and generates:
- 🐦 Tweet  
- 💼 LinkedIn Post  
- 📸 Instagram Caption  

👉 This shows how **one input can produce multiple outputs for different platforms**

---

## 🎯 Objective
Given a single topic:
- Generate a **Tweet**
- Generate a **LinkedIn post**
- Generate an **Instagram caption**

---

## 🔗 Flow

```text
Topic → Tweet  
      → LinkedIn Post  
      → Instagram Caption
````

---

## 🛠️ Tech Stack

* Python
* LangChain (LCEL)
* OpenRouter / OpenAI
* dotenv

---

## ⚙️ Installation

### 1. Clone the repository

```bash id="v0jz0k"
git clone https://github.com/your-username/multi-content-generator.git
cd multi-content-generator
```

### 2. Create virtual environment

```bash id="s0p1mt"
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies

```bash id="qz6n2h"
pip install -r requirements.txt
```

---

## 🔐 Setup Environment Variables

Create a `.env` file:

```env id="n8d1vp"
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the script:

```bash id="3y2n4r"
python main.py
```

Enter topic:

```text id="r7c9l1"
👉 Enter topic: Artificial Intelligence
```

---

## 🧪 Example

### Input

```text id="g1d3xz"
Artificial Intelligence
```

### Output

#### 🐦 Tweet

```text id="d4e2kc"
AI is transforming the world faster than ever! 🚀 #AI #Technology
```

#### 💼 LinkedIn Post

```text id="k9p2qv"
Artificial Intelligence is reshaping industries by enabling smarter decisions...
It plays a key role in automation and innovation across sectors.
```

#### 📸 Instagram Caption

```text id="p8r6tm"
Exploring the future with AI 🤖✨ #AI #Innovation #FutureTech
```

---

## 🧩 Project Structure

```text id="y7b3nm"
multi-content-generator/
│── main.py  
│── requirements.txt  
│── README.md  
│── .env  
```

---

## 🔗 Core Concept

### Parallel / Multi Output Chains

```python id="x3n7va"
tweet_chain = prompt_tweet | model | parser
linkedin_chain = prompt_linkedin | model | parser
instagram_chain = prompt_instagram | model | parser
```

### Flow Implementation

```python id="z4t9ks"
tweet = tweet_chain.invoke({"topic": topic})
linkedin = linkedin_chain.invoke({"topic": topic})
instagram = instagram_chain.invoke({"topic": topic})
```

---

## ⚙️ Features

* Single topic input
* Multi-platform content generation
* Platform-specific tone and style
* Clean and modular chain design

---

## 📚 Learnings

* Multi-output generation using LangChain
* Prompt engineering for different platforms
* Parallel thinking in GenAI workflows
* Real-world content automation

---

## 🚀 Use Cases

👉 Social Media Automation
👉 Content Marketing Tools
👉 Personal Branding Assistants

---

## 🤝 Contributing

Feel free to fork and enhance this project!

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Harsha

