# Implement a program in Python that prompts the user for input and then outputs that same input
# in lowercase. Punctuation and whitespace should be outputted unchanged.
# You’re welcome, but not required, to prompt the user explicitly, as by passing a
# str of your own as an argument to input.

def main():
    indoor_voice = input("What does you indoor voice say? ").lower()
    print(indoor_voice)
    
if __name__ == "__main__":
    main()