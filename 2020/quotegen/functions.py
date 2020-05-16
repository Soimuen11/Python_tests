from random import randint
from quotestore import *

def all_quotes():
    i = 0
    for quote in got_quotes:
        print("Quote: ", quote["quote"])
        print("---------------------------")
        print("Author: ", quote["author"])
        i+=1
        print("Id: ", i)
    print("<=============END OUTPUT================>")

def rand_quote():
    rand = randint(1, len(got_quotes))
    print(got_quotes[rand])
    print("Id: ", rand)
