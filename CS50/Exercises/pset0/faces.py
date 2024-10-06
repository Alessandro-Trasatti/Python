# In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any
# :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face).
# All other text should be returned unchanged.
# Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input,
# and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your
# own as an argument to input. Be sure to call main at the bottom of your file.

def main():
    input_string = input("Please enter a sentence: ")
    string_mod = convert(input_string)
    print(string_mod)
    string_mod_re = convert_re(input_string)
    print(string_mod_re)
    string_mod_re_dict = convert_re_dictionary(input_string)
    print(string_mod_re_dict)
    
def convert(string):
    string = string.replace(":)", "🙂").replace(":(", "🙁")
    return string

import re

def convert_re(string):
    string = re.sub(r":\)", "🙂", re.sub(r":\(", "🙁", string))
    return string

def convert_re_dictionary(string): # This soloution is to be preferred if a lot of replacements have to be done. The same could be done with str.replace()
    # Define the replacements in a dictionary
    replacements = {
        r":\)": "🙂",
        r":\(": "🙁"
    }
    # Perform the replacements using re.sub
    for pattern, emoji in replacements.items():
        string = re.sub(pattern, emoji, string)
    return string

if __name__ == "__main__":
    main()