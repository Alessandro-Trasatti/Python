# In a file called playback.py, implement a program in Python that prompts the user for input
# and then outputs that same input, replacing each space with ... (i.e., three periods).

def main():
    sentence = input("What do you want to say? ")
    whitespace_transformer(sentence)
    whitespace_transformer_re(sentence)
    whitespace_transformer_brute_force(sentence)

def whitespace_transformer(string):
    print(string.replace(" ", "..."))
    
def whitespace_transformer_brute_force(string):

    string_mod = ""
    
    for char in string:
        if char == " ":
            string_mod += "..."
        else:
            string_mod += char
    print(string_mod)
        

import re
# Let's do the same with regexes!
def whitespace_transformer_re(string):
    print(re.sub(r" ", "...", string))
    
    

    
if __name__ == '__main__':
    main()