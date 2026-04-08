

# 🚀 LangChain Simple Explanation Generator

## 📌 Project Overview

This project is a simple *LangChain-based application* that takes a user input (topic) and generates a **short, clean 3-line explanation** using an LLM.

It demonstrates the use of:

* LangChain Expression Language (LCEL)
* Prompt Templates
* Output Parsers
* LLM integration (OpenAI)

---

## 🎯 Features

* Accepts user input dynamically
* Generates concise explanations (no fluff)
* Limits output length (≤ 100 tokens)
* Clean and structured response
* Beginner-friendly implementation

---

## 🛠️ Tech Stack

* Python
* LangChain
* OpenAI GPT (gpt-4o-mini)
* dotenv

---

## ⚙️ Installation

### 1. Clone the repository

git clone [https://github.com/your-username/langchain-explainer.git](https://github.com/your-username/langchain-explainer.git)
cd langchain-explainer

### 2. Create virtual environment (optional but recommended)

python -m venv venv
venv\Scripts\activate   (Windows)
source venv/bin/activate (Mac/Linux)

### 3. Install dependencies

pip install -r requirements.txt

### 4. Setup environment variables

Create a `.env` file and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here

---

## ▶️ Usage

Run the script:
python main.py

Enter a topic when prompted:
Enter topic: What is Kubernetes?

---

## 🧪 Example

### Input

What is Kubernetes?

### Output

Kubernetes is an open-source platform for managing containerized applications.
It automates deployment, scaling, and operations of containers.
It is widely used in cloud-native and microservices architectures.

---

## 🧩 Project Structure

langchain-explainer/
│── main.py
│── requirements.txt
│── README.md
│── .env

---

## 🔗 Core Concept Used

### LCEL Chain

chain = prompt | model | StrOutputParser()

Flow:
User Input → Prompt → LLM → Parser → Output

---

## ⚠️ Constraints Implemented

* Temperature = 0.7
* Max output tokens = 100
* Output restricted to 3 lines

---

## 📚 Learnings

* How to build chains using LCEL (`|`)
* How to structure prompts effectively
* How to parse LLM outputs
* How to control response length

---

## 🤝 Contributing

Feel free to fork this repo and improve the project!

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Harsha


