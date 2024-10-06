# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case
# and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

def main():
    camel_filename = input("Please enter a filename in camel case: ")
    snake_filename = from_camel_to_snake_case(camel_filename)
    print("snake_filename: ", snake_filename)

    
def from_camel_to_snake_case(camel_filename: str):
    snake_filename = ""
    for character in camel_filename:
        if character.isupper():
            snake_filename += "_" + character.lower()
        else:
            snake_filename += character
    return snake_filename

def camel_to_snake_case_efficient(camel_filename: str): # This more efficient as strings are immutable in Python, concatenating them repeatedly (+=) can be inefficient because it creates a new string each time. Instead, you can build a list of characters and join them at the end.
    snake_filename = []
    for character in camel_filename:
        if character.isupper():
            snake_filename.append("_" + character.lower())
        else:
            snake_filename.append(character)
    return "".join(snake_filename)
        
    
    
if __name__ == '__main__':
    main()