# Suppose that you’re in the habit of making a list of items you need from the grocery store.

# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d
# (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item.
# No need to pluralize the items. Treat the user’s input case-insensitively.


def main():
    grocery_list = get_grocery_list()
    format_grocery_list(grocery_list)
    
def get_grocery_list():
    grocery_list = dict()
    try:
        while True:
            item = input("Item: ").lower()
            if item not in grocery_list:
                grocery_list[item] = 1
            else:
                grocery_list[item] += 1
            
    except EOFError:
        print("\n")
        return grocery_list
    
def format_grocery_list(grocery_list):
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")
        
    
if __name__ == '__main__':
    main()
    