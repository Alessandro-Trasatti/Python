# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice
# of letters and numbers instead of random ones. Among the requirements, though, are:
# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements
# or Invalid if it does not. Assume that any letters in the user’s input will be uppercase.
import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    starts_with_two_letters = re.match(r"^[A-Z]{2}", s) is not None # re.match() returns a match object if the pattern is found at the start of the string, or None if there is no match. 
    is_correct_length = 2 <= len(s) <= 6
    ends_with_numbers_if_present = re.match(r'^([A-Z]*)([1-9][0-9]*)$', s) is not None
    has_no_special_characters = re.match(r"^[A-Z0-9]*$", s) is not None
    
    return starts_with_two_letters and is_correct_length and ends_with_numbers_if_present and has_no_special_characters

if __name__ == "__main__":
    main()