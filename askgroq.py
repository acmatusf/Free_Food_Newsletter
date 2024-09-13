import os

from dotenv import load_dotenv  # Load environment variables from a .env file

# Load the .env file
load_dotenv()
import openai

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is USF",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
