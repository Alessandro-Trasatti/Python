# The goal is to validate whether the user input is actually an email or not
email = input("What is your email address? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
# Not very good check like that...

# Better would be like this
username, domain = email.split("@")

# if username: # This is a way to see if username is not None or ""
#     print("Valid")
# else:
#     print("Invalid")
# better is like the following
if username and "." in domain: # If username not empty string and "." is in the domain
    print("Valid")
else:
    print("Invalid")
    
# If you want to check if it ends with a .edu
if username and domain.endswith(".edu"): # If username not empty string and "." is in the domain
    print("Valid")
else:
    print("Invalid")
    
# Notice that this process escalates quickly: to imptove one might want to check that there is something between
# the "@" and the "." for example and some other stuff. Thet is where regexes come into play!

import re

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")
# This was not a big step forward as it is just a different way of writing the block 4-7 (not exactly, the check about the "." is missing)
# We can imporve much more using regexes. We want the email to be like something @ somethingelse .edu
if re.search(".*@.*", email): # . is represents just a character, and so we put .*, which means any repetitions of some characters, i.e. a string of any length
    print("Valid")
else:
    print("Invalid")
 # The previous version won't work properly as the * even accepts lenght 0 strings (as it is made also for 0) To fix this, just use the +
if re.search(".+@.+", email): # equivqlently, you can write if re.search("..*@..*"). The first dot in ..* guarantees you that there is at least one character :)
    print("Valid")
else:
    print("Invalid")
# If we also want to check the email to finish with a .edu, then one might think to do the following:
if re.search(".+@.+.edu", email):
    print("Valid")
else:
    print("Invalid")
# This won't work well as in this context "." means any character, so that also malan@harvard?edu would pass
# Just use escape character (in this case the backslash) to say that you really want a point. To makew the regular expression to be
# properly read, you should make the string raw, by putting r at its beginning
if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
# Again, this won't work as one could type something like my email address is malan@harvard.ed and this would be considered valid.
# To avoid this, we will use the ^ and $ characters
if re.search(r"^.+@.+\.edu$", email): # In other words, this means that we don't want our email to contain such a pattern, but that we want a perfect match with our pattern
    print("Valid")
else:
    print("Invalid")
    
# To make it even better, we use the [] and [^]
if re.search(r"^[^@]+@[^@]+\.edu$", email): # Here we substituted the dot with [^@], which means allow any character except @
    print("Valid")
else:
    print("Invalid")
    
# Even better would be to specify characters that we want to allow in ourusernames (automatically defining what we don't want to allow)
# For example, we will just accept letters a trough z (lowercase and uppercase), numbers and underscores. This can be easly done using
# ranges, which are implemented using hyphens
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
# There is actually a shortcut: \w means in regexes alphanumerical code and the underscore, so that we can write (\w stands for "word" :))
if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
# a more refined version with multiple ends is
if re.search(r"^\w+@\w+\.(edu|com|org|gov|net)$", email, re.IGNORECASE): # the third argument re.IGNORECASE makes sure that the mathc is done without caring about lowecasde/uppercase. Another solution could be to force the userinput to lowercase, with the .lower method
    print("Valid")
else:
    print("Invalid")
# We can do even better: the current version doesn't support email addresses with subdomains, for example malan@cs50.harvard.edu (because of the multiple dots!)
# We can use the ? symbol to indicate the possible presence of a subdomain
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com|org|gov|net)$", email, re.IGNORECASE): # the third argument re.IGNORECASE makes sure that the mathc is done without caring about lowecasde/uppercase. Another solution could be to force the userinput to lowercase, with the .lower method
    print("Valid")
else:
    print("Invalid")
# Above the ? allows to say that the (\w+\.), which means literally any word followed by a dot, might be there or not