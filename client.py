import requests
import streamlit as st

st.title("LangChain Code Checker")

def get_ollama_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/check/invoke",
            json={'input': {'input_code': input_text}},
            timeout=180
        )
        data = response.json()
        return data.get("output", "⚠️ No output from backend.")
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Text box for code input
input_text = st.text_area("Write or paste your code here")

# Button to trigger check
if st.button("Check Code") and input_text.strip():
    result = get_ollama_response(input_text)
    st.text_area("Result", result, height=300)
