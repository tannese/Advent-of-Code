While working on the second part I Googled and found working with sets. After submitting my answer for part 2 I went back and reworked part 1 using sets as well. 

I'm sure there is a better way to slice the input line into 2 sets. I will keep looking. 
##
[1.1.py](2022/Day3/1.1.py) is the reworked code using sets.  

## Using strings
[Reddit User xprotocol_ninesix](https://www.reddit.com/user/xprotocol_ninesix/) utilized the string module to generate the priority map in [their code](https://www.reddit.com/r/adventofcode/comments/zb865p/comment/iyuc2dc/?utm_source=share&utm_medium=web2x&context=3)

[    ]import string
[    ]# make priorityMap
[    ]priorityMapLower = dict(zip(string.ascii_lowercase, [x for x in range(1, 27)]))
[    ]priorityMapUpper = dict(zip(string.ascii_uppercase, [x for x in range(27, 53)]))
[    ]priorityMap = {**priorityMapLower, **priorityMapUpper}