def main():
    n = int(input("What is n? "))
    for s in sheep(n):
        print(s)
        
        
# This doesn't work well with huge values of n. In fact, the
# following chunk of code, is trying to generate a poyentially huge
# list of sheep (a triangular n rows of sheep!)
# If n is too big, we could surpass our computer capability or
# memory. It would seem better to print one row of sheep at a time, or at
# least in a more efficient way...
def sheep_inefficient(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

# ... use generators and yield instead!
def sheep(n): 
    for i in range(n):
        yield "🐑" * i # Like this it returns one value at a time for this loop, not the whole data all together. Writing return would end the program at the first iteration as you know
        
if __name__ == "__main__":
    main()