import os
import nest_asyncio
from dotenv import load_dotenv
from litellm import completion

# User se question lena
user_input = input("Enter your question: ")

# Asyncio loop apply karna
nest_asyncio.apply()

# Environment variables load karna
load_dotenv()

# Gemini API key set karna
api_key = os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = api_key

# User message send karna
messages = [{"role": "user", "content": f"{user_input}"}]
response = completion(model="gemini/gemini-2.0-flash", messages=messages)

# AI ka response print karna
print(response['choices'][0]['message']['content'])
