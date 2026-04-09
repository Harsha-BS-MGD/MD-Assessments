
# 🚀 LangChain Blog Generator (2-Step Chain)

## 📌 Project Overview
This project demonstrates how to build a **2-step sequential chain** using LangChain (LCEL).

The application:
1. Generates a **blog title** from a given topic  
2. Uses that title to generate **full blog content**

👉 This shows how **output of one step becomes input to the next step**

---

## 🎯 Objective
Build a chain where:
- Step 1 → Generate Blog Title  
- Step 2 → Generate Blog Content using that Title  

---

## 🔗 Chain Flow

```text
Topic → Blog Title → Blog Content
````

---

## 🛠️ Tech Stack

* Python
* LangChain (LCEL)
* OpenAI / OpenRouter
* dotenv

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langchain-blog-generator.git
cd langchain-blog-generator
```

### 2. Create virtual environment

```bash id="dx3k6b"
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies

```bash id="4h0f5v"
pip install -r requirements.txt
```

---

## 🔐 Setup Environment Variables

Create a `.env` file:

```env id="b2grjh"
OPENAI_API_KEY=your_api_key_here
```

(or use OpenRouter if configured)

---

## ▶️ Usage

Run the script:

```bash id="a8x8oz"
python main.py
```

Enter topic:

```text id="b1k5h3"
👉 Enter topic: Artificial Intelligence
```

---

## 🧪 Example

### Input

```text id="r8g9tk"
Artificial Intelligence
```

### Output

#### 📝 Generated Title

```text id="pl6qzy"
The Future of Artificial Intelligence in Everyday Life
```

#### 📄 Generated Blog Content

```text id="6m8m3p"
Artificial Intelligence (AI) is transforming the way we live and work.
From automation to decision-making, AI is integrated into many industries.
It continues to evolve and shape the future of technology.
```

---

## 🧩 Project Structure

```text id="0u9v0x"
langchain-blog-generator/
│── main.py  
│── requirements.txt  
│── README.md  
│── .env  
```

---

## 🔗 Core Concept

### Sequential Chain (LCEL)

```python id="r0x2xs"
title_chain = prompt_title | model | parser
content_chain = prompt_content | model | parser
```

### Flow Implementation

```python id="0m0zjz"
title = title_chain.invoke({"topic": topic})
content = content_chain.invoke({"title": title})
```

---

## ⚙️ Features

* Dynamic topic input
* Automatic blog title generation
* Content generation using previous output
* Clean and modular chain design

---

## 📚 Learnings

* How to build **sequential chains**
* Passing output between chains
* Prompt engineering for different steps
* Building real-world GenAI workflows

---

## 🤝 Contributing

Feel free to fork and improve this project!

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Harsha

