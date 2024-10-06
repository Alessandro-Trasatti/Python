# Suppose that the data we are going to reformat is the user name and surname. For example we would like to have something standardized
# like Alessandro Trasatti. But some people might write something like Trasatti, Alessandro instead.
name = input("What is your name? ").strip()
# Hereby we will try to reformat name, in different ways and incrementally better
if ", " in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
# This won't work for example if the user doesn't type a space, which can happen with a lot of users
# Again, let's use regular expressions
import re
    
name = input("What is your name? ").strip()
matches = re.search(r"^(.+), *(.+)$") # This is one strong functionality of re.search : I could have written just r"^.+, .+$"
# Using parentheses as I did, will create groups that i can later get as in the following
if matches: # This is equivalent to saying "If I got a match" or "If I didn't get none"
    #last, first = matches.groups()
    #name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")

# I can tighten the code above using the walrus operator :=
name = input("What is your name? ").strip()

if matches := re.search(r"^(.+), *(.+)$"): 
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")