#!/usr/bin/py

file = "input.txt"

opponent={ 'A':'Rock', 'B':'Paper', 'C':'Scissors'}
me={ 'X':'Rock', 'Y':'Paper', 'Z':'Scissors'}
points={ 'Rock':1, 'Paper':2, 'Scissors':3}
with open(file, 'r') as f:
    data = f.read().strip().split("\n")
f.close()

points = 0
for item in data:
    game = item.split(' ')
    print(game)
    if (game[0] == 'A'):  # Rock
        if (game[1] == 'X'):  # Rock
            # Draw
            points += 3 # For the draw
            points += 1 # For the Rock
        elif (game[1] == 'Y'):  # Paper
            # Win
            points += 6 # For the win
            points += 2 # For the Paper
        else:  # Scissors
            # Loss
            points += 3 # For the Scissors
    elif (game[0] == 'B'):  # Paper
        if (game[1] == 'X'):  # Rock
            # Loss
            points += 1 # For the Rock
        elif (game[1] == 'Y'):  # Paper
            # Draw
            points += 3 # For the draw
            points += 2 # For the Paper
        else:  # Scissors
            # Win
            points += 6 # For the win
            points += 3 # For the Scissors
    else: # Scissors
        if (game[1] == 'X'):  # Rock
            # Win
            points += 6 # For the win
            points += 1 # For the Rock
        elif (game[1] == 'Y'):  # Paper
            # Loss
            points += 2 # For the Paper
        else:  # Scissors
            # Draw
            points += 3 # For the draw
            points += 3 # For the Scissors

print(points)     

""" for key, value in points.items():
    print(f'Key: {key} and Value:{value}') """