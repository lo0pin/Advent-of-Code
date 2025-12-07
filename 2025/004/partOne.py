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
        """
        neigbor_rolls = 0
        try:
            if lines[line][character]  == "@":
                if lines[line-1][character]  == "@":
                    neigbor_rolls +=1
                if lines[line+1][character]  == "@":
                    neigbor_rolls +=1
                if lines[line][character-1]  == "@":
                    neigbor_rolls +=1
                if lines[line][character+1]  == "@":
                    neigbor_rolls +=1
            if neigbor_rolls < 4:
                rolls_of_paper +=1
        except:
            None        
        """

        ############################################
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

#print(all_of_rolls)
print(rolls_of_paper)
