import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()


def main():

    print("Hello from aipythonagent!")
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) <= 1:
        print("Please include prompt")
        sys.exit(1)
        return

    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    content = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {content.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {content.usage_metadata.candidates_token_count}")

    print(content.text)


if __name__ == "__main__":
    main()
