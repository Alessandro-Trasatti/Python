def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")
    

def goodbye(name):
    print(f"Goodbye, {name}")
    
print(f"In sayings.py __name__ = {__name__}") # <-- This will be always executed, whether or not the file is directly executed
    
# main() <-- BAD PRACTICE (SEE README.md)
if __name__ == "__main__": # This gets executed only when the file is executed directly
    main()