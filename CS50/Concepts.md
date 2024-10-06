# Learning

## Git basics

First thing first, we pulled from the Github repository using the command <code>git clone</code>, copying the ssh. address. Now, I changed the file locally. This can be checked using the command <code>git status</code>. In fact I modified the *README.md* file and I added *test.cpp*. If I want to add all these files (in general *every file*) just run the command

                        git add .
If you want to add just a file, for instance just *test.cpp*, the command is the following

                     git add test.cpp
After adding the files, it is important to commit them. To do that, use

                      git commit -m
To push these changes to a remote repository, that in Git Hub for instance, we use the command

                    git push origin master
The *origin* keyword is a word taht stands for the location of our git repository. The keyword *master* (try *main* instead of *master* if it doesn't work) stands for the branch we want our changes to be pushed to.

### Branching

Using the command <code>git branch</code>, you can see all the branches of the repository you are working with. The output in our case is <code>*main</code>. The* is telling us that we are on that branch at the moment. To continue using the terminal press <code>q</code> on the keyboard.

To create a new branch (and also to move among branches) the command to use is <code>git checkout</code>.
More precisely, **to create a new branch** (and automatically move to it)

                                        git checkout -b name_of_branch
By using the command <code>git branch</code> again, now you will see two branches.
To move to another branch, just use

                                        git checkout name_of_branch
You can scheck that you actually switched by using the command <code>git branch</code> and by observing the *.

### Changes visible only in the feature-readme-instructions branch

Some changes. These are **only** visible in the feature-readme-instructions branch. This is evidend by checking out on the main branch and observing that this part of the readme file goes away. To push them to GitHub, use the <code>git push origin same_name_of_local_branh</code>. The fact that we use the same name on the local machine and on GitHub is only for practical reasons and it is a convention.

## Python

For the moment, I am following the course **Harvard CS50’s Introduction to Programming with Python**, which can be freely found on YouTube.

A useful resorce for the Python documentation is the official (website)[https://docs.python.org/3/library/functions.html] or, more generally [docs.python.org]. To look for a specific method or function, just add (before the *.html*) <code>#name_of_function</code>.

### Virtual environments

- <code>source nameOfVirtualEnvironment/bin/activate </code> to activate the virtual environment desired.

### Useful commands in VS code

We can do all sorts of useful things from the terminal. Opening VS code gives us access to an instance of the terminal window (which is simply a *command line interface*) to your pc. Some useful commands are

1. <code>code name_of_file.extension</code>(e.g. *example.py*), to create and start coding the file.
2. <code>python name_of_file.py</code> to execute the code in the file. Precisely, *python* not only is a language in which one can write code, but it is also an *interpreter*, which basically takes your commands and translates it into something that the machine can understand, typically a sequence of zeros and ones.
3. By writing just <code>python</code> in the command line, you enter the *interactive mode*, where you can instantly execute single lines of code (without creating and or saving new files).

### Facts about python documentation

1. If you have a $*$ just before an argument, it means that the function can take *any* finite number of thise inputs (e.g. <code>print(*objects)</code>, meaning you can do <code>print(str1, str2, ..., strn)</code>, for any $n$). If the $*$ is not present, this means that the function can take just one input associated to that argument (e.g. <code>round(number)</code>)
2. Square brackets '[...]' in the documentation of a function mean the presence of some optional arguments (e.g. <code>round(number[, ndigits])</code> will round to the closest integer if just <code>number</code> is specified or will round to <code>ndigits</code> number of digits after the floating point if specified. For example, <code>round(3.141521, 3)</code> will output $3.141$).

### Make your own libraries/modules/packages

You can create your own libraries/modules/packages to store code that you (or others) will potentially reuse.

This is done by reating a certain python file that stores your functions and then importing it into a different pyhton file, where you need some functionality offered by your library/module/package.

For example see how <code>sayings.py</code> is imported into <code>say.py</code> to exploit its functionality.

**NB**: If we do it like in <code>say.py</code>, just by importing the function <code>hello</code> from <code>sayings.py</code>, we will see that all the code present in the <code>sayings.py</code> gets executed and then the program <code>say.py</code> continues, even if we were just asking for the function <code>hello</code>.

In fact, what python does is he looks for the file <code>sayings.py</code> reads it from top to bottom, left to right and only then looks for (and imports) the desired method. That is why we see that code in <code>say.py</code>, because python is executing (in particular) line $12$ before giving back the function <code>hello</code>.

This means that it is not the right way to call <code>main</code> in <code>sayings.py</code>, and we should use a different practice. That is where the special symbol <code> \_\_name\_\_</code> comes into play.

The <code>\_\_main\_\_</code> concept in Python revolves around how Python scripts are executed. It helps control whether a block of code should be executed when the script is run directly, or if it should be skipped when the script is imported as a module in another script.

Understanding <code>\_\_main\_\_</code> in Python

1. Python Modules and Scripts

	- In Python, a file (e.g., my_script.py) is a module. It can be run directly as a script or imported into another script as a module.
	- When a Python file is executed, Python automatically sets some special variables. One of them is <code>\_\_name\_\_</code>.

2. The <code>\_\_name\_\_</code> Variable

	- If the Python file is run directly (e.g., python my_script.py), the value of <code>\_\_name\_\_</code> is set to "<code>\_\_main\_\_</code>.
	- If the Python file is imported as a module in another script (e.g., import my_script), the value of <code>\_\_name\_\_</code> is set to the name of the module (e.g., "my_script").

3. Using if <code>\_\_name\_\_</code> == "<code>\_\_main\_\_</code>":

	- The if <code>\_\_name\_\_</code>== "<code>\_\_main\_\_</code>": construct is a way to allow or prevent parts of code from running when the script is run as a module.
	- Code inside this block runs only when the script is executed directly, not when it’s imported.

That is why line $12$ caused a problem in <code>sayings.py</code> and the best practice is to use the block from line $14$ to $16$.

### Some data structures

#### Sets
It is a list with no duplicates (literally a mathematical set).

### Unit tests
It is the practice of testing your code using your own code. "Unit testing" means to test "units" of your code, typically functions.
A good practice could be to create a *unit test*, which is simply anoter .py file (generally, when testing <code>sample.py</code>, we should create a file like <code>test_sample.py</code>).

When unit testing, a central tool is the keyword <code>assert</code>, which allows you to test if something is true. If the property turns out to be false, an error message will be displayed (an *AssertionError*). A great library when it comes to unit testing is *pytest* (see it in action in <code>test_calculator.py</code>). Just run <code>pytest test_calculator.py</code>, instead of <code>python test_calculator.py</code>.

You can organise your tests in separate folders. For example, you can do <code>mkdir test</code>, which will create a directory named *test* within the current directory and move your tests there. To directly create a test there via the terminal, you will need to do the following

<code>code test/test_something.py</code>.

To make everything wprk, you will have to create a \_\_init\_\_ file as well (with <code>code test/\_\_init\_\_.py</code>). This file, despite being empty has the property to tell python to treat our folder not as a "normal" folder, but as a **package**. A package is a Python module (or more Python modules) that are oragnised in a folder.

Now, in the terminal, just write <code>pytest name_of_test_folder</code> to run all the tests within the folder (that in our case has been named *test*).

### File I/O
It is the feauture of being able to modify an existing file and/or export some data from our program, which, normally, when the program terminates gets lost. This can be done in Python.

Typical files are *.txt* and *.csv*. The *.csv* is for when we want to store multiple types of information, for example the name of a wizard and its associated house (e.g. see *names.csv*). The separator is a "comma". The file separates values with commas and differnt types of values with a newline.

To work with .csv there exists a dedicated library called, you guessed it, <code>csv</code>.

### Regular expressions

*Regular expressions*, often called *regexs* is really just a pattern. In programming it is quite to use patterns to match on some kind of data (often user input), for instance if a user types in an email address on your program, on your app or website, you might ideally want to validate they indeed typed in an email address and not something completely different. So, using regular expressions we will be able to define patterns in our code to compare them with data we are receiving from someone else to validate it or clean it for example.

In Python, you have the <code>re</code> library. Handy is the following list, when it comes to regexes is Python

- $\cdot$ --> any character except a newline
- $*$ --> $0$ or more repetitions
- $+$ --> $1$ or more repetitions
- $?$ --> $0$ or $1$ repetition, meaning that the character to the left is optional
- $\{m\}$ --> $m$ repetitions of what's immediately to the left
- $\{m, n\}$ --> $m-n$ repetitions (between $m$ and $n$ repetitions) repetitions of what's immediately to the left
- ^ --> matches the start of the string
- $ --> matches the end of the string or the newline at the end of the string
- [] --> set of characters to look for specifically (to be indeicated within the square brackets)
- [^] --> complementing the set of characters within the square brackets
- \w --> means "word". Stands for any alphanumeric character plus the underscore.
- \W --> the complementary of \w
- \d --> decimal digit (0-9)
- \D --> the complementary of \d
- \s --> whitespace characters
- \S --> the complementary of \s
- \b --> only if it appears by itself as a word, not as part of a larger word (to be combined with something).
- | --> means the logical *or*
- (...) --> a group

Another use of regexes is to clean data (see for example *format.py*) or to extract information from the input (see for example *twitter.py*).


## OOP
The central structure in *Object Oriented Programming* is the <code>class</code>.

A <code>class</code> is a general purpose tool that allows us to create our own data types.  Intuitively, it is like a blueprint for pieces of data, objects.

By convention, the name of a class starts wwith a capital letter.

A class can have <code>attributes</code>, properties of sorts (e.g. for a football player some attributes could be
name, height, weight, team, etc). Given an instance of a class (i.e. an <code>object</code>) we can access its attributes via the <code>.</code> operator (e.g. Messi.team access the team where the player Messi plays). A class can also have <code>methods</code>, which are functions that our class or its objects can use. Very common methods are for example the constructor, the *getter* and *setter* methods (see <code>student2.py</code>)

Examples of classes are <code>int</code>, <code>str</code>, <code>dict</code> etc...

An object is typically created via the following syntax:
<code>name_of_calss(*args)</code> (e.g. player = Player())

More precisely, when writing <code>name_of_calss(*args)</code>, we are calling the <code>constructor</code>, which is a <code>method</code>.

### The constructor
The syntax in Python is the following:

<code>def \_\_init\_\_(self, *args)</code>.

This is also called *dunder method* (because of the double underscore before and after). <code>\_\_init\_\_</code> stands for *initialise*, and indeed the method is building (or initialising an object of the class). <code>self</code> is just something giving access to the object that waj just instantiated by calling the constructor.

### <code>\_\_str\_\_</code>
It is a special method (a *dunder method*) that if you defined it inside your class, Pyhton will just authomatically call anytime some other function wants to see your object as a string. For example, <code>print</code> wants to see your object as a string $\Rightarrow$ <code>\_\_str\_\_</code> is called. If not implemeted (actually overriiden, as under the hood these methods are implemented when creating a class), when printing an object, for example, we will get a description of the object plus its memory location.

### Properties
It is just an attribute that has some more defensive mechanisms/functionalities: for example, you can prevent modifying an attribute in something other than a list of objects. A property is declared using the keyword (or better *decorator*) <code>@property</code>. 

In general, a *decorator* is just a function that modifies the behavior of other functions or adds some functionality to it. In mathematica terms it is a function that has as input one or more functions.

#### Getters
A *getter* is a method getting some attribute of the object.
We can  oblige anyone wanting to *access* some attribute to pass through this type of function. In Python it takes just the current object, i.e. <code>self</code>.

#### Setters
A *setter* is a method setting some value to an attribute.
We can  oblige anyone wanting to *set* some attribute to pass through this type of function. In Python it takes two arguments:
- the current object, i.e. <code>self</code>.
- the attribute we want to change (or set).

Methods like *getters* and *setters* are used, for example, to include any error correction mechanism in a robust way.

**NB**

Observe that once getters and settrs are implemented in python (for example the house getter/setter in students2.py)
writing something like object.attribute = boh (e.g. student.house = "Number Four, Privet Drive") won't make you access the attribute directly, but it will *automatically* call the getter and setter methods. This is done indeed thorugh decorators. For the getter it is <code>@property</code>, for the setter it is <code>@name_of_attribute.setter</code> (e.g. <code>@house.setter</code>, again see <code>steudents2.py</code>).

To avoid confusion between getters and setters and attributes, we distinguish them by employing an underscore just before the attributes. See again <code>students2.py</code>. So, by default, when implementing getters and setters for an attribute, we will name the attribute with an underscore just before its actual name (this is just a convention, you could do whatever you want), while the getters and setters just with the name.

**NB**

Note that in Python there is no such thing as *public*, *protected*, *private*. Hence, technically, even after getters and setters, one can always access attributes and change them (for example in <code>students2.py</code> one could malicoiusly dodge all the intelligence and defensiveness of getters and setters by simply writing <code>student._house = "Number Four, Prive Drive"</code>). It is just a convention that says that if there is an underscore it is an attribute and you should not touch it.

### Class methods
These are methods that can be called withoud instantiating an object of the class. These are specified with <code>@classmethod</code>. Differently from (instance) methods, they do not take <code>self</code> as argument. Instead, they take <code>cls</code>. <code>cls</code> just like <code>self</code> allowws to access class variables using the <code>.</code> notation (see for example <code>hat.py</code>).

### Static methods
A *static method* is a method that doesn’t take the self or cls (class) parameter. It behaves just like a regular function but belongs to the class’s namespace.

It cannot modify the state of the instance or the class.
Static methods are defined using the <code>@staticmethod</code> decorator.

**When to use a static method?**

Use a static method when the logic inside the method doesn’t need to access or modify the instance or the class itself. It is simply a function that logically belongs to the class.

**Example**

    class MathOperations:
        @staticmethod
        def add(a, b):
            return a + b

    # Calling a static method
    print(MathOperations.add(2, 3))  # Output: 5

### Innheritance
You can define your classes hierarcically, by making one class *inherit* from another. Inherit means borrowing attributes and method. The inherited class can implement its own methods and attributes (additionally to the ones inherited).

We will call the hinheriting class as the *child class* while the one who is being inherited *parent class*.

In Python, given a parent class, a child class is defined just by introducing parenthesis after the child class name and writing the parent class name inside:

    def Animal():
        ...

    def Cat(Animal):
        ...

Again, the child class inherits all the attributes and methods of the parent class, which, in Python, within the child class is referred to as <code>super()</code>. For example:

    class Wizard:
        def __init__(self, name):
            if not name:
                raise ValueError("No name specified")
            self.name = name

    class Student(Wizard):
        def __init__(self, name, house):
            # Calls the constructor of the parent class
            super().__init__(name) 
            self.house = house

### Operator overloading
It is the concept of takig very common symbols, like +, - or other symbols on the keyboard and implement your interpretation thereof. For example, for the class <code>str</code> + has been programmed to be concatenation.

See <code>vault.py</code> for an example, where + is overloaded using the dunder method <code>\_\_add\_\_</code>.

## Et Cetera

### Global variables
It turns out that it is possible and easy to access and read gloabal variables in Python (variables on top of your .py files that can be accessed by any of your functions). However, modifying them causes an <code>UnboundLocalError</code>. To solve this, you need to use the keyword <code>gloabl</code>. (see <code>code.py</code>)

Better is just to use a class actually (see again <code>code.py</code>)

### Type hinting
We know that in Python the type of a given variable is *mutable* (it is *dynamically typed*). However, for robustness, we can suggest python what types of data a certain variable should have or what type of data a given function should output. This is the concept of **type hinting**. A useful tool that helps you check wheter the code you are using is consistent with the type hinting you coded is <code>mypy</code>. Just use <code>mypy filename.py</code>.

### Command line arguments
Other than the classic library <code>sys</code>, quite useful can be the library <code>arparse</code>.

### Unpacking
Say that I have a function that expects $3$ arguments and instead I pass just a list, contaning $3$ values. This will raise a <code>ValueError</code> as two arguments of the functions are missing. To dodge this problem, we can use *unpacking*. Just pass an asterisk before the list, this will automatically unpack values for you! See for example <code>unpack.py</code>. Unpacking is possible on structures that have a notion of order, like <code>list</code>, <code>tuple</code>, <code>dict</code>. Hence, it won't work on something like <code>set</code>.

Another super robust way to unpack is to use dictionaries with <code>**</code>, again, see <code>unpack.py</code>.
Basically this allows to pass arguments with their name!
Hence, with this kind of unpacking, no need to pass arguments
in order!

### <code>*args, **kwargs</code>
It turns out that the syntax with <code>*</code> and with <code>**</code> is not only used for unpacking.

Their are used to indicate that some function takes a variable number of arguments. See <code>unpack.py</code>.
- <code>args</code> is for positional arguments. They are organised in a tuple.
- <code>kargs</code> is for keyword arguments (arguments with their name). They are organised in a dictionaries, where the name are going to be the *keys*, the *values* are going to be the values of the arguments inputed in the function.

An example using this paradigm is the function <code>print</code> function.

### <code>map</code>
It is a function that allows you to apply some function to every element of a sequence, e.g. a list.

### <code>filter</code>
It is a function that allows you to filter elements in an iterable, say <code>vec</code>. It is an alternative to list comprehension.

Define a filter criteria (a function outputting a boolean) to be passed in <code>filter()</code>, say <code>f</code>.

The syntax is 

<code>filter(f, vec)</code>

which outputs another iterable whose elements are the ones from the original iterable that outputted <code>true</code> when passed to the filter criteria <code>f</code>.

Observe that the filter, if simple, can be implemented using a <code>lambda</code> function.

### Dictionary comprehension
Just like list comprehension, but with dictionaries. See <code>gryffindor.py</code>.

### Generators
Generators are a special type of iterator in Python that allow you to iterate over data in a memory-efficient way. Instead of generating all the values at once and storing them in memory (as lists do), generators yield one value at a time and only when requested. This can significantly reduce memory consumption, especially when dealing with large datasets or streams of data that don’t need to be fully stored in memory.

**Key Benefits**:

-	Memory efficiency: Since generators produce values lazily, they use memory efficiently by only holding one value at a time in memory.
-	Improved performance: They can handle large or even infinite sequences without causing memory overflow.
-	Readable code: Generators allow you to write cleaner, more concise code for iterations, often avoiding the need for complex loops and conditional statements.

When it comes to Python, the central command for generators is <code>yield</code>.

**Example of a Generator**

Here’s an example where we create a generator to yield Fibonacci numbers:

    def fibonacci_sequence():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    # Usage:
    fib_gen = fibonacci_sequence()
    for _ in range(10):
        print(next(fib_gen))

In this example:

-	The fibonacci_sequence() generator yields the next Fibonacci number each time it’s called with next().
-	Unlike a list that would generate all Fibonacci numbers up to a certain point, the generator only calculates the next number when needed, conserving memory.

For another coded example, see <code>sleep.py</code>.

**Conclusion**

Generators are ideal for working with large data sets or when you’re working in environments with limited memory. They offer a simple yet powerful tool for managing iteration in Python.