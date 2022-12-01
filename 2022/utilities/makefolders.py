#!/usr/bin/python3

# Sets up Advent of Code folders (see: https://adventofcode.com/ )
# Tony Annese
# tannese@gmail.com

import os
import datetime

today = datetime.date.today()
year = str(today.year)
os.mkdir(year)


i = 1
while (i < 26):
    day = f"{year}/Day {i}"
    os.mkdir(day)
    i += 1

 