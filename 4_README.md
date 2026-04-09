# 🚀 LangChain SEO Blog Generator (Multi-Step Chain)

## 📌 Project Overview
This project demonstrates how to build a **multi-step sequential chain** using LangChain (LCEL) to generate a complete SEO-friendly blog.

The application performs:
1. Generate **keywords** from a topic  
2. Create a **blog outline** using those keywords  
3. Generate a **full article** based on the outline  

👉 This mimics a **real-world SEO content generation workflow**

---

## 🎯 Objective
Build a chain where:
- Step 1 → Topic → Keywords  
- Step 2 → Keywords → Blog Outline  
- Step 3 → Outline → Full Article  

---

## 🔗 Chain Flow

```text
Topic → Keywords → Outline → Full Article
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

```bash
git clone https://github.com/your-username/langchain-seo-blog-generator.git
cd langchain-seo-blog-generator
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
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Enter topic:

```text
👉 Enter topic: Digital Marketing
```

---

## 🧪 Example

### Input

```text
Digital Marketing
```

### Output

#### 🔑 Keywords

```text
digital marketing strategies, SEO, social media marketing, content marketing
```

#### 🧩 Blog Outline

```text
1. Introduction to Digital Marketing  
2. Importance of SEO  
3. Role of Social Media  
4. Content Marketing Strategies  
5. Conclusion  
```

#### 📄 Full Article

```text
Digital marketing is essential for businesses in the modern world...
It includes SEO, social media, and content strategies to reach audiences...
These techniques help businesses grow and compete effectively...
```

---

## 🧩 Project Structure

```text
langchain-seo-blog-generator/
│── main.py  
│── requirements.txt  
│── README.md  
│── .env  
```

---

## 🔗 Core Concepts

### Multi-Step Sequential Chains

```python
keyword_chain = prompt_keywords | model | parser
outline_chain = prompt_outline | model | parser
article_chain = prompt_article | model | parser
```

### Flow Implementation

```python
keywords = keyword_chain.invoke({"topic": topic})
outline = outline_chain.invoke({"keywords": keywords})
article = article_chain.invoke({"outline": outline})
```

---

## ⚙️ Features

* Dynamic topic input
* SEO keyword generation
* Structured blog outline creation
* Full article generation
* Real-world content pipeline

---

## 📚 Learnings

* Multi-step chaining in LangChain
* Passing outputs between steps
* Prompt engineering for SEO
* Building real-world GenAI applications

---

## 🚀 Use Case

👉 SEO Blog Automation
👉 Content Marketing Tools
👉 AI Writing Assistants

---

## 🤝 Contributing

Feel free to fork and enhance this project!

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Harsha

