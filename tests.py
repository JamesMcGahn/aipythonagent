from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# def test_files(tests):
#     for x in tests:
#         working, dir = x
#         print(f"Result for {dir} directory:")
#         print(get_files_info(working, dir))


# test_cases = [
#     ("calculator", "."),
#     ("calculator", "pkg"),
#     ("calculator", "/bin"),
#     ("calculator", "../"),
# ]
# test_files(test_cases)


# def test_files(tests):
#     for x in tests:
#         working, dir = x
#         print(f"Result for {dir} directory:")
#         print(get_files_info(working, dir))


# test_cases = [
#     ("calculator", "."),
#     ("calculator", "pkg"),
#     ("calculator", "/bin"),
#     ("calculator", "../"),
# ]
# test_files(test_cases)
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))
