#Even if you haven’t studied physics (recently or ever!), you might have heard that E = mc^2, wherein 
# E represents energy (measured in Joules), 
# m represents mass (measured in kilograms), and 
# c represents the speed of light (measured approximately as 300000000 meters per second). Essentially, the formula means that mass and energy are equivalent.

# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer
# (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
c = 3 * 10e8

def main():
    try :
        mass = int(input("Input an integer representing a mass in kg: "))
        energy = energy_computer(mass)
        print(f"The equivalent energy is {energy}J")
    except ValueError:
        print("That is not a number!")
    
def energy_computer(mass):
    return mass * c * c 

if __name__ == "__main__":
    main()