import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.write_file import schema_write_file_info
from functions.run_python_file import schema_run_python_file_info
from functions.get_file_content import schema_get_files_content
from functions.call_function import call_function

load_dotenv()


def main():

    print("Hello from aipythonagent!")
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) <= 1:
        print("Please include prompt")
        sys.exit(1)
        return
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_write_file_info,
            schema_run_python_file_info,
            schema_get_files_content,
        ]
    )
    try:
        for _ in range(0, 4):
            content = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=system_prompt
                ),
            )

            candidates = content.candidates
            for can in candidates:
                messages.append(can.content)

            verbose = False
            if "--verbose" in sys.argv:
                verbose = True
                print(f"User prompt: {user_prompt}")
                print(f"Prompt tokens: {content.usage_metadata.prompt_token_count}")
                print(
                    f"Response tokens: {content.usage_metadata.candidates_token_count}"
                )

            calls = content.function_calls
            parts_list = []
            if not calls and not content.text:
                break
            if calls:
                for function_call_part in calls:
                    response = call_function(function_call_part, verbose)
                    if response and len(response.parts) > 0:
                        parts_list.append(response.parts[0])

                        if verbose:
                            print(f"-> {response.parts[0].function_response.response}")

                    else:
                        raise Exception("Error")
                messages.append(types.Content(role="user", parts=parts_list))
            else:
                print(content.text)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
