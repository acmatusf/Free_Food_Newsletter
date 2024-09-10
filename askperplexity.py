import requests  # Library to send HTTP requests
import os  # Used to interact with the operating system
from dotenv import load_dotenv  # Load environment variables from a .env file

# Load the .env file
load_dotenv()

# Fetch the API key from the .env file
api_key = os.getenv("PERPLEXITY_API_KEY")
base_url = "https://api.perplexity.ai/chat/completions"  # API endpoint URL

# Set up the HTTP request headers with authorization and content type
headers = {
    "Authorization": f"Bearer {api_key}",  # Check if the API key is valid
    "Content-Type": "application/json"  # The request body is in JSON format (search up JSON format for more information)
}

#!!!!!!!!!!!!!!!!!!!

user_question = "Tell me about Perplexity AI." #Change the content of the question based on your needs

#!!!!!!!!!!!!!!!!!!!

# The request body containing the model and messages to send
data = {
    "model": "llama-3.1-sonar-small-128k-online",  # Model to use for the API request
    "messages": [
        {"role": "user", "content": user_question}  # The user input message
    ]
}

# Send the POST request to the API and get the response
response = requests.post(base_url, headers=headers, json=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the content of the response if successful
    print(response.json()["choices"][0]["message"]["content"])
else:
    # Print the error message if the request fails
    print(f"Error: {response.status_code} - {response.text}")
