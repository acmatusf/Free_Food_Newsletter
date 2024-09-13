import os

from dotenv import load_dotenv  # Load environment variables from a .env file

# Load the .env file
load_dotenv()
import openai

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)
#Write it down
with open("eventcredential.txt", "r") as file:
    event_content = file.read()

#The end
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Write a short overview of each event, don't forget to include event name, time and place {event_content}",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
