import os
from google.genai import types


def get_file_content(working_directory, file_path):
    try:
        working_dir = os.path.abspath(working_directory)
        full_path_dir = os.path.abspath(os.path.join(working_directory, file_path))
        print(full_path_dir)
        if not os.path.isfile(full_path_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        elif not full_path_dir.startswith(working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        MAX_CHARS = 10000

        with open(full_path_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        return file_content_string
    except Exception as e:
        return f'Error: {e}"'


schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="reads file content for specified file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file path to read content from",
            ),
        },
    ),
)
