import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

class Chatbot:
    def __init__(self):
        try:
            # Initialize Gemini with API key from environment variable
            api_key = os.getenv('GEMINI_API_KEY')
            if not api_key:
                raise ValueError("GEMINI_API_KEY not found in environment variables")
            
            # Configure the API
            genai.configure(api_key=api_key)
            
            # Print available models
            print("\nAvailable models:")
            for m in genai.list_models():
                print(f"- {m.name}")
            print()
            
            # Initialize the model
            generation_config = {
                "temperature": 0.9,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": 2048,
            }
            
            # Initialize the model with the correct name
            self.model = genai.GenerativeModel("gemini-pro",
                                             generation_config=generation_config)
            
            # Start chat
            self.chat = self.model.start_chat(history=[])
            
        except Exception as e:
            print(f"Initialization error: {str(e)}")
            exit(1)
        
    def chat_gemini(self, prompt):
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
            if user_input.lower() == 'quit':
                print("Chatbot: Goodbye!")
                break
                
            response = chatbot.chat_gemini(user_input)
            print("Chatbot:", response)
            
    except KeyboardInterrupt:
        print("\nChatbot: Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()