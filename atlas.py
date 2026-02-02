import os
import csv
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv

# Load the API Key from .env
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def log_result(prompt, response, category):
    file_exists = os.path.isfile('failures.csv')
    with open('failures.csv', mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Date', 'Prompt', 'Response', 'Category'])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), prompt, response, category])

def test_model(prompt):
    print("--- Sending to Groq (Llama 3) ---")
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    user_prompt = input("Enter your adversarial prompt: ")
    ai_response = test_model(user_prompt)
    
    print(f"\nAI Response:\n{ai_response}\n")
    
    is_failure = input("Did it fail? (y/n): ")
    if is_failure.lower() == 'y':
        cat = input("Category (Hallucination/Safety/Logic): ")
        log_result(user_prompt, ai_response, cat)
        print("Logged to failures.csv")