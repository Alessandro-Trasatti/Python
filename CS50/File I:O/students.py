with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") # the rstrip() method eliminates any spaces before of at the end of the string, while the split() method removes separates the string into multiple strings whenever the specified separator is encountered (in this case a comma)
        print(f"{name} is in {house}")
        
# What if I also want to say "hello" in order (with respect to the name alphabetical order)
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        students.append(name)

for student in sorted(students):
    print("Hello, ", student)
    
# A cleaner and more robust solution is the following: create a list of dictionaries
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)
        
# Print sorteing the disctionary by the key "name"
def get_name(student):
    return student['name']

for student in sorted(students, key = get_name):
    print(f"{student['name']} is in {student['house']}")

# NB: I am passing a function (get_name) into another function (sorted). Why is this necessary? The function sorted needs to know how to 
# get the name of the student in order to alphabetical sorting for you. Clearly, back in the days, the authors of Python didn't know
# that we would have created the varibale students in this class, so they couldn't have anticipated wwriting code in advance that
# specifically sorts on a field called "name", or "house". So what they did, to make the function well coded and general, they built this
# name parameter "key" that allows all of us to tell their function sorted how to sort this list of dictionaries.
# The python documentations says that key specifies a function of one argument that is used to extract a comparison 
# key from each element in iterable (for example, key=str.lower). The default value is None (compare the elements directly).

# Instead of using a dedicated function, you can use a lambda function. This is considered a good practice!
for student in sorted(students, key = lambda student: student['name']):
    print(f"{student['name']} is in {student['house']}")