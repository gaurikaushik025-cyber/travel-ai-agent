import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def ask_llm(prompt, system_prompt=""):
    """Ask Gemini LLM with structured output"""
    full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def parse_json_from_text(text):
    """Extract JSON from LLM response"""
    try:
        # Find JSON block
        start = text.find('{')
        end = text.rfind('}') + 1
        json_str = text[start:end]
        return json.loads(json_str)
    except:
        return {}