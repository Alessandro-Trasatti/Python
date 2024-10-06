# Observe that the mechanism of controlling input in the __init__ method (that in student.py) can be easily circumnavigated.
# In fact, in Python, not only we can access attributes using the dot notation, but also change them.
# So for example line 20, would introduce an invalid house and would pass unnoticed!

class Student:
    def __init__(self, name, house):
        self.name = name # This is now call the setter!
        self.house = house # This is now calling the setter!
        # self._house = house <- This would avoid the setter taking away all the effort made...
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
    @property
    def name(self):
        return self.name
    
    # Getter -> a method getting some attribute 
    @property
    def house(self):
        return self._house
    
    @name.setter
    def name(self, name):
        if not name: # Is the name attribute empty?
            raise ValueError("Missing name")
        self._name = name
        
    # Setter -> a method setting some value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
    
def main():
    student = Student.get()
    student.house = "Number Four, Privet Drive" # <- This will trigger the setter raising a Value Error. More robust than students.py
    print(f"{student.name} from {student.house}")    
    

if __name__ == "__main__":
    main()