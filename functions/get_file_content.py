import os


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
