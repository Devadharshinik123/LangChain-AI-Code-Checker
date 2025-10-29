## 🧠 LangChain-Powered Code Checker — Built with Gemini 2.5 Flash Pro

## Overview
This project goes beyond simple syntax checking, it's an AI-powered code reviewer that understands your code, explains errors in plain English, and even provides corrected versions.

By integrating LangChain with Google Gemini, I explored how AI can reason about code like a human reviewer — understanding logic, intent, and best practices.

## Tech Stack

🐍 Python 3.12 — Core programming language for building logic and backend

🦜 LangChain — Manages LLM reasoning and structured prompt flow

🤖 Google Gemini — Powers the AI’s understanding and code correction

🌐 FastAPI — Handles backend routes and connects to the Gemini model

🎨 Streamlit — Builds an interactive, user-friendly interface

🔐 python-dotenv — Secures environment variables and API keys

🧠 Git + GitHub — Version control and project hosting

⚡ requests, json — For data handling and API communication

## Project WorkFlow

🧑‍💻 User Input (Frontend – Streamlit)
The user pastes their Python code into the Streamlit interface and clicks “Check Code.”

📡 Request Handling (Backend – FastAPI)
The backend (app.py) receives the code via an API call and sends it to the Gemini model through LangChain.

🧠 AI Reasoning (Gemini + LangChain)

Gemini 2.5 analyzes the code and understands what the user intended.

It identifies syntax or logic errors.

Then it explains each issue in plain English and provides a corrected version of the code.

💬 Response Display (Frontend)
Streamlit displays both the error explanation and fixed code side-by-side — helping users learn from mistakes.

🔐 Secure Environment & Smooth UX

.env keeps your API keys safe.

The system remains responsive even under multiple user requests.

A smart AI-powered code checker that not only finds what’s wrong, but also teaches you why — bridging the gap between debugging and understanding.

## Features

🧠 AI-Powered Code Review — Uses Gemini model via LangChain to detect syntax and logic issues.

💬 Human-Like Explanations — Explains code mistakes in plain English for better learning.

⚙️ Real-Time Correction — Suggests improved or corrected versions of the input code.

🌐 Interactive Interface — Simple web app (Streamlit/FastAPI) for easy code submission and response.

🧩 Customizable Framework — Easily extendable to support other models or languages.

## Project Structure

CodeChecker/
│
├── app.py                  # FastAPI backend that connects to Gemini via LangChain  
├── client.py               # Streamlit frontend for user input and result display  
│
├── .env                    # Stores your Gemini API key securely (not uploaded to GitHub)  
├── requirements.txt        # Lists all required dependencies  
├── README.md               # Project documentation  
│
└── assets                  # Screenshots or demo images for README display  

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/code-checker-langchain.git
   cd code-checker-langchain

2. **Create a virtual environment**
   python -m venv venv
source venv/Scripts/activate  # On Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Add your Gemini API key**
Create a .env file in the root folder:
GEMINI_API_KEY=your_api_key_here

5. **Run the backend**
uvicorn app:app --reload

6. **Run the frontend**
streamlit run client.py

## Acknowledgement
Inspired by [Krish Naik’s](https://www.youtube.com/@krishnaik06) tutorials, which guided my understanding of AI integrations.
Grateful to ChatGPT (GPT-5) for structured assistance during development and documentation.
Built with curiosity, learning, and a drive to make AI reasoning more accessible.
## Connect with me
- 💼 [LinkedIn](https://linkedin.com/in/yourprofile)
- 🐙 [GitHub](https://github.com/yourusername)
- ✉️ 19devadharshini@gmail.com
