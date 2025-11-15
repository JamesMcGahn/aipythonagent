import os


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
