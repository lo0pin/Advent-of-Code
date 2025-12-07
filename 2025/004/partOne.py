from input import *

lines = data.splitlines()

all_of_rolls = 0
rolls_of_paper = 0
neigbor_rolls = 0

for line in range(len(lines)):
    for character in range(len(lines[line])):
        ############################################
        if lines[line][character]  == "@":
            all_of_rolls +=1 
        ############################################
        
        neigbor_rolls = 0
        try:
            if lines[line][character]  == "@":
                #oben
                if lines[line-1][character-1]  == "@":
                    neigbor_rolls +=1
                if lines[line-1][character]  == "@":
                    neigbor_rolls +=1
                if lines[line-1][character+1]  == "@":
                    neigbor_rolls +=1
                #nebenan
                if lines[line][character-1]  == "@":
                    neigbor_rolls +=1
                if lines[line][character+1]  == "@":
                    neigbor_rolls +=1
                #darunter
                if lines[line+1][character-1]  == "@":
                    neigbor_rolls +=1
                if lines[line+1][character]  == "@":
                    neigbor_rolls +=1
                if lines[line+1][character+1]  == "@":
                    neigbor_rolls +=1
                if neigbor_rolls < 4:
                    rolls_of_paper +=1
        except:
            None    


        ############################################
#ecken
if lines[0][0]  == "@":    
    rolls_of_paper +=1
if lines[0][len(lines[0])-1]  == "@":    
    rolls_of_paper +=1
if lines[len(lines)-1][0]  == "@":    
    rolls_of_paper +=1
if lines[len(lines)-1][len(lines[len(lines)-1])-1]   == "@":    
    rolls_of_paper +=1

#oberste Zeile
for i in range(1, len(lines[0])-1):
    neigbor_rolls = 0
    #nebenan
    if lines[0][i-1]  == "@":
        neigbor_rolls +=1
    if lines[0][i+1]  == "@":
        neigbor_rolls +=1
    #darunter
    if lines[1][i-1]  == "@":
        neigbor_rolls +=1
    if lines[1][i]  == "@":
        neigbor_rolls +=1
    if lines[1][i+1]  == "@":
        neigbor_rolls +=1
    if neigbor_rolls < 4:
        rolls_of_paper +=1

#unterste Zeile
for i in range(1, len(lines[0])-1):
    neigbor_rolls = 0
    #nebenan
    if lines[len(lines)-1][i-1]  == "@":
        neigbor_rolls +=1
    if lines[len(lines)-1][i+1]  == "@":
        neigbor_rolls +=1
    #darüber
    if lines[len(lines)-2][i-1]  == "@":
        neigbor_rolls +=1
    if lines[len(lines)-2][i]  == "@":
        neigbor_rolls +=1
    if lines[len(lines)-2][i+1]  == "@":
        neigbor_rolls +=1
    if neigbor_rolls < 4:
        rolls_of_paper +=1


#linkeste Spalte
for i in range(1, len(lines)-1):
    neigbor_rolls = 0
    #oben oder unten
    if lines[i-1][0]  == "@":
        neigbor_rolls +=1
    if lines[i+1][0]  == "@":
        neigbor_rolls +=1
    #rechts daneben
    if lines[i-1][1]  == "@":
        neigbor_rolls +=1
    if lines[i][1]  == "@":
        neigbor_rolls +=1
    if lines[i+1][1]  == "@":
        neigbor_rolls +=1
    if neigbor_rolls < 4:
        rolls_of_paper +=1

#rechtest Spalte
for i in range(1, len(lines)-1):
    neigbor_rolls = 0
    #oben oder unten
    if lines[i-1][len(lines[i])-1]  == "@":
        neigbor_rolls +=1
    if lines[i+1][len(lines[i])-1]  == "@":
        neigbor_rolls +=1
    #links daneben
    if lines[i-1][len(lines[i])-2]  == "@":
        neigbor_rolls +=1
    if lines[i][len(lines[i])-2]  == "@":
        neigbor_rolls +=1
    if lines[i+1][len(lines[i])-2]  == "@":
        neigbor_rolls +=1
    if neigbor_rolls < 4:
        rolls_of_paper +=1


"""
        neigbor_rolls = 0
        try:
            if lines[line][character]  == "@":
                if lines[line-1][character]  == ".":
                    rolls_of_paper +=1
                    continue
                if lines[line+1][character]  == ".":
                    rolls_of_paper +=1
                    continue
                if lines[line][character-1]  == ".":
                    rolls_of_paper +=1
                    continue
                if lines[line][character+1]  == ".":
                    rolls_of_paper +=1
                    continue
        except:
            None
"""

#print(all_of_rolls)
print(rolls_of_paper)
