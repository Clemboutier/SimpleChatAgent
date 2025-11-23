"""Main chatbot implementation using PocketFlow."""

import pocketflow


class PocketChatbot:
    """A simple chatbot using PocketFlow framework."""
    
    def __init__(self, model_name="gpt-3.5-turbo"):
        """Initialize the chatbot with a specific model.
        
        Args:
            model_name: The LLM model to use
        """
        self.model_name = model_name
        self.conversation_history = []
    
    def chat(self, user_message):
        """Send a message and get a response.
        
        Args:
            user_message: The user's message
            
        Returns:
            The chatbot's response
        """
        self.conversation_history.append({"role": "user", "content": user_message})
        
        # TODO: Implement PocketFlow integration
        response = "Echo: " + user_message
        
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def clear_history(self):
        """Clear the conversation history."""
        self.conversation_history = []