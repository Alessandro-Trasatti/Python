# Consider before.csv
# Even though each “row” in the file has three values (last name, first name, and house),
# the first two are combined into one “column” (name), escaped with double quotes, with last name and first name separated by a comma
# and space.
# Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:
# Dear Potter, Harry,
# Rather than with, for instance:
# # Dear Harry,
# In a file called scourgify.py, implement a program that:

# Expects the user to provide two command-line arguments:
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house,
# and the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

# Converts that input to that output, splitting each name into a first name and last name.
# Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments,
# or if the first cannot be read, the program should exit via sys.exit with an error message.

import os
from sys import argv, exit
from csv import DictReader, DictWriter


def main():
    validate_output()
    first_file_path = argv[1].strip()
    second_file_path = argv[2].strip()
    try:
        with open(first_file_path, 'r') as first_file:
            with open(second_file_path, 'w') as second_file:
                reader = DictReader(first_file)
                headers = ["first name", "last name", "house"]
                writer = DictWriter(second_file, fieldnames=headers)
                writer.writeheader()
                for row in reader:
                    first_name, last_name = row["name"].split(", ")
                    writer.writerow({"first name": first_name.strip(), "last name": last_name.strip(), "house": row["house"].strip()})
    except OSError as e:
        print(e)                
            
    
    
def validate_output() -> None:
    error_message = "Usage: scourgify.py <path1/some_file.csv> <path2/some_other_file.csv>"
    if len(argv) != 3:
        exit(error_message)
        
    first_file_path = argv[1].strip()
    second_file_path = argv[2].strip()
    if not first_file_path.endswith(".csv") or not second_file_path.endswith(".csv"):
        exit(f"The command line arguments should point to .csv files, but got {first_file_path} and {second_file_path}")
        exit(error_message)
    if not os.path.exists(first_file_path):
        exit(f"{first_file_path} does not exist.\n{error_message}")
    
if __name__ == "__main__":
    main()
