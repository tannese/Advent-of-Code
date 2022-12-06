#!/usr/bin/python3

# Sets up Advent of Code folders (see: https://adventofcode.com/ )
# Tony Annese
# tannese@gmail.com

import os
import datetime
import subprocess

path = '/Users/tony.annese/Documents/VS Code/Advent of Code'
today = datetime.date.today()
year = str(today.year)
files = ['1.py', 'input.test.txt', 'input.txt', 'README.md']
python = subprocess.run(["which", "python3"], capture_output=True, text=True).stdout

i = 1
while (i < 26):
    day = f"{path}/{year}/Day{i}"
    os.makedirs(day)
    for file in files:
        fp = open(os.path.join(path, day, file), 'x')
        fp.close()
        if file == '1.py':
            body = f"#!{python}\n#file = 'input.txt'\nfile = 'input.test.txt'\n\nif __name__ == '__main__':"
            fp = open(os.path.join(path, day, file), 'w')
            fp.write(body)
            fp.close()
        elif file == 'README.md':
            body = f"## Day {i}\n"
            fp = open(os.path.join(path, day, file), 'w')
            fp.write(body)
            fp.close()
    i += 1

 