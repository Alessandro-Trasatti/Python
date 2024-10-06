import csv

students = []

with open('students_withDictReader.csv') as file: # Differentely from "students_with_csv_lib.csv" we included a column on top with the keys "name", "home". This allows the usage of the very flexible dictReader
    reader = csv.DictReader(file) # Even better is to include the keys in the .csv file and use csv.DictReader. See students_withDictReader.py
    for row in reader: # Now evry line is loaded as a dictionary, not as a list
        students.append({"name": row["name"], "home": row["home"]}) # This is much more robust as if someone pertmutes the ordwer of name and home in the csv file, the code will still work, while with a list the order of information would be swappwed!
        
for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")