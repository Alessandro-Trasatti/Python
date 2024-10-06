import re

def main():
    price = get_price()
    dollars = dollars_to_float(price)
    tip_percentage = get_percentage_tip()
    percent = percent_to_float(tip_percentage)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def get_price():
    '''
    should accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
    '''
    while True:
        price = input("How much was the meal? ")
        mathces = re.match(r"^\$(\d)?\d\.(\d)?(\d)?$", price)
        if mathces:
            return price
        else:
            print("Invalid format, please try again. ", end = "")
            
    
def get_percentage_tip():
    '''
    should accept a str as input (formatted as ##%, wherein each # is a decimal digit),
    '''
    while True:
        tip_percentage = input("What percentage would you like to tip? ")
        matches = re.match(r"^\d*\%$", tip_percentage)
        if matches:
            return tip_percentage
        else:
            print("Invalid format, please try again. ", end = "")
        

def dollars_to_float(d):
    '''
    remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
    '''
    return float(d[1:]) # again, you could use the .replace()


def percent_to_float(p):
    '''
    remove the leading %, and return the amount as a float.
    '''
    return float(p[:-1]) / 100 # again, you could use the .replace()


if __name__ == "__main__":
    main()