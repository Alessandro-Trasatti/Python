students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

# list comprehension can be useful to filter data...
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
    
# Alternative using filter()

# define a filter criteria (a function outputting a boolean) to be passed in filter()
def is_gryffindor(s):
    return s["house"] == "Gryffindor"

# similar in spirit to map()
gryffindors = filter(is_gryffindor, students)
for gryffindor in sorted(gryffindors, key = lambda s: s["name"]):
    print(gryffindor["name"])
    
students = ["Harry", "Hermione", "Ron"]
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# What if I don't want a list? What if I want a dictionary whose 
# keys are the names of the students and the values are the houses?
# This is a usage of dictionary comprehension
gryffindors = {student: "Gryffindor" for student in students}