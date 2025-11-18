import os
from google.genai import types


def write_file(working_directory, file_path, content):
    try:
        working_dir = os.path.abspath(working_directory)
        full_path_dir = os.path.abspath(os.path.join(working_directory, file_path))

        if not full_path_dir.startswith(working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_path_dir):
            os.makedirs(os.path.dirname(full_path_dir), exist_ok=True)
        with open(full_path_dir, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {e}"


schema_write_file_info = types.FunctionDeclaration(
    name="write_file",
    description="writes file content for specified file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file path to read content from",
            ),
            "content": types.Schema(
                type=types.Type.STRING, description="content to write to the file"
            ),
        },
    ),
)
