# from google import genai
from openai import OpenAI
import os

# Function for Google Gemini LLM call
#def call_llm(messages):
#    client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY", "--"))

    # Format messages with role labels for better context
#    prompt = "\n".join(f"{m['role'].capitalize()}: {m['content']}" for m in messages)

#    response = client.models.generate_content(
 #       model="gemini-3-pro-preview",
  #      contents=prompt,
   # )

#    return response.text

# Function for OpenAI LLM call
def call_llm(messages):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "--"))
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )
    
    return response.choices[0].message.content
    
if __name__ == "__main__":
    # Test the LLM call
    messages = [{"role": "user", "content": "In a few words, what's the meaning of life?"}]
    response = call_llm(messages)
    print(f"Prompt: {messages[0]['content']}")
    print(f"Response: {response}")