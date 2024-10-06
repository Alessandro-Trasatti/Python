# sys is a module that can give you access to stuff typed in the command line
# sys.argv gives you all the words the user typed in before pressing "Enter". argv stands for "argument vector".
# Each entry of the vector is a word the user typed.
# This can be useful as what the user typed might be used to influence the program!

import sys

#try: 
#    print("Hello, my name is ", sys.argv[1])
#    # In this case when lauching the file, you need to enter your name with a spece after the .py
#    print("The firste entry of sys.argv is the name of the program, in this case", sys.argv[0])
#except IndexError:
#    print("Too few arguments, please enter your name")

# Another way of doing this is like follows:
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("Hello, my name is ", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
    
for arg in sys.argv[1:]:
    print("Hello, my name is ", arg)

