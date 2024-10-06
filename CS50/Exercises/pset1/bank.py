# In a file called bank.py, implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”),
# output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
# and treat the user’s greeting case-insensitively.

def main():
    greeting = input("Say a greeting: ").lower().strip()
    print(f"${prize(greeting)}")
    
def prize(greeting: str) -> int:
    if greeting[:5] == "hello": # Equivalently, we could use the mothod str.startswith()
        return 0
    if greeting[0] == "h":
        return 20
    return 100

if __name__ == "__main__":
    main()