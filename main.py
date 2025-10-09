import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

def main():
    print("Hello from ai-agent-bootdev!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_prompt = " ".join(sys.argv[1:])
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]  

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages
        )
        print(response.text)
        #print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        #print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    except (IndexError, UnboundLocalError):
        print("Please provide an input within double quotes (\"\")")
        sys.exit(1)


    for arg in sys.argv[1:]:
        if arg == "--verbose":
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    
if __name__ == "__main__":
    main()
