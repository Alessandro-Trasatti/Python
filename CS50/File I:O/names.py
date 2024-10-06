# names = []

# for _ in range(3):
#     names.append(input("What is your name? "))

# for name in sorted(names):
#     print("Hello,", name)

# What if I want to save the printed names in a file? The function open will help a lot
# open, you guessed it, opens a file programmatively, meaning that you can read and/or write information
# to it.
# The syntax is open(path/filename, secondArg).
# secondArg could be "w" (writes on the file, meaning that it creates it from scratch everytime it is run) - hence it overwrites
# secondArg could be "a" (appends on the file, meaning that it does not overwrite it but adds content to it)
# secondArg could be "r" (reads/loads the file )
# The open function will RECREATE the file everytime it is run, erasing whatever was there before.
name = input("What is your name? ")

file = open("names.txt", "a") # You can write on the file
file.write(f"{name}\n")
file.close() # Closes and saves the file

# If you forget to close the file it might get corrupted or even deleted. Another pythonic approach that avoids using the .close()
# is to use "with", that basically states that in this context you shoukd open and close a certain file automatically

name = input("What is your name? ")
with open("names.txt", "a") as file: # This synatax is more or less equivalent to file = open("names.txt", "a"), but that is how it is used
    file.write(f"{name}\n")
    
# Let's read back the file
with open("names.txt", "r") as file:
    lines = file.readlines() # returns a list
    
for line in lines:
    #print("Hello,", line, end="")
    print("Hello,", line.rstrip())
    
print(lines)

# With fewer lines of code, you could do this <-- NO NEED TO OPEN AND CLOSE!
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())
        
# Say now that we want to sort alphabetically the names in the file
names = []
with open("names.txt", "r") as file:
    for name in file:
        names.append(name.rstrip())
        
for name in sorted(names):
    print("Hello,", name)
    
# In a more pythonic way, the following workds as well
with open("names.txt", "r") as sorted(file):
    for line in file:
        print("Hello,", line.rstrip())

