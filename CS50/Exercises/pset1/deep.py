# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

def main():
    correct_answers = ["42", "forty-two", "forty two"]
    ans = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower()
    if ans in correct_answers:
        print("Yes")
    else:
        print("No")
        
if __name__ == "__main__":
    main()