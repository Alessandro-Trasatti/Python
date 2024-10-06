# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
# 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin,
# one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents,
# output how many cents in change the user is owed. Assume that the user will only input integers,
# and ignore any integer that isn’t an accepted denomination.

def main():
    total = 0
    COKE_PRICE = 50  # Using a constant for better readability
    
    while total < COKE_PRICE:
        print(f"Amount due: {COKE_PRICE - total} cents")
        coin = get_coin()
        total += coin
    
    print(f"Change owed: {total - COKE_PRICE} cents")


def get_coin():
    accepted_coins = [5, 10, 25] 
    try:
        coin = int(input("Insert coin (5, 10, 25 cents): "))
    except ValueError:
        # Handle non-integer inputs
        print("Invalid input. Please insert a valid coin.")
        return 0
    
    if coin not in accepted_coins:
        print("Coin not accepted. Please insert 5, 10, or 25 cents.")
        return 0
    
    return coin


if __name__ == "__main__":
    main()
    