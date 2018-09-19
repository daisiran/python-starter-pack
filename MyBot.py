# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import random

first_line = True # do not remove

# global variables can go here
stances = ["Rock", "Paper", "Scissors"]

# loop for each turn
for line in fileinput.input():
    if first_line:
        game = game_API.Game(json.loads(line))
        first_line = False
        continue
    game.update(json.loads(line))

    # ----------YOUR CODE BELOW----------
    # this code will be executed each turn of the game

    paths = game.shortest_paths(game.get_self().location, 3)
    if len(paths) > 0 and len(paths[0]) > 0:
        destination_node = paths[0][0]
    else:
        destination_node = 3

    chosen_stance = stances[random.randint(0, 2)]

    game.submit_decision(destination_node, chosen_stance)
