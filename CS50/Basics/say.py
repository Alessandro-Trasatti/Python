import sys
from Basics.sayings import hello

print(f" In say.py, __name__ = {__name__}")

if len(sys.argv) == 2:
    hello(sys.argv[1])