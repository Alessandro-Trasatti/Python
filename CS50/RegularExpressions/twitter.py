# This script aims at extracting the username from the twitter url inputed
url = input("URL: ").strip()

# Again, this will be done in different methods and incrementally better
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

# This is not ideal as there might be http instead of https, www.twitter.com and some other stuff that I might wwant to allow
# Again, use regexes!
import re

url = input("URL: ").strip()
# You have the re.sub, which stands for "substitute", and works like .replace but with regexes
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

# Note that like this, we won't do the right thing if the user types in something completely different, for example https://google.com
# Indeed, re.sub is used to clean data. But we would like to have some conditional, where I give you a cleaned output if a certain match
# occured or just not give you anything if the match was not found. To do this, we can go back to re.search as it is shown in the following
import re

url = input("URL: ").strip()

matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE) # I put in parenthesis what should be the username, to later recover it with groups!

if matches: # Like this, we make sure that the twitter url is found
    print(f"Username: {matches.group(2)}") # 2 because there is another set of parentheses that wasn't meant to be a gropu though, i.e. the (www\.)
    
# To tell the computer not to count that as a group, just use the following syntax     
url = input("URL: ").strip()

if matches := re.search(r"^(https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE): # Restricted what the username can be, and allowed other stuff after it
    print(f"Username: {matches.group(1)}") # Here I can finally use 1