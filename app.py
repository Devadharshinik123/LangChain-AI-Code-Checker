from fastapi import FastAPI
from langserve import add_routes
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os, uvicorn

# Load your Gemini API key from environment
load_dotenv()
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

# Get Gemini API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

# Set it as GOOGLE_API_KEY (used by Gemini client)
os.environ["GOOGLE_API_KEY"] = gemini_api_key

print("✅ GEMINI_API_KEY loaded successfully!")
# Initialize FastAPI
app = FastAPI(
    title="LangChain Code Checker",
    version="1.0",
    description="Check code for syntax and logical errors"
)
# Prompt Template
prompt = ChatPromptTemplate.from_template("""
You are an expert compiler and code reviewer.
Steps:
1. Parse the exact {input_code}.
2. If the code is syntactically broken, fix the syntax and explain briefly.
3. If the code has logical errors, explain and correct them.
4. Always provide the corrected code.

Respond in this format:

Language: <detected language>
Errors: <syntax or logical error details>
Corrected Code:
<corrected code>
""")

# Model (Gemini)
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-pro",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Output parser
output_parser = StrOutputParser()

# Create the chain
chain = prompt | llm | output_parser

# Register routes
add_routes(app, chain, path="/check")

@app.post("/check_debug")
def check_debug(request: dict):
    input_code = request.get("input_code", "")
    print("Received code:", input_code)
    output = chain.invoke({"input_code": input_code})
    print("Chain output:", output)
    return {"output": output}

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
