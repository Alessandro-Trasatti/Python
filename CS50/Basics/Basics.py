# Input/Output, type casting & f-strings
userName: str = input("What is your name? ")
print(f"Hello {userName}!") 

x = float(input("What is x? "))
y = float(input("What is y? "))

z = x / y
print(f"x / y = {z:.2f}")

# Conditional statements
x = int(input("What is x? "))
y = int(input("What is y? "))

if x < y:
    print("x is smaller than y")
elif x > y: # This gets executed only if the conidtion in the previous 'if' was FALSE
    print("x is bigger than y")
else: # This gets executed only if the conidtion in the previous 'elif' was FALSE
    print("x is equal to y")
    
# or keyword
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
    
# You can shrink the preceding lne of code easily
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
    
    
#and keyword
score = int(input("Score"))
if 90 <= score and score <= 100:
    print("Grade: A")
elif 80<= score and score < 90:
    print("Grade: B")
elif 70 <= score and score < 80:
    print("Grade: C")
elif 60 <= score and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
    
# Make shorter by concatenating conditions
score = int(input("Score"))
if 90 <= score <= 100:
    print("Grade: A")
elif 80<= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
    
# Make shorter (but less readable) using the concept of elif
score = int(input("Score"))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    
def is_even(n):
    return True if n % 2 == 0 else False

# Even better
def is_even_improved(n):
    return n % 2 == 0

# The switch in the newer versions of Python is givrn by match
name = input("What's your name? ")

if name == 'Harry':
    print("Gryffindor")
elif name == 'Hermione':
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
    
# optimize with match
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# optimize with | symbol
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
        
# Loops - create a loop that allows you to meow a variable number of times (inputed by the user!)
#while True:
#    n = int(input("How many meows? "))
#    if n < 0:
#        continue
#    else:
#        break

while True:
    n = int(input("How many meows? "))
    if n >= 0:
        break
 # The previous loop allows to get a positive input from the user
for _ in range(n): 
    print("Meow")
    
# This can be improved using functions
def main():
    number = get_number()
    meow()
    
def get_number():
    while True:
        n = int(input("How many meows? "))
        if n >= 0:
            return n
def meow():
    for _ in range(n):
        print("meow")
        
# Dictionaries 
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# NB: By design, in Python, when iterating over a dictionary, it will iterate over a its keys!
for student in students:
    print(students)
    
# So, if I want to print both the keys and the values, we can do something like this
for student in students:
    print(student, students[student], sep = ", ")

# Say that now I want to also include the patronus in the dictionary, so to have a sort of tridimensional dictionary
# The way you do it, for the moment, is by creating a list of dictionaries. This is valid for the n dimensionalcase clearly

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}, # First dictionary and first element of our list
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}, # Second dictionary and second element of our list
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"}, # Third dictionary and third element of our list
    {"name": "Draco", "house": "Slytherin", "patronus": None} # Fourth dictionary and fourth element of our list
]

# None = absence of a variable

for student in students:
    print(students["name"], students["house"], students["patronus"], sep = ", ")

    