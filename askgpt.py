# To run the script, type in the terminal: python3 askgpt.py
# Also, to run any python file, remember to type in the terminal: python3 <filename.py>

# Remember to install openai: pip install openai
import openai
from dotenv import load_dotenv
import os
# Load the OpenAI API key from the .env file
load_dotenv()

# Set up the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Create the response
respond = openai.chat.completions.create(
  model="gpt-4o", # You can use either gpt-4o or gpt-4o-mini
  messages=[
    {"role": "system", "content": "You are a helpful assistant."}, # The system prompt
    {"role": "user", "content": "What is the meaning of the  word 'happy'?"} # The user prompt
  ]
)
# Print the response
print(respond.choices[0].message.content)
