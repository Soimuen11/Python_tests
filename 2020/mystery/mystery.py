#!/usr/bin/mystery

from random import randint

mystery = randint(0,100)
user_nb = int(input("Hey user! Guess a number: "))
while user_nb != mystery:
    if user_nb > mystery:
        print("too high")
        user_nb = int(input("Hey user! Guess a number: "))
    elif user_nb < mystery:
        print("too low")
        user_nb = int(input("Hey user! Guess a number: "))
    else:
        print("this is not a number, try again: ")
        user_nb = int(input("Hey user! Guess a number: "))
print("Well done, you have found the mystery number")
