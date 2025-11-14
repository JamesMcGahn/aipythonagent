import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir = os.path.abspath(working_directory)
        full_path_dir = os.path.abspath(os.path.join(working_directory, directory))

        if not os.path.isdir(full_path_dir):
            return f'Error: "{directory}" is not a directory'
        elif not full_path_dir.startswith(working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        output = ""
        for item in os.listdir(full_path_dir):
            is_dir = os.path.isdir(os.path.join(full_path_dir, item))
            size = os.path.getsize(os.path.join(full_path_dir, item))
            output += f" - {item} file_size={size} bytes, is_dir={is_dir}\n"
        return output
    except Exception as e:
        return f"Error: {e}"
