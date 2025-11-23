"""Basic example of using PocketChatbot."""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from chatbot import PocketChatbot


def main():
    """Run a basic chatbot example."""
    bot = PocketChatbot()
    
    print("PocketChatbot initialized! Type 'quit' to exit.")
    print("-" * 50)
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        response = bot.chat(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
