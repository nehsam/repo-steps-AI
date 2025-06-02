import os
import sys
import nest_asyncio
from dotenv import load_dotenv
from litellm import completion

# Apply nest_asyncio first
nest_asyncio.apply()

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Set the API key
os.environ["GEMINI_API_KEY"] = api_key

try:
    user_input = input("Enter your question: ")
    messages = [{"role": "user", "content": user_input}]
    
    response = completion(
        model="gemini/gemini-pro",  # Updated to use the correct model name
        messages=messages
    )
    
    print(response['choices'][0]['message']['content'])
except Exception as e:
    print(f"An error occurred: {str(e)}")