from pocketflow import Node, Flow
from utils import call_llm

class ChatNode(Node):
    def prep(self, shared):
        # Initialize messages if this is the first run
        if "messages" not in shared:
            shared["messages"] = []
            print("Hey this is Oscar! We can chat about anything. Type 'exit' to end the conversation.")
        
        # Get user input
        user_input = input("\n\033[91mYou:\033[0m ")
        
        # Check if user wants to exit
        if user_input.lower() == 'exit' or user_input.lower() == 'quit':
            return None
        
        # Add user message to history
        shared["messages"].append({"role": "user", "content": user_input})
                
        # Return all messages for the LLM
        return shared["messages"]

    def exec(self, messages):
        if messages is None:
            return None
        
        # Call LLM with the entire conversation history
        response = call_llm(messages)
        return response

    def post(self, shared, prep_res, exec_res):
        if prep_res is None or exec_res is None:
            print("\nGoodbye!")
            return None  # End the conversation
        
        # Print the assistant's response
        print(f"\n\033[91mOscar:\033[0m {exec_res}")
        
        # Add assistant message to history
        shared["messages"].append({"role": "assistant", "content": exec_res})
        
        # Loop back to continue the conversation
        return "continue"

# Create the flow with self-loop
chat_node = ChatNode()
chat_node - "continue" >> chat_node  # Loop back to continue conversation

flow = Flow(start=chat_node)

# Start the chat
if __name__ == "__main__":
    shared = {}
    flow.run(shared)

