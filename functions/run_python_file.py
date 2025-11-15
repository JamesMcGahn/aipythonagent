import os
import subprocess
import sys


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
