# In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file
# in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
# Format the table using the library’s grid format.
# If the user does not specify exactly one command-line argument,
# or if the specified file’s name does not end in .csv, or if the specified file does not exist,
# the program should instead exit via sys.exit.

import os
from sys import argv, exit
from csv import DictReader
from tabulate import tabulate

def main():
    validate_input()
    try:
        with open(argv[1], 'r') as file:
            print(tabulate(DictReader(file), headers="firstrow", tablefmt="grid"))
    except OSError as e:
        exit(f"Error: {e}")

def validate_input() -> None:
    error_message = "Usage: pizza.py <path/name_of_some_file.csv>"
    if len(argv) != 2:
        exit(f"Error: Invalid number of arguments.\n{error_message}")
        
    file_path = argv[1].strip()
    if not file_path.endswith(".csv"):
        exit(f"Error: {file_path} is not a .csv file.\n{error_message}")
    if not os.path.exists(file_path):
        exit(f"Error: {file_path} does not exist.\n{error_message}")

if __name__ == '__main__':
    main()