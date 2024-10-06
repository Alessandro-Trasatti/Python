#import random
from random import choice, randint, shuffle

coin = choice(["heads", "tails"])
print(coin)

number = randint(1, 10)
print(number)

cards = ["Jack", "Queen", "King"]
shuffle(cards) # shuffles randomaly the original list of cards, hence modifies it!
for card in cards:
    print(card)