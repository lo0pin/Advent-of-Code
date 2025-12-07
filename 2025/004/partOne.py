from input import *

lines = data.splitlines()

all_of_rolls = 0
rolls_of_paper = 0
neigbor_rolls = 0

for line in range(len(lines)):
    for character in range(len(lines[line])):
        
        neigbor_rolls = 0
        
        if lines[line][character]  == ".":
            continue

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if line+dr in range(0,len(lines)) and character+dc in range(0, len(lines[0])):
                    if lines[line+dr][character+dc] == "@":
                        neigbor_rolls += 1

        
        if neigbor_rolls <4:
            rolls_of_paper +=1


print(rolls_of_paper)
