# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4
# indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each
# of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If,
# though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    fuel_percentage = get_percentage()
    if fuel_percentage <= 1:
        print("E")
    elif fuel_percentage >= 99:
        print("F")
    else:
        print(f"{fuel_percentage}%")

def get_percentage() -> int:
    while True:
        fraction = input("Fraction: ")
        try:
            # Split and convert to integers
            num, den = map(int, fraction.split("/"))

            # Check for division by zero
            if den == 0:
                print("Error: The denominator cannot be zero. Please try again.")
                continue
            
            # Check that numerator is not greater than denominator
            if num > den:
                print("Error: The numerator cannot be greater than the denominator. Please try again.")
                continue
            
            # Calculate the percentage and return
            return round((num / den) * 100)

        # Handle value errors if inputs are not integers
        except ValueError:
            print("Error: Please enter the fraction in the form X/Y, where X and Y are integers.")

            
if __name__ == "__main__":
    main()