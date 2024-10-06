def main():
    yell("This", "is", "CS50")
    
def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)
    
# A Pythonic alternative consists in using map()
def yell2(*words):
    uppercased = map(str.upper(), words)
    print(*uppercased)
    
# Another Pythonic alternative consists in using list comprehension
def yell3(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)
    
if __name__ == '__main__':
    main()
    