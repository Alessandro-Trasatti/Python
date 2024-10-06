from random import choice

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # class variable
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", choice(cls.houses))
    
Hat.sort("harry")