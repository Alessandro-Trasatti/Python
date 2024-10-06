# In a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
# and outputs the number of lines of code in that file, excluding comments and blank lines.
# If the user does not specify exactly one command-line argument,
# or if the specified file’s name does not end in .py,
# or if the specified file does not exist,
# the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
# (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

import os
from sys import argv, exit

def main():
    input_is_valid()
    print(number_of_lines(argv[1]))

def input_is_valid() -> None:
    error_message = "Usage: lines.py <path/name_of_some_file.py>"
    
    # Check for exactly one argument
    if len(argv) != 2:
        exit(error_message)
    
    file_path = argv[1].strip()

    # Check if file is a Python file
    if not file_path.endswith(".py"):
        exit(f"Error: {file_path} is not a Python file.\n{error_message}")
    
    # Check if file exists
    if not os.path.exists(file_path):
        exit(f"Error: {file_path} does not exist.\n{error_message}")

def number_of_lines(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = file.readlines()
        # Strip leading/trailing whitespace and filter out comments or blank lines
        return len([line for line in lines if line.strip() and not line.lstrip().startswith("#")])

if __name__ == "__main__":
    main()