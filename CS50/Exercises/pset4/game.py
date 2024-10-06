# In a file called game.py, implement a program that:
# Prompts the user for a level, 
# . If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and 
# , inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.


from random import randint
import sys


def main():
    level = prompt_for_positive_integer("Level")
    number = randint(1,level)
    while True:
        guess = prompt_for_positive_integer("Guess")
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            sys.exit("Just right!")
    
    
    
def prompt_for_positive_integer(string: str) -> int:
    while True:
        try:
            integer = int(input(string + ": ").strip())
            if integer > 0:
                return integer
            else:
                print(f"The program is expecting a positive integer!")
        except ValueError:
            print(f"The program is expecting a positive integer!")
    

if __name__ == '__main__':
    main()