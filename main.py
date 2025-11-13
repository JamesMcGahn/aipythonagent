import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()


def main():
    print("Hello from aipythonagent!")
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) != 2:
        print("Please include prompt")
        sys.exit(1)
        return

    prompt = sys.argv[1]

    content = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt,
    )
    print(content.text)
    print(f"Prompt tokens: {content.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {content.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
