# In a file called um.py, implement a function called count that expects a line of text as input as a str and returns, as an int,
# the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word.
# For instance, given text like hello, um, world, the function should return 1.
# Given text like yummy, though, the function should return 0.

import re

def main():
    print(count(input("Text: ")))

def count(s: str) -> int:
    # Use word boundaries (\b) to match "um" as a standalone word
    pattern = r"\bum\b"
    return len(re.findall(pattern, s, re.IGNORECASE))

if __name__ == "__main__":
    main()