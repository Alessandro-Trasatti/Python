import csv

students = []

with open('students_with_csv_lib.csv') as file:
    reader = csv.reader(file) # Even better is to include the keys in the .csv file and use csv.DictReader. See students_withDictReader.py
    for name, home in reader:
        students.append({"name": name, "home": home})
        
for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")