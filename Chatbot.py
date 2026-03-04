import os
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def start_chatbot():
    print("🤖 OpenAI Chatbot Active! (Type 'exit' to quit)")

    while True:
        # 1. Accept user input
        user_input = input("You: ")

        # 2. Check for exit condition
        if user_input.lower() == "exit":
            print("Shutting down... Goodbye!")
            break

        try:
            # sending the request to OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
            )

            # 5. Extract the AI's response
            ai_message = response.choices[0].message.content
            print(f"AI: {ai_message}")

        except Exception as e:
            print(f" An error occured: {e}")


if __name__ == "__main__":
    start_chatbot()
