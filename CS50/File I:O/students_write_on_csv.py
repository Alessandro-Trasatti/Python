import csv

name = input("What is the name? ")
home = input("Where is your home? ")

with open("students_write_on_csv.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "home": home})
    