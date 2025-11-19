from .get_file_content import get_file_content
from .get_files_info import get_files_info
from .run_python_file import run_python_file
from .write_file import write_file
from google.genai import types


def call_function(function_call_part, verbose=False):
    func_name = function_call_part.name
    func_args = function_call_part.args
    func_args["working_directory"] = "./calculator"
    if verbose:
        print(f"Calling function: {func_name}({func_args})")
    else:
        print(f" - Calling function: {func_name}")

    functions = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }
    func = functions.get(func_name, False)
    print("found func", func)
    if not func:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"error": f"Unknown function: {func_name}"},
                )
            ],
        )
    else:
        function_result = func(**func_args)
        print("*********", function_result)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"result": function_result},
                )
            ],
        )
