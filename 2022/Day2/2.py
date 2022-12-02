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
        if (game[1] == 'X'):  # Lose
            points += 3 # For the Scissors
        elif (game[1] == 'Y'):  # Draw
            points += 3 # For the draw
            points += 1 # For the Rock
        else:  # Win
            points += 6 # For the win
            points += 2 # For the Paper
    elif (game[0] == 'B'):  # Paper
        if (game[1] == 'X'):  # Lose
            points += 1 # For the Rock
        elif (game[1] == 'Y'):  # Draw
            # Draw
            points += 3 # For the draw
            points += 2 # For the Paper
        else:  # Win
            points += 6 # For the win
            points += 3 # For the Scissors
    else: # Scissors
        if (game[1] == 'X'):  # Lose
            points += 2 # For the Paper
        elif (game[1] == 'Y'):  # Draw
            points += 3 # For the draw
            points += 3 # For the Scissors
        else:  # Win
            points += 6 # For the win
            points += 1 # For the Rock

print(points)     

""" for key, value in points.items():
    print(f'Key: {key} and Value:{value}') """