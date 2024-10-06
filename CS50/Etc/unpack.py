def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

# print(total(coins[0], coins[1], coins[2]), "Knuts") Too verbose...
print(total(*coins), "Knuts") # Unpack what's in coins and passes it to the function.

# Another possibility...
print(total(galleons = 100, sickles = 50, knuts = 25), "Knuts") # Like this we do not care actually about the order we are passing the arguments

# Since we are using both names and values it looks like a 
# good idea to implement a dictionary... we see it in a moment
# why

coins = {"galleons": 100, "knuts": 50, "sickles": 25}

# We could write 
print(total(coins["galleons"], coins["knuts"], coins["sickles"]), "Knuts") # ... but it is quite verbose again

# Again, much better is to use unpacking! And with dictionaries it is
# super robust as it achieves what was done in line 10
print(total(**coins), "Knuts")

def f(*args, **kwargs):
    print("Positional: ", args)
    print("Named: ", kwargs)
    
f(100, 50, 25) # Prints the args... a tuple!
f(galleons = 100, sickles = 50, knuts = 25) # Prints the kwargs... a dictionary!
    