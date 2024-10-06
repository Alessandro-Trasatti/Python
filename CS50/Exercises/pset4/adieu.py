# In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d.
# Assume that the user will input at least one name.
# Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and, in general, 
# n names with n-1 commas and a final "and".

import inflect

def main():
    formatted_names = get_names()
    print(f"\nAdieu, adieu, to {formatted_names}")
    
def get_names():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            if name:
                names.append(name) # Only non-empty names are being appended
        except EOFError:
            p = inflect.engine()
            return p.join(names)
        
def format_names(names): # In case you don't want to use the library inflect
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}"
    else:
        return f"{', '.join(names[:-1])}, and {names[-1]}"
    
    

if __name__ == "__main__":
    main()
