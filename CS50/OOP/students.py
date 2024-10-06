class Student:
    def __init__(self, name, house, patronus):
        if not name: # Is the name attribute empty?
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name # Creates the attribute name and assigns it name
        self.house = house # Creates the attribute house and assigns it house
        self.patronus = patronus # Creates the attribute patronus and assigns it patronus
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
             case "Stag":
                 return "🫎"
             case "Otter":
                 return "🦦"
             case "Jack Russell terrier":
                 return "🐶"
             case _:
                return "🪄"
    
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")    
    
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    try:
        return Student(name, house, patronus)
    except ValueError: # The programmer treats in a special way the case where some exceptions are raised
        ...

if __name__ == "__main__":
    main()