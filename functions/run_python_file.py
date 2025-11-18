import os
import subprocess
import sys
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    working_dir = os.path.abspath(working_directory)
    full_path_dir = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path_dir.startswith(working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if len(file_path) > 3 and file_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    if not os.path.exists(full_path_dir):
        return f'Error: File "{file_path}" not found.'

    args = [sys.executable, full_path_dir] + args
    result = subprocess.run(
        args,
        capture_output=True,
        shell=False,
        cwd=None,
        timeout=30,
    )
    # print(result)

    return f"""STDOUT: {result.stdout}
STDERR: {result.stderr}
{f"Process exited with code {result.returncode}" if result.returncode > 0 else "" }
{"No output produced." if not{result.stdout} or not {result.stderr} else "" }
"""


schema_run_python_file_info = types.FunctionDeclaration(
    name="run_python_file",
    description="runs python file content for specified file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file path to read content from",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional arguments to pass to the function",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
            ),
        },
    ),
)
