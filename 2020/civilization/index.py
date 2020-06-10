#!/bin/python

#### LISTS ####
kingdom_resources = ["gold", "wood", "steel", "iron", "water"]
game_modes = ["history", "multiplayer"]
difficulties = ["easy", "medium", "difficult"]

#### CLASSES ####

# -- Game --
class Game:
    def __init__(self, name):
        self.name = name

    def set_player():
        # get user name
        name = input("Hello Player, what is your name: ")
        # get user genre
        genres = ["1.male", "2.female"]
        for i in genres:
            print(i)

        print("Hello ", name, "are you a man or a woman: ")
        player_genre = parseInt(input("Please enter 1 or 2"))

        titles = ["king", "queen"]
        if player_genre == 1:
            player_title = titles[0]
        else:
            player_title = titles[1]

# -- Player --
class Player:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre # male / female

# -- Kingdom --
class Kingdom:
    def __init__(self, name, resources, territory, army, defenses, money):
        self.name = name
        self.resources = resources
        self.territory = territory
        self.army = army
        self.defenses = defenses
        self.money = money
