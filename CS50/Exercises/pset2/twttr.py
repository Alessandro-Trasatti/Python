# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels,
# much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts
# the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

def main():
    text = input("Enter some text: ")
    print(shorten(text))
    print(shorten_re(text))
    
    
def shorten(text: str) -> str:
    # vowels = ["a", "e", "i", "o", "u"] <- Use sets instead! Sets have an average time complexity of O(1) for lookups compared to O(n) for lists.
    vowels = {"a", "e", "i", "o", "u"}
    # for char in text:
    #     if char.lower() not in vowels:
    #         text_shortened.append(char)        
    # text_shortened = "".join(text_shortened)
    
    # Use list comprehension instead!
    return "".join([char for char in text if char.lower() not in vowels])
    
    
import re

def shorten_re(text: str) -> str:
    return re.sub(r"[aeiou]", "", text, flags = re.IGNORECASE)
    
    
if __name__ == "__main__":
    main()