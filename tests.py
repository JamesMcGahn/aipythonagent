from functions.get_files_info import get_files_info


def test_files(tests):
    for x in tests:
        working, dir = x
        print(f"Result for {dir} directory:")
        print(get_files_info(working, dir))


test_cases = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
]
test_files(test_cases)
