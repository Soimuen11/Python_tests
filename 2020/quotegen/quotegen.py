from random import randint
from quotestore import *

options = [
        {1: "Star Wars"},
        {2: "Game of Thrones"}
    ]
print(options)
user_choice = int(input("Hello user ! Which movie quotes are you in the mood for: "))
# if not a number, throw back an error

def all_quotes():
    i = 0
    for quote in got_quotes:
        # print(got_quotes[i])
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

#what type of quotes do you want ?
#star wars ? game of thrones ?
#how many quotes do you want ?
#show them all ?
#generate one randomly ?
#functions ?
