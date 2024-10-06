# In a file called professor.py, implement a program that:

# Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits.
# No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE
# and prompt the user again, allowing the user up to three tries in total for that problem.
# If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.
# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3

from random import randint

def main():
    level = get_level()
    score = ten_problems(level)
    print(f"Your final score is: {score}/10")


def get_level() -> int:
    admissible_levels = {1, 2, 3}
    while True:
        try:
            level = int(input("Level: "))
            if level in admissible_levels:
                return level
            print("Please insert 1, 2 or 3")
        except ValueError:
            print("Please insert 1, 2 or 3")


def generate_integer(level: int) -> int:
    a = 10 ** (level - 1)
    b = 10 ** level -1
    return randint(a, b)

def ten_problems(level: int) -> int:
    score = 0
    for _ in range(10):
        int1 = generate_integer(level)
        int2 = generate_integer(level)
        correct_ans = int1 + int2
        for j in range(3):
            try:
                user_ans = int(input(f"{int1} + {int2} = "))
                if user_ans == correct_ans:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            if j == 2:
                print(f"The corect answer was {correct_ans}")
    return score

    
if __name__ == "__main__":
    main()