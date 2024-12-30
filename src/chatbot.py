import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chatbot_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an IT help desk assistant."},
                {"role": "user", "content": user_input},
            ],
            max_tokens=200
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"
