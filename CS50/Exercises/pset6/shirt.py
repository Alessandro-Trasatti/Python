# In a file called shirt.py, implement a program that expects exactly two command-line arguments:

# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

# The program should then overlay shirt.png (which has a transparent background)
# on the input after resizing and cropping the input to be the same size, saving the result as its output.

from PIL import ImageOps as imgops, Image as img
import os
from sys import argv, exit

import PIL.ImageOps

def main():
    validate_input()
    
    # open images
    try:
        shirt = img.open(argv[1])
        dog = img.open(argv[2])
    except Exception as exp:
        exit(exp)
    # get size of shirt.png
    size = shirt.size
    # crop muppet to fit shirt
    dog = imgops.fit(dog, size)
    # overlay shirt on mupper
    dog.paste(shirt, shirt)
    # save image
    dog.save(argv[2])
        
    

def validate_input():
    error_msg = "Usage: shirt.py <path1/some_image.[JPEG|PNG]> <path2/some_other_image.[JPEG|PNG]>"
    if len(argv) != 3:
        exit(error_msg)
        
    input_image = argv[1]
    output_image = argv[2]
    
    if not input_image.endswith((".jpg", ".png", "jpeg")) or not output_image.endswith((".jpg", ".png", "jpeg")):
        exit("Invalid file extensions. "+ error_msg)
    
    input_image_extension = find_extension(input_image)
    output_image_extension = find_extension(output_image)
    
    if input_image_extension != output_image_extension:
        exit("The file extensions should be the same. "+ error_msg)
        
    if not os.path.exists(input_image):
        exit(f"The input file {input_image} does not exist. "+ error_msg)
    
        
    
def find_extension(file: str) -> str:
    extension = []
    for char in reversed(file):
        if char == ".":
            break
        extension.append(char)
    return "".join(extension)
    
    
if __name__ == "__main__":
    main()