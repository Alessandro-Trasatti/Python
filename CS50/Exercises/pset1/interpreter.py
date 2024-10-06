# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and
# outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted
# as x y z, with one space between x and y and one space between y and z, wherein:
# x is an integer, y is +, -, * or / and z is an integer.
import re


def main():
    while True:
        math_expression = input("Input some math expression: ")
        if is_valid(math_expression):
            computer(math_expression)
        else:
            print("Invalid math expression, which should be like x y z, with x,z integers, and y an elementary operation. Please retry!")
            
def is_valid(math_expression):
    return re.search(r"^\d (\+|-|\*|/) \d$", math_expression)

def computer(math_expression):
    x, operation, z = math_expression.split(" ")
    
    print("all good")
 
    match operation:
        case "+":
            print(f"{int(x) + int(z):.1f}")
        case "-":
            print(f"{int(x) - int(z):.1f}")
        case "*":
            print(f"{int(x) * int(z):.1f}")
        case "/":
            print(f"{int(x) / int(z):.1f}")

if __name__ == "__main__":    
    main()