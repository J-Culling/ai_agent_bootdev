import os
from dotenv import load_dotenv
from google import genai
import sys

def main():
    print("Hello from ai-agent-bootdev!")

    arg = sys.argv

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [
        genai.types.Contents(role="user", parts=[types.Part(text=user_prompt)])
    ]


    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages
        )
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    except (IndexError, UnboundLocalError):
        print("Please provide an input within double quotes (\"\")")
        sys.exit(1)

if __name__ == "__main__":
    main()
