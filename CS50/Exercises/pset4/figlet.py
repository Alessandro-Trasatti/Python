#In a file called figlet.py, implement a program that:

# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font,
# and the second of the two should be the name of the font.

# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font
# or the second is not the name of a font, the program should exit via sys.exit with an error message.

import sys
from random import choice
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()
    
    if len(sys.argv) == 1:
        font = choice(available_fonts)
    elif len(sys.argv) == 3:
        font = get_figlet_font(available_fonts)
    else:
        sys.exit("Usage: figlet.py [ -f | --font FONT_NAME ]")
    
    figlet.setFont(font=font)
    text = input("Enter the text you want to display: ")
    print(figlet.renderText(text))

def get_figlet_font(available_fonts):
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Error: First argument must be -f or --font.")
    
    if sys.argv[2] not in available_fonts:
        sys.exit(f"Error: '{sys.argv[2]}' is not a valid font. Use a valid font name.")
    
    return sys.argv[2]

if __name__ == "__main__":
    main()