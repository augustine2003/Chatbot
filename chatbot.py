import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()


class Chatbot:
    def __init__(self):
        try:
            # Initialize with API key from environment variable
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("GEMINI_API_KEY not found in environment variables")

            # Configure the API
            genai.configure(api_key=api_key)

            # Use Gemini 1.5 Flash model
            model_name = "gemini-1.5-flash"
            print(f"\nUsing model: {model_name}")

            # Initialize the model with appropriate settings for Gemini 1.5 Flash
            generation_config = {
                "temperature": 0.7,
                "top_p": 0.8,
                "top_k": 40,
                "max_output_tokens": 1024,
            }

            # Initialize the model
            self.model = genai.GenerativeModel(
                model_name, generation_config=generation_config
            )

        except Exception as e:
            print(f"Initialization error: {str(e)}")
            exit(1)

    def generate_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"An error occurred: {str(e)}"


def main():
    try:
        chatbot = Chatbot()
        print("\nChatbot: Hello! How can I help you today? (Type 'quit' to exit)")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                print("Chatbot: Goodbye!")
                break

            response = chatbot.generate_response(user_input)
            print("Chatbot:", response)

    except KeyboardInterrupt:
        print("\nChatbot: Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
